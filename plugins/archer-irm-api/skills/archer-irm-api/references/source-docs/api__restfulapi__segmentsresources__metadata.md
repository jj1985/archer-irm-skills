# Metadata

The Medadata segment is accessed through the System controller. Actions taken on a resource determine the type of action that can be performed.

The following table shows the actions that can be taken on each resource, including the URI and object type of the resource. Segment |  Resource |  URI |  $filter |  $select |  $top |  $skip |  $orderby  
---|---|---|---|---|---|---|---  
[Application](metadata_application.htm) |  application - by id |  /system/application/applicationid |  |  |  |  |   
|  application - all |  /system/application |  |  |  |  |   
|  application version |  /system/applicationinfo/version |  |  |  |  |   
[Event](metadata_event_actions_rules.htm) |  event action - by id |  /system/eventaction/eventactionid |  |  |  |  |   
|  event action - by event rule |  /system/eventaction/eventrule/eventruleid |  |  |  |  |   
|  event rule - by ID |  /system/eventrule/eventruleid |  |  |  |  |   
|  event rule - by level |  /system/eventrule/level/levelid |  |  |  |  |   
[Field](metadata_field.htm) |  field content - by field ID |  /system/content/fieldcontent |  |  |  |  |   
|  field definition - by ID |  /system/fielddefinition/fieldid |  |  |  |  |   
|  field definition - by application ID |  /system/fielddefinition/application/*applicationid* |  |  |  |  |   
|  field definition - by level |  /system/fielddefinition/level/levelid |  |  |  |  |   
|  field definition - by level for ValuesList |  /system/fielddefinition/level/levelid/valueslist |  |  |  |  |   
|  field display - by level |  /system/fielddisplay/level/levelid |  |  |  |  |   
|  field id - by eventrule filter by level |  api/system/field/eventrulefilter/level/levelId |  |  |  |  |   
[Level](metadata_level.htm) |  level - by id |  /system/level/levelid |  |  |  |  |   
|  level - by module |  /system/level/module/moduleid |  |  |  |  |   
|  level - by reference field |  /system/level/referencefield/fieldid |  |  |  |  |   
|  level - all |  /system/level |  |  |  |  |   
|  level layout - by level id |  /system/levellayout/levelid |  |  |  |  |   
[Questionnaire](metadata_questionnaire.htm) |  questionnaire - by id |  /system/questionnaire/questionnaireid |  |  |  |  |   
|  questionnaire - all |  /system/questionnaire |  |  |  |  |   
|  questionnaire rule - by id |  /system/questionnairerule/id |  |  |  |  |   
|  questionnaire rule - by level |  /system/questionnairerule/level/levelid |  |  |  |  |   
[Security](metadata_security.htm) |  security parameter - by id |  /system/securityparameter/securityparameterid |  |  |  |  |   
|  security parameter - all |  /system/securityparameter |  |  |  |  |   
|  security parameter - create |  /system/securityparameter |  |  |  |  |   
|  security parameter - update |  /system/securityparameter |  |  |  |  |   
|  security parameter - delete |  /system/securityparameter/*securityparameterid* |  |  |  |  |   
[Subform](metadata_subform.htm) |  subform - by id |  /system/subform/subformid |  |  |  |  |   
[Values List](metadata_values_list.htm) |  values list definition - by id |  /system/valueslist/id |  |  |  |  |   
|  values list value - by values list id (flat) |  /system/valueslistvalue/flat/valueslist/valueslistid |  |  |  |  |   
|  values list value - by values list id (hierarchical) |  /system/valueslistvalue/valueslist/valueslistid |  |  |  |  |   
  
**Note:** The following properties are allowed with the $filter, $select, and the $orderby actions in the OData query on the field definition resources available in the table above:

  * Id
  * LevelId
  * Type
  * Name
  * Alias
  * IsActive
  * Guid
  * ASOStatus
  * SystemType
  * IsPrivate
  * IsContentReadOnly
  * EsFieldMappingId
  * UpdateInformation
  * FieldMap

