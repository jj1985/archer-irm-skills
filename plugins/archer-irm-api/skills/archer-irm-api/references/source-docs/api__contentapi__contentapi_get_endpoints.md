# Get Endpoints

The Get Endpoints call returns all of the levels and cross-references in the Archer environment that you have access to and the URLs to access them.

On this page

  * Usage
  * Samples
    * Sample Request
    * Sample Response

## Usage

**Privileges.** Your results from this API call vary based on the Read permissions granted to the session token you provide for the call. If the user account related to the provided session token would be able to see a level in the Archer User Interface, you will see those same levels returned by the Content API.

**URL.** localhost/Archer/contentapi/

**Method.** GET

**Parameters.**

The parameter for the Get Endpoints call is described in the following table. Parameter |  Data Type |  Value  
---|---|---  
Archer   
session-id  |  String |  Valid session token ID for the Content API user. For more information, see [Obtain Session ID](contentapi_obtain_session_id.htm).  
  
**Output.** If the call is successful, the API returns a JSON array. If there is a failure, the API issues an exception.

## Samples

The following is a sample request and response. 

### Sample Request

GET /Archer/contentapi/ HTTP/1.1

Host: localhost

Authorization: Archer session-id=E5E1CEEDA26A199FE2CAE99755CB71DA

Cache-Control: no-cache

### Sample Response

{

"@odata.context": "localhost/Archer/contentapi/$metadata/$metadata",

“value”: [

{

“name” : “_4th_Party”,

“kind” : “EntitySet”,

“url” : “_4th_Party”

},

{

“name” : “_4th_Party_Vendor_Relationships”,

“kind” : “EntitySet”,

“url” : “_4th_Party_Vendor_Relationships”

},

{

“name” : “Account_Scoping”,

“kind” : “EntitySet”,

“url” : “Account_Scoping”

},

{

“name” : “Account_Scoping_Target”,

“kind” : “EntitySet”,

“url” : “Account_Scoping_Target”

},

{

“name” : “Applications”,

“kind” : “EntitySet”,

“url” : “Applications”

}

]

}

**Note:** Each Archer environment is highly customized for your individual business needs. The actual response you receive for your environment can be very different than the examples shown.
