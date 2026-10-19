# ExecuteStatisticSearch

The ExecuteStatisticSearch method runs a statistics search according to custom criteria.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the ExecuteStatisticSearch method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
searchOptions |  String  |  XML string that provides the search criteria **Note:** For details about constructing this string, see [XML Formatting Guidelines for Search Input](xml_formatting_guidelines_for_search_input.htm).  
pageNumber |  Integer  |  Integer of the page (1,2,3,...,n) of search results to return.  
  
**Output.** This method returns a string. The value is an XML string containing the fields of records matching the statistics search criteria.

**Note:** The ExecuteStatisticSearch method displays a default time of 12:00:00 AM in the XML response for Date field issues with Time enabled. If your select Date Only, time is not included.

## Samples

Sample C# Code

sReturnValue = search.ExecuteStatisticSearch(sSessionToken, sXML, 1);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/search.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/ExecuteStatisticSearch"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<ExecuteStatisticSearch xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<searchOptions>**string** </searchOptions>

<pageNumber>**int** </pageNumber>

</ExecuteStatisticSearch>

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

<ExecuteStatisticSearchResponse xmlns="http://archer-tech.com/webservices/">

<ExecuteStatisticSearchResult>**string** </ExecuteStatisticSearchResult>

</ExecuteStatisticSearchResponse>

</soap:Body>

</soap:Envelope>
