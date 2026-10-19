# GetChildRecordIds

The GetChildRecordIds method retrieves a list of records related to the given top-level contentId by a locked cross-reference that is bound to the second level.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetChildRecordIds method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
moduleId |  Integer  |  Internal ID of a parent-level record as returned by the [search.ExecuteSearch](executesearch.htm) method  
contentId |  Integer  |  Internal ID of a parent-level record as returned by the [search.ExecuteSearch](executesearch.htm) method  
  
**Output.** This method returns a string. The value is an XML string containing a list of IDs.

## Samples

Sample C# Call

sReturnValues = record.GetChildRecordIds(sSessionToken, 17, 21677);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetChildRecordIds"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetChildRecordIds xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<moduleId>**int** </moduleId>

<contentId>**int** </contentId>

</GetChildRecordIds>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length  
**

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetChildRecordIdsResponse xmlns="http://archer-tech.com/webservices/">

<GetChildRecordIdsResult>**string** </GetChildRecordIdsResult>

</GetChildRecordIdsResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<Children>

<Id>105</Id>

<Id>104</Id>

<Id>1932</Id>

</Children>
