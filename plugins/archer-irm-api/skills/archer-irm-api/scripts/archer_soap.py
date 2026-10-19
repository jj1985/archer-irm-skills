#!/usr/bin/env python3
"""Minimal Archer Web Services (SOAP) helper, standard library only.

Environment: ARCHER_URL (https://host/Archer), ARCHER_INSTANCE, ARCHER_USER, ARCHER_PASSWORD, ARCHER_DOMAIN.

Examples
  python archer_soap.py login                                    # prints a session token (works even when REST login is blocked by SSO)
  python archer_soap.py record 17 234                            # GetRecordById -> record XML
  python archer_soap.py search --module 331 --page-size 100 --display 9399 9402 \
        --text-contains 9402 "A comment" --sort 9399 Ascending  # ExecuteSearch with a generated SearchReport
  python archer_soap.py search --xml search.xml --page 2         # run your own SearchReport XML
  python archer_soap.py call search GetReports                   # generic call with named params: call <service> <Method> k=v ...
"""
from __future__ import annotations

import argparse
import html
import os
import ssl
import sys
import urllib.error
import urllib.request
from xml.sax.saxutils import escape

try:  # defusedxml protects against XXE / entity-expansion payloads; stdlib fallback keeps the script dependency-free
    import defusedxml.ElementTree as ET  # type: ignore
except ImportError:  # pragma: no cover
    import xml.etree.ElementTree as ET  # noqa: S405
    print("note: install defusedxml for hardened XML parsing (pip install defusedxml)", file=sys.stderr)

NS = "http://archer-tech.com/webservices/"
SOAP_ENV = "http://schemas.xmlsoap.org/soap/envelope/"


class SoapFault(RuntimeError):
    pass


class ArcherSoap:
    def __init__(self, base_url: str, verify_tls: bool = True, ca_bundle: str | None = None, timeout: int = 300):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        # TLS verified by default; pass ca_bundle for self-signed lab certs. verify_tls=False is lab-only (MITM risk).
        self._ctx = ssl.create_default_context(cafile=ca_bundle) if ca_bundle else ssl.create_default_context()
        if not verify_tls:
            print("WARNING: TLS verification disabled (--insecure); do not use against production.", file=sys.stderr)
            self._ctx.check_hostname = False
            self._ctx.verify_mode = ssl.CERT_NONE
        self.token: str | None = None

    def call(self, service: str, method: str, params: dict | None = None, *, namespace: str = NS) -> str:
        """Invoke <method> on <service>.asmx; returns the text of <MethodResult> (XML results are unescaped)."""
        params = params or {}
        if namespace == NS and service.lower() == "module":
            namespace = "http://tempuri.org/"
        body = "".join(f"<{k}>{escape(str(v))}</{k}>" for k, v in params.items())
        envelope = (
            '<?xml version="1.0" encoding="utf-8"?>'
            f'<soap:Envelope xmlns:soap="{SOAP_ENV}"><soap:Body>'
            f'<{method} xmlns="{namespace}">{body}</{method}>'
            "</soap:Body></soap:Envelope>"
        ).encode("utf-8")
        req = urllib.request.Request(
            f"{self.base_url}/ws/{service.lower()}.asmx", data=envelope, method="POST",
            headers={"Content-Type": "text/xml; charset=utf-8", "SOAPAction": f'"{namespace}{method}"'})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as resp:
                text = resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            text = e.read().decode("utf-8", "replace")
            raise SoapFault(self._fault_message(text) or f"HTTP {e.code}: {text[:500]}") from None
        root = ET.fromstring(text)
        fault = root.find(f".//{{{SOAP_ENV}}}Fault")
        if fault is not None:
            raise SoapFault(self._fault_message(text))
        result = root.find(f".//{{{namespace}}}{method}Result")
        return (result.text or "") if result is not None else ""

    @staticmethod
    def _fault_message(text: str) -> str:
        try:
            root = ET.fromstring(text)
            fs = root.find(f".//{{{SOAP_ENV}}}Fault/faultstring")
            return (fs.text or "").strip() if fs is not None else ""
        except ET.ParseError:
            return ""

    # ---------------------------------------------------------------- convenience
    def login(self, username: str, instance: str, password: str, domain: str = "") -> str:
        if domain:
            self.token = self.call("general", "CreateDomainUserSessionFromInstance",
                                   {"username": username, "instanceName": instance, "password": password, "usersDomain": domain})
        else:
            self.token = self.call("general", "CreateUserSessionFromInstance",
                                   {"userName": username, "instanceName": instance, "password": password})
        return self.token

    def logout(self) -> None:
        if self.token:
            try:
                self.call("general", "TerminateSession", {"sessionToken": self.token})
            finally:
                self.token = None

    def get_record(self, module_id: int, content_id: int) -> str:
        return self.call("record", "GetRecordById", {"sessionToken": self.token, "moduleId": module_id, "contentId": content_id})

    def create_record(self, module_id: int, record_xml: str) -> int:
        return int(self.call("record", "CreateRecord", {"sessionToken": self.token, "moduleId": module_id, "fieldValues": record_xml}))

    def update_record(self, module_id: int, content_id: int, record_xml: str) -> int:
        return int(self.call("record", "UpdateRecord", {"sessionToken": self.token, "moduleId": module_id,
                                                         "contentId": content_id, "fieldValues": record_xml}))

    def execute_search(self, search_report_xml: str, page: int = 1) -> str:
        return self.call("search", "ExecuteSearch", {"sessionToken": self.token, "searchOptions": search_report_xml, "pageNumber": page})

    def search_all_pages(self, search_report_xml: str, page_size: int):
        """Yield <Record> elements across pages until a short page."""
        page = 1
        while True:
            xml_text = self.execute_search(search_report_xml, page)
            root = ET.fromstring(xml_text)
            records = root.findall(".//Record")
            yield from records
            if len(records) < page_size:
                break
            page += 1


