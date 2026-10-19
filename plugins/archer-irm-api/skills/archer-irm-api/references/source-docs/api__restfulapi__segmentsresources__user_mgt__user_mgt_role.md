# Role Segment

The Role segment is accessed through the System controller, which includes the following resources:

On this page

  * Create role
    * Request
    * Request Header
    * Request Body
  * Delete role
    * Request
    * Request Header
  * Get all roles
    * Request
    * Request Header
  * Get role memberships
    * Request
    * Request Header
  * Get role by user ID
    * Request
    * Request Header
  * Update role
    * Request
    * Request Header
    * Request Body
    * Response Example

## Create role

The Create role resource creates an access role. The name field is required in the request body.

### Request

POST http://Archer/platformapi/core/system/role

### Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

### Request Body

AcessRoleTasks(permssions) are supported in this phase {"AccessRole": {"Name":"RoleA","Description":"This is a testrole","IsDefault":false},"GroupIds":[1,2],"AccessRoleTasks":null}

## Delete role

The Delete role resource deletes an access role.

### Request

DELETE http://Archer/platformapi/core/system/role/*roleid*

### Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

## Get all roles

The Get all roles resource retrieves all access roles.

### Request

GET http://Archer/platformapi/core/system/role

### Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

## Get role memberships

The Get role memberships resource retrieves memberships for all roles. Membership includes all users and all groups for a role.

### Request

GET http://Archer/platformapi/core/system/rolemembership

### Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

## Get role by user ID

The Get role by user ID resource retrieves the role for a user in the current Archer instance.

### Request

GET http://localhost/Archer/platformapi/core/system/role/user/*userid*

### Request Header

Accept:application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

## Update role

The Update role resource updates an access role. The ID, alias, and name fields are required in the request body.

**Important:** The API request deletes any Default Home Page field details for the role, such as a Dashboard. 

The following table describes required Request body parameter values and the results of including or excluding specific values when updating an Access Role. Parameter | Value | Result  
---|---|---  
AccessRole |  AccessRole not null. |  Depending on the provided properties, the Response succeeds or fails.  
Id |  Access Role ID not null. |  If the Access Role ID exists, the Response is successful.  
Id |  Access Role ID null. |  The Response fails with a Bad Request error.  
Name |  Access Role Name not null |  The Response is successful and the Access Role name is set to the Request body value.  
Name |  Access Role Name null. |  The Response fails with an error due to an invalid string value for the Access Role name.  
Alias |  The Alias must be a valid string. |  The Response is successful and the Alias is set to the Request body value.  
Alias |  Alias null. |  The Response fails due to an invalid string value for the Alias.  
GroupIds |  GroupIds null or contains an empty array. |  The response is successful and all groups are unassigned from the role.  
GroupIds |  GroupIds contains a valid array of integers. |  The Response is successful and the GroupId is set to the Request body value.  
GroupIds |  GroupIds contains an invalid array of integers. |  The Response fails with an error due to invalid GroupIds values.  
The following table describes optional Request body parameter values and the results of including or excluding specific values when updating an Access Role. Parameter | Value | Result  
---|---|---  
Description |  The Description must be a valid string. |  The Response is successful and the Description is set to the Request body value.  
Description |  Description null. |  The Response is successful and the Description is set to null.  
IsDefault |  True  False |  The Response is successful and IsDefault is set to the Request body value.  
IsDefault |  IsDefault null. |  The Response is successful and IsDefault is set to False.  
AccessRoleTasks |  AccessRoleTasks null. |  The Response is successful and AccessRoleTasks properties are not updated.  
AccessRoleTasks |  AccessRoleTasks not null. |  The Response is successful and AccessRoleTasks properties are updated to the Request body values.   
  
### Request

PUT http://Archer/platformapi/core/system/role

### Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

### Request Body

{

"AccessRole":

{

"Id":55,

"Name":"Role A",

"Description": "This is a test role",

"IsDefault": false,

"Alias": "Role_A"

},

"GroupIds": [59],

"AccessRoleTasks": [

{

"TaskId": "16165",

"HasCreate": true,

"HasRead": true,

"HasUpdate": false,

"HasDelete": false

}

]

}

### Response Example

{

"Links":[],

"RequestedObject":

{

"Id":1

},

"IsSuccessful":true,

"ValidationMessages":[]

}

