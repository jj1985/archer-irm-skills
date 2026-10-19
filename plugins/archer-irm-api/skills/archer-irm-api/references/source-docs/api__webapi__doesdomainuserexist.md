# DoesDomainUserExist

The DoesDomainUserExist method returns a Boolean indicating whether the specified user exists.

On this page

  * Usage
  * Samples

## Usage

**Privileges**. This method requires Read privileges.

**Parameters**.

The parameters for the DoesDomainUserExist method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
username |  String  |  User name to search  
usersDomain |  String  |  Name of the domain to which the users and groups belong  
  
**Output.** This method returns a Boolean value. If the user exists, it is set to true, and if the user does not exist, it is set to false. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

bFoundFlag = accesscontrol.DoesDomainUserExist(sSessionToken, “username”, “domain”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/DoesDomainUserExist"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<DoesDomainUserExist xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<userName>**string** </userName>

<usersDomain>**string** </usersDomain>

</DoesDomainUserExist>

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

<DoesDomainUserExistResponse xmlns="http://archer-tech.com/webservices/">

<DoesDomainUserExistResult>**boolean** </DoesDomainUserExistResult>

</DoesDomainUserExistResponse>

</soap:Body>

</soap:Envelope>
