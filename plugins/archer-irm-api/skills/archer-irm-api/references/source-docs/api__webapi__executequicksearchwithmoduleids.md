# ExecuteQuickSearchWithModuleIds

The ExecuteQuickSearchWithModuleIds method runs a keyword search on the specified applications or questionnaires.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the ExecuteQuickSearchWithModuleIds method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
moduleIds |  String  |  Internal IDs of the applications or questionnaires that you want to query  
keywords  |  String  |  Search keywords as you would enter them if searching in the application or questionnaire  
pageNumber |  Integer  |  Integer of the page (1,2,3,…,n) of search results to return  
pageSize |  Integer  |  Number of records to display per page of search results  
  
**Output.** This method returns a string. The value is an XML string containing the fields of records in the specified applications or questionnaires matching the specific keywords.

## Samples

Sample C# Call

sSearchResults = search.ExecuteQuickSearchWithModuleIds(sSessionToken, “17”, “keyword”, 1, 20);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/search.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/WithModuleIds"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<ExecuteQuickSearchWithModuleIds xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<moduleIds>**string** </moduleIds>

<keywords>**string** </keywords>

<pageNumber>**int** </pageNumber>

<pageSize>**int** </pageSize>

</ExecuteQuickSearchWithModuleIds >

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

<ExecuteQuickSearchWithModuleIdsResponse xmlns="http://archer-tech.com/webservices/">

<WithModuleIdsResult>**string** </WithModuleIdsResult>

</ExecuteQuickSearchWithModuleIdsResponse>

</soap:Body>

</soap:Envelope>
