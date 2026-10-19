# GetAccessHistory

The GetAccessHistory method returns access history data for a specific record in a specified application.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetAccessHistory method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
contentId |  Integer  |  Internal ID of a record within the specified application as returned by the [search.ExecuteSearch](executesearch.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value is an XML string that contains access history data for the specific record. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

sResults = record.GetAccessHistory(sSessionToken, 21677);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetAccessHistory"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetAccessHistory xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<contentId>**int** </contentId>

</GetAccessHistory>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetAccessHistoryResponse xmlns="http://archer-tech.com/webservices/">

<GetAccessHistoryResult>**string** </GetAccessHistoryResult>

</GetAccessHistoryResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<ContentHits>

<contentHit>

<user id="200">username</user>

<hitTimestamp>8/18/2012 7:37:11 PM</hitTimestamp>

</contentHit>

</ContentHits>
