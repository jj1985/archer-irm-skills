# GetRoleDependencies

The GetRoleDependencies method retrieves all the dependencies for the specified role. The dependencies are the users and groups that are only assigned to the access role.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetRoleDependencies method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method   
roleId |  Integer |  Internal ID of the role for which to return the dependencies  
  
**Output.** This method returns a string. The value is an XML string containing all of the access role dependencies (users and groups) in the system. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sRoleData = accessrole.GetRoleDependencies(sSessionToken, 123);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accessrole.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetRole  
Dependencies"  
  

<?xml version="1.0" encoding="utf-8"?>  

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetRoleDependencies xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<roleId>**int** </roleId>

</GetRoleDependencies>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetRoleDependenciesResponse xmlns="http://archer-tech.com/webservices/">

<GetRoleDependenciesResult>**string** </GetRoleDependenciesResult>

</GetRoleDependenciesResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<Dependencies>

<Dependency>

<user_id>5</user_id>

<dependency_type>Users</dependency_type>

<dependency>Integration (Integration Integration)</dependency>

</Dependency>

<Dependency>

<user_id>8</user_id>

<dependency_type>Users</dependency_type>

<dependency>rob (Rob Walters)</dependency>

</Dependency>

</Dependencies>
