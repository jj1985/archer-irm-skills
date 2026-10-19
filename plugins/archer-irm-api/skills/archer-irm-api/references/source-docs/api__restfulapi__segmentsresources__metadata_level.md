# Metadata Level

On this page

  * Get all levels
  * Get level by level ID
  * Get levels by module ID
  * Get level by reference field ID
  * Get level layout by level ID

The Level and Level Layout segments are accessed through the System controller, which includes the following resources:

## Get all levels

The Get all levels resource returns all levels in the current instance of the Archer.

Request

POST http://Archer/platformapi/core/system/level

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

Response Example

## Get level by level ID

The Get level by level ID resource retrieves a level by the specified level ID.

Request

POST http://Archer/platformapi/core/system/level/*levelid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

## Get levels by module ID

The Get levels by module ID resource retrieves the levels that are contained by the specified module ID.

Request

POST http://Archer/platformapi/core/system/level/module/*moduleid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

## Get level by reference field ID

The Get level by reference field ID resource retrieves the levels targeted by the specified reference field ID. A cross-reference can target more than 1 level, which returns a collection. the target questionnaire cross-reference targets a single level, which is returned as a collection with 1 element.

Request

POST http://Archer/platformapi/core/system/level/referencefield/*fieldid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

## Get level layout by level ID

The Get level layout by level ID resource retrieves all levels in the current instance of Archer.

Request

POST http://Archer/platformapi/core/system/levellayout/level/*levelid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET
