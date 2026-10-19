# Perform Workflow Actions

The Perform Workflow Actions call commits the workflow action chosen by the user. This API performs these workflow actions irrespective of any prior rules applied to the layout.

On this page

  * Usage
  * Samples
    * Sample Request
    * Sample Response

## Usage

**Privileges.** Your results from this API call vary based on the Write permissions granted to the session token you provide for the call. If the user account related to the provided session token is able to perform actions on a record in the Archer User Interface, you will be able to perform the same actions using this API.

**URL.** localhost/Archer/api/core/system/WorkflowAction

**Method.** POST

Header.

The required header for the API is described in the following table.

Parameter  |  Data Type |  Value  
---|---|---  
Content-Type |  String |  application/json  
Authorization |  String |  Archer session-id=sessionToken  
Archer session-id  |  String |  Valid session token ID for the RESTful API user login  
  
**Request body parameters.**

The parameters for the Perform Workflow Actions call are described in the following table. Parameter |  Data Type |  Value  
---|---|---  
CompletionCode |  Int |  Valid completion code for the record.  This parameter is received in response to the Get Workflow Actions API call.  
WorkflowNodeId |  String |  Valid Workflow node id for the record.  This parameter is received in response to the Get Workflow Actions API call.  
ContentId |  |   
  
**Output.** If the post is successful, the API returns null, HTTP Status code 200. If there is a failure, the API issues exception.

## Samples

The following is a sample request and response. 

### Sample Request

Request

POST /Archer/ api/core/system/WorkflowAction

Request Header

Content-Type:application/json; charset=utf-8

Authorization:Archer session-id= E5E1CEEDA26A199FE2CAE99755CB71DA

Request Body

{

"ContentId": 260068,

"CompletionCode": 1,

"WorkflowNodeId": "17604:CUST"

}

### Sample Response

null
