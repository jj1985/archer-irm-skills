# GetSearchOptionsByGuid

The GetSearchOptionsByGuid method returns a search string based upon the criteria entered. The returned search string can then be used by [search.ExecuteSearch](executesearch.htm).

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetSearchOptionsByGuid method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
searchReportGuid |  String |  The GUID of the report for which you are searching. **Important:** Statistics reports are not supported. **Note:** You can use [search.GetReports](getreports.htm) to find a specific report GUID.  
  
**Output.** This method returns a string. The value is an XML string that can be used as the searchOptions parameter in [search.ExecuteSearch](executesearch.htm). If there is an error, the returned value will either be “NULL” or an empty string.

## Samples

Sample C# Call

sSearchXML = search.GetSearchOptionsByGuid(sessionToken, sGuid);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/search.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetSearchOptionsByGuid"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetSearchOptionsByGuid xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<searchReportGuid>**string** </searchReportGuid>

</GetSearchOptionsByGuid>

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

<GetSearchOptionsByGuidResponse xmlns="http://archer-tech.com/webservices/">

<GetSearchOptionsByGuidResult>**string** </GetSearchOptionsByGuidResult>

</GetSearchOptionsByGuidResponse>

</soap:Body>

</soap:Envelope>
