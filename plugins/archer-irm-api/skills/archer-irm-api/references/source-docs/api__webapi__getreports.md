# GetReports

The GetReports method returns all reports and their associated report GUIDs that the user making the API call has permissions to.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetReports method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
  
**Output.** This method returns a string. The value is an XML string containing the information from the reports and their corresponding GUIDs.

## Samples

Sample C# Code

sReturnValue = search.GetReports(sSessionToken);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/search.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetReports"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetReports xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

</GetReports>

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

<GetReportsResponse xmlns="http://archer-tech.com/webservices/">

<GetReportsResult>**string** </GetReportsResult>

</GetReportsResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<ReportValues>

<ReportValue>

<ReportName>Policies - Summary view</ReportName>

<ReportDescription>This report displays a listing of all security Policies.</ReportDescription>

<ReportGUID>22961b81-4866-40ea-a298-99afb348598d</ReportGUID>

<ApplicationName>Policies</ApplicationName>

<ApplicationGUID>4cf0d0c6-4b51-404c-91c2-40ade972e95b  
</ApplicationGUID>

</ReportValue>

</ReportValues>
