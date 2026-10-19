# GetValueListForField

The GetValueListForField returns the values list for the specified field.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetValueListForField method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
fieldId |  Integer |  Internal ID of the Values List field. **Note:** The ID of a field can be determined by reviewing the Application Detail Report from within Application Builder or by invoking the [record.GetRecordById](getrecordbyid.htm) method and reviewing the mappings.  
  
**Output.** This method returns a string. The value is an XML string containing all available values list items (ID, Value, and Description) in the values list. Second-level items are nested within the first-level SelectDefValue element. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

sValuesList = field.GetValueListForField(sSessionToken, 302);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetValueListForField"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetValueListForField xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<fieldId>**int** </fieldId>

</GetValueListForField>

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

<GetValueListForFieldResponse xmlns="http://archer-tech.com/webservices/">

<GetValueListForFieldResult>**string** </GetValueListForFieldResult>

</GetValueListForFieldResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<SelectDefValues>

<SelectDefValue>

<guid>d074d029-66b2-4631-b555-119e5ec3c274</guid>

<Id>3156</Id>

<Name>False</Name>

<select_value_desc />

<AssociativeFlag>false</AssociativeFlag>

<select_value_color />

<DefaultFlag>false</DefaultFlag>

</SelectDefValue>

<SelectDefValue>

<guid>5b92db8d-dc94-430f-99bf-785d0ccaabf8</guid>

<Id>3155</Id>

<Name>True</Name>

<select_value_desc />

<AssociativeFlag>false</AssociativeFlag>

<select_value_color />

<DefaultFlag>false</DefaultFlag>

</SelectDefValue>

</SelectDefValues>
