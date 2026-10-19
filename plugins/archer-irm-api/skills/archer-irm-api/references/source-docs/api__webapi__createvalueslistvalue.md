# CreateValuesListValue

The CreateValuesListValue method creates a values list item within the specified valuesListId.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CreateValuesListValue method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
valuesListId Integer  |  Integer |  Internal ID of the specific values list for which you want to create a value as included in the results of the [field.GetValueListForField](getvaluelistforfield.htm) method  
valuesListItemName |  String  |  Value to add  
  
For instructions on determining the ID of the values list, see [Determine ID of Values List](determine_id_of_values_list.htm).

**Output.** This method returns an integer. The value is the ID of the values list item in the system. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iReturnCode = field.CreateValuesListValue(sSessionToken, 63, “newvalue”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CreateValuesListValue"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateValuesListValue xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<valuesListId>**int** </valuesListId>

<valuesListValueName>**string** </valuesListValueName>

</CreateValuesListValue>

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

<CreateValuesListValueResponse xmlns="http://archer-tech.com/webservices/">  

<CreateValuesListValueResult>**int** </CreateValuesListValueResult>

</CreateValuesListValueResponse>

</soap:Body>

</soap:Envelope>
