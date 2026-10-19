# Archer REST / V2 / Content API quick reference

Base: `https://<host>/<instance>` (instance usually `Archer`). Prefix `/platformapi/core/` ≡ `/api/core/`.
Header on every call: `Authorization: Archer session-id=<token>`, `Content-Type: application/json`,
`Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8`.
"(POST+override)" below = documented as `POST` with `X-Http-Method-Override: GET`; plain GET also works
unless marked "body required". OData options: query string `?$select=..&$filter=..&$top=..&$skip=..&$orderby=..`
or body `{"Value":"?$select=..."}` with POST+override.

Response envelope: `{"Links":[],"RequestedObject":<payload>,"IsSuccessful":bool,"ValidationMessages":[...]}`;
lists are arrays of envelopes. Check `IsSuccessful`.

## Contents
1. Authentication & PAT
2. Content (records) & attachments
3. Metadata: applications, levels, fields, values lists, events, questionnaires, subforms
4. Users, groups, roles, tasks, security parameters
5. Workflow actions
6. Data feeds
7. Packages
8. Access Control reports, deleted content, Smart Data Publications
9. Content API (OData) summary
10. NGRX

---
## 1. Authentication & Personal Access Tokens

| Op | Request | Body / notes |
|---|---|---|
| Login | `POST /platformapi/core/security/login` (no auth header) | `{"InstanceName":"Archer","Username":"u","UserDomain":"","Password":"p"}` → `{"SessionToken":"<32 hex>"}` (newer builds wrap it in the envelope under `RequestedObject.SessionToken`). SSO instances need "Allow manual bypass" in the Control Panel, else use SOAP `general.CreateUserSessionFromInstance`. |
| Logout | `POST /platformapi/core/security/logout` | `{"Value":"<token>"}` |
| Create PAT | `POST /api/V2/PersonalAccessToken/Create` | `{"request":{"UserId":123,"Name":"n","Description":"d","ExpirationDate":"yyyy-MM-dd"}}` (1 day..1 year ahead). Response includes `Token` once. Admins can create for any user. |
| List PATs | `GET /api/V2/PersonalAccessToken?userId=123` | array of `{Id,IsRevoked,UserId,ExpirationDate,Name,Description,CreateDate}` |
| Revoke | `DELETE /api/V2/PersonalAccessToken(<patId>)` | 200 |
| Rotate by id | `POST /api/V2/PersonalAccessToken(<patId>)/Rotate` | optional `{"expirationDate":"yyyy-MM-dd"}`; returns new token |
| Self-rotate | `POST /api/V2/PersonalAccessToken/SelfRotate` | auth with the PAT itself; optional `{"expirationDate":...}` |

A PAT is sent exactly like a session token: `Authorization: Archer session-id=<PAT>`.

## 2. Content (records) & attachments

