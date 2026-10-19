# DeleteSecurityParameter

The DeleteSecurityParameter method removes a security parameter from the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Delete privileges.

**Parameters.**

The parameters for the DeleteSecurityParameter method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken  |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method   
securityParameterId  |  Integer |  Internal ID of the security parameter as contained in the results of the [accesscontrol.GetSecurityParameters](getsecurityparameters.htm) method   
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = accesscontrol.DeleteSecurityParameter(sSessionToken, 654);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/DeleteSecurityParameter"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<DeleteSecurityParameter xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<securityParameterId>**int** </securityParameterId>

</DeleteSecurityParameter>

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

<DeleteSecurityParameterResponse xmlns="http://archer-tech.com/webservices/">

<DeleteSecurityParameterResult>**int** </DeleteSecurityParameterResult>

</DeleteSecurityParameterResponse>

</soap:Body>

</soap:Envelope>