# -------------------------------------------------------------------- SearchReport builder
def build_search_report(module: int | str, display_fields: list, page_size: int = 100, max_records: int | None = None,
                        conditions: list[str] | None = None, operator_logic: str | None = None,
                        sort: list[tuple] | None = None, keywords: str | None = None) -> str:
    """conditions = list of already-formed <XxxFilterCondition> XML strings (see helpers below)."""
    parts = [f"<SearchReport><PageSize>{page_size}</PageSize>"]
    if max_records:
        parts.append(f"<MaxRecordCount>{max_records}</MaxRecordCount>")
    parts.append("<DisplayFields>" + "".join(f"<DisplayField>{f}</DisplayField>" for f in display_fields) + "</DisplayFields>")
    parts.append("<Criteria>")
    if keywords:
        parts.append(f"<Keywords>{escape(keywords)}</Keywords>")
    parts.append(f"<ModuleCriteria><Module>{module}</Module><IsKeywordModule>{'true' if keywords else 'false'}</IsKeywordModule>")
    if sort:
        parts.append("<SortFields>" + "".join(f"<SortField><Field>{f}</Field><SortType>{t}</SortType></SortField>" for f, t in sort) + "</SortFields>")
    parts.append("</ModuleCriteria>")
    if conditions:
        parts.append("<Filter>")
        if operator_logic:
            parts.append(f"<OperatorLogic>{escape(operator_logic)}</OperatorLogic>")
        parts.append("<Conditions>" + "".join(conditions) + "</Conditions></Filter>")
    parts.append("</Criteria></SearchReport>")
    return "".join(parts)


def text_condition(field, value: str, operator: str = "Contains") -> str:
    # Values inside the search XML must be double-encoded (the XML string itself is escaped again by SOAP).
    return f"<TextFilterCondition><Operator>{operator}</Operator><Field>{field}</Field><Value>{escape(escape(value))}</Value></TextFilterCondition>"


def numeric_condition(field, value, operator: str = "Equals") -> str:
    return f"<NumericFilterCondition><Operator>{operator}</Operator><Field>{field}</Field><Value>{value}</Value></NumericFilterCondition>"


def values_list_condition(field, value_ids: list[int], operator: str = "Contains", include_no_selection: bool = False) -> str:
    vals = "".join(f"<Value>{v}</Value>" for v in value_ids)
    return (f"<ValueListFilterCondition><Operator>{operator}</Operator><Field>{field}</Field>"
            f"<IsNoSelectionIncluded>{'True' if include_no_selection else 'False'}</IsNoSelectionIncluded><Values>{vals}</Values></ValueListFilterCondition>")


def date_condition(field, value: str, operator: str = "Equals") -> str:
    return f"<DateComparisonFilterCondition><Operator>{operator}</Operator><Field>{field}</Field><Value>{escape(value)}</Value></DateComparisonFilterCondition>"


def date_range_condition(field, begin: str, end: str) -> str:
    return (f"<DateRangeFilterCondition><Operator>Between</Operator><Field>{field}</Field>"
            f"<BeginValue>{escape(begin)}</BeginValue><EndValue>{escape(end)}</EndValue></DateRangeFilterCondition>")


