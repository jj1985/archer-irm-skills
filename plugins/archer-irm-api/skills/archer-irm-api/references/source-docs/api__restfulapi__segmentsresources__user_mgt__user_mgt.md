# User Management

Actions taken on a resource determine the type of action that can be performed.

The following table shows the actions that can be taken on each resource, including the URI and object type of the resource. Segment |  Resource |  URI |  $filter |  $select |  $top |  $skip |  $orderby  
---|---|---|---|---|---|---|---  
[Group](user_mgt_group.htm) |  group - by ID |  /system/group/groupid |  |  |  |  |   
|  group - by user |  /system/group/user/userid |  |  |  |  |   
|  group - all |  /system/group |  |  |  |  |   
|  group hierarchy - all |  /system/grouphierarchy  |  |  |  |  |   
|  group - create |  /system/group |  |  |  |  |   
|  group - update |  /system/group |  |  |  |  |   
|  group - delete |  /system/group/*groupid* |  |  |  |  |   
|  group membership - all |  /system/groupmembership |  |  |  |  |   
|  group - add member |  /system/groupmember |  |  |  |  |   
|  group - remove member |  /system/groupmember |  |  |  |  |   
|  group - add to role |  /system/rolegroup |  |  |  |  |   
|  group - remove from role |  /system/rolegroup |  |  |  |  |   
[Role](user_mgt_role.htm) |  role - all |  /system/role |  |  |  |  |   
|  role - by user ID |  /system/role/user/*userid* |  |  |  |  |   
|  role - memberships |  /system/role |  |  |  |  |   
|  role - create |  /system/role |  |  |  |  |   
|  role - update |  /system/role |  |  |  |  |   
|  role - delete |  /system/role/*roleid* |  |  |  |  |   
[Selected User Group](../metadata_selected_user_group.htm) |  selected user group - by field id |  /system/usergroupselection/fieldid |  |  |  |  |   
[User](user_mgt_user.htm) |  user - tasks |  /system/task |  (Only for IsComplete) |  |  |  |   
|  user - by id |  /system/user/userid |  |  |  |  |   
|  user - by group |  /system/user/group/groupid |  |  |  |  |   
|  user - all |  /system/user |  |  |  |  |   
|  user - create |  /system/user |  |  |  |  |   
|  user - update |  /system/user |  |  |  |  |   
|  user - delete |  /system/user/*userid* |  |  |  |  |   
|  user - activate |  /system/user/status/active/*userid* |  |  |  |  |   
|  user - deactivate |  /status/inactive/*userid* |  |  |  |  |   
|  user - change password |  /system/userpassword |  |  |  |  |   
|  user - add to group |  /system/usergroup |  |  |  |  |   
|  user - remove from group |  /system/usergroup |  |  |  |  |   
|  user - add to role |  /system/userrole |  |  |  |  |   
|  user - remove from role |  /system/userrole |  |  |  |  |   
|  user contacts- all  |  /system/usercontact |  |  |  |  |   
|  user contacts - by user ID |  /system/usercontact/*userid* |  |  |  |  |   
  
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

