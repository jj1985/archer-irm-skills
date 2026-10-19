# CreateSubformRecord

The CreateSubformRecord method creates a sub-form record using the specified values. When you save the sub-form, the API returns the sub-form content ID, which you then use when saving the parent record.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CreateSubformRecord method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
subformModuleId |  Integer  |  Internal ID of the sub-form as specified in the Application Builder Sub-Form Detail Report  
subformFieldID |  Integer  |  Internal ID of the Sub-Form field as specified in the Application Builder Application Detail Report  
fieldValues |  String  |  XML structure of the fields and values to add **Note:** For details about constructing this string, see [XML Formatting Guidelines for Field Input](xml_formatting_guidelines_for_field_input.htm).  
  
**Output.** This method returns an integer. If the method is successful, the value is the content ID of the newly created sub-form record. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iContentID = record.CreateSubformRecord(sSessionToken, 316, 7621, sXML);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archertech.com/webservices/CreateSubform  
Record"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateSubformRecord xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<subformModuleId>**int** </subformModuleId>

<subformFieldId>**int** </subformFieldId>

<fieldValues>**string** </fieldValues>

</CreateSubformRecord>

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

<CreateSubformRecordResponse xmlns="http://archer-tech.com/webservices/">

<CreateSubformRecordResult>**int** </CreateSubformRecordResult>

</CreateSubformRecordResponse>

</soap:Body>

</soap:Envelope>