| Op | Request | Notes |
|---|---|---|
| Get record | `GET /platformapi/core/content/contentid?id=<contentId>` (POST+override) | `$select=LastUpdated` etc. Returns `Content` (see shape below). |
| Records via reference field | `GET /platformapi/core/content/referencefield/referencefieldid?id=<fieldId>` (POST+override) | `$filter=SequentialId eq 3`, `$select`, `$top`, `$skip`, `$orderby=SequentialId`. Questionnaire target x-ref → all target content; normal x-ref/related records → record-lookup content. |
| Selected fields of selected records | `POST /platformapi/core/content/fieldcontent` + override (body required) | `{"FieldIds":[..],"ContentIds":[..]}`; OData in query string (`?$top=2`, `$select=Id`, `$orderby=Id`). |
| History log data | `GET /platformapi/core/content/history/<contentId>` (POST+override; documented under `/api/core`) | all History Log fields of the record's application |
| Create record | `POST /platformapi/core/content` | `{"Content":{"LevelId":9,"FieldContents":{"<fieldId>":{"Type":t,"FieldId":<fieldId>,"Value":...}}},"SubformFieldId":<only for subform content>}` → `RequestedObject.Id`. 403 if `Id` names an existing record. |
| Update record | `PUT /platformapi/core/content` | same body with `"Content":{"Id":<contentId>,...}`; only sent fields change; works on user-locked records. 403 if record does not exist. |
| Delete record | `DELETE /platformapi/core/content/<contentId>` (documented `/api/core`) | success → `RequestedObject:<id>`; missing → `IsSuccessful:false`, key `ContentSaveNoContentsFound` |
| Get attachment | `GET /platformapi/core/content/attachment/<attachmentId>` (POST+override) | `RequestedObject:{AttachmentName,AttachmentBytes(base64)}` |
| Upload attachment (JSON) | `POST /platformapi/core/content/attachment` | `{"AttachmentName":"f.pdf","AttachmentBytes":"<base64>","IsSensitive":true}` → `RequestedObject.Id`; then put the id in a Type 11 (attachment) / 12 (image) field value `[id]` |
| Upload attachment (multipart) | `POST /platformapi/core/content/multipartattachment` | form parts `AttachmentName`, `AttachmentBytes` (file), `IsSensitive` |
| Data-gateway change notification | `PUT /platformapi/core/content/externalContentChangeNotification` (+override header shown) | `{"Alias":"ARCHER","ContentPartIds":["234811"],"ExternalFieldIds":["19649"]}` |

`Content` shape (response): `{Id, LevelId, SequentialId, FieldContents:{"<fieldId>":{Type, FieldId, Value|IpAddressBytes, IsError, UpdateInformation}}, CheckSum, LastUpdated, Version, Identity:{BaseContentId, Locators:[{Identity:{Value},Location:{Alias}}]}, UpdateInformation:{CreateDate,UpdateDate,CreateLogin,UpdateLogin}}`.
Read-only system fields show up with Types 6 (tracking id), 20 (record status), 21 (first published), 22 (last updated), 25 (history log) and no `Value`.
Field value shapes per `Type`: see `field-types.md`.

## 3. Metadata (System controller) - all GET (POST+override)

| Resource | Path | Notes |
|---|---|---|
| All applications | `/platformapi/core/system/application` | `$select=Name,Description`, `$orderby`, `$top/$skip`. Each: `{Id,Name,Alias,Guid,Description,KeepLicensed,IsDeprecated,...}` |
| Application by id | `/platformapi/core/system/application/<id>` | |
| Platform version | `/platformapi/core/system/applicationinfo/version` | |
| All levels | `/platformapi/core/system/level` | `{Id,ModuleId,Name,Alias,Guid,...}` |
| Level by id / by module / by reference field | `/system/level/<levelId>`, `/system/level/module/<moduleId>`, `/system/level/referencefield/<fieldId>` | x-ref may target several levels (array) |
| Level layout | `/system/levellayout/level/<levelId>` | |
| Field defs by application / level / field | `/system/fielddefinition/application/<appId>`, `/system/fielddefinition/level/<levelId>`, `/system/fielddefinition/<fieldId>` | OData only on base props: Id, LevelId, Type, Name, Alias, IsActive, Guid, ASOStatus, SystemType, IsPrivate, IsContentReadOnly, EsFieldMappingId, UpdateInformation, FieldMap. e.g. `$filter=Type eq 4`, `$select=Id,Name,Alias,Type` |
| Values-list field defs by level | `/system/fielddefinition/level/<levelId>/valueslist` | typed as ValuesListFieldDefinition → `RelatedValuesListId` usable |
| Field displays by level | `/system/fielddisplay/level/<levelId>` | |
| Fields referenced by event-rule filters | `/system/field/eventrulefilter/level/<levelId>` | |
| Values list definition | `/system/valueslist/<valuesListId>` | |
| Values list values flat / tree | `/system/valueslistvalue/flat/valueslist/<vlId>`, `/system/valueslistvalue/valueslist/<vlId>` | `{Id,Name,ValuesListId,ParentId,NumericValue,IsSelectable,SortOrder,Guid,...}` |
| Selected users/groups of a UG field | `/system/usergroupselection/usergrouplist/<fieldId>` | All Users/All Groups flags are on the field definition |
| Subform | `/system/subform/<subformId>` | |
| Questionnaires / by id | `/system/questionnaire`, `/system/questionnaire/<id>` | |
| Questionnaire rules by id / by level | `/system/questionnairerule/<id>`, `/system/questionnairerule/level/<levelId>` | |
| Event actions by id / by rule | `/system/eventaction/<id>`, `/system/eventaction/eventrule/<ruleId>` | data-driven events |
| Event rules by id / by level | `/system/eventrule/<id>`, `/system/eventrule/level/<levelId>` | |

