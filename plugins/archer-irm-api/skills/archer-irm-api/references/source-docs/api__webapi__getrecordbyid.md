# GetRecordById

The GetRecordById method returns all details of the specified record. The search filters are based on the specified option setting: System ID or Application ID.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetRecordByID method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
moduleId |  Integer  |  Internal ID of an application as specified in the Application Builder Application Detail Report **Note:** This parameter has no effect on the function of the GetRecordById method.  
contentId |  Integer  |  Internal ID of a record within the specified application as returned by the [search.ExecuteSearch](executesearch.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value is the XML structure of the requested record. If there is a failure, the API issues an exception.

For details about the returned XML string, see [XML Formatting Used in Field Results](xml_formatting_used_in_field_results.htm).

## Samples

Sample C# Call

sResults = record.GetRecordById(sSessionToken, 17, 234);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetRecordById"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetRecordById xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<moduleId>**int** </moduleId>

<contentId>**int** </contentId>

</GetRecordById>

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

<GetRecordByIdResponse xmlns="http://archer-tech.com/webservices/">

<GetRecordByIdResult>**string** </GetRecordByIdResult>

</GetRecordByIdResponse>

</soap:Body>

</soap:Envelope>
