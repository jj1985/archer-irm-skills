# Archer field types and value encodings

The integer `Type` is shared by REST `FieldContents`, REST field definitions, and the SOAP `type=` attribute.

| Type | Field type | REST read | REST write (Post/Put content) | Content API | SOAP write (CreateRecord/UpdateRecord XML) |
|---|---|---|---|---|---|
| 1 | Text (single line, text area, rich/HTML) | yes | yes | yes | yes |
| 2 | Numeric | yes | yes | yes | yes |
| 3 | Date / Date+time | yes | yes | yes | yes |
| 4 | Values List | yes | yes | yes | yes |
| 6 | Tracking ID | read-only | - | (as `<Alias>_Id`) | read-only |
| 7 | External Links | yes | yes | no | yes |
| 8 | Users/Groups List (also Record Permissions) | yes | yes | yes | yes (type 8; Record Permissions = 15 in SOAP) |
| 9 | Cross-Reference | yes | yes | yes | yes |
| 11 | Attachment | yes | yes (by attachment id) | no | read-only |
| 12 | Image | yes | yes (by attachment id) | no | read-only |
| 14 | CAST (Cross-Application Status Tracking) | yes | no | no | via `record.CreateCMSTEntry` |
| 16 | Matrix | yes | yes | no | yes |
| 18 | Cross-Reference (internal relationship) | - | - | - | yes (SOAP only) |
| 19 | IP Address | yes | yes | yes | yes |
| 20 | Record Status | read-only | - | no | read-only (`New`/`Updated`) |
| 21 | First Published | read-only | - | yes | read-only |
| 22 | Last Updated | read-only | - | yes | read-only |
| 23 | Related Records | yes | yes | yes | (via 9/18 semantics) |
| 24 | Sub-Form | yes | yes | yes | sub-form record via `record.CreateSubformRecord` |
| 25 | History Log | yes (content/history) | - | no | - |
| 27 | Multiple Reference Display Control | - | - | - | - |
| 28 | Questionnaire Reference | - | - | - | - |
| 29 | Access History | - | - | - | `record.GetAccessHistory` |
| 30 | Voting | - | - | - | - |
| 31 | Scheduler | - | - | - | - |
| 1001 | CAST Field Value | read (SOAP) | - | - | read-only |

Calculated Text/Numeric/Date/Values List fields and rule-driven Record Permissions fields are read-only through every API.

## REST `FieldContents` entry shapes

Every entry: `"<fieldId>": {"Type": <t>, "FieldId": <fieldId>, "Tag": "<optional label, ignored>", "Value": ...}`.
Omit a field to leave it unchanged (update) or empty (create). Do not add `Tag` or any extra property to Type 19.

```jsonc
"9402":  {"Type":1,  "FieldId":9402,  "Value":"plain text or <p>HTML</p>"}
"1234":  {"Type":2,  "FieldId":1234,  "Value":123450.6789}
"123451":{"Type":3,  "FieldId":123451,"Value":"10/21/1956 11:59AM"}     // also "2016-12-14", "2014-03-06T21:30:00"
"123453":{"Type":3,  "FieldId":123453,"Value":"0"}                      // null date
"34564": {"Type":4,  "FieldId":34564, "Value":{"ValuesListIds":[2,3,4],"OtherText":"Severity"}}
"34563": {"Type":4,  "FieldId":34563, "Value":{0}}                      // null values list (as documented; {"ValuesListIds":[]} also clears on most builds)
"11234": {"Type":7,  "FieldId":11234, "Value":[{"Name":"Archer","Url":"https://www.archerirm.com"}]}
"12234": {"Type":8,  "FieldId":12234, "Value":{"UserList":[{"Id":19},{"Id":20}],"GroupList":[{"Id":1}]}}  // UserList/GroupList may be null
"13877": {"Type":8,  "FieldId":13877, "Value":{"UserList":[{"Id":190}],"GroupList":[{"Id":19}]}}            // Record Permissions uses Type 8 too
"12235": {"Type":9,  "FieldId":12235, "Value":[{"ContentId":205522},{"ContentId":205643}]}
"12334": {"Type":11, "FieldId":12334, "Value":[1234]}                   // attachment ids from Post attachment
"12335": {"Type":12, "FieldId":12335, "Value":[2234]}                   // image = attachment id, Type 12
"15674": {"Type":16, "FieldId":15674, "Value":[{"RowId":63800,"ColumnId":63823}]}
"14410": {"Type":19, "FieldId":14410, "IpAddressBytes":"127.0.0.1"}     // NO Value, NO Tag
"18975": {"Type":23, "FieldId":18975, "Value":[345155,234512]}          // related record content ids
"13886": {"Type":24, "FieldId":13886, "Value":[339019]}                 // sub-form record content ids (create them first with SubformFieldId)
```

Nulls: omit the field for most types; Date needs `"0"`, Values List `{0}` (or empty list), Users/Groups an object with empty/null lists.

Response entries add `IsError`, `UpdateInformation` and, for system fields (6, 20, 21, 22), no `Value`.

## Content API (alias-keyed) shapes

Read: text/number/date as JSON scalars; values list as `["Value text", ...]`; cross-ref/related as `[contentId, ...]`;
users/groups as objects. Write (`POST /contentapi/<LevelAlias>`):

```json
{
  "Exception_Requests_Id": 0,
  "Risk_Rating": {"ValuesListIds": [1199]},
  "Submitter": {"UserList": [{"Id": 2}]},
  "Submission_Due_Date": "07/07/2018",
  "Exception_Description": "text",
  "Business_Unit": [226446]
}
```

## SOAP XML input (CreateRecord / UpdateRecord / CreateSubformRecord `fieldValues`)

Root `<Record>` (or `<UpdateRecord>`; multiple records wrapped in `<Records>` for CreateRecords/UpdateRecords).
`id` = field ID; `type` optional on input except where noted; all fields must belong to one level.

```xml
<Record>
  <Field id="9402" value="Text, UTF-8 ok" />
  <Field id="9403" value="&lt;p&gt;HTML must be XML-encoded&lt;/p&gt;" />
  <Field id="123"  value="125.75" />                                  <!-- numeric; smallest unit of measure -->
  <Field id="9412" value="12/31/2099 11:59AM" /> <Field id="9411" value="01/01/1980" /> <Field id="42065" value="0" /> <!-- date; "0" = null -->
  <Field id="4870" value="2"><MultiValue value="3" /><MultiValue value="4" /></Field>   <!-- values list ids -->
  <Field id="4871" value="4181" type="4" otherText="MyTextItem" />    <!-- values list with Other text -->
  <Field id="8323" type="4" value="0"></Field>                        <!-- null values list -->
  <Field id="9413" value="Archer" link="http://example"><MultiValue value="Other" link="http://other" /></Field> <!-- external links -->
  <Field id="9420"><Users><User id="221" /></Users><Groups><Group id="91" /></Groups></Field>          <!-- type 8 users/groups; type 15 record permissions same shape -->
  <Field id="9424" value="1000"><MultiValue value="1001" /></Field>   <!-- cross-reference / related (type 9 / 18): content ids -->
  <Field id="9423" rowId="1253" columnId="730"><MultiValue rowId="1254" columnId="728" /></Field>      <!-- matrix -->
  <Field id="9415" value="191.167.0.255" /> <Field id="9429" value="0054:0230:0253:0511:0747:0066:0034:0023" /> <!-- IP v4/v6 -->
</Record>
```

Single value: no `MultiValue` sub-element. Attachments/Images cannot be written via SOAP. CAST via `record.CreateCMSTEntry`.

## SOAP XML output (GetRecordById / ExecuteSearch results)

Common attributes on every `<Field>`: `id`, `type`, `createDate`, `updateDate` (`MM/DD/YYYY HH:MM:SS AM`), `createLogin`, `updateLogin`.
Per type: 1 `value` (HTML double-encoded) · 2 `value` + `<UnitOfMeasure id value unitLabel/>` children · 3 `value="7/8/1999 6:50 AM"` ·
4 `value` + `<MultiValue value/>` · 6 `value` tracking id · 7 `value`+`link` + MultiValue · 8/15 `<Groups><Group id name desc/></Groups><Users><User id firstName lastName/></Users>` ·
9 `<Reference id="269954">display</Reference>` children (+ `guid` attr on Field) · 11/12 `fileID fileName width height` (+ MultiValue) ·
16 `rowId rowValueName rowValueColor columnId columnValueName columnValueColor` (+ MultiValue) · 19 `value` · 20 `value="New|Updated"` · 21/22 `value` date ·
1001 CAST `childFieldId childModuleId childModuleName totalCount` + `<RecordValue selectValueId selectValueName selectValueDefaultFlag selectValueColor count/>`.
`search.ExecuteSearch` responses include a `<Metadata><FieldDefinitions><FieldDefinition id name alias guid/>` block.

## Dates

REST accepts `M/d/yyyy h:mmtt`, `yyyy-MM-dd`, ISO `yyyy-MM-ddTHH:mm:ss`; returns ISO (`2019-12-06T21:09:46.137`). SOAP uses `MM/DD/YYYY [H:MM AM/PM]`.
Date-only fields default the time to 12:00 AM. Time zones for users/search: Windows IDs such as `Central Standard Time` (list in `source-docs/api__webapi__timezones.md`); locales like `en-US` (`source-docs/api__webapi__locales.md`).
