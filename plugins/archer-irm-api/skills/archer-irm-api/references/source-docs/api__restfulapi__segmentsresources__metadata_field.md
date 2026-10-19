# Metadata Field

Some text fields allow for both plain text and rich text. For example, an address can be formatted as 1 line in plain text or multiple lines in rich text.

On this page

  * Metadata Fields
  * Supported field types for RESTful API
  * Get field definition by application ID
  * Get field definition by field ID
  * Get field definition by level ID
  * Get values list field definition by level ID
  * Get field display by level ID
  * Get field IDs by Event Rule filter by level ID

## Metadata Fields

The following table shows which fields accept both plain text and rich text. Metadata | Field  
---|---  
Group |  Description  
Role |  Description  
Security Parameter |  Description  
User |  Address  
User |  AdditionalNote  
  
## Supported field types for RESTful API

The following table shows supported field types. Field Type ID |  Field Type |  Syntax  
---|---|---  
1 |  Text |  FieldType.Text  
2 |  Numeric |  FieldType.Numeric  
3 |  Date |  FieldType.Date  
4 |  Values List |  FieldType.ValuesList  
6 |  TrackingID |  FieldType.TrackingID  
7 |  External Links |  FieldType.ExternalLinks  
8 |  Users/Groups List |  FieldType.UsersGroupsList  
9 |  Cross-Reference |  FieldType.CrossReference  
11 |  Attachment |  FieldType.Attachment  
12 |  Image |  FieldType.Image  
14 |  Cross-Application Status Tracking (CAST) |  FieldType.CastScoreCard  
16 |  Matrix |  FieldType.Matrix  
19 |  IP Address |  FieldType.IpAddress  
20 |  Record Status |  FieldType.RecordStatus  
21 |  First Published |  FieldType.FirstPublishedDate  
22 |  Last Updated Field |  FieldType.LastUpdatedField  
23 |  Related Records |  FieldType.RelatedRecords  
24 |  Sub-Form |  FieldType.SubForm  
25 |  History Log |  FieldType.HistoryLog  
27 |  Multiple Reference Display Control |  FieldType.MultipleReferenceDisplayControl  
28 |  Questionnaire Reference |  FieldType.QuestionnaireReference  
29 |  Access History |  FieldType.ContentAccessHistory  
30 |  Voting |  FieldType.Voting  
31 |  Scheduler |  FieldType.Scheduler  
1001 |  Cross-Application Status Tracking Field Value |  FieldType.CrossApplicationStatusTrackingFieldValue  
  
The Field Definition and Field Display segments are accessed through the System controller, which includes the following resources.

## Get field definition by application ID

Retrieves field definition for an application ID in the current Archer instance.

Request

GET http://localhost/Archer/platformapi/core/system/fielddefinition/application/*applicationid*

Request Header

Accept:application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

## Get field definition by field ID

Retrieves the field definition of the specified field ID. Although this field definition will be of a specific derived type, (for example, ValuesListFieldDefinition, TextFieldDefinition, and others) the field definition will be returned as the base class FieldDefinition. Only properties of the base class can be used in OData query strings. To filter or select by properties of a specific type of field definition, use the URI dedicated to that field definition type. For example, to filter by properties of ValuesListFieldDefinition, use the URI /system/fielddefinition/level/levelid/valueslist.

Request

POST http://Archer/platformapi/core/system/fielddefinition/*fielddefinitionid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Get field definition by level ID

Retrieves all field definitions for the level by the specified level ID.

Request

POST http://Archer/platformapi/core/system/fielddefinition/level/*levelid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Get values list field definition by level ID

Retrieves the field definition by the specified level ID. Because field definitions, regardless of their derived type, are all returned as the base class FieldDefinition, only properties of the base class can be used in OData query strings. This method provides filtering by properties specific to ValuesListFieldDefinition.

Request

POST http://Archer/platformapi/core/system/fielddefinition/level/*levelid*/valueslist

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Get field display by level ID

Retrieves field displays for the level by the specified level ID.

Request

POST http://Archer/platformapi/core/system/fielddisplay/level/*levelid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Get field IDs by Event Rule filter by level ID

Retrieves a list of the field definitions that are referenced by an Event Rule filter on the specified level.

Request

GET http://Archer/platformapi/core/system/field/eventrulefilter/level/*levelid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json
