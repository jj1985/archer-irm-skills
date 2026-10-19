# User Segment

On this page

  * Activate user
  * Add user to role
  * Add user to user group
  * Change user password
  * Create user
    * Rules for creating users
  * Deactivate user
  * Delete user
  * Get all users
  * Get all user contacts
  * Get contact information for a user
    * Contact types and contact subtypes
  * Get user by ID
  * Get users by group
  * Get user tasks
  * Remove user from user group
  * Remove user from role
  * Update user
    * Null in user values

The User segment is accessed through the System controller, which includes the following resources:

## Activate user

The Activate user resource changes the user status to Active.

Request

POST http://Archer/platformapi/core/system/user/status/active/*userid*

POST http://Archer/platformapi/core/system/user/status/active/1470

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

none

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":1470

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Add user to role

The Add user to role resource adds a user to an access role.

**Note:** The user and role must exist.

Request

PUT http://Archer/platformapi/core/system/userrole

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"UserId":1470,

"RoleId":3,

"IsAdd":true

} 

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":3

},

"IsSuccessful":true,

"ValidationMessages":[]

} 

## Add user to user group

The Add user to user group resource adds a user to a group.

**Note:** The user and group must exist.

Request

PUT http://Archer/platformapi/core/system/usergroup

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"UserId":1470,

"GroupId":16,

"IsAdd":true

}

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":16

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Change user password

The Change user password resource changes the user password.

Request

PUT http://Archer/platformapi/core/system/userpassword

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"UserId":1470,

"NewPassword":"Brilliant123!"

}

Response Example

{

"Links":[],

"RequestedObject":{},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Create user

The Create user resource creates a new user.

### Rules for creating users

The new user name must be provided in the body of the request in the Content-Type header format. 

When creating a user, adhere to the following rules:

  * The following required fields must be completed:
    * FirstName
    * LastName 
    * Password
  * Valid AccountStatus are 1 (Active), 2(Inactive), 3(Locked).
  * If Roles are not provided, the default is General User Role.
  * If Language ID is not provided, the default language is used.
  * The default user name is LastnameFirstnameinitial IE: doej for John Doe.

If the save is successful, the requested object returned from the URI includes the ID of the user. If the save is not successful, validation messages explaining the nature of the failure are returned.  

Request

POST http://Archer/platformapi/core/system/user

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"User":

{

"FirstName":"John",

"LastName":"Doe"

},

"Password":"NewUser2005!"

}

[Example Request with more parameters](../json_examples/create_new_user.txt "Successful")

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":1470

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Deactivate user

The Deactivate user resource changes the user status to Inactive (value is 2).

Request

POST http://Archer/platformapi/core/system/user/status/inactive/*userid*

POST http://Archer/platformapi/core/system/user/status/inactive/1470

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

none

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":1470

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Delete user

The Delete user resource deletes a user.

Request

DELETE http://Archer/platformapi/core/system/user/*userid*

DELETE http://Archer/platformapi/core/system/user/1471

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

none

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":1470

},

"IsSuccessful":true,

"ValidationMessages":null

}

## Get all users

The Get all users resource retrieves all users in the current Archer instance.

