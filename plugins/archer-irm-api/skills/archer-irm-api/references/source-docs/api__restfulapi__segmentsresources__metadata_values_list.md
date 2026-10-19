# Metadata Values List Values

On this page

  * Get values list definition by ID
  * Get values list values by values list ID (flat)
  * Get values list values by values list ID (hierarchical)

The Values List Definitions and Values List Values segments are accessed through the System controller, which includes the following resources:

## Get values list definition by ID

The Get values list definition by ID resource retrieves the definition of a values list by its ID.

Request

POST http://Archer/platformapi/core/system/valueslist/*valueslistid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

## Get values list values by values list ID (flat)

The Get values list values by values list ID (flat) resource retrieves a flat list of all ValuesListValues for the specified ValuesListDefinition. 

**Note:** This list is in a flat format. To get the list in a tree format, use the following URI: http://Archer/platformapi//core/system/valueslistvalue/valueslist/*valueslistid*

Request

POST http://Archer/platformapi/core/system/valueslistvalue/flat/valueslist/valueslistid

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

## Get values list values by values list ID (hierarchical)

The Get values list values by values list ID (hierarchical) resource retrieves a hierarchical list of all ValuesListValues for the specified ValuesListDefinition. 

**Note:** This list is in a tree format. To get the list in flat format, use the following URI: http://Archer/platformapi//core/system/valueslistvalue/flat/valueslist/*valueslistid*

Request

POST http://Archer/platformapi/core/system/valueslistvalue/valueslist/*valueslistid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET
