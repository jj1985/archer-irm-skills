# Archer Web Services API (SOAP)

Seven ASMX services under `https://<host>/<instance>/ws/`: `accesscontrol.asmx`, `accessrole.asmx`, `field.asmx`,
`general.asmx`, `module.asmx`, `record.asmx`, `search.asmx` (plus the fully disabled `technology.asmx`).
WSDL per service: `.../ws/<service>.asmx?WSDL`, also downloadable from Administration > Integration > Obtain API Integration,
which also offers a C# code generator that emits GUID constants for an application's fields and values.
Per-method signatures: `web-services-method-catalog.md`. Permissions: same as the user's UI rights; verb prefix implies
Create/Read/Update/Delete need (Create*, Get/Lookup/Search*, Add/Update/Set*, Delete/Remove/Terminate*).

## Transport
```
POST /Archer/ws/record.asmx HTTP/1.1
Content-Type: text/xml; charset=utf-8
SOAPAction: "http://archer-tech.com/webservices/CreateRecord"      (module.asmx uses http://tempuri.org/)

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CreateRecord xmlns="http://archer-tech.com/webservices/">
      <sessionToken>...</sessionToken><moduleId>17</moduleId><fieldValues>&lt;Record&gt;...&lt;/Record&gt;</fieldValues>
    </CreateRecord>
  </soap:Body>
</soap:Envelope>
```
Response: `<CreateRecordResponse><CreateRecordResult>int</CreateRecordResult></CreateRecordResponse>`. Methods that return XML
return it as an escaped string inside `<...Result>`; unescape then parse. SOAP 1.2 also accepted. Faults come back as `soap:Fault`
with the Archer exception message. `scripts/archer_soap.py` wraps all of this.

## Sessions (general.asmx)
- `CreateUserSessionFromInstance(userName, instanceName, password)` → 32-char token. Works even when SSO blocks REST login; the token is valid for REST calls too.
- `CreateDomainUserSessionFromInstance(username, instanceName, password, usersDomain)` for domain users.
- `TerminateSession(sessionToken)`. `CreateUserSession`/`CreateDomainUserSession` (no instance) are disabled.

## Records (record.asmx)
| Method | Use |
|---|---|
| `CreateRecord(sessionToken, moduleId, fieldValues)` → contentId | `fieldValues` = `<Record>` XML (see `field-types.md`) |
| `UpdateRecord(sessionToken, moduleId, contentId, fieldValues)` → 1 | only listed fields change; updates locked records |
| `CreateRecords` / `UpdateRecords(sessionToken, moduleId, contentRecords)` | `<Records><Record>...</Record>...</Records>`; UpdateRecords returns XML of failures |
| `CreateSubformRecord(sessionToken, subformModuleId, subformFieldId, fieldValues)` → subform contentId, then reference it from the parent's sub-form field |
| `CreateQuestionnaireRecord(sessionToken, questionnaireModuleId, targetContentId)` | |
| `GetRecordById(sessionToken, moduleId, contentId)` → record XML (moduleId ignored) |
| `DeleteRecord(sessionToken, moduleId, contentId)` |
| `GetChildRecordIds(sessionToken, moduleId, contentId)`; `GetAccessHistory(sessionToken, contentId)` |
| `GetAttachmentFile(sessionToken, fileId)` → `<files><file id name length>base64</file></files>` |
| `CreateCMSTEntry(sessionToken, contentId, fieldId, parentId, valueId, comments)` for CAST |
| Mail merge: `PerformMailMerge(sessionToken, contentId, templateId)` → bytes; async `StartAsyncMailMerge` → exportId, `CheckAsyncMailMergeProgress`, `GetAsyncMailMergeDocument` |

## Search (search.asmx)
`ExecuteSearch(sessionToken, searchOptions, pageNumber)` → XML records; `ExecuteStatisticSearch(sessionToken, searchOptions, pageNumber)` → grouped aggregates;
`SearchRecordsByReport(sessionToken, reportIdOrGuid, pageNumber)` / `ExecuteStatisticSearchByReport` run a saved report; `GetReports(sessionToken)` lists reports;
`GetSearchOptions(sessionToken, reportId)` / `GetSearchOptionsByGuid` return a saved report's `searchOptions` XML you can edit and resubmit;
`ExecuteQuickSearchWithModuleIds(sessionToken, moduleIds, keywords, pageNumber, pageSize)` / `ExecuteQuickSearchWithSolutionId`.
Deprecated: `SearchRecords`, `RetrieveSearchResultsPage[ByPageSize]`, `CheckSearchStatus[ByPageSize]` (use `ExecuteSearch`); `SearchRecordsByField` disabled.
Prefer field/module **GUIDs** over integer ids in search XML (both accepted). Paging: set `<PageSize>`, iterate `pageNumber` 1..n until fewer rows than PageSize.
Dates with time appear as `12:00:00 AM` when the field is date-only.

### `SearchReport` grammar (ExecuteSearch)
```xml
<SearchReport>
  <PageSize>100</PageSize>                                   <!-- required -->
  <MaxRecordCount>1000</MaxRecordCount>                      <!-- optional -->
  <DisplayFields><DisplayField>9402</DisplayField><DisplayField>{GUID}</DisplayField></DisplayFields>   <!-- or ContainedDisplayFields -->
  <ContainedDisplayFields>                                   <!-- for sub-form / history-log fields -->
    <ContainedDisplayField><Field>12977</Field><DisplayFields><DisplayField>12972</DisplayField></DisplayFields></ContainedDisplayField>
  </ContainedDisplayFields>
  <Criteria>
    <Keywords>Windows</Keywords>                             <!-- optional; needs IsKeywordModule true -->
    <ModuleCriteria>
      <Module>331</Module>                                   <!-- app/questionnaire id or GUID -->
      <IsKeywordModule>false</IsKeywordModule>
      <BuildoutRelationship>Union</BuildoutRelationship>     <!-- Union (outer) | Intersection (inner) -->
      <LeveledBuildoutOptions>BuildUp</LeveledBuildoutOptions>
      <SortFields><SortField><Field>9399</Field><SortType>Ascending</SortType></SortField></SortFields>
      <Children><ModuleCriteria> ...related module, same elements, LeveledBuildoutOptions BuildDown... </ModuleCriteria></Children>
    </ModuleCriteria>
    <Filter>
      <OperatorLogic>1 AND (2 OR NOT 3)</OperatorLogic>      <!-- 1-based condition numbers; omit = AND all -->
      <Conditions>
        <TextFilterCondition><Operator>Contains</Operator><Field>9402</Field><Value>A comment</Value></TextFilterCondition>
        <NumericFilterCondition><Operator>GreaterThan</Operator><Field>5</Field><ParentField>8</ParentField><Value>22.5</Value></NumericFilterCondition>
        <DateComparisonFilterCondition><Operator>Equals</Operator><Field>5</Field><Value>1/1/2008</Value><TimeZoneId>Central Standard Time</TimeZoneId><IsTimeIncluded>TRUE</IsTimeIncluded></DateComparisonFilterCondition>
      </Conditions>
    </Filter>
  </Criteria>
</SearchReport>
```
Filter condition elements (all take `<Field>` = GUID or id, optional `<ParentField>` for sub-form fields):

| Condition | Operators | Extra elements |
|---|---|---|
| `TextFilterCondition` | Equals, DoesNotEqual, Contains, DoesNotContain | `Value` (special chars **double**-encoded: `&amp;amp;`, `&amp;quot;`, `&amp;#39;`, `&amp;lt;`, `&amp;gt;`) |
| `NumericFilterCondition` | Equals, NotEqual, GreaterThan, LessThan | `Value` |
| `NumericBetweenFilterCondition` | Between | `BeginValue`, `EndValue` |
| `NumericRangeFilterCondition` | Contains, DoesNotContain | `Values/Value` = numeric range ids |
| `DateComparisonFilterCondition` | Equals, DoesNotEqual, GreaterThan, LessThan, AfterToday, PriorToToday | `Value`, `TimeZoneId`, `IsTimeIncluded` |
| `DateRangeFilterCondition` | Between | `BeginValue`, `EndValue`, `TimeZoneId`, `IsTimeIncluded` |
| `DateTimeRangeFilterCondition` | (none) | `BeginDate`, `BeginTime`, `EndDate`, `EndTime`, `TimeZoneId`, `IsTimeIncluded` |
| `DateOffsetFilterCondition` | LastXDays/Months/Quarters/Years, NextXDays/Months/Quarters/Years | `Value` (integer) |
| `CurrentDateFilterCondition` | CurrentDay, CurrentMonth, CurrentQuarter, CurrentYear | |
| `ValueListFilterCondition` | Equals, DoesNotEqual, Contains, DoesNotContain | `Values/Value` = value ids, `IsNoSelectionIncluded`, `IncludeChildren` |
| `UserGroupFilterCondition` | Equals, DoesNotEqual, Contains, DoesNotContain | `Users/User`, `Groups/Group` ids, `IsNoSelectionIncluded` |
| `ReferenceFilterCondition` | Equals, DoesNotEqual, Contains, DoesNotContain | `<Level id="1"><Content>5</Content></Level>`, `IsNoSelectionIncluded` |
| `ContentFilterCondition` | Equals, DoesNotEqual | `Level`, `Values/Value` = record ids ("filter by record") |
| `RecordStatusFilterCondition` | Equals, DoesNotEqual | `RecordStatusType` New / Updated |
| `MatrixFilterCondition` | Equals, DoesNotEqual, Contains, DoesNotContain | `<Row id="1"><Column>5</Column></Row>`, `IsNoSelectionIncluded` |
| `IpAddressFilterCondition` | Equals, DoesNotEqual | `Octet1..4` (v4) or `Value` (v4/v6) |
| `CastFilterCondition` | Equals, DoesNotEqual, Contains, DoesNotContain | `Value` = values list id/GUID |

Time-based filtering (Equals/Between/Time Interval etc.) needs the date field configured to show time; rules in `source-docs/api__webapi__time_based_filters_api.md`.

### `SearchStatisticReport` grammar (ExecuteStatisticSearch)
```xml
<SearchStatisticReport>
  <PageSize>5</PageSize><ShowStatSummaries>false</ShowStatSummaries>
  <Criteria><ModuleCriteria><Module>89</Module></ModuleCriteria><Filter>...</Filter></Criteria>
  <StatisticCriteria>
    <StatisticSteps>
      <StatisticStep><Field>698</Field><StepIndex>0</StepIndex><Name>Engagement Types</Name><StepType>GroupBy</StepType></StatisticStep>
      <StatisticStep><Field>670</Field><StepIndex>1</StepIndex><Name>Count</Name><StepType>Count</StepType></StatisticStep>
    </StatisticSteps>
    <SortSteps><SortStep><StepIndex>1</StepIndex><SortType>Descending</SortType></SortStep></SortSteps>
    <IncludeEmptyGroups>true</IncludeEmptyGroups>
  </StatisticCriteria>
</SearchStatisticReport>
```
StepType: Count, DateAggregate (Action Min/Max), GroupBy, GroupByDateRange (Action GroupByDay/Week/Month/Quarter/Year), GroupByHierarchicalValuesList (needs `DepthField`, 0-based), GroupByMatrix (Action Row/Column), NumericAggregate (Action Average/Min/Max/Sum/Median/Mode).
Output: `<Groups count><Metadata>...</Metadata><Group FieldId Value><Aggregates><Aggregate FieldId Count|Sum.../></Aggregates></Group>...</Groups>`.

### Legacy `<Search>` XML (quick/keyword searches, older methods)
```xml
<Search>
  <Keywords value="Windows" />                       <!-- supports "phrase", wild*, fuzzy~, AND/OR; default OR -->
  <Display><Field id="7205" /><Field id="7226" /></Display>
  <KeywordModules><Module id="17" /></KeywordModules>
  <PrimarySort id="7205" order="ASC" /><SecondarySort id="7226" order="DESC" />
  <DisplayFormat value="3" />                        <!-- 3 = summary, only value -->
  <Matching><Field id="7612"><Include noValues="1"><Value value="1740" /></Include></Field></Matching>  <!-- values-list filter; Exclude also allowed -->
  <Workflow value="1" /><Published value="1" /><MyRecord value="1" />   <!-- special characteristics -->
</Search>
```

## Users, groups, roles, values lists (accesscontrol / accessrole / field)
Typical sequence (from the help's C# sample):
```
id = accesscontrol.CreateUserEx(token, "First","Middle","Last","Company","Title", securityParamId, "Address", "", "Central Standard Time", "en-US")
accesscontrol.ChangePassword(token, id, "NewPassword"); accesscontrol.ForcePasswordChange(token, id, false)
accesscontrol.AddUserToRole(token, id, roleId); accesscontrol.AddUserToGroup(token, id, groupId); accesscontrol.UpdateUserName(token, id, "login")
accesscontrol.AddContactInfo(token, id, "<ContactInfo><ContactTypeId>7</ContactTypeId><ContactSubTypeId>2</ContactSubTypeId><ContactInfo>a@b.com</ContactInfo><ContactDefault>true</ContactDefault></ContactInfo>")
```
Lookups: `LookupUserId(userName)`, `LookupUserName(userId)`, `LookupUserByFirstName/LastName(keyword)`, `LookupGroup(keyword)`, `LookupEveryoneGroup()`,
`GetUserListPaginated(pageSize, page)`, `GetDomainUserList*`. Values lists: `GetValueListForField(fieldId)`, `LookupListValue(fieldId, keyword)` → value id,
`CreateValuesListValue(valuesListId, name)`, `CreateValuesListItemWithNumericValue`, `UpdateValuesListValue`, `DeleteValuesListValue`, `GetFieldIdByGUID`,
`GetValuesListIdByGUID`, `GetValuesListValueIdByGUID`. Module: `GetModuleIdByGUID(instanceId, GUID)`. Roles: `CreateRole`, `UpdateRole`, `GetRoles`,
`GetRolePagePermissions[ForModule]`, `UpdateRolePagePermissions2` (v1 deprecated). `CreateUser`/`UpdateUser` deprecated → `CreateUserEx`/`UpdateUserEx`.

## Deprecated and disabled (as of 5.x; still true in 2026.08)
Deprecated: CheckSearchStatus, CheckSearchStatusByPageSize (always 100), CreateUser→CreateUserEx, RetrieveSearchResultsPage[ByPageSize]→ExecuteSearch,
SearchRecords→ExecuteSearch, UpdateUser→UpdateUserEx, UpdateRolePagePermissions→UpdateRolePagePermissions2.
Disabled: whole Technology class (→ CreateRecord/UpdateRecord/DeleteRecord/GetRecordById/ExecuteSearch), Bind/Unbind*LevelContent (→ UpdateRecord),
CreateChildValuesListItemWithNumericValue, CreateValuesListValueChild, GetValueListByParent, CreateUserSession/CreateDomainUserSession (→ *FromInstance),
DeleteAllRecords, GetParentRecordIds (→ GetRecordById), GetTimeZones, UseDaylightSavings, SearchRecordsByField.
