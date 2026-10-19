# CreateDomainUserSessionFromInstance

The CreateDomainUserSessionFromInstance method creates a session using the specified credentials. 

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the CreateDomainUserSessionFromInstance method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
username |  String |  Name of the instance where the session should be created.  
instanceName |  String  |  Company identification number.  
password |  String  |  User password.  
usersDomain |  String  |  Name of the domain to which the users and groups belong.  
  
**Output.** This method returns a string. If the method is successful, the value is a 32-character alphanumeric sessionToken. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

sSessionToken = general.CreateDomainUserSessionFromInstance(“username, “instance”, “password”, “domain” );

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/general.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CreateDomainUserSessionFromInstance"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateDomainUserSessionFromInstance xmlns="http://archer-tech.com/webservices/">

<userName>**string** </userName>

<instanceName>**string** </instanceName>

<password>**string** </password>

<usersDomain>**string** </usersDomain>

</CreateDomainUserSessionFromInstance>

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

<CreateDomainUserSessionFromInstanceResponse xmlns="http://archer-tech.com/webservices/">

<CreateDomainUserSessionFromInstanceResult>**string** </CreateDomainUserSessionFromInstanceResult>

</CreateDomainUserSessionFromInstanceResponse>

</soap:Body>

</soap:Envelope>
