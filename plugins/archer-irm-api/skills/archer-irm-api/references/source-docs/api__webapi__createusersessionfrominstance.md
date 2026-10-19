# CreateUserSessionFromInstance

The CreateUserSessionFromInstance method creates a session using the specified credentials.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the CreateUserSessionFromInstance method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
userName |  String |  Valid user name to log on with that has permissions to the appropriate API pages  
instanceName |  String  |  Name of the instance in which the session should be created  
password  |  String |  User password  
  
**Note:** The sessionToken parameter is required for all other methods.

**Output.** This method returns a string. If the method is successful, the value is a 32-character alphanumeric sessionToken. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sSessionToken = general.CreateUserSessionFromInstance(“username”, “instance”, “password”);

Sample Request

The following is a sample SOAP1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/general.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CreateUserSession  
From Instance"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateUserSessionFromInstance xmlns="http://archer-tech.com/webservices/">

<userName>**string** </userName>

<instanceName>**string** </instanceName>

<password>**string** </password>

</CreateUserSessionFromInstance>

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

<CreateUserSessionFromInstanceResponse xmlns="http://archer-tech.com/webservices/">

<CreateUserSessionFromInstanceResult>**string** </CreateUserSessionFromInstanceResult>

</CreateUserSessionFromInstanceResponse>

</soap:Body>

</soap:Envelope>
