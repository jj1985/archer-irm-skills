# CreateRecords

The CreateRecords method enables the bulk creation of records in an application. When adding contact records, this method adds the user record when the User Account is selected and the user has rights to manage users.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CreateRecords method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
moduleId |  Integer  |  Internal ID of an application as specified in the Application Builder Application Detail Report  
contentRecords  |  String  |  XML structure of the records to add **Note:** For details about constructing this string, see [XML Formatting Guidelines for Field Input](xml_formatting_guidelines_for_field_input.htm).  
  
**Output.** This method returns a string. If the method is successful, the string contains an XML list of the content IDs for the newly created records. If there is a failure, the API issues an exception.

**Important:** If invalid data is supplied, no record is created. In this case, the output is the originally supplied data.

## Samples

Sample C# Code

sResults = record.CreateRecords(sSessionToken, 17, sXML);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CreateRecords"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateRecords xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<moduleId>**int** </moduleId>

<contentRecords>**string** </contentRecords>

</CreateRecords>

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

<CreateRecordsResponse xmlns="http://archer-tech.com/webservices/">

<CreateRecordsResult>**string** </CreateRecordsResult>

</CreateRecordsResponse>

</soap:Body>

</soap:Envelope>
