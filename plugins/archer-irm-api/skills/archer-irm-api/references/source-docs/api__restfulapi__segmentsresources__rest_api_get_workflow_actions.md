# Get Workflow Actions

The Get Workflow Actions call retrieves available user Workflow Actions. 

On this page

  * Usage
  * Samples
    * Sample Request
    * Sample Response

## Usage

**Privileges.** Your results from this API call vary based on the Read permissions granted to the session token you provide for the call. If the user account related to the provided session token would be able to see actions present in a record in the Archer User Interface, you will see those same levels returned by this API.

**URL.** localhost/Archer/api/core/system/WorkflowAction/content_id

**Method.** GET

Header.

The required header for the API is described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
Content-Type |  String |  application/json  
Authorization |  String |  Archer session-id=sessionToken  
X-HTTP-Method-Override |  String |  GET  
Archer session-id  |  String |  Valid session token ID for the RESTful API user login  
  
**Output.** If the call is successful, the API returns a HTTP Status code 200. If there is a failure, the API returns other HTTP Status code.

## Samples

The following is a sample request and response. 

### Sample Request

Request:

GET /Archer/api/core/system/WorkflowAction/260068

Request Header:

Content-Type:application/json; charset=utf-8 

X-Http-Method-Override:GET

Authorization:Archer session-id= E5E1CEEDA26A199FE2CAE99755CB71DA

### Sample Response

{

"Links":[

],

"RequestedObject":{ 

"WorkflowNodeId":"18304:CUST", 

"WorkflowNodeName":"Exception Requests:57", 

"JobStatus":"Running",

"Actions":[

{

"WorkflowTransitionId":"2221:CUST", 

"WorkflowTransitionName":"Deny",

"CompletionCode":10

},

{

"WorkflowTransitionId":"2222:CUST", 

"WorkflowTransitionName":"Reject", 

"CompletionCode":2

},

{

"WorkflowTransitionId":"2247:CUST", 

"WorkflowTransitionName":"Approve", 

"CompletionCode":1

},

{

"WorkflowTransitionId":"2256:CUST",

"WorkflowTransitionName":"ReAssign Stakeholders",

"CompletionCode":3

}

]

},

"IsSuccessful":true, 

"ValidationMessages":[

]

}
