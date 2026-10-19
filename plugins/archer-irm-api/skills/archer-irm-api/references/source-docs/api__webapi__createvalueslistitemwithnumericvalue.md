# CreateValuesListItemWithNumericValue

The CreateValuesListItemWithNumericValue method creates a values list item with an associated numeric value. For example, you could create the value "High" with a numeric value of 10 using this method.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CreateValuesListItemWithNumericValue method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
valuesListId Integer  |  Integer |  Internal ID of the specific values list for which you want to create a value as included in the results of the [field.GetValueListForField](getvaluelistforfield.htm) method  
valuesListItemName |  String  |  Value to add  
valuesListItemNumericValue |  Decimal  |  Numeric value to associate with the values list item  
  
**Note:** For instructions on determining the ID of the values list, see [Determine System IDs](determine_id_of_values_list.htm).

**Output.** This method returns an integer. If the method was successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/  
CreateValuesListItemWithNumericValue"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateValuesListItemWithNumericValue xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<valuesListId>**int** </valuesListId>

<valuesListItemName>**string** </valuesListItemName>

<valuesListItemNumericValue>**decimal** </valuesListItemNumericValue>

</CreateValuesListItemWithNumericValue>

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

<CreateValuesListItemWithNumericValueResponse xmlns="http://archer-tech.com/webservices/">

<CreateValuesListItemWithNumericValueResult>**int** </CreateValuesListItemWithNumericValueResult>

</CreateValuesListItemWithNumericValueResponse>

</soap:Body>

</soap:Envelope>
