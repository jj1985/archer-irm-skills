# GetValuesList

The GetValuesList method returns the first level of values for the specified values list.

**Note:** If using a 2-level values list, second-level values cannot be returned. They can be discovered with the [field.GetValueListByParent](getvaluelistbyparent.htm) method.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetValuesList method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
valuesListId |  Integer |  Internal ID of the specific values list you want to retrieve as included in the results of the [field.GetValueListForField](getvaluelistforfield.htm) method  
  
For instructions on determining the ID of the values list, see [Determine ID of Values List](determine_id_of_values_list.htm).

**Output.** This method returns a string. The value is an XML string containing all of the top-level items (ID, Value, and Description) in the values list. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sValuesList = field.GetValuesList(sSessionToken, 63);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetValuesList"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetValuesList xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<valuesListId>**int** </valuesListId>

</GetValuesList>

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

<GetValuesListResponse xmlns="http://archer-tech.com/webservices/">

<GetValuesListResult>**string** </GetValuesListResult>

</GetValuesListResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<SelectDefValues>

<SelectDefValue>

<guid>a765b5c7-60f1-49a7-861d-2065422131a0</guid>

<Id>3156</Id>

<Name>False</Name>

<select_value_desc />

<AssociativeFlag>false</AssociativeFlag>

<select_value_color />

<DefaultFlag>false</DefaultFlag>

</SelectDefValue>

<SelectDefValue>

<guid>9d72c7a7-4620-448b-9f26-038f076d76a1</guid>

<Id>3155</Id>

<Name>True</Name>

<select_value_desc />

<AssociativeFlag>false</AssociativeFlag>

<select_value_color />

<DefaultFlag>false</DefaultFlag>

</SelectDefValue>

</SelectDefValues>
