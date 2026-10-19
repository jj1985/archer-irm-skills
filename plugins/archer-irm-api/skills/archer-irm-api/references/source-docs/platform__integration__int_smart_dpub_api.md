# Smart Data Publications API

The Smart Data Publications (SDP) API retrieves an exported ZIP file for a specific SDP, in the form of a content stream.

On this page

  * Usage
  * Example
    * Request Header
    * Response Header

## Usage

**Privileges.** This API requires read privileges to Manage Smart Data Publication, which can be found under Access Roles.

**URL.** https://archer/api/core/smartdatapublication/download/*sdpid*

**Method.** GET

Resources.

The resource information for the API is described in the following table. Resource |  Description  
---|---  
Response Format |  Stream  
Requires Authentication |  Yes  
  
**Request headers.**

The required request headers for the API are described in the following table. Parameter |  Data Type |  Value  
---|---|---  
Accept |  String |  application/octet-stream  
Authorization |  String |  Archer session-id=sessionToken sessionToken is a valid session token ID for the API user login.  
  
**Response headers.**

The required response headers for the API are described in the following table. Parameter |  Data Type |  Value  
---|---|---  
Content-Disposition |  String |  The type and file name of the downloaded ZIP file  
zip-crc |  String |  CRC of the downloaded ZIP file to validate file integrity  
  
**Output.**

This response returns file data as a stream. If the request is successful, the response returns an exported ZIP file for the specified smart data publication, in the form of a content stream. The API also returns the HTTP Status code 200.

If the request fails, the API issues an exception and returns 1 of 2 HTTP Status codes, 400 - Bad Request or 500 - Internal Server Error.

## Example

The following example is a Smart Data Publications API request and response, which includes examples of both successful and failed responses. Replace the placeholders below with actual values.

### Request Header

Authorization: Archer session-id="session token ID from login"

Accept: application/octet-stream

### Response Header

  * Smart data publications API successful response

Content-Disposition: attachment; filename="Modules_Export_164.zip"

zip-crc: 66C42CD5

  * Smart data publications API failure response

"500 Could not download exported files for Smart Data Publication Modules Export."

