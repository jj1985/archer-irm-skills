# CreateRole

The CreateRole method creates an access role in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CreateRole method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken  |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
roleName |  String |  Role name  
roleDesc  |  String  |  Role descriptio   
defaultFlag  |  Boolean  |  Indicates whether the role is the default role  
requiredFlag  |  Boolean  |  Indicates whether members of the role can view all records in the applications for which they have at least Read access rights   
  
**Output.** This method returns an integer. If the method is successful, the value is the role ID. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

accessrole.CreateRole(sSessionToken, “rolename”, “description”, false, false);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accessrole.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CreateRole"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateRole xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<roleName>**string** </roleName>

<roleDesc>**string** </roleDesc>

<defaultFlag>**boolean** </defaultFlag>

<requiredFlag>**boolean** </requiredFlag>

</CreateRole>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateRoleResponse xmlns="http://archer-tech.com/webservices/">

<CreateRoleResult>**int** </CreateRoleResult>

</CreateRoleResponse>

</soap:Body>

</soap:Envelope>
