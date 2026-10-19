# GetRoles

The GetRoles method retrieves all of the access roles in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameter.**

The parameter for the GetRoles method is described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
  
**Output.** This method returns an XML string containing all of the access roles in the system. Each access role contains the role ID, company ID, role name, role description, required flag, and default flag. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

sRoles = accessrole.GetRoles(sSessionToken);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accessrole.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetRoles"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetRoles xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

</GetRoles>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetRolesResponse xmlns="http://archer-tech.com/webservices/">

<GetRolesResult>**string** </GetRolesResult>

</GetRolesResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<List>

<Role>

<Id>1</Id>

<CompanyId>10000</CompanyId>

<Name>General User</Name>

<Description>The General User role is the default role that is granted to users of the application. This role will have no right to manage access to the application, and only minimal self administration rights.</Description>

<RequiredFlag>False</RequiredFlag>

<DefaultFlag>True</DefaultFlag>

</Role>

</List>