def records_to_dicts(xml_text: str) -> list[dict]:
    """Flatten ExecuteSearch XML to a list of {fieldId: value} dicts (text/number/date values; multi-values joined)."""
    root = ET.fromstring(xml_text)
    out = []
    for rec in root.findall(".//Record"):
        row = {"contentId": rec.get("contentId")}
        for f in rec.findall("Field"):
            fid = f.get("id")
            vals = []
            if f.get("value") is not None:
                vals.append(html.unescape(f.get("value")))
            vals += [html.unescape(mv.get("value")) for mv in f.findall("MultiValue") if mv.get("value") is not None]
            vals += [(r.text or "") for r in f.findall("Reference")]
            vals += [u.get("firstName", "") + " " + u.get("lastName", "") for u in f.findall("Users/User")]
            vals += [g.get("name", "") for g in f.findall("Groups/Group")]
            row[fid] = vals[0] if len(vals) == 1 else vals
        out.append(row)
    return out


# -------------------------------------------------------------------- CLI
def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--url", default=os.environ.get("ARCHER_URL", ""))
    p.add_argument("--instance", default=os.environ.get("ARCHER_INSTANCE"))
    p.add_argument("--user", default=os.environ.get("ARCHER_USER"))
    p.add_argument("--password", default=os.environ.get("ARCHER_PASSWORD"))
    p.add_argument("--domain", default=os.environ.get("ARCHER_DOMAIN", ""))
    p.add_argument("--ca-bundle", default=os.environ.get("ARCHER_CA_BUNDLE"), help="PEM CA file for self-signed certs (preferred over --insecure)")
    p.add_argument("--insecure", action="store_true", help="disable TLS verification (lab only)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("login")
    s = sub.add_parser("record"); s.add_argument("module_id", type=int); s.add_argument("content_id", type=int)
    s = sub.add_parser("search"); s.add_argument("--xml", help="file with a SearchReport"); s.add_argument("--module"); s.add_argument("--display", nargs="*", default=[])
    s.add_argument("--page-size", type=int, default=100); s.add_argument("--page", type=int, default=1); s.add_argument("--all", action="store_true")
    s.add_argument("--text-contains", nargs=2, action="append", metavar=("FIELD", "VALUE"), default=[])
    s.add_argument("--sort", nargs=2, action="append", metavar=("FIELD", "Ascending|Descending"), default=[])
    s.add_argument("--keywords"); s.add_argument("--flatten", action="store_true")
    s = sub.add_parser("call"); s.add_argument("service"); s.add_argument("method"); s.add_argument("params", nargs="*", help="k=v (sessionToken added automatically)")
    a = p.parse_args(argv)

    c = ArcherSoap(a.url, verify_tls=not a.insecure, ca_bundle=a.ca_bundle)
    try:
        token = c.login(a.user, a.instance, a.password, a.domain)
        if a.cmd == "login":
            print(token)
            c.token = None  # keep the session alive for the caller
            return 0
        if a.cmd == "record":
            print(c.get_record(a.module_id, a.content_id))
        elif a.cmd == "search":
            if a.xml:
                report = open(a.xml, encoding="utf-8").read()
            else:
                if not a.module:
                    p.error("--module or --xml required")
                conds = [text_condition(f, v) for f, v in a.text_contains]
                report = build_search_report(a.module, a.display, a.page_size, conditions=conds, sort=[tuple(x) for x in a.sort], keywords=a.keywords)
            if a.all:
                import json
                rows = []
                for rec in c.search_all_pages(report, a.page_size):
                    rows.append(records_to_dicts(ET.tostring(rec, encoding="unicode").join(["<R>", "</R>"]))[0])
                print(json.dumps(rows, indent=1, ensure_ascii=False))
            else:
                xml_text = c.execute_search(report, a.page)
                if a.flatten:
                    import json
                    print(json.dumps(records_to_dicts(xml_text), indent=1, ensure_ascii=False))
                else:
                    print(xml_text)
        elif a.cmd == "call":
            params = {"sessionToken": token}
            for kv in a.params:
                k, _, v = kv.partition("=")
                params[k] = v
            print(c.call(a.service, a.method, params))
        return 0
    except SoapFault as e:
        print(f"SOAP fault: {e}", file=sys.stderr)
        return 1
    finally:
        c.logout()


if __name__ == "__main__":
    sys.exit(main())
