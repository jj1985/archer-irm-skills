# ExecuteQuickSearchWithSolutionId

The ExecuteQuickSearchWithSolutionId method runs a keyword search on the specified solution.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the ExecuteQuickSearchWithSolutiond method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
solutionId |  Integer  |  Internal ID of the solution that you want to query  
keywords  |  String  |  Search keywords as you would enter them if searching in the solution  
pageNumber |  Integer  |  Integer of the page (1,2,3,…,n) of search results to return  
pageSize |  Integer  |  Number of records to display per page of search results  
  
**Output.** This method returns a string. The value is an XML string containing the fields of records in the specified solution matching the specific keywords.

## Samples

Sample C# Code

sSearchResults = search.ExecuteQuickSearchWithSolutionId(sSessionToken, 6, “keyword”, 1, 20);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/search.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/WithSolutionId"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<ExecuteQuickSearchWithSolutiond xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<solutionId>**int** </solutionId>

<keywords>**string** </keywords>

<pageNumber>**int** </pageNumber>

<pageSize>**int** </pageSize>

</ExecuteQuickSearchWithSolutiond>

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

<ExecuteQuickSearchWithSolutiondResponse  
xmlns="http://archer-tech.com/webservices/">

<WithSolutionIdResult>**string** </WithSolutionIdResult>

</ExecuteQuickSearchWithSolutiondResponse>

</soap:Body>

</soap:Envelope>
