# TerminateSession

The TerminateSession method expires the specified session.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Delete privileges.

**Parameter.**

The parameter for the TerminateSession method is described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

**Important:** For backwards compatibility with version 4.x, do not terminate a sysadmin session.

## Samples

Sample C# Code

iReturnCode = general.TerminateSession(sSessionToken);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/general.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/TerminateSession"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<TerminateSession xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

</TerminateSession>

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

<TerminateSessionResponse xmlns="http://archertech.com/webservices/">

<TerminateSessionResult>**int** </TerminateSessionResult>

</TerminateSessionResponse>

</soap:Body>

</soap:Envelope>
