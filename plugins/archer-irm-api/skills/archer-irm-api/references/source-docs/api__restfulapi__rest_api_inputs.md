# Inputs of a RESTful API Segment

Archer RESTful API segments use many different fields within inputs. This section explains how to format those inputs in an API call.

On this page

  * Validation
  * Optional Tags
  * Null Value
  * Input Fields

## Validation

Double check your input carefully before creating or updating records. Invalid inputs are ignored despite an apparently successful API response of True for IsSuccessful. Validation messages are not provided.

Examples of invalid inputs are incorrect IP addresses and non-existent ContentIds. 

## Optional Tags

Inputs can become lengthy and difficult to scan quickly. To avoid confusion, it is recommended that you use placeholders within your inputs to leave breadcrumbs through the logic. The examples in this document include an optional input value, Tag. This placeholder allows you to easily follow the logic of each input. The system ignores placeholder inputs during command execution.

The following is an example of a tag used in a date input.

"Tag":"Date of Birth"

**Note:** Do not use this optional field for the IP input.

## Null Value

Null indicates a condition where values are missing. There are times where you want to reset an existing value to null. In most cases, simply omit the input field from the API command to pass a null value into the record. Some input fields require specific values to indicate a null condition. Those input fields are:

  * Date
  * Values List
  * Users/Groups List

## Input Fields

The following table details the inputs of a RESTful API segment within Archer. Input Field | Segment Used In |  Sample Code  
---|---|---  
Text |  Create/Update Content,  Post Attachment,  Execute Data Feed,  Add Group Member,  Create/Update Group,  Create/Update Role,  Create/Update a Security Parameter,  Change User Password,  Create/Update User | 

"9402" { "Type": 1, "Tag":"TextString", "Value": "ABCDEFG hijk LMNOP qrstuvwxyz ÃÄÇËÑßÜ áòëæñü 信息報이ÜФ", "FieldId":9402 } 
"9403" { "Type": 1, "Tag":"TextHTML", "Value": "<p>1234 Main Street<br>Anytown, AA 12345</p>", "FieldId":9403 } 
**Note:** Use Text as an input for any string or HTML text block.  
Numeric |  Get Content by Content ID and Field ID,  Create/Update Content,  Add/Remove Group Member,  Add/Remove Group to Role,  Update Group,  Create/Update a Security Parameter, Add User to Role,  Add User to User Group,  Change User Password,  Deactivate/Delete/Update User,  Get Contact Information for a User, Remove User from User Group,  Remove User from Role | 

"1234" { "Type": 2, "Tag":"Numeric", "Value": 123450.6789, "FieldId":1234 } 
**Note:** Use Numeric as an input for numbers.  
Date |  Create/Update Content, Create/Update a Security Parameter, Create/Update User | 

"123451" { "Type": 3, "Tag":"Date with Time", "Value": "10/21/1956 11:59AM", "FieldId":123451 } 
"123452" { "Type": 3, "Tag":"Date", "Value": "12/27/2016", "FieldId":123452 } 
**Note:** Use Date as an input for any Date or Date with a time. 

"123453" { "Type": 3, "Tag":"Null (Date)", "Value": "0", "FieldId":123453 } 
**Note:** To set as Null, use "0" as the input.  
Values List |  Create/Update Content,  Create/Update User | 

"34564" { "Type": 4, "Tag":"Severity (Values List)", "Value": { "ValuesListIds":[2,3,4], "OtherText":"Severity" } "FieldID":34564 } 
"34563" { "Type": 4, "Tag":"Null (Values List)", "Value": {0} "FieldID":34563 } 
  
External Links |  Create/Update Content,  Create/Update User | 

"11234" { "Type": 7, "Tag":"External Links", "Value":  [ { "Name": "Archer", "URL":"https://www.archerirm.com" }, { "Name":"Archer Community", "URL":"https://www.archerirm.community/" } ], "FieldId": 11234 } 
  
Users/Groups List |  | 

"12234" { "Type": 8, "Tag":"Users or Group List", "Value":  { "UserList": [ { "ID" : 19 }, { "ID" : 20 } ], "GroupList": [ { "ID" : 1 } ] }, "FieldId": 12234 } 
  
Record Permissions |  | 

"13877" { "Type": 8, "Tag":"Record Permissions", "Value":  { "UserList": [ { "ID" : 190 }, { "ID" : 191 } ], "GroupList": [ { "ID" : 19 } ] }, "FieldId": 13877 } 
  
Cross-Reference |  Create/Update Content,  Create/Update User | 

"12234" { "Type": 9, "Tag":"Cross-Reference", "Value":  [ { "ContentID":205522 }, { "ContentID":205643 }, { "ContentID":205783 }, ], "FieldId" : 12234 } 
  
Attachment |  Create/Update Content,  Create/Update User | 

"12334" { "Type": 11, "Tag":"Attachments", "Value":  [ 1234 ], "FieldId" : 12334 } 
**Note:** The value in this input is the Attachment ID, which is returned by the _Post Attachment by Bytes_ and _Post attachment from multipart form data_ segment. See [Content](segmentsresources/content.htm) for more details on these segments.  
Image |  Create/Update Content,  Create/Update User | 

"12334" { "Type": 12, "Tag":"Screenshot (Image)", "Value":  [ 2234 ], "FieldId": 12334 } 
**Note:** An Image is a type of attachment, so they are treated the same way. The difference is the Type number. Images are Type 12.  
Matrix |  Create/Update Content,  Create/Update User | 

"15674" { "Type": 16, "Tag":"Matrix", "Value":  [ { "RowId":63800, "ColumnId":63823 } ], "FieldId": 15674 } 
  
IP Address |  Create/Update Content,  Create/Update User | 

"12334" { "Type": 19, "IpAddressBytes":"127.0.0.1", "FieldId": 12334 } 
**Note:** Do not include any additional fields. If there are additional fields, this input fails without returning a message.   
Related Records |  Create/Update Content,  Create/Update User | 

"18975" { "Type": 23, "Tag":"Related Records", "Value":  [ 345155, 234512 ], "FieldId": 18975 } 
**Note:** The Value contains a set of content IDs that were assigned when the Related Record was originally created.  
Sub-Form |  Create/Update Content,  Create/Update User | 

"18975" { "Type": 24, "Tag":"Subforms", "Value":  [ 345155 ], "FieldId": 18975 } 
**Note:** The Value contains a set of content IDs that were assigned when the Sub-Form was originally created.
