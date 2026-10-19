# Archer RESTful API  
  
For information on Archer RESTful API see the Archer API Help on the [Archer Help Center](https://help.archerirm.cloud/archer_suite_help/Default.htm "Archer Help Center").

On this page

  * RESTful API Overview
  * Sample: JSON response
  * RESTful service criteria

## RESTful API Overview

The RESTful API service is a collection of resources organized in functional segments that are accessed through controllers. Each resource can be acted upon either individually, by key/ID, or in batch. Collections are used broadly to submit requests and construct responses.

The RESTful API uses the JavaScript Object Notation (JSON) format by default for requests and responses, but also supports XML. After a resource is identified, Create, Read, and Delete operations can be performed against the resource using standard HTTP verbs to indicate which action should be used.

The response examples are limited, as responses vary based on the originating requests.

## Sample: JSON response

The response results will vary based on the request. Some responses may be very complex based on the originating call, for example, Get All Applications.

The following example shows the JSON response for a request for a list of applications by Name and Description only:

[{

"Links": [],

"RequestedObject": {

"Name": "Technologies",

"KeepLicensed":false,

"IsDeprecated":false,

"Description": "<html><head><style type=\"text/css\">.c0 { font-family: 'Arial' } .c1 { margin: 0px 0px 13px } </style></head><p class=\"c1\">The Technologies application provides a searchable and extensible repository of technology version information that can be leveraged to relate objects of like technology.</p></html>"

},

"IsSuccessful": true,

"ValidationMessages": []

},

{

"Links": [],

"RequestedObject": {

"Name": "Test Application 10",

"Description": null

},

"IsSuccessful": true,

"ValidationMessages": []

},

{

"Links": [],

"RequestedObject": {

"Name": "Test Application",

"Description": "This is my description"

},

"IsSuccessful": true,

"ValidationMessages": []

},

{

"Links": [],

"RequestedObject": {

"Name": "Test Application 2",

"Description": "This is my description"

},

"IsSuccessful": true,

"ValidationMessages": []

},

{

"Links": [],

"RequestedObject": {

"Name": "Test Application 3",

"Description": "This is my description"

},

"IsSuccessful": true,

"ValidationMessages": []

},

{

"Links": [],

"RequestedObject": {

"Name": "Mobile Packaging Application",

"Description": "This is my description"

},

"IsSuccessful": true,

"ValidationMessages": []

}]

## RESTful service criteria

The following table describes how Archer has implemented RESTful services for the mobile app. Criteria |  Implementation  
---|---  
Identification of resources |  Instead of exposing methods that can be called, Archer exposes resources that can be retrieved. For example, instead of listing methods that have names with verbs in them, such as UpdateQuestionnaire.Archer exposes questionnaires as resources with the means to interact with them using standard HTTP verbs like GET and POST.  
Manipulation of resources through representations |  Rather than having a service return strongly typed objects (C# objects with all the expected properties), Archer returns representations of those resources. The caller determines the form that these representations take.

  * If the caller wants a response in JSON, the Accept header must contain application/json.
  * If the caller wants a response in XML, the Accept header must contain application/xml.

  
Self-descriptive messages |  Rather than relying on the method name having meaning for Archer to figure out how the method interacts with the resource, HTTP verbs are used. Each message describes itself.

  * If the resource is accessed at /api/core/application and the method of the request is POST (POST to /api/core/application/vendors), the user is trying to save the new application called Vendors.
  * If the request is a GET to /api/core/application/vendors, the user is requesting application vendors.

  
Hypermedia as the engine of application state |  Instead of knowing the API that interacts with RPC methods, a RESTful API provides the root URI and a place to start for interacting with the resource. Each response contains the links that help move through the rest of the API. For example, when the user sends a GET to /api/core/application/vendors, the response includes a link that shows how to update that application (PUT /api/core/application/vendors) and how to delete the application (DELETE /api/core/application/vendors). The hypermedia (the links) serve as the engine of application state (moving the caller through the different states of the application).
