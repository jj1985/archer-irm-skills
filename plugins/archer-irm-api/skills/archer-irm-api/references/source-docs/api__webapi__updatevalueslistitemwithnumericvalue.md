# UpdateValuesListItemWithNumericValue

The UpdateValuesListItemWithNumericValue method enables you to update the text value and numeric value of a values list item. It also enables you to associate a numeric value with a values list item that does not currently have an assigned numeric value.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateValuesListItemWithNumericValue method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
valuesListItemId |  Integer  |  Internal ID of the specific values list value that you want to modify as returned by the [field.LookupListValue](lookuplistvalue.htm) method.  
valuesListItemNumericValue |  Decimal  |  Numeric value that you want to associate with the values list item.  **Note:** This can be a positive, negative, or decimal value.  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = field.UpdateValuesListItemWithNumericValue(sSessionToken, 1125, “newitemname”, 10);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/  
UpdateValuesListItemWithNumericValue"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateValuesListItemWithNumericValue xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<valuesListItemId>**int** </valuesListItemId>

<valuesListItemName>**string** </valuesListItemName>

<valuesListItemNumericValue>**decimal** </valuesListItemNumericValue>

</UpdateValuesListItemWithNumericValue>

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

<UpdateValuesListItemWithNumericValueResponse xmlns="http://archer-tech.com/webservices/">

<UpdateValuesListItemWithNumericValueResult>**int** </UpdateValuesListItemWithNumericValueResult>

</UpdateValuesListItemWithNumericValueResponse>

</soap:Body>

</soap:Envelope>
