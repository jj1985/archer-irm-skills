# Content

The Content segment is accessed through the Content controller. Actions taken on a resource determine the type of action that can be performed. 

On this page

  * Resource Content Actions
  * Get content by ID
    * Without Using an Action
    * Using the $select Action
  * Get content by reference field ID
    * Without Using an Action
    * Using the "$filter" Action
    * Using the "$select" Action
    * Using the "$top" Action
    * Using the "$skip" Action
    * Using the "$orderby" Action
  * Get content by content ID and field ID
    * Without Using an Action
    * Using the "$filter" Action
    * Using the "$select" Action
    * Using the "$top" Action
    * Using the "$skip" Action
    * Using the "$orderby" Action
  * Expose History Log Data
  * Post content
  * Put content
  * Data Gateway
  * Get attachment
  * Post attachment from bytes
  * Post attachment from multipart form data
  * Delete content by id

## Resource Content Actions

The following table describes which actions can be taken on the content of resources. Resource |  URI |  $filter |  $select |  $top |  $skip |  $orderby  
---|---|---|---|---|---|---  
content - by id |  /content/contentid |  |  |  |  |   
content - by reference field ID |  /content/referencefield/referencefieldid |  |  |  |  |   
content - by content ID and field ID |  /content/fieldcontent |  |  |  |  |   
content - expose history log data |  /content/history/ID |  |  |  |  |   
content - post |  /content |  |  |  |  |   
content - put |  /content |  |  |  |  |   
attachment - get |  /content/attachment/attachmentid |  |  |  |  |   
attachment - post using bytes |  /content/attachment |  |  |  |  |   
attachment - post using multipart form data |  /content/multipartattachment |  |  |  |  |   
delete - by id |  /content/contentid |  |  |  |  |   
  
Actions

  * $filter: returns the content records within the result set that match the specified filter criteria
  * $select: returns only the value of the specified field in each content record within the result set
  * $top: returns the top n content records within the result set 
  * $skip: skips the top n content records within the result set
  * $orderby: returns the content records within the result set, in order of the specified field. 

## Get content by ID

The Get content by ID resource retrieves a content record by the specified ID. This resource allows for the "$select" action to be added into the content API call.

Request

### Without Using an Action

POST http://archer/platformapi/core/content/contentid?id="contentid"

The following example call returns the content record that matches the specified content ID value of 184630:

POST http://archer/platformapi/core/content/contentid?id=184630

### Using the $select Action

POST http://archer/platformapi/core/content/contentid?id="contentid"&$select=LastUpdated

The following example call returns only the value of the "LastUpdated" field in the content record that matches the specified content ID value of 184630:

POST http://archer/platformapi/core/content/contentid?id=184630&$select=LastUpdated

Request Header

Accept:application/json,text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8

Authorization:Archer session-id="session token ID from login"

Content-Type:application/json

X-Http-Method-Override:GET

Response Examples

  * [Without Using an Action](json_examples/get-content-by-id.txt "Without Using an Action")
  * [Using the $select Action](json_examples/get-content-by-id--select.txt "Using the $select Action")

## Get content by reference field ID

The Get content by reference field ID resource retrieves all the content records by the specified reference field ID. If the reference field is a target cross reference for a questionnaire, this URL returns all content in the target application. If the reference field is a regular cross-reference or a related-record field, this URL returns the record lookup content. This resource allows you to add the following actions to the content API call: $filter, $select, $top, $skip, and $orderby.

Request

### Without Using an Action

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id="referencefieldid"

The following example call returns all of the content records that match the specified reference field ID value of 18501:

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id=18501

### Using the "$filter" Action

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id="referencefieldid"&$filter="field to filter by"

The following example call returns the content record that matches the specified reference field ID value of 18501 and the "SequentialId" field value of 3:

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id=18501&$filter=SequentialId eq 3

### Using the "$select" Action

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id="referencefieldid"&$select="field to select by"

The following example call returns only the value of the "SequentialId" field in all of the content records that match the specified reference field ID value of 18501:

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id=18501&$select=SequentialId

### Using the "$top" Action

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id="referencefieldid"&$top="number of top content records to return"

The following example call returns the top content record that matches the specified reference field ID value of 18501:

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id=18501&$top=1

### Using the "$skip" Action

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id="referencefieldid"&$skip="number of top content records to skip"

The following example call returns all content records that match the reference field ID value of 18501, except for the top 2 records:

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id=18501&$skip=2

### Using the "$orderby" Action

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id="referencefieldid"&$orderby="field to order by"

The following example call returns all content records that match the reference field ID value of 18501, in order of the "SequentialId" field value: 

POST http://archer/platformapi/core/content/referencefield/referencefieldid?id=18501&$orderby=SequentialId

Request Header

Accept:application/json,text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8

Authorization:Archer session-id="session token ID from login"

Content-Type:application/json

X-Http-Method-Override:GET

Response Examples

  * [Without Using an Action](json_examples/get-content-by-reference-field-id.txt "Without Using an Action")
  * [Using the $filter Action](json_examples/get-content-by-reference-field-id--filter.txt "Using the $filter Action")
  * [Using the $select Action](json_examples/get-content-by-reference-field-id--select.txt "Using the $select Action")
  * [Using the $top Action](json_examples/get-content-by-reference-field-id--top.txt "Using the $top Action")
  * [Using the $skip Action](json_examples/get-content-by-reference-field-id--skip.txt "Using the $skip Action")
  * [Using the $orderby Action](json_examples/get-content-by-reference-field-id--orderby.txt "Using the $orderby Action")

## Get content by content ID and field ID

The Get content by content ID and field ID resource retrieves field content by content ID and field ID in the current Archer instance. This resource allows for the following actions to be added into the content API call: $filter, $select, $top, $skip, and $orderby.

Request

The "FieldID" values and the "ContentId" values in the following example request calls are found in the "Request Body" section below.

### Without Using an Action

The following example call returns all content records that match the specified criteria: "FieldId" values: [18503,18504,18505,18506,18507] and "ContentId" values: [184630,184631,184632,184633]:

POST http://archer/platformapi/core/content/fieldcontent

### Using the "$filter" Action

POST http://archer/platformapi/core/content/fieldcontent?$filter="field to filter by"

The following example call returns the content record that matches the specified criteria: "FieldId" values: [18503,18504,18505,18506,18507], "ContentId" values: [184630,184631,184632,184633], and the "SequentialId" field value of 3:

POST http://archer/platformapi/core/content/fieldcontent?$filter=SequentialId eq 3

### Using the "$select" Action

POST http://archer/platformapi/core/content/fieldcontent?$select="field to select by"

The following example call returns only the value of the "ContentId" field in all content records that match the specified criteria: "FieldId" values: [18503,18504,18505,18506,18507] and "ContentId" values: [184630,184631,184632,184633]:

POST http://archer/platformapi/core/content/fieldcontent?$select=Id

### Using the "$top" Action

POST http://archer/platformapi/core/content/fieldcontent?$top="number of top content records to return"

The following example call returns the top 2 content records that match the specified criteria: "FieldId" values: [18503,18504,18505,18506,18507] and "ContentId" values: [184630,184631,184632,184633]:

POST http://archer/platformapi/core/content/fieldcontent?$top=2

### Using the "$skip" Action

POST http://archer/platformapi/core/content/fieldcontent?$skip="number of top content records to skip"

The following example call returns all content records that match the specified criteria: "FieldId" values: [18503,18504,18505,18506,18507] and "ContentId" values: [184630,184631,184632,184633], except for the top result:

POST http://archer/platformapi/core/content/fieldcontent?$skip=1

### Using the "$orderby" Action

POST http://archer/platformapi/core/content/fieldcontent?$orderby="field to order by"

The following example call returns all content records that match the specified criteria: "FieldId" values: [18503,18504,18505,18506,18507] and "ContentId" values: [184630,184631,184632,184633], in order of the "ContentId" field value: 

POST http://archer/platformapi/core/content/fieldcontent?$orderby=Id

Request Header

Accept:application/json,text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8

Authorization:Archer session-id="session token ID from login"

Content-Type:application/json

Request Body

{

"FieldIds":[18503,18504,18505,18506,18507],

"ContentIds":[184630,184631,184632,184633]

}

Response Examples

  * [Without Using an Action](json_examples/get-content-by-content-id-and-field-id.txt "Without Using an Action")
  * [Using the $filter Action](json_examples/get-content-by-content-id-and-field-id--filter.txt "Using the $filter Action")
  * [Using the $select Action](json_examples/get-content-by-content-id-and-field-id--select.txt "Using the $select Action")
  * [Using the $top Action](json_examples/get-content-by-content-id-and-field-id--top.txt "Using the $top Action")
  * [Using the $skip Action](json_examples/get-content-by-content-id-and-field-id--skip.txt "Using the $skip Action")
  * [Using the $orderby Action](json_examples/get-content-by-content-id-and-field-id--orderby.txt "Using the $orderby Action")

## Expose History Log Data

The Expose History Log Data resource retrieves content on every history log field in the application. If there is no content in the History Log field, the response for that field is empty. If no history log fields in the application contain relevant content, the response for the application is empty.

Request

POST http://localthost/Archer/api/core/content/history/ID

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Post content

The Post content resource saves a content record. The content must be provided in the body of the request in the format specified by the content-type header. Attempting to update an existing content record using POST results in a 403 - Forbidden error.

Request

POST http://archer/platformapi/core/content

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

Request Body

[Request body example](json_examples/post_content_request_body.txt "Request body example")

The request body shows an example of a content record serialized in JSON format. This content record contains thirteen fields.

Use the optional "Tag" property in the request body example to display the field name, field type, or a comment about the field.

The following table describes the "Type" property value and the corresponding field types. "Type" Value |  Field Type  
---|---  
1 |  Text - Single Line, Text Area - HTML  
2 |  Numeric  
3 |  Date Only, Date and Time  
4 |  Values List  
7 |  External Links  
8 |  Record Permissions, User/Groups List  
9 |  Cross-Reference  
11 |  Attachment  
12 |  Image  
16 |  Matrix  
19 |  IP Address  
23 |  Related Records  
24 |  Sub-Form  
  
When saving subform content, the request body must contain a SubformFieldId. Otherwise, you must omit this parameter.

  * If the save is successful, the requested object returned from this URL includes the ID of the content. 
  * If the save is not successful, a validation messages explaining the nature of the failure is displayed.

Response Example

{

"Links":[],

"RequestedObject":

{

"Id":123454

},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Put content

The Put content resource updates an existing content record. The content must be provided in the body of the request in the format specified by the content-type header. Attempting to insert a new content record using PUT results in a 403 - Forbidden error.

Request

PUT http://archer/platformapi/core/content

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

Request Body

{

"Content":

{

"Id": 123, 

"LevelId" : 9,

"FieldContents" : 

{

"3204" : 

{

"Type" : 2, 

"Value" : 0.0, 

"FieldId" : 3204

}, 

"3202" : 

{

"Type" : 4, 

"Value" : 

{

"ValuesListIds" : [2405], 

"OtherText" : null

}, 

"FieldId" : 3202

}, 

"10066" : 

{

"Type" : 23, 

"Value" : [150622], 

"FieldId" : 10066

}

}, 

"Version": "44"

}, 

"SubformFieldId":123

}

The request body shows an example of a Content Wrapper, which contains a content record serialized in JSON format. This content record contains 3 fields: 

  * A numeric field.
  * A values list field.
  * A cross-reference field. 

The Content Wrapper can also contain a SubformFieldId that must be passed when subform content is being saved. Otherwise, this parameter can be omitted.

  * If the save was successful, the requested object returned from this URL will include the id of the content.
  * If the save was not successful, a validation messages explaining the failure is displayed.

## Data Gateway

The Data Gateway allows external data storage applications to notify Archer when content changes within their system. The resource accepts Archer content IDs and external application fields, then returns a validation message reporting success or failure. When successful, 2 things happen:

  * The external application marks the external fields for update and notifies Archer.
  * Archer saves the content.

Request

PUT http://archer/platformapi/core/content/externalContentChangeNotification

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

Request Body

{

"Alias":"ARCHER",

"ContentPartIds":["234811"], 

"ExternalFieldIds":["19649"]

}

There are 2 inputs for this resource:

  * ContentPartIds receives 1 or more IDs that correspond to the Archer Content ID.
  * ExternalFieldIds receives 1 or more IDs that correspond to a external data storage application. 

## Get attachment

The Get attachment resource retrieves an attachment from the Archer file repository. The Get API automatically retrieves encrypted and unencrypted files from the correct store.

The actual object returned is an AttachmentWrapper, which has 2 properties: 

  * AttachmentName
  * AttachmentBytes

The bytes are represented as a Base64 encoded string.

Request

POST http://archer/platformapi/core/content/attachment/*attachmentid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Post attachment from bytes

The Post attachment from bytes resource accepts a serialized AttachmentWrapper with the AttachmentName, AttachmentBytes, and IsSensitive properties. If AttachmentName or AttachmentBytes is not present, the post fails with a validation message indicating that the request was badly formatted. AttachmentBytes must contain a Base64 encoded string representation of the bytes of the attachment file. On success, the API returns the newly assigned id of the attachment file. 

The IsSensitive flag determines whether the attachment is encrypted. The flag is true if the attachment requires encryption and false if the attachment does not require encryption. Encrypted files are stored in the Encrypted folder in the file repository. When the IsSensitive flag is not included in the request, the attachment posts and saves as unencrypted in the file repository.

Request

POST http://archer/platformapi/core/content/attachment

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

Request Body

"Attachment Bodie"

{

"AttachmentName":"Bodie.jpg",

"AttachmentBytes":"/9j/4AAQSkZJRgABAgAAAQABAAD/4QDmRXhpZgAASUkqAAgAAAAFABIBAwABAAAAAQAAADEBAgAcAAAASgAAADIBAgAUA  
AAAZgAAABMCAwABAAAAAQAAAGmHBAABAAAAegAAAAAAAABBQ0QgU3lzdGVtcyBEaWdpdGFsIE"

"IsSensitive":"true"

}

## Post attachment from multipart form data

The Post attachment from multipart form data resource accepts multipart form data containing an attachment and attachment name. These values must be included in content headers with the AttachmentName and AttachmentBytes names. If either of these content headers is not present, the post fails with a validation message indicating that the request was badly formatted. AttachmentBytes must contain a Base64 encoded string representation of the bytes of the attachment file. If the request is being posted from a form, this request is handled by the browser when the request is submitted. On success, the API returns the newly assigned ID of the attachment file.

The IsSensitive flag determines whether the attachment is encrypted. The flag is true if the attachment requires encryption and false if the attachment does not require encryption. Encrypted files are stored in the Encrypted folder in the file repository. When the IsSensitive flag is not included in the request, the attachment posts and saves as unencrypted in the file repository.

Request

POST http://archer/platformapi/core/content/multipartattachment

Request Header

Content-Type: multipart/form-data; boundary=-------------------------acebdf13572468

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Request Body

\---------------------------acebdf13572468

Content-Disposition: form-data; name="AttachmentName"

MyPhoto.jpg

\---------------------------acebdf13572468

Content-Disposition: form-data; name="IsSensitive" True

\---------------------------acebdf13572468

Content-Disposition: form-data; name="AttachmentBytes";

filename="Account.jpg"

Content-Type: image/jpeg

LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5QmZMRkloZUhkdzluWDhNeA0KQ29udGVudC

1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJfX1ZJRVdTVEFURSINCg0KL3dF

UER3VUxMVEV3TVRrd

09EazBNallQWkJZQ1pnOWtGZ0lDQXc4V0J

\---------------------------acebdf13572468--

## Delete content by id

The delete content by ID resource deletes a content record by the specified ID.

Request

DELETE http://localhost/Archer/api/core/content/ID

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=.9,/;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

Response Examples

  * [Delete content when ID exists](json_examples/delete_content_by_id_success.txt)

  * [Delete content when ID does not exist](json_examples/delete_content_by_id_failure.txt)

