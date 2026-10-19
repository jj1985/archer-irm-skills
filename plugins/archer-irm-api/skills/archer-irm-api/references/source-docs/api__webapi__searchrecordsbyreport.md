# SearchRecordsByReport

The SearchRecordsByReport method runs a search of records according to the specified report ID or report GUID.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the SearchRecordsByReport method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
reportIdOrGuid |  String  |  Internal ID or GUID of the report whose records you want to query  
pageNumber |  Integer  |  Integer of the page (1,2,3,…,n) of search results to return  
  
**Output.** This method returns a string. The value is an XML string containing the fields of records matching the report ID or GUID.

## Samples

Sample C# Call

sSearchResults = search.SearchRecordsByReport(sSessionToken,   
“7538F922-7794-11E2-BCD8-634F61887098”, 1);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/search.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/SearchRecordsByReport"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<SearchRecordsByReport xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<reportIdOrGuid>**string** </reportIdOrGuid>

<pageNumber>**int** </pageNumber>

</SearchRecordsByReport>

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

<SearchRecordsByReportResponse xmlns="http://archer-tech.com/webservices/">

<SearchRecordsByReportResult>**string** </SearchRecordsByReportResult>

</SearchRecordsByReportResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<Records count="18">

<Metadata>

<FieldDefinitions>

<FieldDefinition id="1580" name="Policy Name" alias="Policy_Name" />

<FieldDefinition id="1583" name="Policy Statement" alias="Policy_Statement" />

</FieldDefinitions>

</Metadata>

<LevelCounts>

<LevelCount id="3" count="18" />

</LevelCounts>

<Record contentId="1720" levelId="3" moduleId="65" parentId="0">

<Field id="1580" type="1">00.0 Introduction</Field>

<Field id="1583" type="1">The Company's Information Security Policy defines the fundamental principles for the protection of Company information resources, the proper controls needed to ensure compliance with internal and external regulations, and to uphold the Company's reputation with its clients. All personnel are responsible for ensuring compliance with the Company's Information Security Policy.</Field>

</Record>

</Records>