Typical discovery chain: application → `level/module/<appId>` → `fielddefinition/level/<levelId>` → for Type 4 fields `valueslistvalue/flat/valueslist/<RelatedValuesListId>`.

## 4. Users, groups, roles, tasks, security parameters

### Users (`/platformapi/core/system/...`)
| Op | Request | Body |
|---|---|---|
| All users | `GET user` (POST+override; OData in body recommended) | `$filter=UserName eq 'jdoe'`, `$select=Id,UserName` |
| User by id / by group | `GET user/<userId>`, `GET user/group/<groupId>` | |
| Create | `POST user` | `{"User":{"FirstName","LastName",["UserName","AccountStatus":1,"SecurityId","LanguageId","Locale","TimeZoneId","Address","Company","Title","AdditionalNote","ForcePasswordChange","EnableApproveContentByEmail","DomainId"]},"Password":"..","Notification":true,"Roles":[..],"Groups":[..],"Contacts":[{"ContactType":7,"ContactSubType":2,"Value":"a@b","IsDefault":true}]}` → Id. Defaults: role General User, username `<lastname><firstinitial>`. |
| Update | `PUT user` | same shape with `User.Id`; **full replacement** (see SKILL.md). Domain users: send `DomainId`+`SecurityId`. `DefaultHomeDashboardId`+`DefaultHomeWorkspaceId` must be sent together. |
| Delete | `DELETE user/<userId>` | |
| Activate / deactivate | `POST user/status/active/<userId>`, `POST user/status/inactive/<userId>` | no body; AccountStatus 1 Active, 2 Inactive, 3 Locked |
| Change password | `PUT userpassword` | `{"UserId":1470,"NewPassword":"..."}` |
| Add/remove user↔group | `PUT usergroup` | `{"UserId":1470,"GroupId":16,"IsAdd":true|false}` |
| Add/remove user↔role | `PUT userrole` | `{"UserId":1470,"RoleId":3,"IsAdd":true|false}` |
| Contacts all / by user | `GET usercontact`, `GET usercontact/<userId>` | ContactType 7 Email, 9 Phone; subtypes 1 Assistant 2 Business 3 Business2 4 Business Fax 5 Home 6 Home2 7 Home Fax 8 ISDN 9 Mobile 10 Mobile2 11 Other 12 Other2 13 Other Fax 14 Pager (email cannot use 1,4,7,8,13) |
| My tasks | `POST task` + override (body) | `{"Value":"?$skip=0&$top=25&$filter=IsComplete eq false"}` → `{TaskId,Title,Description,DueDate,IsComplete,TargetContentId}` |

### Groups
| Op | Request | Body |
|---|---|---|
| All / by id / by user | `GET group` (POST+override), `GET group/<groupId>`, `GET group/user/<userId>` (POST+override) | `{Id,Name,DisplayName,Description(html),EveryoneFlag,Guid,SystemFlag,LdapFlag,DomainId,DistinguishedName,...}` |
| Create / update | `POST group`, `PUT group` | `{"Group":{"Id"?,"Name","Description"},"ParentGroups":[..]|null,"ChildGroups":[..]|null,"ChildUsers":[..]|null}` (null = unchanged, list = replace) |
| Delete | `DELETE group/<groupId>` | |
| Hierarchy | `GET grouphierarchy` | `{Id,RelatedId,Generation}` (0 self, 1 parent, ...) |
| Memberships | `GET groupmembership` | `{GroupId,UserIds,ParentGroupIds}` |
| Child group add/remove | `PUT groupmember` | `{"GroupId":<parent>,"GroupMemberId":<child>,"IsAdd":bool}` |
| Group↔role | `PUT rolegroup` | `{"GroupId":206,"RoleId":3,"IsAdd":bool}` |

### Roles
| Op | Request | Body |
|---|---|---|
| All / by user / memberships | `GET role`, `GET role/user/<userId>`, `GET rolemembership` | |
| Create | `POST role` | `{"AccessRole":{"Name","Description","IsDefault":false},"GroupIds":[..],"AccessRoleTasks":null}` |
| Update | `PUT role` | `{"AccessRole":{"Id","Name","Alias","Description","IsDefault"},"GroupIds":[..] (null/[] unassigns all),"AccessRoleTasks":[{"TaskId":"16165","HasCreate":true,"HasRead":true,"HasUpdate":false,"HasDelete":false}] or null}`. Clears the role's Default Home Page setting. |
| Delete | `DELETE role/<roleId>` | |

### Security parameters
`GET /system/securityparameter`, `GET /system/securityparameter/<id>`, `POST`/`PUT /system/securityparameter`, `DELETE /system/securityparameter/<id>`.
Body (create): `{"Name","Description","MinPasswordLength","AlphaCharsRequired","NumericCharsRequired","UppercaseCharsRequired","LowercaseCharsRequired","SpecialCharsRequired","PasswordChangeInterval","PasswordChangeLimit":false,"GraceLogins","MaximumFailedLoginAttempts","PreviousPasswordsDisallowed","LockoutPeriod","LockoutPeriodType":1h/2m/3d,"SessionTimeout","SessionTimeoutType":1h/2m/3d,"StaticSessionTimeout":null,"PasswordExpirationNotice","AutomaticAccountDeactivation","IsLimitByTimeFrame","PermittedFromTime","PermittedToTime","IsDisallowedByDays","DisallowedSessionDays":[bits 1 Sun..64 Sat],"IsDisallowedByDates","DisallowedDates":[{"LockedDate":"2015-04-01T00:00:00"}],"Default":false,"TimeZoneCode":"Central Standard Time","SecurityParameterType":2}`. Update adds `Id`, `Alias`, `GUID`.

## 5. Workflow actions (Advanced Workflow)
| Op | Request | Notes |
|---|---|---|
| Available actions | `GET /platformapi/core/system/WorkflowAction/<contentId>` (+override; documented `/api/core`) | `RequestedObject:{WorkflowNodeId:"18304:CUST",WorkflowNodeName,JobStatus,Actions:[{WorkflowTransitionId,WorkflowTransitionName,CompletionCode}]}` filtered by the user's read rights |
| Perform action | `POST /platformapi/core/system/WorkflowAction` | `{"ContentId":260068,"CompletionCode":1,"WorkflowNodeId":"17604:CUST"}` → `null` + 200. Ignores layout rules. |

## 6. Data feeds (`/platformapi/core/datafeed/...`)
| Op | Request | Body |
|---|---|---|
| Execute | `POST execution` | `{"DataFeedGuid":"<guid>","IsReferenceFeedsIncluded":false}` (user needs rights to run feeds) |
| Recent run | `POST history/recent` + override (body) | `{"Guid":"<guid>"}`; status 1 Running 2 Completed 3 Faulted 4 Warning 5 Terminating 6 Terminated 7 Pending |
| Run history | `POST history` + override (body) | `{"Guid":"<guid>"}` |
| History message | `GET historymessage/<historyId>` (+override) | |

## 7. Packages (`/api/core/package/...`, alias `/platformapi/core/package/...`)
Create `POST package/` `{"Name","Description","PreparedBy","PackageObjects":[{"Guid","Type":"Application"}]}` → Id ·
Generate `POST package/generate/<packageId>` · Upload `POST package/upload` (multipart zip) → Id ·
Download `GET package/download/<packageId>` (zip) · Install `POST package/install`
`{"PackageId","InactivateUnusedFields":false,"PrefixInactivatedFields":null,"InstallOptions":[{"Guid","Name","Type":"Application|GlobalReport|SubForm|...","TranslationOption":1,"InstallMethod":2,"InstallOption":1}]}`.
The UI's Manage Packages / Import and Install pages generate these bodies with the right GUIDs; copy from there.

## 8. Reports, deleted content, Smart Data Publications
| Op | Request | Body / notes |
|---|---|---|
| Security Events report | `POST /api/core/system/AccessControlReports/SecurityEvents?page=N` + override | `{"InstanceName":"Archer","EventType":"All Events","EventsForDate":"YYYY-MM-DD"}` (date 1–6 days ago; 50,000/page). Events: `{Event,InitiatingUser,Timestamp,EventDetails}`. Event types: All Events, Access Role Created/Deleted/Modified, Account Status Changed, Configuration Admin Added/Deleted, Content Admin Added/Deleted, Content Decrypted/Encrypted In Bulk, Login Failed, Full Module Content Delete, Report Permission Granted/Revoked, LDAP Configuration Delete Started/Completed, Login Retries Exceeded, Password Changed by Admin/by User, Pin Request Successful/Failed, Password Reset Requested, Role Assigned to User, Role Removed from User, Security Events Started/Stopped, Security Parameter Assignment Changed, Security Parameter Created/Deleted/Modified, SubForm Config Admin Added/Deleted, Translation Export/Import Requested, User Added, User Deleted, User Account Modified, User Added to Group, Full Name Modified, Login Success, Login Name Modified, Logout, User Removed from Group. Needs read rights to the report. |
| Field admin activity log | `POST /api/core/system/AdministrationActivityLogsReports/AdministrationActivityLogsReport?page=N` + override (also documented as `.../FieldAdministrationActivityLogsReport`) | `{"InitiatingUserId":2,"ActionsForDate":"YYYY-MM-DD","ApplicationId":635,"ActionType":"Field Creation"}` → `[{InitiatingUser,UserId,ModuleId,ModuleName,LevelId,LevelName,ObjectName,ActionType,PropertyName,NewValue,OldValue,Timestamp,SectionName}]` |
| Deleted content log | `GET /api/V2/DeletedContent?startDate=&endDate=&moduleid=&levelid=&skip=0&take=10000` | System Administrator or Deleted Record Auditor only. `{TotalRecords,RecordsShown,DeletedContents:[{ContentId,DeletedDateTime,UserId,ModuleId,LevelId}]}`; bad dates → 400 `CustomErrorResponse.InternalMessage` |
| Smart Data Publication export | `GET /api/core/smartdatapublication/download/<sdpId>` with `Accept: application/octet-stream` | zip stream; headers `Content-Disposition`, `zip-crc`; 400/500 on failure |

## 9. Content API (OData) - summary (full detail in `content-api.md`)
`GET /contentapi/` entity sets · `GET /contentapi/$metadata` · `GET /contentapi/<LevelAlias>?skip=&top=|all&$filter=&$select=&$orderby=` (≤1,000/page) ·
`GET /contentapi/<LevelAlias>(<contentId>)` · `GET /contentapi/<LevelAlias>_<FieldAlias>` relationship pairs ·
`POST /contentapi/<LevelAlias>` save (`"<LevelAlias>_Id":0` creates; other id updates; identical values → 400).

## 10. NGRX (SaaS only)
First call with `cookie: __ArcherSessionCookie__=<session token or PAT>` e.g. `GET /ngrx/record/v1/levels/<levelId>` → `Set-Cookie: <JWT>`; reuse that cookie. Swagger UI at `<tenant>/ngrx/record/swagger/index.html` (non-production tenants only) is the authoritative contract; fetch it from the user's tenant when NGRX endpoints beyond this are needed.
