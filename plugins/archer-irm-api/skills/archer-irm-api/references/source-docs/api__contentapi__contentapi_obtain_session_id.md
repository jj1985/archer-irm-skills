# Obtain Session ID

When using the Content API, you must include a user Session ID in your queries. Your Session ID is what the Content API uses to determine what metadata you can interact with.

The following RESTful API call creates an Archer session using the specified credentials on the specified instance. The API request returns a serialized representation of a SessionContext object. 

On this page

  * Obtain Session ID
    * Request
    * Request Header
    * Request Body
    * Response Example

## Request

POST http://Archer/api/core/security/login

## Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Content-Type: application/json

## Request Body

{

"InstanceName":"v6.4",

"Username":"sysadmin",

"UserDomain":"",

"Password":"Archer123"

}

## Response Example

{

“SessionToken”:” C204E18D0ED58E288533F39C455A36E8”

}

**Important:** Your Session ID remains valid as long as the user session is active. Depending on the security parameter set for your Session ID user, the active user session can change frequently.
