# Data Gateway API (`/platformapi/DataGateway/...`)

Data Gateway maps fields of an Archer level directly onto an external data set (no copy, unlike data feeds). Must be enabled per
instance in the Archer Control Panel; the API user needs role rights to Data Gateway. Property *names* are case-insensitive, *values* case-sensitive.
Errors arrive as `IsSuccessful:false` with `MessageKey` such as `ValidationMessageTemplates:DataGatewayNotEnabled`,
`InvalidDataGatewayConnectionOrLevel`, `InvalidDatagatewayLevelFieldMapping`, `DataGatewayTestError`.

| Op | Request | Body / result |
|---|---|---|
| List connections | `GET Connections[?$filter=targetId eq 530]` | `RequestedObject:[{TargetId,TargetName,Connection:{Id,LocationAlias,LastUpdated,DatagatewayConnector:{ConnectorType}}}]` |
| Add connection | `POST Connections` | `{"TargetId":<levelId>,"Connection":{"LocationAlias":"EXT_SQL2" (≤10 chars),"DatagatewayConnector":{"ConnectorType":"ArcherTech.Datasource.Content.GenericSql.GenericSqlDataSource","Properties":[{"Name":"dbProviderType","Value":"System.Data.SqlClient"},{"Name":"connectionString","Value":"..."},{"Name":"tableName","Value":"EXT_SR"},{"Name":"idColumnName","Value":"ext_sr_id"},{"Name":"idColumnType","Value":"int"}]}}}` → `RequestedObject:<connectionId>` |
| Edit connection | `PUT Connections` | same with `Connection.Id`; `LocationAlias`/`TargetId` ignored |
| Test connection | `POST Connections/Test` | body = the `DatagatewayConnector` object; `RequestedObject:true/false` (custom connectors must implement test) |
| Delete connection | `DELETE Connections?connection=<LocationAlias>` | async → `RequestedObject:{JobId}`; clears field and content maps, affected fields go blank |
| Get field maps | `GET FieldMaps[?$filter=DataGatewayFieldMaps/any(dgfm:dgfm/targetId eq 335) and DataGatewayFieldMaps/any(dgfm:dgfm/Connections/any(conn:conn/Name eq 'SQLCON1'))]` | `[{ModuleId,ModuleName,DataGatewayFieldMaps:[{TargetId,TargetName,Connections:[{Name,FieldMapping:[{SourceFieldId,ArcherFieldId}]}]}]}]` |
| Add/edit field maps | `PUT` or `POST FieldMaps` | `{"TargetId":375,"Connections":[{"Name":"GENERICSQL","FieldMapping":[{"SourceFieldId":"Column1","ArcherFieldId":22404}]}]}` → `{ProcessedIds,RejectedIds}`; partial success = `IsSuccessful:false` |
| Revert field maps | `PUT`/`POST FieldMaps` | same shape with connection `"Name":"ARCHER"` and only `ArcherFieldId` entries |
| Get content maps | `GET ContentMaps/?connection=<alias>[&$top=50&$skip=100]` | default 100, max `$top` 1000: `{TargetId,LocationAlias,ContentMaps:[{ContentPartId,TrackingId}]}` |
| Add/edit content maps | `PUT`/`POST ContentMaps` | `{"TargetId":328,"LocationAlias":"STIG_DATA","ContentMaps":[{"TrackingId":249457,"ContentPartId":"1"}]}` (TrackingId = Archer content id; ContentPartId = external key ≤100 chars) |
| Delete content maps by content | `DELETE ContentMaps/Delete` | `{"LocationAlias":"STIG_DATA","ContentMaps":[{"TrackingId":249457}]}` |
| Delete all content maps of a connection | `DELETE ContentMaps/DeleteAll/?connection=<alias>` | async → `{JobId}` |
| Notify Archer of external change | `PUT /platformapi/core/content/externalContentChangeNotification` | `{"Alias":"ARCHER","ContentPartIds":["234811"],"ExternalFieldIds":["19649"]}` |

Supported mapped field types: Flexible SQL Connector → Date, IpAddress, Numeric, Text; custom connectors add Attachment, ExternalLinks, Image, Matrix,
RecordPermissions, Scheduler, Users/Groups Lists, ValuesList, Voting. Field maps require the connection, level (`TargetId`) and `ArcherFieldId` to agree.
Records read through `content/contentid` show gateway-backed parts in `Identity.Locators[].Location.Alias` (`ARCHER` = native, otherwise the connection alias).
Example bodies: `source-docs/examples/restfulapi__segmentsresources__dg_ex__*.txt`.