**Note:** The data that this API returns is more secure when you use an Open Data Protocol (OData) query in the request body (for more information, see [Open Data Protocol (Odata](../../odata.htm)). In this case you must use the HTTP verb POST instead of GET. Also, using POST is valid only if you include the X-Http-Method-Override:GET statement in the request header. Otherwise, POST returns an error.

Request

POST http://Archer/platformapi/core/system/user

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

Request Body

none

Response Example

**Note:** This example is 1 user. The command retrieves as many users as there are in your environment.

[

{

"Links":[],

"RequestedObject":

{

"Id":229,

"DisplayName":"Archer, Eric",

"FirstName":"Eric",

"MiddleName":"",

"LastName":"Archer",

"LastLoginDate":"2016-07-28T17:19:01.137",

"UserName":"ericsc",

"AccountStatus":1,

"DomainId":null,

"SecurityId":6,

"Locale":"en-US",

"TimeZoneId":"Eastern Standard Time",

"Address":"",

"Company":"",

"Title":"",

"AdditionalNote":null,

"BusinessUnit":null,

"Department":null,

"ForcePasswordChange":false,

"DistinguishedName":null,

"Type":1,

"LanguageId":null,

"DefaultHomeDashboardId":-1,

"DefaultHomeWorkspaceId":-1,

"UpdateInformation":

{

"CreateDate":"2015-06-29T17:12:29.107",

"UpdateDate":"2016-07-18T20:01:12.333",

"CreateLogin":2,

"UpdateLogin":229

}

},

"IsSuccessful":true,

"ValidationMessages":[]

}

]

## Get all user contacts

The Get all user contacts resource retrieves contact information for all users in the current Archer instance.

Request

GET http://localhost/Archer/platformapi/core/system/usercontact

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

none

Response Example

**Note:** This example is 1 contact for a user. The command retrieves as many contacts for the user as there are in your environment.

[

{

"Links":[],

"RequestedObject":

{

"UserId":1470,

"Contacts"

[

{

"ContactType":7,

"ContactSubType":2,

"IsDefault":true,

"Value":"example@domain.com",

"Id":1135

}

]

},

"IsSuccessful":true,

"ValidationMessages":[]

}

]

## Get contact information for a user

The Get contact information for a user resource retrieves contact information for a user in the current Archer instance.

### Contact types and contact subtypes

When the Contact Type is set to 9 - Phone, Contact Sub Types 3 - 14 are available. When the Contact Type is set to 7 - Email, Contact Sub Types 1, 4, 7,8, and 13 are not available.

The following table shows the numbers and definitions of contact types and sub-types. Contact Type | Definition |  Contact Sub Type |  Definition  
---|---|---|---  
7 |  Email |  1 |  Assistant  
9 |  Phone |  2 |  Business  
|  |  3 |  Business2  
|  |  4 |  Business Fax  
|  |  5 |  Home  
|  |  6 |  Home2  
|  |  7 |  Home Fax  
|  |  8 |  ISDN  
|  |  9 |  Mobile  
|  |  10 |  Mobile2  
|  |  11 |  Other  
|  |  12 |  Other2  
|  |  13 |  Other Fax  
|  |  14 |  Pager  
  
Request

GET http://localhost/Archer/platformapi/core/system/usercontact/*userid*

GET http://localhost/Archer/platformapi/core/system/usercontact/1470

Request Header

Accept:application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

none

Response Example

[

{

"Links":[],

"RequestedObject":

{

"ContactType":7,

"ContactSubType":2,

"IsDefault":true,

"Value":"example@domain.com",

"Id":1135

},

"IsSuccessful":true,

"ValidationMessages":[]

}

]

## Get user by ID

The Get user by ID resource retrieves a user by the specified ID.

**Note:** The data that this API returns is more secure when you use an Open Data Protocol (OData) query in the request body (for more information, see [Open Data Protocol (Odata](../../odata.htm)). In this case you must use the HTTP verb POST instead of GET. Also, using POST is valid only if you include the X-Http-Method-Override:GET statement in the request header. Otherwise, POST returns an error.

Request

POST http://Archer/platformapi/core/system/user/*userid*

POST http://Archer/platformapi/core/system/user/1470

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

Request Body

none

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":1470,

"DisplayName":"Doe, John",

"FirstName":"John",

"MiddleName":null,

"LastName":"Doe",

"LastLoginDate":"2016-09-13T15:16:18.35",

"UserName":"doej",

"AccountStatus":1,

"DomainId":null,

"SecurityId":1,

"Locale":null,

"TimeZoneId":"Eastern Standard Time",

"Address":null,

"Company":null,

"Title":null,

"AdditionalNote":null,

"BusinessUnit":null,

"Department":null,

"ForcePasswordChange":false,

"DistinguishedName":null,

"Type":1,

"LanguageId":null,

"DefaultHomeDashboardId":-1,

"DefaultHomeWorkspaceId":-1,

"UpdateInformation":

{

"CreateDate":"2016-09-12T19:30:49.043",

"UpdateDate":"2016-09-13T17:54:48.807",

"CreateLogin":2,

"UpdateLogin":2

}

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Get users by group

The Get users by group resource retrieves all users that are members of the specified group.

**Note:** The data that this API returns is more secure when you use an Open Data Protocol (OData) query in the request body (for more information, see [Open Data Protocol (Odata](../../odata.htm)). In this case you must use the HTTP verb POST instead of GET. Also, using POST is valid only if you include the X-Http-Method-Override:GET statement in the request header. Otherwise, POST returns an error.

Request

POST http://Archer/platformapi/core/system/user/group/*groupid*

POST http://Archer/platformapi/core/system/user/group/85

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

Request Body

none

Response Example

**Note:** This example is just 1 user. This command retrieves as many users as there are in the given group.

[

{

"Links":[],

"RequestedObject":

{

"Id":1470,

"DisplayName":"Doe, John",

"FirstName":"John",

"MiddleName":null,

"LastName":"Doe",

"LastLoginDate":"2016-09-13T15:16:18.35",

"UserName":"doej",

"AccountStatus":1,

"DomainId":null,

"SecurityId":1,

"Locale":null,

"TimeZoneId":"Eastern Standard Time",

"Address":null,

"Company":null,

"Title":null,

"AdditionalNote":null,

"BusinessUnit":null,

"Department":null,

"ForcePasswordChange":false,

"DistinguishedName":null,

"Type":1,

"LanguageId":null,

"DefaultHomeDashboardId":-1,

"DefaultHomeWorkspaceId":-1,

"UpdateInformation":

{

"CreateDate":"2016-09-12T19:30:49.043",

"UpdateDate":"2016-09-13T17:54:48.807",

"CreateLogin":2,

"UpdateLogin":2

}

},

"IsSuccessful":true,

"ValidationMessages":[]

}

] 

## Get user tasks

The Get User Tasks resource retrieves all the tasks assigned to a user in the current Archer instance.

**Note:** The data that this API returns is more secure when you use an Open Data Protocol (OData) query in the request body (for more information, see [Open Data Protocol (Odata](../../odata.htm)). In this case you must use the HTTP verb POST instead of GET. Also, using POST is valid only if you include the X-Http-Method-Override:GET statement in the request header. Otherwise, POST returns an error.

Request

POST http://Archer/platformapi/core/system/task

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

Request Body

{"Value":"?$skip=0&$top=25&$filter=IsComplete eq false"}

Response Example

[{

"Links": [],

"RequestedObject": {

"TaskId": 234137,

"Title": "Exception Request Submission Pending For 2",

"Description": "The exception request 2 requires input and submission to the reviewer.",

"DueDate": "2018-05-31T00:00:00",

"IsComplete": false,

"TargetContentId": 234136

},

"IsSuccessful": true,

"ValidationMessages": []

},

{

"Links": [],

"RequestedObject": {

"TaskId": 235439,

"Title": "Exception Request Submission Pending For 3",

"Description": "The exception request 3 requires input and submission to the reviewer.",

"DueDate": "2018-07-22T00:00:00",

"IsComplete": false,

"TargetContentId": 235438

},

"IsSuccessful": true,

"ValidationMessages": []

}]

## Remove user from user group

The Remove user from user group resource removes a user from a group.

**Note:** The user and group must exist.

Request

PUT http://Archer/platformapi/core/system/usergroup

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"UserId":1470,

"GroupId":85,

"IsAdd":false

}

Response Example

{

"Links":[],

"RequestedObject":{"Id":85},

"IsSuccessful":true,

"ValidationMessages":[]

} 

## Remove user from role

The Remove user from role resource removes a user from an access role.

**Note:** The user a role must exist.

Request

PUT http://Archer/platformapi/core/system/userrole

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"UserId":1470,

"RoleID":25,

"IsAdd":false

}

Response Example

{

"Links":[],

"RequestedObject":{"Id":35},

"IsSuccessful":true,

"ValidationMessages":[]

} 

## Update user

The Update user resource updates an existing user. 

When updating a Domain user, 2 additional properties are added: SecurityID and DomainID. If DomainID is not given, the user account Domain shows No Domain, and if SecurityID is not given, the user account is set to the default parameter.

The FirstName, LastName, UserName, Id, and AccountStatus properties cannot be null.

DefaultHomeDashboardId, DefaultHomeWorkspaceId must be passed together in order for reflect the home dashboard.

**Important:** When you are using the Update user API to change specific property values in the user profile, you must also include in the body of the API all the remaining property values as they currently exist, even if you do not intend to change them. Omitting them causes the API to set the following properties to null or to their original default values.

The following table shows which properties are set to null or to their original default values. Property |  Value  
---|---  
MiddleName |  Null  
Title |  Null  
Locale |  Null  
LanguageId |  Null  
DefaultHomeDashboardId |  Null  
DefaultHomeWorkspaceId |  Null  
TimeZoneId |  Default  
ForcePasswordChange |  Default  
SecurityId |  Default  
DomainId |  Default  
  
### Null in user values

The following table describes the results of including or excluding null values when updating a user. Value |  Result  
---|---  
Contacts list null |  User contacts are not changed.  
Contacts list not null |  User contacts are replaced by new list.  
Roles list null |  User roles are not changed.  
Roles list not null |  User roles are replaced by new list.  
Groups list null |  User groups are not changed.  
Groups list not null |  User groups are replaced by new list.  
  
Request

PUT http://Archer/platformapi/core/system/user

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"User":

{

"ID":"1470",

"FirstName":"John", 

"LastName":"Doe", 

"UserName":"DoeJ",

"AccountStatus":"1"

},

"Contacts":

[ 

{ 

"ContactType":7,

"ContactSubType":2, 

"Value":"none@none.com", 

"IsDefault":true

}, 

{

"ContactType":9,

"ContactSubType":2, 

"Value":"9999999999"

} 

],

"Roles":[1], 

"Groups":[]

}

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":1470

},

"IsSuccessful":true,

"ValidationMessages":[]

} 

