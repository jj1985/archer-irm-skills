# Field Administration Activity Logs Report API

The Field Administration Activity Logs Report API returns sets of activity logs for the date specified in the request. Each set can contain up to 50,000 records. The API supports pagination using a query parameter called page.

On this page

  * Usage
  * Example
    * Request Header
    * Request Body Example
    * Response Example

## Usage

**Privileges.** This API requires read privileges to the Administration Activity Logs Report, which can be found under the Access Control Reports.

**URL.** localhost/Archer/api/core/system/AdministrationActivityLogsReports/AdministrationActivityLogsReport/

**Method.** POST

Resources.

The resource information for the API is described in the following table. Resource |  Description  
---|---  
Response Format |  JSON  
Requires Authentication |  Yes  
  
**Request body parameters.**

The required request body parameters for the API are described in the following table. Parameter |  Data Type |  Description  
---|---|---  
InitiatingUserId | Int | A valid user identifier representing the user who initiated the action.  
ActionsForDate | String | The target date for which actions are being requested, in the format YYYY-MM-DD.  
ApplicationId | Int | A valid identifier of the application where the action occurred.  
ActionType |  String |  The type of action being queried or logged, such as Field Creation.  
  
**Headers.**

The required headers for the API are described in the following table. Parameter |  Data Type |  Value  
---|---|---  
Content-Type |  String |  application/json  
Authorization |  String |  Archer session-id=sessionToken sessionToken is a valid session token ID for the API user login.  
X-HTTP-Method-Override |  String |  GET  
  
**Pagination.**

The API supports pagination. Each page returns at most 50,000 events. The page number is specified as a query parameter.

For example, to access the first page, the query parameter should be specified as below:

**URL**. localhost/Archer/api/core/system/AdministrationActivityLogsReports/FieldAdministrationActivityLogsReport?page=1

  * The URL without the page parameter always returns the first page of results.

  * The API also returns the HTTP Status code 200.

  * If the request fails, the API issues an exception and returns other HTTP Status Codes.

## Example

The following example is a Administration Activity Logs API request and response. Replace the placeholders below with actual values.

### Request Header

Content-Type: application/json;odata.metadata=none

Authorization: Archer session-id="session token ID from login"

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

X-Http-Method-Override: GET

**Note:** Insert the session token ID from your login. In this documentation, the Archer session-id is represented as "session token ID from login."

### Request Body Example

{

"InitiatingUserId":"2",

"ActionsForDate":"2025-03-20",

"ApplicationId":"635",

"ActionType":"Field Creation"

}

### Response Example

[Administration Activity Logs response](segmentsresources/json_examples/administration_activity_logs_response.txt "Administration Activity Logs response")
