# GetRole

The GetRole method retrieves an access role in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetRole method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method   
roleId |  Integer |  Internal ID of the role to be deleted  
  
**Output.** This method returns a string. The value is an XML string containing the role ID, company ID, role name, role description, required flag, and default flag. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sRole = accessrole.GetRole(sSessionToken, 123);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accessrole.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetRole"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetRole xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<roleId>**int** </roleId>

</GetRole>

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

<GetRoleResponse xmlns="http://archer-tech.com/webservices/">

<GetRoleResult>**string** </GetRoleResult>

</GetRoleResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<Role>

<Id>1</Id>

<CompanyId>10000</CompanyId>

<Name>General User</Name>

<Description>The General User role is the default role that is granted to users of the application. This role will have no right to manage access to the application, and only minimal self administration rights.</Description>

<RequiredFlag>False</RequiredFlag>

<DefaultFlag>True</DefaultFlag>

</Role>
