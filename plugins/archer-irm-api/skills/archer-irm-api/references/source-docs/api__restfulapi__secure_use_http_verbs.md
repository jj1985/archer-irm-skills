# Secure Use of HTTP Verbs  
  
A standard GET request is unencrypted. To avoid this inherent vulnerability, the API watches for and responds to the X-HTTP-Method-Override header. You can submit a request with the HTTP verb POST and the override header set to GET. 

On this page

  * X-HTTP-Method-Override Header Example
  * HTTP verb mapping
  * Request verbs and actions

## X-HTTP-Method-Override Header Example

An example of the correct format of this header is as follows:

X-Http-Method-Override: GET

This request can contain additional data in the body, rather than in a query string. A handler early in the processing pipeline watches for this header and unpacks it. If the override verb is supported, the verb is changed and the request is passed along the processing pipeline. 

A standard use of the GET request provides the additional information needed to fulfill the request in the query string. This data is plainly readable in web logs, as well as by anyone monitoring the HTTP communication. 

Additional data could be placed in the request body, but is a non-standard use of a GET request and is not supported. 

## HTTP verb mapping

The following table lists HTTP verb mappings. Mapping |  HTTP Verb |  HTTP Request |  HTTP Response Type  
---|---|---|---  
Retrieve/Get |  GET |  Record |  Record Set / Collection  
Create |  POST |  Collection |  Record Set / Collection  
Update |  PUT |  Collection |  Record Set / Collection  
Delete |  DELETE |  Record |  Record Set / Collection  
  
## Request verbs and actions

The following table lists request verbs and actions. Request Verb |  Action |  Example  
---|---|---  
GET |  Select vendor 123 |  GET /platformapi/core/application/123  
GET |  Select all vendors |  GET /platformapi/core/application/  
POST |  Insert a new vendor |  POST /platformapi/core/application/  
PUT |  Update vendor 123 |  PUT /platformapi/core/application/123  
DELETE |  Delete vendor 123 |  DELETE /platformapi/core/application/123  
PATCH |  Submit a partial modification to a source (for example, if you only need to update 1 field for the resource, use the PATCH method) |  PATCH / platformapi/core/application/123
