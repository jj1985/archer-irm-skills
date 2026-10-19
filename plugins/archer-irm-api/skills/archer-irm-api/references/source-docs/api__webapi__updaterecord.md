# UpdateRecord

The UpdateRecord method modifies the specified record.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateRecord method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
moduleId |  Integer  |  ID of an application as specified in the Application Builder Application Detail Report.  
contentId |  Integer  |  System ID for the record within the specified application as returned by the [search.ExecuteSearch](executesearch.htm) method. This is a unique value used throughout all of Archer, and not the [Field Specific Attribute](field-specific_attributes.htm) Tracking ID.  **Note:** This cannot be an Application ID.  
fieldValues  |  String |  XML string of the fields and values to modify.  **Note:** For details about constructing this string, see [[XML Formatting Guidelines for Field Input](xml_formatting_guidelines_for_field_input.htm)](xml_formatting_guidelines_for_field_input.htm).  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iReturnCode = record.UpdateRecord(sSessionToken, 17, 234, sXML);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateRecord"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateRecord xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<moduleId>**int** </moduleId>

<contentId>**int** </contentId>

<fieldValues>**string** </fieldValues>

</UpdateRecord>

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

<UpdateRecordResponse xmlns="http://archer-tech.com/webservices/">

<UpdateRecordResult>**int** </UpdateRecordResult>

</UpdateRecordResponse>

</soap:Body>

</soap:Envelope>
