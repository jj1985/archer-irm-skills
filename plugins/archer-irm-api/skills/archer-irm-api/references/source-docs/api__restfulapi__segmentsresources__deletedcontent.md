# Retrieve a log of deleted content

The _DeletedContent_ segment retrieves a list of deleted records. This list can be used for audit purposes. Results can be filtered with request parameters.

**Important:** Only the System Administrator role and Deleted Record Auditor role can access this API segment.

Request

GET localhost/Archer/api/V2/DeletedContent

Request Header

Authorization: Archer session-id="session token ID from login"

Request Parameters

Use these parameters with your request to filter your results. All of these parameters are optional.

The following table describes the parameters that can be used with _DeletedContent_. Parameter Name |  Data Type |  Description  
---|---|---  
startDate |  Date Only |  Returns records created on and after a certain date. Null returns all deleted records. Format for startDate is yyyy-mm-dd.  
endDate |  Date Only |  Returns records created on and before a certain date.  If Null, endDate defaults to the current date and returns all deleted records Format for endDate is yyyy-mm-dd.  
moduleid |  Numeric |  Returns records from the application, questionnaire, or sub-form associated with the given module ID. Null returns all application, questionnaire, or sub-form records that you have access to.  
levelid |  Numeric |  Returns records from the level associated with the given level ID. Null returns all levels you have access to.   
skip |  Numeric |  Return records after the skipping the provided number of records. Used in pagination. Default value is 0.  
take |  Numeric |  Returns the given number of records. Used in pagination. Default value is 10000.  
  
Response Parameters

Responses can contain the following parameters.

The following table describes the parameters returned by _DeletedContent_. Parameter Name | Data Type |  Description  
---|---|---  
TotalRecords |  Numeric |  Total number of records available  
RecordsShown |  Numeric |  Total number of records fetched  
DeletedContents |  ContentID |  Numeric |  Deleted record of content ID  
DeletedDateTime |  DateTime |  Date and time stamp the record was deleted  
UserID |  Numeric |  User who deleted the record  
ModuleID |  Numeric |  Application, questionnaire, or sub-form that the record was deleted from  
LevelID |  Numeric |  Level the record was deleted from  
  
Request Examples

  * localhost/Archer/api/V2/DeletedContent?StartDate=yyyy-mm-dd&levelID=###

  * localhost/Archer/api/V2/DeletedContent?StartDate=yyyy-mm-dd&skip=#

  * localhost/Archer/api/V2/DeletedContent?StartDate=yyyy-mm-dd&take=##

Response Examples

  * [Successful response](json_examples/deleted_content_success.txt)

  * [End date must be earlier than or equal to today's date.](json_examples/deleted_content_bad_end.txt)

  * [Start date must be earlier than or equal to the end date.](json_examples/deleted_content_bad_start.txt)

  * [Start or end date must be earlier than or equal to today's date.](json_examples/deleted_content_bad_start_or_end.txt)

