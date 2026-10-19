# LookupUserId

The LookupUserId method returns a user ID from the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the LookupUserId method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
userName |  String |  Provides the user name of the user as returned by the [accesscontrol.LookupUserName](lookupusername.htm) method  
  
**Output.** This method returns an integer. If the method is successful, the value is the corresponding user ID. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iUserID = accesscontrol.LookupUserId(sSessionToken, “username”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/LookupUserId"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<LookupUserId xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<username>**string** </username>

</LookupUserId>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<LookupUserIdResponse xmlns="http://archer-tech.com/webservices/">

<LookupUserIdResult>**int** </LookupUserIdResult>

</LookupUserIdResponse>

</soap:Body>

</soap:Envelope>
