# DeleteValuesListValue

The DeleteValuesListValue method removes the specified values list item.

**Important:** Delete any child values before deleting a parent value.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Delete privileges.

**Parameters.**

The parameters for the DeleteValuesListValue method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
valuesListId |  Integer |  Internal ID of the specific values list that you want to delete as included in the results of the [field.GetValueListForField](getvaluelistforfield.htm) method  
valuesListValueId |  Integer |  Internal ID of the specific values list value that you want to delete as returned by the [field.LookupListValue](lookuplistvalue.htm) method  
  
For instructions on determining the ID of the values list, see [Determine ID of Values List](determine_id_of_values_list.htm).

**Output.** This method returns an integer. The value is 1 if the method was successful. The API issues an exception if there is a failure.

## Samples

Sample C# Call

iReturnCode = field.DeleteValuesListValue(sSessionToken, 63, 1125);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/DeleteValuesListValue"

<?xml version="1.0" encoding="utf-8"?>  
  

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<DeleteValuesListValue xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<valuesListId>**int** </valuesListId>

<valuesListValueId>**int** </valuesListValueId>

</DeleteValuesListValue>

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

<DeleteValuesListValueResponse xmlns="http://archer-tech.com/webservices/">

<DeleteValuesListValueResult>**int** </DeleteValuesListValueResult>

</DeleteValuesListValueResponse>

</soap:Body>

</soap:Envelope>
