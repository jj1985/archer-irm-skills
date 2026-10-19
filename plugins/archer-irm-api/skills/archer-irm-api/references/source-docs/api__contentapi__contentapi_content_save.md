# Content Save

The Content Save call helps to save the content of an application. 

On this page

  * Usage
  * Samples
    * Sample Request
    * Sample Response

## Usage

**Privileges.** Your results from this API call vary based on the Write permissions granted to the session token you provide for the call. 

**URL.** localhost/Archer/contentapi/application_alias

**Method.** POST

**Parameters.**

The parameter for the Content Save call is described in the following table. Parameter |  Data Type |  Value  
---|---|---  
_Archer   
SessionCookie_  |  String |  Valid session token ID for the Content API user.   
  
**Output.** If the call is successful, the API returns a HTTP Status code 200. If there is a failure, the API returns other HTTP Status code. 

## Samples

The following is a sample request and response. 

### Sample Request

Request:

POST /Archer/contentapi/Exception_Requests

Request Header:

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Cookie: ArcherSessionCookie = E5E1CEEDA26A199FE2CAE99755CB71DA

Content-Type: application/json

Request Body:

{

"Exception_Requests_Id":0,

"Risk_Rating":{

"ValuesListIds":[

1199  

]

},

"Submitter":{

"UserList":[

{

“Id": 2

}

]  
},

"Submission_Due_Date":"07/07/2018",

"Exception_Description":"This is an exception description",

"Business_Justification":"This is a business justification",

"Business_Unit":[

226446

],

"Reviewer":{

"UserList":[

{

“Id": 2

}

]  
},

"Review_Due_Date":"07/07/2018",

"Initial_Expiration_Date":"07/20/2018"  
}  

**Note:** In this example for the Request Body, the 0 in the "Exception_Request_ID" line creates a new record; any other content updates the existing record.

### Sample Response

200 Ok
