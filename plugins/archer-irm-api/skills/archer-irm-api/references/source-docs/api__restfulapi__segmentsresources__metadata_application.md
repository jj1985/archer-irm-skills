# Metadata Application

The Application segment is accessed through the System controller, which includes the following resources:

On this page

  * Get all applications
  * Get application by ID
  * Get application version

## Get all applications

The Get all applications resource retrieves metadata for all applications.

Request

POST http://Archer/platformapi/core/system/application

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Get application by ID

The Get application by ID resource retrieves metadata for the application by the application ID.

Request

POST http://Archer/platformapi/core/system/application/*applicationid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Get application version

The Get application version resource retrieves the version number for the Archer instance against which the API is running.

Request

POST http://Archer/platformapi/core/system/applicationinfo/version (http://Archer/platformapi/core/system/applicationinfo/version)

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET
