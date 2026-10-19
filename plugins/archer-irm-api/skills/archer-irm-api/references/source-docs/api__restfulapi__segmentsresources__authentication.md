# Authentication

On this page

  * SessionContext 
  * Login
    * Request
    * Request Header
    * Request Body
  * Logout
    * Request
    * Request Header
    * Request Body

## SessionContext 

SessionContext can be obtained by passing valid credentials to the Login method of the Security controller. This SessionContext contains a string called SessionToken which appears in every subsequent request in a custom Authentication header.

**Example:**

Authorization: Archer session-id=D45BB616F3F564B12199F8198522042D

**Note:** Insert the session token ID from your login.

Because SessionContext is obtained through the AuthenticationManager, each call must conform to the normal restrictions of their associated security parameters in Archer. Every request of the API must contain a valid Authentication header using the Archer authentication scheme.

**Important:** If Single Sign-on is enabled, you must select Allow manual bypass in the Archer Control Panel for the RESTful API generate the session token. However, the Web Services API generates session tokens, even if the Allow manual bypass option is not selected. The token that the Web Services API generates can be used to make RESTful API calls. See the "Configuring an Instance for Single Sign-On" in the [Archer Control Panel Help](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/platform_home.htm). 

The Authentication segment is accessed through the Security controller and includes the following services.

## Login

Login creates an Archer session using the specified credentials on the specified instance. The API request returns a serialized representation of a SessionContext object. 

### Request

POST http://Archer/platformapi/core/security/login

### Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Content-Type: application/json

### Request Body

{

"InstanceName":"v5.0",

"Username":"sysadmin",

"UserDomain":"",

"Password":"Archer123"

}

Response Example

{

“SessionToken”: "C204E18D0ED58E288533F39C455A36E8"

}

## Logout

Logout calls a service that terminates the specified session. If the session in question is already terminated or is invalid, the method still returns true. The user associated with the session in the authorization header must have the necessary permissions to terminate the session of another user.

Normally, the session token ID is the same for both Login and Logout, assuming it is the same user. If a user has permission to log other users out, the Logout session token ID is for the user logging out.

### Request

POST http://Archer/platformapi/core/security/logout

### Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id=SessionToken

Content-Type: application/json

### Request Body

{

"Value": SessionToken

}

