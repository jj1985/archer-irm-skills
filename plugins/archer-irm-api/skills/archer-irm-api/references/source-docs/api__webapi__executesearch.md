# ExecuteSearch

The ExecuteSearch method runs a search according to custom criteria. 

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the ExecuteSearch method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
searchOptions |  String  |  XML string that provides the search criteria. **Note:** For details about constructing this string, see [XML Formatting Guidelines for 5.x Search Input](xml_formatting_guidelines_for_search_input.htm).  
pageNumber |  Integer  |  Integer of the page (1,2,3,...,n) of search results to return  
  
**Output.** This method returns a string. The value is an XML string containing the fields of records matching the search criteria.

**Note:** The ExecuteSearch method displays a default time of "12:00:00 AM" in the XML response for Date field issues with Time enabled. If your select Date Only, time is not included.

## Samples

Sample C# Call

sReturnValue = search.ExecuteSearch(sSessionToken, sXML, 1);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/search.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/ExecuteSearch"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<ExecuteSearch xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<searchOptions>**string** </searchOptions>

<pageNumber>**int** </pageNumber>

</ExecuteSearch>

</soap:Body>

</soap:Envelope>

Sample Search XML

<SearchReport>

<PageSize>20</PageSize>

<MaxRecordCount>100</MaxRecordCount>

<ShowStatSummaries>false</ShowStatSummaries>

<DisplayFields>

<DisplayField>7205</DisplayField>

<DisplayField>7226</DisplayField>

<DisplayField>7232</DisplayField>

<DisplayField>7242</DisplayField>

</DisplayFields>

<Criteria>

<Keywords>Windows</Keywords>

<ModuleCriteria>

<Module>17</Module>

<IsKeywordModule>true</IsKeywordModule>

<SortFields>

<SortField>

<Field>7205</Field>

<SortType>Ascending</SortType>

</SortField>

</SortFields>

</ModuleCriteria>

</Criteria>

</SearchReport>

Sample Search XML

<SearchReport>

<PageSize>100</PageSize>

<DisplayFields>

<DisplayField>9399</DisplayField>

<DisplayField>9402</DisplayField>

<DisplayField>9403</DisplayField>

<DisplayField>9405</DisplayField>

<DisplayField>9411</DisplayField>

<DisplayField>9413</DisplayField>

</DisplayFields>

<Criteria>

<ModuleCriteria>

<Module>331</Module>

<IsKeywordModule>false</IsKeywordModule>

<SortFields>

<SortField>

<Field>9399</Field>

<SortType>Ascending</SortType>

</SortField>

</SortFields>

</ModuleCriteria>

<Filter>

<Conditions>

<TextFilterCondition>

<Operator>Contains</Operator>

<Field>9402</Field>

<Value>A comment</Value>

</TextFilterCondition>

<TextFilterCondition>

<Operator>Contains</Operator>

<Field>9403</Field>

<Value>123 Lotus</Value>

</TextFilterCondition>

</Conditions>

<OperatorLogic>1 OR 2</OperatorLogic>

</Filter>

</Criteria>

</SearchReport>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length  
**

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<ExecuteSearchResponse xmlns="http://archer-tech.com/webservices/">

<ExecuteSearchResult>**string** </ExecuteSearchResult>

</ExecuteSearchResponse>

</soap:Body>

</soap:Envelope>
