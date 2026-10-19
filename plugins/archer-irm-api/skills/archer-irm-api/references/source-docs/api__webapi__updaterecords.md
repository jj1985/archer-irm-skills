# UpdateRecords

The UpdateRecords method enables the bulk update of records in an application.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateRecords method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
moduleId |  Integer  |  ID of an application as specified in the Application Builder Application Detail Report.  
contentRecords |  String |  XML structure of the records to modify.  **Note:** For details about constructing this string, see [XML Formatting Guidelines for Field Input](xml_formatting_guidelines_for_field_input.htm).  
  
**Output.** This method returns an XML string indicating the records that failed to update.

## Samples

Sample C# Call

sResults = record.UpdateRecords(sSessionToken, 17, sXML);

**Note:** The last parameter is in XML-- multiple <Record></Record> entries surrounded by <Records></Records>

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateRecords"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateRecords xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<moduleId>**int** </moduleId>

<contentRecords>**string** </contentRecords>

</UpdateRecords>

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

<UpdateRecordsResponse xmlns="http://archer-tech.com/webservices/">

<UpdateRecordsResult>**string** </UpdateRecordsResult>

</UpdateRecordsResponse>

</soap:Body>

</soap:Envelope>
