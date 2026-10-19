# Security Events Report API  
  
The Security Events Report API returns sets of security events for the date specified in the request. Each set can contain up to 50,000 events. The API supports pagination via a query parameter called page.

On this page

  * Usage
  * Example
    * Request Header
    * Request Body Example
    * Response Examples

## Usage

**Privileges.** This API requires read privileges to the Security Events Report, which can be found under the Access Control Reports. 

**URL.** localhost/Archer/api/core/system/AccessControlReports/SecurityEvents

**Method.** POST

Resources.

The resource information for the API is described in the following table. Resource |  Description  
---|---  
Response Format |  JSON  
Requires Authentication |  Yes  
  
**Request body parameters.**

The required request body parameters for the API are described in the following table. Parameter  |  Data Type |  Description  
---|---|---  
eventType |  String |  A valid eventType that the Security Events Report API supports. For additional details, see [Supported eventTypes](supported_event_types.htm).  
eventsForDate |  String |  A valid date that the Security Events Report API generates events for, in the format YYYY-MM-DD. The selected date can range from 6 days to 1 day before the selected date. For example, if today is 2021-01-06 (January 6, 2021), then the range of acceptable dates is between 2021-01-05 (January 5, 2021) and 2021-01-01 (January 1, 2021).  
instanceName |  String |  A valid instance name, which the IIS logs use to track the API request.  
  
**Headers.**

The required headers for the API are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
Content-Type |  String |  application/json  
Authorization |  String |  Archer session-id=sessionToken sessionToken is a valid session token ID for the API user login.  
X-HTTP-Method-Override |  String |  GET  
  
**Pagination.**

The API supports pagination. Each page returns at most 50,000 events. The page number is specified as a query parameter. 

For example, to access the first page, the query parameter should be specified as below:

**URL**. localhost/Archer/api/core/system/AccessControlReports/SecurityEvents?page=1

Similarly, to access the second page, the query parameter should specify page=2

**URL**. localhost/Archer/api/core/system/AccessControlReports/SecurityEvents?page=2

The URL without the page parameter always returns the first page of results.

**Output.**

This response returns Strings. If the request is successful, the response returns the Event, the user that started the event, the event timestamp, and the event details. The API also returns the HTTP Status code 200. 

If the request fails, the API issues an exception and returns other HTTP Status Codes.

## Example

The following example is a Security Events API request and response, which includes examples of both successful and failed responses. Replace the placeholders below with actual values. 

### Request Header

Content-Type: application/json;odata.metadata=none

Authorization: Archer session-id="session token ID from login"

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

X-Http-Method-Override: GET

**Note:** Insert the session token ID from your login. In this documentation, the Archer session-id is represented as "session token ID from login."

### Request Body Example

{

"InstanceName":"Archer",

"EventType": "all events",

"EventsForDate": "2021-06-17"

}

### Response Examples

  * [Security Events Report API successful response](segmentsresources/json_examples/security_event_response.txt "Security Events Report API successful response")

  * [Security Events Report API failure response](segmentsresources/json_examples/security_event_response_failure.txt "Security Events Report API failure response")

In the failure response example, the API request failed due to an invalid parameter, All vents, where Events is misspelled.

