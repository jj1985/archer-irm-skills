# GetRolePagePermissionsForModule

The GetRolePagePermissionsForModule method retrieves all of the Read/Write/Delete page permissions for the specified role and application.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetRolePagePermissionsForModule method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
roleId |  Integer |  Internal ID of the role for which to return the dependencies  
moduleId |  Integer |  Internal ID of the application for which to return the role page permissions  
  
**Output**. This method returns an XML string containing all of the access role page permissions in the system for the specified application. The page permissions contains the application ID, application name, page ID, page name, page number, page type, page class, and Create/Read/Update/Delete access role page permissions. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sRole = accessrole.GetRolePagePermissionsForModule(sSessionToken, 1, 17);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accessrole.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetRolePagePermissionsForModule"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetRolePagePermissionsForModule xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<roleId>**int** </roleId>

<moduleId>**int** </moduleId>

</GetRolePagePermissionsForModule>

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

<GetRolePagePermissionsForModuleResponse xmlns="http://archer-tech.com/webservices/">

<GetRolePagePermissionsForModuleResult>**string** </GetRolePagePermissionsForModuleResult>

</GetRolePagePermissionsForModuleResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<PageList>

<Page>

<access_role_id>500</access_role_id>

<module_id>201</module_id>

<module_name>Policies</module_name>

<page_id>2013</page_id>

<page_name>Policies: Content Record</page_name>

<page_num>i2188</page_num>

<page_type_id>2</page_type_id>

<page_type_desc>Action</page_type_desc>

<page_class_id>8</page_class_id>

<page_class_name>View Mode Page</page_class_name>

<is_admin>false</is_admin>

<xpagesaccessroles_create>true</xpagesaccessroles_write>

<xpagesaccessroles_read>true</xpagesaccessroles_read>

<xpagesaccessroles_update>true</xpagesaccessroles_write>

<xpagesaccessroles_delete>true</xpagesaccessroles_delete>

</Page>

</PageList>
