# GetValuesListValue

The GetValuesListValue method retrieves the text value of the specified valuesListValueId.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetValuesListValue method are described in the following table. Parameter  | Data Type | Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
valuesListValueId |  Integer |  Internal ID of the specific values list value, as returned by the [field.LookupListValue](lookuplistvalue.htm) method, whose text value you want to retrieve  
  
**Output.** This method returns a string. If the method is successful, the value represents the text value of the values list item. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

sValue = field.GetValuesListValue(sSessionToken, 468);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetValuesListValue"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetValuesListValue xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<valuesListValueId>**int** </valuesListValueId>

</GetValuesListValue>

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

<GetValuesListValueResponse xmlns="http://archer-tech.com/webservices/">

<GetValuesListValueResult>**string** </GetValuesListValueResult>

</GetValuesListValueResponse>

</soap:Body>

</soap:Envelope>
