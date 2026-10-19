# Get Cross-Reference or Related Records Relationships

The Get Cross-Reference or Related Records Relationships call returns a list of all the records referenced by either a cross-reference or related records field.

On this page

  * Usage
  * Samples
    * Sample Request
    * Sample Response

## Usage

**Privileges.** Your results from this API call vary based on the Read permissions granted to the session token you provide for the call. If the user account related to the provided session token would be able to see a level in the Archer User Interface, you will see those same levels returned by the Content API.

**URL.** localhost/Archer/contentapi/_levelalias_ __fieldalias_

**Method.** GET

**Parameters.**

The parameter for the Get Cross-Reference or Related Records Relationships call is described in the following table. Parameter |  Data Type |  Value  
---|---|---  
Archer   
session-id  |  String |  Valid session token ID for the Content API user. For more information, see [Obtain Session ID](contentapi_obtain_session_id.htm).  
  
**Output.** If the call is successful, the API returns a JSON array. If there is a failure, the API issues an exception.

## Samples

The following is a sample request and response. 

### Sample Request

GET /Archer/contentapi/Incidents_Risks/$metadata#Incidents_Risks HTTP/1.1

Host: localhost

Authorization: Archer session-id=E5E1CEEDA26A199FE2CAE99755CB71DA

Cache-Control: no-cache

### Sample Response

{

"@odata.context": "localhost/Archer/contentapi/Incidents_Risks/$metadata#Incidents_Risks",

“value”: [

{

“Incidents_Id” : 224931,

“Risk_Register_Id” : 224961,

},

{

“Incidents_Id” : 224931

“Risk_Register_Id” : 224962,

},

]

}

**Note:** Each Archer environment is highly customized for your individual business needs. The actual response you receive for your environment can be very different than the examples shown.
