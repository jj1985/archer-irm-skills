# UpdateValuesListValue

The UpdateValuesListValue method modifies the text value of the specified valuesListValueId.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateValuesListValue method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
valuesListValueId |  Integer  |  Internal ID of the specific values list value that you want to modify as returned by the [field.LookupListValue](lookuplistvalue.htm) method  
valuesListValueName |  String |  Value that you want to assign the specified values list value  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = field.UpdateValuesListValue(sSessionToken, 1125, “newervalue”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateValuesList  
Value"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateValuesListValue xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<valuesListValueId>**int** </valuesListValueId>

<valuesListValueName>**string** </valuesListValueName>

</UpdateValuesListValue>

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

<UpdateValuesListValueResponse xmlns="http://archer-tech.com/webservices/">

<UpdateValuesListValueResult>**int** </UpdateValuesListValueResult>

</UpdateValuesListValueResponse>

</soap:Body>

</soap:Envelope>
