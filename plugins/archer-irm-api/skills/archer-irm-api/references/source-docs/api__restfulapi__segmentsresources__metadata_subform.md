# Metadata Subform

The Subform segment is accessed through the System controller, which includes the Get Subform by ID resource.

## Get Subform by ID

This resource retrieves a Subform by the specified ID.

Request

POST http://Archer/platformapi/core/system/subform/*subformid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET
