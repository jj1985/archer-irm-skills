# Metadata Selected User Group

The Selected User Group segment is accessed through the System controller, which includes the Get selected user group list by field ID resource.

## Get selected user group list by field ID

This resource retrieves a list of SelectedUserGroups for the specified UserGroupListField by ID. This list represents the list of available selections of users and groups.

**Note:** To get the value for All Users and All Groups associated with this field, use the "Get field definition by field ID" segment. For more information, see [Metadata Field](metadata_field.htm).

Request

POST http://Archer/platformapi/core/system/usergroupselection/usergrouplist/*fieldid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET
