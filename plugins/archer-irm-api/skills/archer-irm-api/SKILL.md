---
name: archer-irm-api
description: >-
  Work with the Archer IRM (formerly RSA Archer) platform programmatically: RESTful Platform API
  (/platformapi/core, /api/core), V2 API (/api/V2: Personal Access Tokens, DeletedContent), Content API
  (OData /contentapi), Data Gateway, packages, Access Control reports, the SOAP Web Services API
  (/ws/*.asmx: accesscontrol, accessrole, field, general, module, record, search) and NGRX. Use it
  whenever a task mentions Archer, RSA Archer, Archer IRM, archerirm, GRC records, data feeds, Archer
  applications/levels/fields/values lists, session-id tokens, platformapi, contentapi,
  ExecuteSearch/SearchReport XML, or integrating, scripting, exporting, bulk-loading or automating
  anything against an Archer instance, even if the user never says "API". Covers auth, record CRUD,
  field value encoding by type, search, user/group/role admin, workflow, attachments, OData paging and
  the pitfalls (HTTP 200 with IsSuccessful:false, POST + X-Http-Method-Override, IDs vs GUIDs,
  update-replaces-all semantics).
---

# Archer IRM APIs

Archer exposes several API families on the same web server. Pick the family by task, then read the
matching reference file. Everything here was reconstructed from the official Archer API Help 2026.08
(https://help.archerirm.cloud/api_202608/content/api/archer_apis.htm); a verbatim Markdown snapshot
of every help page lives in `references/source-docs/` (see its `INDEX.md`) for anything not covered.

## Which API for which job

| Task | Use | Reference |
|---|---|---|
| Log in, get a session token | REST `POST /platformapi/core/security/login` (or SOAP `general.CreateUserSessionFromInstance` when SSO blocks REST login) | `references/rest-api-quickref.md` |
| Long-lived automation credential | Personal Access Token via `/api/V2/PersonalAccessToken/*`; used exactly like a session token | `references/rest-api-quickref.md` |
| Read one record, with field IDs and typed values | REST `GET /platformapi/core/content/contentid?id=` | `references/rest-api-quickref.md`, `references/field-types.md` |
| Create / update / delete a record | REST `POST`/`PUT`/`DELETE /platformapi/core/content` with `FieldContents` keyed by field ID | `references/field-types.md` |
| Pull a whole application as flat rows by field *alias* (reporting, exports, sync) | Content API `GET /contentapi/<LevelAlias>` (OData, 1,000-row pages) | `references/content-api.md` |
| Search with filters, keywords, sorting, statistics across modules | SOAP `search.ExecuteSearch` / `ExecuteStatisticSearch` with `SearchReport` XML (REST has no general search) | `references/web-services-soap.md` |
| Discover applications, levels, fields, values lists, IDs and GUIDs | REST `/platformapi/core/system/*` metadata resources | `references/rest-api-quickref.md` |
| Users, groups, roles, security parameters | REST `/platformapi/core/system/user|group|role|securityparameter` (SOAP `accesscontrol`/`accessrole` also) | `references/rest-api-quickref.md` |
| Advance a record through Advanced Workflow | REST `WorkflowAction` get + post | `references/rest-api-quickref.md` |
| Run a data feed, check its history | REST `/platformapi/core/datafeed/*` | `references/rest-api-quickref.md` |
| Attachments | REST `/platformapi/core/content/attachment` (SOAP `record.GetAttachmentFile` read-only) | `references/rest-api-quickref.md` |
| External data via Data Gateway, package deploy, security/audit reports, deleted-record audit | REST, see quickref sections | `references/rest-api-quickref.md`, `references/data-gateway.md` |
| Mail merge, CAST entries, questionnaire record creation, child record IDs | SOAP `record.*` | `references/web-services-method-catalog.md` |
| NGRX (SaaS "next-gen" UI) data | `/ngrx/record/v1/...`; Swagger lives in the tenant | `references/rest-api-quickref.md` (NGRX section) |

The machine-readable contract for everything except SOAP is `references/archer-irm.openapi.yaml`
(OpenAPI 3.1, 115 operations). Use it to generate clients, validate payloads, or look up a schema.

## Core mechanics (read before any call)

**Base URL.** `https://<host>/<instance>/...` where `<instance>` is the IIS application name,
usually `Archer` on-prem. SaaS tenants may have no instance segment. `/platformapi/core/...` and
`/api/core/...` are the same controllers; if one 404s, try the other.

**Auth header.** Every REST/V2/Data Gateway call: `Authorization: Archer session-id=<token>`
(custom scheme, not Bearer). The Content API also accepts cookie `ArcherSessionCookie=<token>`;
NGRX wants cookie `__ArcherSessionCookie__=<token>` and then returns a JWT cookie to reuse.
Session lifetime follows the user's security parameter; re-login on 401. Log out when done
(`POST .../security/logout` with `{"Value":"<token>"}`) so sessions do not pile up against the
user's concurrent-session limit.

**Reads are documented as POST + `X-Http-Method-Override: GET`.** That lets OData options go in
the body as `{"Value":"?$select=Name,Description&$top=50&$skip=100&$orderby=Name desc"}` instead
of a logged URL. Plain `GET` with the same options as a query string also works. Some reads are
*only* POST+override because they need a body: `content/fieldcontent`, `datafeed/history`,
`system/task`, the two Access Control reports.

**Envelope.** Platform API replies look like
`{"Links":[],"RequestedObject":{...},"IsSuccessful":true,"ValidationMessages":[]}`; collections are
arrays of these. HTTP 200 does **not** mean success: always check `IsSuccessful` and surface
`ValidationMessages[].ResourcedMessage`/`Description`. Creates return `RequestedObject.Id`.
V2 endpoints (`/api/V2/...`) return bare objects and real 4xx codes with an OData
`CustomErrorResponse` (`InternalMessage`).

**IDs.** Records are addressed by content ID (also called tracking ID / system ID). Fields,
levels, applications, values-list values all have integer IDs *and* GUIDs; REST uses the integer
IDs, SOAP search prefers GUIDs. Get them from metadata calls rather than from the UI when scripting.
`Determine System IDs` in the help: Application Builder > Applications > app > Fields tab, hover a field.

**Field values are typed by integer `Type`.** The same number means the same field type in REST
`FieldContents`, in field definitions, and in SOAP XML `type=` attributes. The value *shape* differs
by type and by API; `references/field-types.md` is the authoritative table. Invalid inputs
(bad IP, nonexistent ContentId) are silently ignored by Post/Put content while `IsSuccessful`
stays true, so re-read the record after writing when correctness matters.

**Update semantics.** `PUT content` changes only the fields you send. `PUT user`, `PUT group`,
`PUT role` are *full replacements*: omitted user properties reset to null/default, and
`Contacts`/`Roles`/`Groups` (user) or `ParentGroups`/`ChildGroups`/`ChildUsers` (group) are
replaced when non-null and untouched when null. Read first, then write back the whole object.

**Permissions mirror the UI.** An API user sees and changes exactly what it could in the UI.
Missing rights usually surface as `IsSuccessful:false` + "resource cannot be found", not 403.

## Workflow for a typical integration task

1. **Confirm the target.** Host, instance name, whether SaaS, credential type (user/password vs PAT),
   and which application/level/fields are involved. Never print or store passwords or tokens in
   outputs; read them from env vars (`ARCHER_URL`, `ARCHER_INSTANCE`, `ARCHER_USER`, `ARCHER_PASSWORD`
   or `ARCHER_PAT`) as `scripts/archer_rest.py` does.
2. **Discover metadata before touching content.** Applications → levels (`/system/level/module/{id}`)
   → field definitions (`/system/fielddefinition/level/{id}`, note `Type`, `Alias`, `Guid`,
   `RelatedValuesListId`) → values list values (`/system/valueslistvalue/flat/valueslist/{id}`).
   Cache the ID↔alias map; everything else keys off it.
3. **Read a sample record** (`content/contentid?id=`) to see real value shapes before writing.
4. **Write with explicit `Type` and `FieldId`** per field; omit fields you do not want to change.
   For attachments upload first, then reference the returned ID in a Type 11/12 field.
5. **Verify**: re-read the record, or query the Content API for the alias values.
6. For bulk reads prefer the Content API (1,000/page, flat aliases). For bulk filtered reads or
   cross-module joins use SOAP `ExecuteSearch` with `PageSize`/`pageNumber` paging.
7. For bulk writes loop `POST content`; there is no REST batch endpoint (SOAP `record.CreateRecords`
   / `UpdateRecords` accept a `<Records>` wrapper).

## Scripts

- `scripts/archer_rest.py` - dependency-free Python client + CLI for the REST, V2 and Content APIs
  (login/logout, PAT auth, get/post/put/delete content, metadata lookups, attachment upload,
  Content API paging, workflow actions). Run `python scripts/archer_rest.py --help`. Import it
  (`from archer_rest import ArcherClient`) when writing larger tools.
- `scripts/archer_soap.py` - minimal SOAP helper (`general.CreateUserSessionFromInstance`,
  `record.GetRecordById`, `search.ExecuteSearch` with a `SearchReport` builder, generic `call()`).
  No third-party deps.

Both scripts verify TLS. For a self-signed lab certificate pass `--ca-bundle ca.pem` (or `ARCHER_CA_BUNDLE`);
`--insecure` exists for throwaway labs only because it exposes the session token to interception.

## Reference files

- `references/rest-api-quickref.md` - every REST/V2/Data Gateway/Content API/NGRX endpoint with
  verb, body shape and notes, grouped by area (metadata, content, users, groups, roles, workflow,
  data feed, packages, reports, PAT, deleted content).
- `references/field-types.md` - field type IDs; REST value shapes per type; SOAP XML input/output
  shapes per type; null conventions; date formats.
- `references/content-api.md` - OData Content API: endpoints, aliases, paging, filtering, save body.
- `references/web-services-soap.md` - SOAP transport, sessions, record XML, the full `SearchReport`
  grammar (filters, statistics, module criteria, time-based filters), legacy `Search` XML,
  deprecated/disabled methods.
- `references/web-services-method-catalog.md` - all 108 SOAP methods with signatures, parameters,
  privileges and status (generated from the docs).
- `references/data-gateway.md` - Data Gateway connections, field maps, content maps, change notification.
- `references/gotchas.md` - error patterns and pitfalls, with the fix for each.
- `references/source-docs/INDEX.md` - index of the 245-page documentation snapshot plus 84 example
  payload files (`source-docs/examples/`). Grep here when the curated files are not enough.

## Conventions when answering

- Show requests as `METHOD path` plus headers plus a JSON body; put the session header once and
  say "same auth header" after that.
- Use field IDs/aliases from the user's instance when given; otherwise use placeholder IDs and say
  they must be looked up via the metadata endpoints (show the exact call).
- When the user wants a one-off answer (e.g. "how do I set a values list via the API"), give the
  payload fragment from `field-types.md` directly instead of the whole workflow.
- Flag deprecated/disabled SOAP methods and name the replacement (list in `web-services-soap.md`).
