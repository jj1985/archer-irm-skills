# Archer API gotchas and error patterns

| Symptom | Cause | Fix |
|---|---|---|
| HTTP 200 but nothing happened | Platform API signals failure inside the envelope | Check `IsSuccessful`; print `ValidationMessages[].ResourcedMessage` and `MessageKey`. Severity 2 = partial/warning, 3 = error, 4 = not found. |
| `IsSuccessful:true` yet the field is unchanged | Post/Put content silently drops invalid inputs (wrong `Type`, bad IP, nonexistent ContentId/ValuesListId, extra properties on a Type 19 entry, field from another level) | Re-read the record after writing; validate ids against metadata first; keep Type 19 entries to `Type`,`FieldId`,`IpAddressBytes` only. |
| 403 on `POST content` | Body contains `Content.Id` of an existing record | Use `PUT` to update, `POST` to create. |
| 403 on `PUT content` | Record id does not exist (or was deleted) | Use `POST`, or confirm the id with `content/contentid?id=`. |
| 404 on a documented path | Prefix mismatch (`/api/core` vs `/platformapi/core`), missing `/Archer` instance segment (SaaS), or trailing-slash sensitivity | Try the alternate prefix; drop/add the instance segment; the OpenAPI operations carry `x-archer-documented-path`. |
| POST returns an error on a read endpoint | Missing `X-Http-Method-Override: GET` | Add the header, or use plain GET with the options in the query string. |
| Login returns a token but every call is "not authorized" | Header scheme wrong | Exactly `Authorization: Archer session-id=<token>` (no `Bearer`, no quotes needed). |
| REST login fails on an SSO instance | "Allow manual bypass" is off | Enable it in the Control Panel, or create the session with SOAP `general.CreateUserSessionFromInstance` and reuse the token for REST. |
| Session suddenly 401s | Session timeout from the user's security parameter, or concurrent-session limit hit because scripts never logged out | Re-login on 401; always `POST security/logout`; prefer a PAT for automation. |
| `WebApi:WebApiResourceNotFoundQuery` / "The resource cannot be found." | Object does not exist **or** user lacks rights to it (Archer does not distinguish) | Verify the id with an admin account; check role permissions on the application/level/page. |
| User update wiped middle name, locale, dashboard... | `PUT user` is a full replacement | GET the user first and send back every property; null lists keep contacts/roles/groups, non-null lists replace them. |
| Group/role membership not as expected after update | Same replace semantics on `ParentGroups`/`ChildGroups`/`ChildUsers` and `GroupIds` | Send null to keep, arrays to replace; note `GroupIds:[]` on role update unassigns all groups. |
| Role lost its default home page/dashboard | Documented side effect of `PUT role` | Re-set the home page in the UI afterwards. |
| Values list write ignored | Sent value **text** instead of value **ids** | Resolve ids via `valueslistvalue/flat/valueslist/<RelatedValuesListId>` (or SOAP `LookupListValue`). Hierarchical lists: child ids are distinct from parent ids. |
| Cross-reference write ignored | Target content id not in a level the field targets, or the field is a questionnaire target reference | Check `level/referencefield/<fieldId>`; for questionnaires create via SOAP `CreateQuestionnaireRecord`. |
| Attachment field write fails | Attachment not uploaded first | `POST content/attachment` (base64) → id, then `Value:[id]` in the Type 11/12 field; SOAP cannot write attachments. |
| Sub-form data missing | Sub-form records are separate content | Create each sub-form record with `POST content` + `SubformFieldId`, then put the returned ids into the parent's Type 24 field. |
| Date parsed wrong | Culture-specific `M/d/yyyy` vs ISO | Prefer ISO `yyyy-MM-ddTHH:mm:ss` on REST; SOAP needs `MM/DD/YYYY h:mm AM`. `"0"` clears a date. |
| Content API 400 on save | Values identical to current record (documented), bad alias casing, unsupported field type (attachment, matrix...) | Compare before writing; aliases are case-sensitive; use REST for unsupported types. |
| Content API returns only 1,000 rows | Page size cap | Loop with `skip`/`top` (see `content-api.md`). |
| OData `$filter` rejected on content | Filtering/projecting inside collections is not supported for content | Filter client-side or use SOAP `ExecuteSearch`. |
| OData body ignored | Sent as GET with a body | OData body form requires POST + override; otherwise use query string. |
| SOAP text filter mis-matches on `&`, quotes | Values must be **double** XML-encoded inside the searchOptions string | `&` → `&amp;amp;`, `"` → `&amp;quot;`, `'` → `&amp;#39;`, `<` → `&amp;lt;`, `>` → `&amp;gt;`. |
| SOAP returns result but it is escaped XML text | Normal: XML inside the `<...Result>` string | Unescape (`html.unescape`) then parse. |
| SOAP method "disabled" fault | Method removed (Technology class, Bind/Unbind, CreateUserSession...) | See replacement table in `web-services-soap.md`. |
| `ExecuteSearch` returns `12:00:00 AM` times | Date-only field | Ignore the time component. |
| Security Events report "invalid parameter" | `EventType` misspelled or date outside 1–6 days ago | Use an exact name from the list; `EventsForDate` between yesterday and six days ago. |
| DeletedContent 400 | Dates in the future or start > end | Dates must be ≤ today and start ≤ end (`yyyy-mm-dd`). |
| Data Gateway calls fail with `DataGatewayNotEnabled` | Instance setting | Enable Data Gateway in the Archer Control Panel. |
| Field maps "partially successful" | Field ids not in the level, or connection name wrong | Check `RejectedIds` and the `XmlData` in the message; `TargetId` must be the level id. |
| Package install does nothing | Install body must come from the UI-generated code with the right GUIDs/options | Copy the body from Import and Install Packages, then automate. |
| Locked record updated unexpectedly | APIs bypass UI record locks | Expected behaviour (PUT content, UpdateRecord(s), data feeds); coordinate with users. |
| Large metadata responses are slow | Full objects returned | Project with `$select=Id,Name,Alias,Type` and page with `$top/$skip`. |
