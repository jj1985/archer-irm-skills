# Group Segment

The Group segment is accessed through the System controller.

On this page

  * Add group member
  * Add group to role
  * Create group
  * Delete group
  * Get all groups
  * Get group by ID
  * Get group hierarchy
  * Get all group memberships
  * Get groups by user
  * Remove group from role
  * Remove group member
  * Update group

## Add group member

The Add group member resource adds a group to another group. GroupId is the ID of a parent group and GroupMemberId is the ID of a child group. Both parent group and child group must exist. 

Request

PUT http(s)://<Archer URL>/platformapi/core/system/groupmember

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"GroupId":123,

"GroupMemberId":789,

"IsAdd":true

}

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":206

},

"IsSuccessful":true,

"ValidationMessages":[]

} 

## Add group to role

Adds a group to an access role. Both group and access role must exist.

Request

PUT http://Archer/platformapi/core/system/rolegroup

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"GroupId":206,

"RoleId":3,

"IsAdd":true

}

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":206

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Create group

Creates a group. The name field is required in the request body.

Request

POST http://Archer/platformapi/core/system/group

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"Group":

{

"Name":"GroupA",

"Description":"Group A description"

},

"ParentGroups":[1],

"ChildGroups":[2],

"ChildUsers":null

}

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":159

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Delete group

Deletes a group.

Request

DELETE http://Archer/platformapi/core/system/group/*groupid*

DELETE http://Archer/platformapi/core/system/group/206

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

None

Response Example

{

"Links":[],

"RequestedObject":206,

"IsSuccessful":true,

"ValidationMessages":null

}

## Get all groups

Retrieves all groups.

Request

POST http://Archer/platformapi/core/system/group

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

Request Body

None

Response Example

[

{

"Links":[],

"RequestedObject":

{

"Id":206,

"Name":"New Group Name",

"DisplayName":"New Group Name",

"Description":"<html><head></head><p style=\"margin: 0px\">New Group Description</p></html>",

"EveryoneFlag":false,

"Guid":"6dc2e265-2796-4e3c-ab8e-549ba03422d8",

"SystemFlag":false,

"LdapFlag":false,

"DomainId":null,

"DistinguishedName":null,

"DefaultHomeDashboardId":-1,

"DefaultHomeWorkspaceId":-1,

"UpdateInformation":

{

"CreateDate":"2016-09-21T18:04:02.643",

"UpdateDate":"2016-09-21T18:06:51.027",

"CreateLogin":1470,

"UpdateLogin":1470

}

},

"IsSuccessful":true,

"ValidationMessages":[]

}

]

**Note:** The above example is just 1 group. This command will bring up as many groups that exist in your environment.

## Get group by ID

Retrieves a group by the specified group ID.

Request

GET http://Archer/platformapi/core/system/group/*groupId*

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

"Id":208,

"Name":"Updated Group Name",

"DisplayName":"Updated Group Name",

"Description":"<html><head></head><p style=\"margin: 0px\">WAS: New Group Description</p></html>",

"EveryoneFlag":false,

"Guid":"4eec52f1-bc2f-4460-ac2b-e6e179b5744d",

"SystemFlag":false,

"LdapFlag":false,

"DomainId":null,

"DistinguishedName":null,

"DefaultHomeDashboardId":null,

"DefaultHomeWorkspaceId":null,

"UpdateInformation":

{

"CreateDate":"2016-09-22T16:07:59.807",

"UpdateDate":"2016-09-22T16:09:01.083",

"CreateLogin":1470,

"UpdateLogin":1230

}

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Get group hierarchy

Retrieves the hierarchy for all groups. Using this hierarchy, the relationships between groups can be composed into a tree structure. A group hierarchy record consists of the group id, a related id, and a generation. The related id refers to a group that is an ancestor of the current group. The generation describes how far removed the current group is from that related group. A group is always in generation zero (0) for itself. A group is in generation 1 for its immediate parent.

Request

GET http://Archer/platformapi/core/system/grouphierarchy

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

None

Response Example

[

{

"Links":[],

"RequestedObject":

{

"Id":2,

"RelatedId":2,

"Generation":0

},

"IsSuccessful":true,

"ValidationMessages":[]

},

{

"Links":[],

"RequestedObject":

{

"Id":3,

"RelatedId":3,

"Generation":0

},

"IsSuccessful":true,

"ValidationMessages":[]

},

{

"Links":[],

"RequestedObject":

{

"Id":4,

"RelatedId":4,

"Generation":0

},

"IsSuccessful":true,

"ValidationMessages":[]

}

]

## Get all group memberships

Retrieves memberships for all groups. Membership includes all users and all parent groups for a group.

Request

GET http://Archer/platformapi/core/system/groupmembership

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

None

Request Response

[

{

"Links":[],

"RequestedObject":

{

"GroupId":1,

"UserIds":null,

"ParentGroupIds":null

},

"IsSuccessful":true,

"ValidationMessages":[]

},

{

"Links":[],

"RequestedObject":

{

"GroupId":2,

"UserIds":null,

"ParentGroupIds":[16]

},

"IsSuccessful":true,

"ValidationMessages":[]

},

{

"Links":[],

"RequestedObject":

{

"GroupId":16,

"UserIds":[1470],

"ParentGroupIds":null

},

"IsSuccessful":true,

"ValidationMessages":[]

},

{

"Links":[],

"RequestedObject":

{

"GroupId":17,

"UserIds":null,

"ParentGroupIds":[16]

},

"IsSuccessful":true,

"ValidationMessages":[]

},

{

"Links":[],

"RequestedObject":

{

"GroupId":18,

"UserIds":null,

"ParentGroupIds":[16]

},

"IsSuccessful":true,

"ValidationMessages":[]

},

{

"Links":[],

"RequestedObject":

{

"GroupId":19,

"UserIds":[1355],

"ParentGroupIds":[16]

},

"IsSuccessful":true,

"ValidationMessages":[]

}

]

## Get groups by user

Retrieves all groups of which the specified user is a member.

Request

POST http://Archer/platformapi/core/system/group/user/*userId*

POST http://Archer/platformapi/core/system/group/user/1470

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

Request Body

None

Response Example

[

{

"Links":[],

"RequestedObject":

{

"Id":204,

"Name":"Asset Catalog Administator",

"DisplayName":"Asset Catalog Administator",

"Description":"<html><head></head><p style=\"margin: 0px\">The Asset Catalog Administrator group is for users who have full administrative access to the following core applications: Applications, Devices, Storage Devices, Technologies, Business Processes, Corporate Objectives, Products and Services, Information Assets, Facilities, and Contacts.</p></html>",

"EveryoneFlag":false,

"Guid":"44690160-29e2-4b31-8c98-68cb5f0d014a",

"SystemFlag":false,

"LdapFlag":false,

"DomainId":null,

"DistinguishedName":null,

"DefaultHomeDashboardId":null,

"DefaultHomeWorkspaceId":null,

"UpdateInformation":

{

"CreateDate":"2016-05-26T13:41:11.677",

"UpdateDate":"2016-05-26T13:41:11.677",

"CreateLogin":2,

"UpdateLogin":2

}

},

"IsSuccessful":true,

"ValidationMessages":[]

}

]

The following example shows the response if no group can be found.

[

{

"Links":[],

"RequestedObject":{},

"IsSuccessful":false,

"ValidationMessages":

[{

"Reason": "WebApi:WebApiResourceNotFoundQueryReason",

"Severity": 3,

"MessageKey": "WebApi:WebApiResourceNotFoundQuery",

"Description": "The resource cannot be found.",

"Location": -1,

"ErroredValue": null,

"Validator": "ArcherApi.Controllers.System.UserGroupController, ArcherApi, Version=6.2.100.1061, Culture=neutral, PublicKeyToken=null",

"XmlData": null,

"ResourcedMessage": "No resource found."

}]

}

]

## Remove group from role

Removes a group from an access role. Both group and access role must exist.

Request

PUT http://Archer/platformapi/core/system/rolegroup

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"GroupId":206,

"RoleId":162,

"IsAdd":false

}

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":206

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Remove group member

Removes a Group from another Group. GroupId is the ID of a parent group and GroupMemberId is the id of a child group. Both parent group and child group must exist.

Request

PUT http://Archer/platformapi/core/system/groupmember

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"GroupMemberId":208,

"GroupId":162,

"IsAdd":false

}

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":208

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Update group

Updates a group. The name and ID cannot be set to null.

The following table describes the results of including or excluding null values when updating a group. Value |  Result  
---|---  
ParentGroups null |  Parent groups are not changed.  
ParentGroups not null |  Existing parent groups replaced by new list.  
ChildGroups null |  Child groups are not changed.  
ChildGroups not null |  Existing child groups replaced by new list.  
ChildUsers null |  Child users are not changed.  
ChildUsers not null |  Existing child users replaced by new list.  
  
Request

PUT http://Archer/platformapi/core/system/group

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{

"Group":

{

"Id":208,

"Name":"Updated Group Name",

}

"ParentGroups":null,

"ChildGroups":null,

"ChildUsers":

[

204,

2

]

}

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":208

},

"IsSuccessful":true,

"ValidationMessages":[]

}

