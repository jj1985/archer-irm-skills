# GetSecurityParameterName

The GetSecurityParameterName method returns the textual name of a security parameter defined in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetSecurityParameterName method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
securityParameters |  Integer |  Internal ID of the security parameter as contained in the results of the [accesscontrol.GetSecurityParameters](getsecurityparameters.htm) method   
  
**Output.** This method returns a string. If the method is successful, the value is a text description of the security parameter's name as it appears in the GUI. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sSecName = accesscontrol.GetSecurityParameterName(sSessionToken, 1);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetSecurityParameterName"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetSecurityParameterName xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<securityParameter>**int** </securityParameter>

</GetSecurityParameterName>

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

<GetSecurityParameterNameResponse xmlns="http://archer-tech.com/webservices/">

<GetSecurityParameterNameResult>**string** </GetSecurityParameterNameResult>

</GetSecurityParameterNameResponse>

</soap:Body>

</soap:Envelope>
