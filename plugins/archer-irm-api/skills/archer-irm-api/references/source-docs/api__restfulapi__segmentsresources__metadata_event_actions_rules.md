# Metadata Event Actions and Rules

The Event Actions segment is accessed through the System controller, which includes the following resources:

On this page

  * Get event action by ID
  * Get event action by event rule ID
  * Get event rule by ID
  * Get event rule by level ID

## Get event action by ID

The Get event action by ID resource retrieves the data driven event action of the specified ID.

Request

POST http://Archer/platformapi/core/system/eventaction/*eventactionid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Get event action by event rule ID

The Get event action by event rule ID resource retrieves the data driven event actions associated with the event rule by the specified event rule ID.

Request

POST http://Archer/platformapi/core/system/eventaction/eventrule/*eventruleid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

The Event Rules segment is accessed through the System controller, which includes the following resources:

## Get event rule by ID

The Get event rule by ID resource retrieves the data driven event rule by the specified ID.

Request

POST http://Archer/platformapi/core/system/eventrule/*eventruleid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Get event rule by level ID

The Get event rule by level ID resource retrieves the data driven event rule associated with the level by the level ID.

Request

POST http://Archer/platformapi/core/system/eventrule/level/*levelid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET
