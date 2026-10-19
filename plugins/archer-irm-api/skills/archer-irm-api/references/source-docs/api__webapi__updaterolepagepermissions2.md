# UpdateRolePagePermissions2

The UpdateRolePagePermissions2 method updates the page permissions (Create, Read, Update, and Delete) for the specified role and page.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateRolePagePermissions2 method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
roleId |  Integer |  Internal ID of the role for which to update the page permissions  
pageId |  Integer |  Internal ID of the page for which to update the page permissions  
create |  Boolean |  Create page permission  
read  |  Boolean |  Read page permission  
update |  Boolean |  Update page permission  
delete  |  Boolean |  Delete page permission  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iReturnCode = accessrole.UpdateRolePagePermissions2(sSessionToken, 1, 3496, true, false, true, true);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accessrole.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateRolePage  
Permissions2"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateRolePagePermissions2 xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<roleId>**int** </roleId>

<pageId>**int** </pageId>

<create>**boolean** </create>

<read>**boolean** </read>

<update>**boolean** </update>

<delete>**boolean** </delete>

</UpdateRolePagePermissions2>

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

<UpdateRolePagePermissionsResponse2 xmlns="http://archer-tech.com/webservices/">

<UpdateRolePagePermissions2Result>**int** </UpdateRolePagePermissions2Result>

</UpdateRolePagePermissions2Response>

</soap:Body>

</soap:Envelope>
