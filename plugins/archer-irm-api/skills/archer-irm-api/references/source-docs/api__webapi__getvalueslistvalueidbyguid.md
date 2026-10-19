# GetValuesListValueIdByGUID

The GetValuesListValueIDByGUID method returns the ID of the values list value associated with the specified GUID.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetValuesListValueIDByGUID method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
GUID  |  String  |  The GUID for the desired values list value  
  
**Output.** This method returns an integer. If the method is successful, the value is the ID of the values list value associated with the GUID. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iReturnCode = field.GetValuesListValueIdByGUID(sSessionToken,   
“7538F922-7794-11E2-BCD8-634F61887098”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetValuesListValueIdByGUID"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetValuesListValueIdByGUID xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<GUID>**string** </GUID>

</GetValuesListValueIdByGUID>

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

<GetValuesListValueIdByGUIDResponse xmlns="http://archer-tech.com/webservices/">

<GetValuesListValueIdByGUIDResult>**int** </GetValuesListValueIdByGUIDResult>

</GetValuesListValueIdByGUIDResponse>

</soap:Body>

</soap:Envelope>
