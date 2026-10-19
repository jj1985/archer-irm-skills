# UpdateValuesListNumericValueToNull

The UpdateValuesListNumericValueToNull method sets the numeric value associated with the specified valuesListValueID to null.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateValuesListNumericValueToNull method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
valuesListItemId |  Integer  |  Internal ID of the specific values list value that you want to modify as returned by the [field.LookupListValue](lookuplistvalue.htm) method  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iReturnCode = field.UpdateValuesListNumericValueToNull(sSessionToken, iItemID);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateValuesListNumericValueToNull"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateValuesListNumericValueToNull xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<valuesListItemId>**int** </valuesListItemId>

</UpdateValuesListNumericValueToNull>

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

<UpdateValuesListNumericValueToNullResponse xmlns="http://archer-tech.com/webservices/">

<UpdateValuesListNumericValueToNullResult>**int** </UpdateValuesListNumericValueToNullResult>

</UpdateValuesListNumericValueToNullResponse>

</soap:Body>

</soap:Envelope>
