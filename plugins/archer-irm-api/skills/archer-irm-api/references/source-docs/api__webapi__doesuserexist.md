# DoesUserExist

The DoesUserExist method returns a Boolean value indicating whether the specified user exists.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the DoesUserExist method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken  |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method   
userName  |  Integer |  User name to search   
  
**Output.** This method returns a Boolean value. If the user exists, it is set to true, and if the user does not exist, it is set to false. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

bFoundFlag = accesscontrol.DoesUserExist(sSessionToken, “username”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/DoesUserExist"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<DoesUserExist xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<userName>string</userName>

</DoesUserExist>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<DoesUserExistResponse xmlns="http://archer-tech.com/webservices/">

<DoesUserExistResult>boolean</DoesUserExistResult>

</DoesUserExistResponse>

</soap:Body>

</soap:Envelope>
