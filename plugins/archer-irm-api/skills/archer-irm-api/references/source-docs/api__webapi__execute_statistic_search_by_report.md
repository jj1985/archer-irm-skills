# ExecuteStatisticSearchByReport

The ExecuteStatisticSearchByReport method runs a statistics search according to custom criteria.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the ExecuteStatisticSearchByReport method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
reportIdOrGuid |  String  |  Internal ID or GUID of the report whose records you want to query  
pageNumber |  Integer  |  Integer of the page (1,2,3,...,n) of search results to return  
  
**Output.** This method returns a string. The value is an XML string containing the fields of records matching the statistics search criteria.

## Samples

Sample C# Code

sSearchResults = search.ExecuteStatisticSearchByReport(sSessionToken, "3156", 1);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/search.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/ExecuteStatisticSearchByReport"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<ExecuteStatisticSearchByReport xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<reportIdOrGuid>**string** </reportIdOrGuid>

<pageNumber>**int** </pageNumber>

</ExecuteStatisticSearchByReport>

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

<ExecuteStatisticSearchByReportResponse xmlns="http://archer-tech.com/webservices/">

<ExecuteStatisticSearchByReportResult>**string** </ExecuteStatisticSearchByReportResult>

</ExecuteStatisticSearchByReportResponse>

</soap:Body>

</soap:Envelope>
