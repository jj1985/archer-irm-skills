#!/usr/bin/env python3
"""Archer IRM REST / V2 / Content API client and CLI (standard library only).

Environment (or CLI flags): ARCHER_URL (https://host/Archer), ARCHER_INSTANCE, ARCHER_USER,
ARCHER_PASSWORD, ARCHER_DOMAIN (optional), ARCHER_PAT (skips login when set).

Examples
  python archer_rest.py apps                                   # list applications (Id, Name, Alias)
  python archer_rest.py levels 123                             # levels of application 123
  python archer_rest.py fields 456 [--type 4]                  # field definitions of level 456
  python archer_rest.py values 789                             # values list values (flat)
  python archer_rest.py get 184630                             # record by content id
  python archer_rest.py create 456 '{"13867":{"Type":1,"Value":"hello"}}'   # FieldId filled in from key
  python archer_rest.py update 184630 456 '{"13890":{"Type":2,"Value":5}}'
  python archer_rest.py delete 184630
  python archer_rest.py upload ./file.pdf --sensitive          # -> attachment id
  python archer_rest.py workflow 260068                        # available workflow actions
  python archer_rest.py contentapi-sets                        # Content API entity sets
  python archer_rest.py contentapi-dump Risk_Register --out rr.json
  python archer_rest.py raw GET /platformapi/core/system/level
  python archer_rest.py raw POST /platformapi/core/system/user --override --body '{"Value":"?$top=5"}'
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Iterator

ACCEPT = "application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"


class ArcherError(RuntimeError):
    def __init__(self, message: str, payload: Any = None, status: int | None = None):
        super().__init__(message)
        self.payload = payload
        self.status = status


class ArcherClient:
    """Thin client. All methods return parsed JSON; Platform API calls return the *unwrapped*
    RequestedObject (or list of them) and raise ArcherError when IsSuccessful is false."""

    def __init__(self, base_url: str, instance: str | None = None, username: str | None = None,
                 password: str | None = None, domain: str = "", pat: str | None = None,
                 verify_tls: bool = True, ca_bundle: str | None = None, timeout: int = 120):
        self.base_url = base_url.rstrip("/")
        self.instance = instance
        self.username = username
        self.password = password
        self.domain = domain or ""
        self.token = pat
        self._is_pat = pat is not None
        self.timeout = timeout
        # TLS: verified by default. For a self-signed lab certificate pass ca_bundle (preferred).
        # verify_tls=False disables verification entirely and exposes the session token to MITM - lab use only.
        self._ctx = ssl.create_default_context(cafile=ca_bundle) if ca_bundle else ssl.create_default_context()
        if not verify_tls:
            print("WARNING: TLS verification disabled (--insecure); do not use against production.", file=sys.stderr)
            self._ctx.check_hostname = False
            self._ctx.verify_mode = ssl.CERT_NONE

    # ------------------------------------------------------------------ transport
    def request(self, method: str, path: str, body: Any = None, *, override_get: bool = False,
                query: dict | None = None, raw: bool = False, headers: dict | None = None,
                auth: bool = True, content_type: str = "application/json") -> Any:
        url = self.base_url + path
        if query:
            qs = urllib.parse.urlencode({k: v for k, v in query.items() if v is not None}, safe="$,'() ")
            url += ("&" if "?" in url else "?") + qs
        hdrs = {"Accept": ACCEPT}
        if auth:
            if not self.token:
                self.login()
            hdrs["Authorization"] = f"Archer session-id={self.token}"
        if override_get:
            hdrs["X-Http-Method-Override"] = "GET"
        data = None
        if body is not None:
            if isinstance(body, (bytes, bytearray)):
                data = bytes(body)
                hdrs["Content-Type"] = content_type
            else:
                data = json.dumps(body).encode("utf-8")
                hdrs["Content-Type"] = "application/json"
        elif method in ("POST", "PUT"):
            hdrs["Content-Type"] = "application/json"
            data = b""
        if headers:
            hdrs.update(headers)
        req = urllib.request.Request(url, data=data, method=method, headers=hdrs)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout, context=self._ctx) as resp:
                payload = resp.read()
                if raw:
                    return payload, dict(resp.headers)
                text = payload.decode("utf-8-sig") if payload else ""
        except urllib.error.HTTPError as e:
            text = e.read().decode("utf-8", "replace")
            try:
                parsed = json.loads(text)
            except ValueError:
                parsed = text
            raise ArcherError(f"HTTP {e.code} {method} {path}: {text[:500]}", parsed, e.code) from None
        if not text:
            return None
        try:
            return json.loads(text)
        except ValueError:
            return text

    # ------------------------------------------------------------------ auth
    def login(self) -> str:
        if self._is_pat and self.token:
            return self.token
        if not (self.instance and self.username and self.password):
            raise ArcherError("Need ARCHER_INSTANCE, ARCHER_USER and ARCHER_PASSWORD (or ARCHER_PAT) to log in")
        body = {"InstanceName": self.instance, "Username": self.username,
                "UserDomain": self.domain, "Password": self.password}
        res = self.request("POST", "/platformapi/core/security/login", body, auth=False)
        token = None
        if isinstance(res, dict):
            token = res.get("SessionToken") or (res.get("RequestedObject") or {}).get("SessionToken")
        if not token:
            raise ArcherError("Login did not return a SessionToken", res)
        self.token = token
        return token

    def logout(self) -> None:
        if self.token and not self._is_pat:
            try:
                self.request("POST", "/platformapi/core/security/logout", {"Value": self.token})
            finally:
                self.token = None

    def __enter__(self):
        self.login()
        return self

    def __exit__(self, *exc):
        self.logout()

    # ------------------------------------------------------------------ envelope helpers
    @staticmethod
    def unwrap(res: Any) -> Any:
        """Return RequestedObject(s); raise on IsSuccessful false."""
        if isinstance(res, list):
            out = []
            errors = []
            for item in res:
                if isinstance(item, dict) and "IsSuccessful" in item:
                    if item.get("IsSuccessful"):
                        out.append(item.get("RequestedObject"))
                    else:
                        errors.append(item.get("ValidationMessages"))
                else:
                    out.append(item)
            if errors and not out:
                raise ArcherError(f"Archer returned errors: {json.dumps(errors)[:800]}", res)
            return out
        if isinstance(res, dict) and "IsSuccessful" in res:
            if not res.get("IsSuccessful"):
                msgs = res.get("ValidationMessages") or []
                summary = "; ".join(str(m.get("ResourcedMessage") or m.get("Description") or m) for m in msgs) if isinstance(msgs, list) else str(msgs)
                raise ArcherError(f"Archer call failed: {summary or 'IsSuccessful=false'}", res)
            return res.get("RequestedObject")
        return res

    def get(self, path: str, query: dict | None = None, override: bool = False, body: Any = None) -> Any:
        """GET (or POST+override when a body is needed) and unwrap."""
        if override or body is not None:
            return self.unwrap(self.request("POST", path, body, override_get=True, query=query))
        return self.unwrap(self.request("GET", path, query=query))

    # ------------------------------------------------------------------ metadata
    def applications(self, select: str = "Id,Name,Alias,Guid") -> list[dict]:
        return self.get("/platformapi/core/system/application", {"$select": select} if select else None)

    def application(self, app_id: int) -> dict:
        return self.get(f"/platformapi/core/system/application/{app_id}")

    def levels(self, module_id: int | None = None) -> list[dict]:
        path = f"/platformapi/core/system/level/module/{module_id}" if module_id else "/platformapi/core/system/level"
        return self.get(path)

    def field_definitions(self, level_id: int, field_type: int | None = None, select: str | None = None) -> list[dict]:
        q: dict = {}
        if field_type is not None:
            q["$filter"] = f"Type eq {field_type}"
        if select:
            q["$select"] = select
        return self.get(f"/platformapi/core/system/fielddefinition/level/{level_id}", q or None)

    def field_definition(self, field_id: int) -> dict:
        return self.get(f"/platformapi/core/system/fielddefinition/{field_id}")

    def values_list_values(self, values_list_id: int, flat: bool = True) -> list[dict]:
        p = "flat/valueslist" if flat else "valueslist"
        return self.get(f"/platformapi/core/system/valueslistvalue/{p}/{values_list_id}")

    def field_map(self, level_id: int) -> dict[str, dict]:
        """alias -> field definition for a level (handy for building FieldContents)."""
        return {f["Alias"]: f for f in self.field_definitions(level_id) if isinstance(f, dict) and f.get("Alias")}

    # ------------------------------------------------------------------ content
    def get_content(self, content_id: int, select: str | None = None) -> dict:
        q = {"id": content_id}
        if select:
            q["$select"] = select
        return self.get("/platformapi/core/content/contentid", q)

    def get_field_content(self, content_ids: list[int], field_ids: list[int], **odata) -> list[dict]:
        q = {f"${k}": v for k, v in odata.items()} or None
        return self.get("/platformapi/core/content/fieldcontent", q, body={"FieldIds": field_ids, "ContentIds": content_ids})

    def content_by_reference_field(self, field_id: int, **odata) -> list[dict]:
        q = {"id": field_id}
        q.update({f"${k}": v for k, v in odata.items()})
        return self.get("/platformapi/core/content/referencefield/referencefieldid", q)

    @staticmethod
    def _normalise_field_contents(field_contents: dict) -> dict:
        out = {}
        for key, entry in field_contents.items():
            e = dict(entry)
            e.setdefault("FieldId", int(key))
            out[str(key)] = e
        return out

    def create_content(self, level_id: int, field_contents: dict, subform_field_id: int | None = None) -> int:
        body = {"Content": {"LevelId": level_id, "FieldContents": self._normalise_field_contents(field_contents)}}
        if subform_field_id:
            body["SubformFieldId"] = subform_field_id
        res = self.unwrap(self.request("POST", "/platformapi/core/content", body))
        return res["Id"] if isinstance(res, dict) else res

    def update_content(self, content_id: int, level_id: int, field_contents: dict, subform_field_id: int | None = None) -> int:
        body = {"Content": {"Id": content_id, "LevelId": level_id, "FieldContents": self._normalise_field_contents(field_contents)}}
        if subform_field_id:
            body["SubformFieldId"] = subform_field_id
        res = self.unwrap(self.request("PUT", "/platformapi/core/content", body))
        return res["Id"] if isinstance(res, dict) else res

    def delete_content(self, content_id: int) -> Any:
        return self.unwrap(self.request("DELETE", f"/platformapi/core/content/{content_id}"))

    def upload_attachment(self, path: str, name: str | None = None, sensitive: bool = False) -> int:
        with open(path, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode("ascii")
        body = {"AttachmentName": name or os.path.basename(path), "AttachmentBytes": b64, "IsSensitive": sensitive}
        res = self.unwrap(self.request("POST", "/platformapi/core/content/attachment", body))
        return res["Id"] if isinstance(res, dict) else res

    def download_attachment(self, attachment_id: int) -> tuple[str, bytes]:
        res = self.get(f"/platformapi/core/content/attachment/{attachment_id}")
        return res["AttachmentName"], base64.b64decode(res["AttachmentBytes"])

    # ------------------------------------------------------------------ workflow / users
    def workflow_actions(self, content_id: int) -> dict:
        return self.get(f"/platformapi/core/system/WorkflowAction/{content_id}")

    def perform_workflow_action(self, content_id: int, completion_code: int, node_id: str) -> Any:
        return self.request("POST", "/platformapi/core/system/WorkflowAction",
                            {"ContentId": content_id, "CompletionCode": completion_code, "WorkflowNodeId": node_id})

    def users(self, odata: str | None = None) -> list[dict]:
        return self.get("/platformapi/core/system/user", body={"Value": odata} if odata else None, override=True)

    def user(self, user_id: int) -> dict:
        return self.get(f"/platformapi/core/system/user/{user_id}")

    # ------------------------------------------------------------------ Content API (OData)
    def contentapi_sets(self) -> list[dict]:
        res = self.request("GET", "/contentapi/")
        return res.get("value", []) if isinstance(res, dict) else res

    def contentapi_page(self, level_alias: str, skip: int = 0, top: int = 1000, **odata) -> list[dict]:
        q = {"skip": skip, "top": top}
        q.update({f"${k}": v for k, v in odata.items()})
        res = self.request("GET", f"/contentapi/{level_alias}", query=q)
        return res.get("value", []) if isinstance(res, dict) else res

    def contentapi_iter(self, level_alias: str, page_size: int = 1000, **odata) -> Iterator[dict]:
        skip = 0
        while True:
            page = self.contentapi_page(level_alias, skip=skip, top=page_size, **odata)
            yield from page
            if len(page) < page_size:
                break
            skip += page_size

    def contentapi_record(self, level_alias: str, content_id: int) -> dict:
        return self.request("GET", f"/contentapi/{level_alias}({content_id})")

    def contentapi_save(self, level_alias: str, record: dict) -> Any:
        return self.request("POST", f"/contentapi/{level_alias}", record)


# ---------------------------------------------------------------------- CLI
def _client_from_args(a) -> ArcherClient:
    return ArcherClient(
        base_url=a.url or os.environ.get("ARCHER_URL", ""),
        instance=a.instance or os.environ.get("ARCHER_INSTANCE"),
        username=a.user or os.environ.get("ARCHER_USER"),
        password=a.password or os.environ.get("ARCHER_PASSWORD"),
        domain=a.domain or os.environ.get("ARCHER_DOMAIN", ""),
        pat=a.pat or os.environ.get("ARCHER_PAT"),
        verify_tls=not a.insecure,
        ca_bundle=a.ca_bundle or os.environ.get("ARCHER_CA_BUNDLE"),
    )


def _dump(obj: Any) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--url"); p.add_argument("--instance"); p.add_argument("--user"); p.add_argument("--password")
    p.add_argument("--domain"); p.add_argument("--pat")
    p.add_argument("--ca-bundle", help="PEM file with the CA that signed the Archer certificate (preferred over --insecure)")
    p.add_argument("--insecure", action="store_true", help="disable TLS verification (lab instances only)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("apps")
    s = sub.add_parser("levels"); s.add_argument("module_id", type=int, nargs="?")
    s = sub.add_parser("fields"); s.add_argument("level_id", type=int); s.add_argument("--type", type=int); s.add_argument("--select", default="Id,Name,Alias,Type,IsRequired,IsCalculated,RelatedValuesListId,Guid")
    s = sub.add_parser("values"); s.add_argument("values_list_id", type=int); s.add_argument("--tree", action="store_true")
    s = sub.add_parser("get"); s.add_argument("content_id", type=int); s.add_argument("--select")
    s = sub.add_parser("create"); s.add_argument("level_id", type=int); s.add_argument("field_contents_json"); s.add_argument("--subform-field-id", type=int)
    s = sub.add_parser("update"); s.add_argument("content_id", type=int); s.add_argument("level_id", type=int); s.add_argument("field_contents_json"); s.add_argument("--subform-field-id", type=int)
    s = sub.add_parser("delete"); s.add_argument("content_id", type=int)
    s = sub.add_parser("upload"); s.add_argument("path"); s.add_argument("--name"); s.add_argument("--sensitive", action="store_true")
    s = sub.add_parser("download"); s.add_argument("attachment_id", type=int); s.add_argument("--out")
    s = sub.add_parser("workflow"); s.add_argument("content_id", type=int)
    s = sub.add_parser("workflow-do"); s.add_argument("content_id", type=int); s.add_argument("completion_code", type=int); s.add_argument("node_id")
    s = sub.add_parser("users"); s.add_argument("--odata", help='e.g. "?$filter=UserName eq \'jdoe\'&$select=Id,UserName"')
    sub.add_parser("contentapi-sets")
    s = sub.add_parser("contentapi-dump"); s.add_argument("level_alias"); s.add_argument("--out"); s.add_argument("--page-size", type=int, default=1000); s.add_argument("--filter"); s.add_argument("--select")
    s = sub.add_parser("contentapi-get"); s.add_argument("level_alias"); s.add_argument("content_id", type=int)
    s = sub.add_parser("raw"); s.add_argument("method"); s.add_argument("path"); s.add_argument("--body"); s.add_argument("--override", action="store_true"); s.add_argument("--no-unwrap", action="store_true")
    a = p.parse_args(argv)

    c = _client_from_args(a)
    try:
        if a.cmd == "apps":
            _dump(c.applications())
        elif a.cmd == "levels":
            _dump(c.levels(a.module_id))
        elif a.cmd == "fields":
            _dump(c.field_definitions(a.level_id, a.type, a.select))
        elif a.cmd == "values":
            _dump(c.values_list_values(a.values_list_id, flat=not a.tree))
        elif a.cmd == "get":
            _dump(c.get_content(a.content_id, a.select))
        elif a.cmd == "create":
            print(c.create_content(a.level_id, json.loads(a.field_contents_json), a.subform_field_id))
        elif a.cmd == "update":
            print(c.update_content(a.content_id, a.level_id, json.loads(a.field_contents_json), a.subform_field_id))
        elif a.cmd == "delete":
            _dump(c.delete_content(a.content_id))
        elif a.cmd == "upload":
            print(c.upload_attachment(a.path, a.name, a.sensitive))
        elif a.cmd == "download":
            name, data = c.download_attachment(a.attachment_id)
            out = a.out or name
            with open(out, "wb") as fh:
                fh.write(data)
            print(out)
        elif a.cmd == "workflow":
            _dump(c.workflow_actions(a.content_id))
        elif a.cmd == "workflow-do":
            _dump(c.perform_workflow_action(a.content_id, a.completion_code, a.node_id))
        elif a.cmd == "users":
            _dump(c.users(a.odata))
        elif a.cmd == "contentapi-sets":
            _dump(c.contentapi_sets())
        elif a.cmd == "contentapi-dump":
            odata = {}
            if a.filter:
                odata["filter"] = a.filter
            if a.select:
                odata["select"] = a.select
            rows = list(c.contentapi_iter(a.level_alias, a.page_size, **odata))
            if a.out:
                with open(a.out, "w", encoding="utf-8") as fh:
                    json.dump(rows, fh, indent=1, ensure_ascii=False)
                print(f"{len(rows)} rows -> {a.out}")
            else:
                _dump(rows)
        elif a.cmd == "contentapi-get":
            _dump(c.contentapi_record(a.level_alias, a.content_id))
        elif a.cmd == "raw":
            body = json.loads(a.body) if a.body else None
            res = c.request(a.method.upper(), a.path, body, override_get=a.override)
            _dump(res if a.no_unwrap else c.unwrap(res))
        return 0
    except ArcherError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        if e.payload is not None:
            print(json.dumps(e.payload, indent=2, default=str)[:4000], file=sys.stderr)
        return 1
    finally:
        c.logout()


if __name__ == "__main__":
    sys.exit(main())
