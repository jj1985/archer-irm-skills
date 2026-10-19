# Archer Content API (OData v4, `/contentapi`)

A translation layer that exposes each level (and each cross-reference / related-records relationship)
the user can read as an OData entity set keyed by **field alias**, the way end users see data in the UI.
Best choice for exports, reporting, sync jobs and "give me every record of application X".

## Auth
`Authorization: Archer session-id=<token>` or `Cookie: ArcherSessionCookie=<token>` (token from `POST /platformapi/core/security/login`, or a PAT).
Results are limited to what the session user can see; an alias the user cannot read is simply absent.

## Endpoints

| Call | Request | Returns |
|---|---|---|
| Get endpoints | `GET /contentapi/` | `{"@odata.context":".../contentapi/$metadata","value":[{"name":"Risk_Register","kind":"EntitySet","url":"Risk_Register"},...]}` - one entry per readable level plus one per relationship (`<Level>_<Field>`) |
| Metadata | `GET /contentapi/$metadata` | CSDL XML: entity types, properties (alias → EDM type), navigation. Use it to learn aliases and types without guessing. |
| Level content | `GET /contentapi/<LevelAlias>` | `{"@odata.context":"...#Risk_Register","value":[{"Risk_Register_Id":107826,"Actual_Response_Date":null,"Adjusted_Qual_Residual_Risk":["Not Rated"],"Business_Units":[],...}]}` - **up to 1,000 records per call** |
| Single record | `GET /contentapi/<LevelAlias>(<contentId>)` | one object (parentheses required) |
| Relationships | `GET /contentapi/<LevelAlias>_<FieldAlias>` | `{"value":[{"Incidents_Id":224931,"Risk_Register_Id":224961},...]}` pairs of linked record ids |
| Save | `POST /contentapi/<LevelAlias>` body = flat alias-keyed object | HTTP 200, empty body. `"<LevelAlias>_Id":0` creates; any other value updates that record |

Aliases are **case-sensitive**. If two levels share an alias the entity set is `<ModuleAlias>_<LevelAlias>` (e.g. `ModuleA_FirstLevel`).
Each tenant is customised; always discover with `GET /contentapi/` first.

## Paging and query options
- `?skip=N` and `?top=N` or `?top=all` are the documented forms (`skip` counts records; the doc's wording "in thousands" reflects the 1,000-row pages).
- Standard OData `$top`, `$skip`, `$filter`, `$select`, `$orderby` are honoured too; the help itself mixes them (`?skip=10&$top=20`).
- Loop: `skip=0`, `skip=1000`, ... until `value` is shorter than the page size. Do not assume `@odata.nextLink` is present.
- Filter examples (OData v4 syntax): `$filter=Risk_Rating/any(v: v eq 'High')` for values lists on builds that expose collections,
  `$filter=Last_Updated gt 2025-01-01T00:00:00Z`, `$filter=contains(Name,'vendor')`. Verify against `$metadata` because collection
  properties cannot always be filtered; fall back to client-side filtering or SOAP `ExecuteSearch` when the server rejects the filter.

## Supported field types
Cross-Reference / Related Records, Date, First Published Date, IP Address, Last Updated, Numeric, Record Permissions, Sub-Form, Text, User/Groups List, Values List.
Everything else (attachments, images, external links, matrix, CAST, history log, calculated display controls) is **not** exposed; use the Platform REST API for those.

## Save semantics
- Values list: `{"ValuesListIds":[1199]}` (ids, not text).
- Users/groups / record permissions: `{"UserList":[{"Id":2}],"GroupList":[{"Id":5}]}`.
- Cross-reference / related records / sub-form: array of content ids `[226446]`.
- Dates: `"07/07/2018"` or ISO.
- An update whose values equal the current values fails with **HTTP 400** ("cannot update a content record with the same values"). Compare before writing, or ignore that 400 as a no-op.
- Write permissions mirror the UI.

## Example: export an application to CSV (pseudo-code)
```
sets = GET /contentapi/            -> pick "Risk_Register"
rows = []; skip = 0
loop: page = GET /contentapi/Risk_Register?skip={skip}&top=1000 ; rows += page.value ; break if len(page.value) < 1000 ; skip += 1000
flatten lists (values lists -> "; ".join, refs -> ids) and write CSV
```
`scripts/archer_rest.py contentapi-dump Risk_Register --out risk_register.json` does exactly this.
