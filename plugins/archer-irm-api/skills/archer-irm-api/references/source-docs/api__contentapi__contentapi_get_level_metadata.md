# Get Level Metadata

The Get Level Metadata call returns a page of up to 1,000 contents in a level.

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

The parameters for the Get Level Metadata call are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
Archer session-id  |  String |  Valid session token ID for the Content API user. For more information, see [Obtain Session ID](contentapi_obtain_session_id.htm).  
LevelAlias |  String  |  The entity level alias returned by the [Get Endpoints](contentapi_get_endpoints.htm) call.  **Important:** Level alias IDs are case-sensitive. **Note:** If 2 or more levels share the same alias, then the alias call is ModuleAlias_LevelAlias. For example: 

  * ModuleA_FirstLevel
  * ModuleB_FirstLevel
  * ModuleC_FirstLevel

  
?skip= |  Integer  |  (Optional) If you need to work with more than 1,000 results, run multiple calls to the same API, appending ?skip=N to the URL, where N is the number of records you have already processed (in thousands). For example: localhost/Archer/contentapi/Risk_Register?skip=2 Use $top with $skip, to return a certain number of responses after completing the skip function. For example, localhost/Archer/contentapi/Risk_Register?skip=10&$top=20 skips the first 10 records and returns the next 20 records.  
?top= |  Integer |  (Optional) If you want to display a certain number of records at a time, append ?top=N to the URL, where N is the number of records to display at a time. N must be greater than 0. For example:

  * To process the top 20 records, use localhost/Archer/contentapi/Risk_Register?top=20
  * To process all the records in the level, use localhost/Archer/contentapi/Risk_Register?top=all

Use $top with $skip, to return a certain number of responses after completing the skip function. For example, localhost/Archer/contentapi/Risk_Register?skip=10&$top=20 skips the first 10 records and returns the next 20 records. For more information on limiting record counts, see Running Searches in Applications and Questionnaires.  
(TrackingID) |  Integer |  (Optional) If you want to search for a specific record ID within an entity, append (TrackingID) to the URL, where TrackingID is the ID of the record. For example: localhost/Archer/contentapi/Business_Unit(107826) **Important:** The TrackingID must be enclosed in parentheses.  
  
**Output.** If the call is successful, the API returns a JSON array. If there is a failure, the API issues an exception.

## Samples

The following is a sample request and response. 

### Sample Request

GET /Archer/contentapi/Applications HTTP/1.1

Host: localhost

Authorization: Archer session-id=E5E1CEEDA26A199FE2CAE99755CB71DA

Cache-Control: no-cache

### Sample Response

{

"@odata.context": "localhost/Archer/contentapi/$metadata/$metadata#Risk_Register",

“value”: [

{

"Risk_Register_Id": 107826,

"Actual_Annualized_Loss_Amount": 0,

"Actual_Response_Date": null,

"Adjusted_Qual_Residual_Risk": ["Not Rated"],

"Adjusted_Qual_Risk_Impact": ["Not Rated"],

"Adjusted_Qual_Risk_Likelihood": ["Not Rated"],

"Adjusted_Quantitative_Residual_Risk": ["Not Rated"],

"Adjusted_Quantitative_Risk_Helper": 0,

"Annual_Inherent_Risk": 0,

"Annual_Loss_Expectancy": 0,

"Annual_Residual_Risk": 0,

"Applications_Risk_Register": [],

"Assessment_Approach": [],

"Average_Cost_of_Controls": 0,

"Average_Loss_Amount": 0,

"Business_Processes_Risk_Register": [],

"Business_Units": [],

"Company_Objectives": [],

"Content_Source": ["Archer"],

}

]

}
