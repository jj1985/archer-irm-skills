# UpdateRole

The UpdateRole method updates an access role in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateRole method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
roleId |  Integer |  Internal ID of the role to update  
moduleId |  Integer |  Internal ID of the application for which to return the role page permissions  
roleName |  String  |  New role name  
roleDesc |  String |  New role description  
defaultFlag |  Boolean |  Indicates if the role is the default role  
requiredFlag |  Boolean |  Indicates if members of the role can view all records in the applications for which they have at least Read access rights  
  
**Output.** This method returns an integer. If the method was successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iReturnCode = accessrole.UpdateRole(sSessionToken, iRoleID, “newrolename”, “newdescription”, false, true);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accessrole.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateRole"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateRole xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<roleId>**int** </roleId>

<roleName>**string** </roleName>

<roleDesc>**string** </roleDesc>

<defaultFlag>**boolean** </defaultFlag>

<requiredFlag>**boolean** </requiredFlag>

</UpdateRole>

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

<UpdateRoleResponse xmlns="http://archer-tech.com/webservices/">

<UpdateRoleResult>**int** </UpdateRoleResult>

</UpdateRoleResponse>

</soap:Body>

</soap:Envelope>
