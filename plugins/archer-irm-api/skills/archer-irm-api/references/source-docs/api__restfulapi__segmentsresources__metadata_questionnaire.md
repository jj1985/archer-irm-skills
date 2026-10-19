# Metadata Questionnaire

On this page

  * Get all questionnaires
  * Get questionnaire by ID
  * Get questionnaire rule by ID
  * Get questionnaire rule by level

The Questionnaire segment is accessed through the System controller, which includes the following resources:

## Get all questionnaires

The Get all questionnaires resource retrieves all questionnaires.

Request

POST http://Archer/platformapi/core/system/questionnaire

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

## Get questionnaire by ID

The Get questionnaire by ID resource retrieves a questionnaire by the specified questionnaire ID.

Request

POST http://Archer/platformapi/core/system/questionnaire/*questionnaireid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

The Questionnaire Rule segment is accessed through the System controller, which includes the following resources:

## Get questionnaire rule by ID

The Get questionnaire rule by ID resource retrieves a questionnaire rule by the specified ID.

Request

POST http://Archer/platformapi/core/system/questionnairerule/*questionnaireruleid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

## Get questionnaire rule by level

The Get questionnaire rule by level resource retrieves all questionnaire rules by the specified level.

Request

POST http://Archer/platformapi/core/system/questionnairerule/level/*levelid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET
