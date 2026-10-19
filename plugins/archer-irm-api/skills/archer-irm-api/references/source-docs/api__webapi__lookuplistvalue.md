# LookupListValue

The LookupListValue method returns the ID of the values list item containing the search string.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the LookupListValue method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
fieldId |  Integer  |  Internal ID of the field using the values list you want to query  
keyword |  String |  A keyword for which to search in the values list  
  
**Note:** The ID of a field can be determined by reviewing the Application Detail Report from within the Application Builder, or by invoking [record.GetRecordById](getrecordbyid.htm) and reviewing the mappings.

**Output.** This method returns an integer. The value is the ID of the values list item in the system. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iNewID = field.LookupListValue(sSessionToken, 302, “newvalue”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/LookupListValue"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<LookupListValue xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<fieldId>**int** </fieldId>

<keyword>**string** </keyword>

</LookupListValue>

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

<LookupListValueResponse xmlns="http://archer-tech.com/webservices/">

<LookupListValueResult>**int** </LookupListValueResult>

</LookupListValueResponse>

</soap:Body>

</soap:Envelope>
