# GetRolePagePermissions

The GetRolePagePermissions method retrieves all the page permissions (Create, Read, Write, and Delete) for the specified role.

**Note:** Write permissions in the output for this method correspond with Update permissions in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetRolePagePermissions method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method   
roleId |  Integer |  Internal ID of the role for which to return the dependencies  
  
**Output**. This method returns an XML string containing all of the access role page permissions in the system. The page permissions contain the application ID, application name, page ID, page name, page number, page type, page class, and Create/Read/Write/Delete access role page permissions. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sRole = accessrole.GetRolePagePermissions(sSessionToken, 1);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accessrole.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetRolePagePermissions"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetRolePagePermissions xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<roleId>**int** </roleId>

</GetRolePagePermissions>

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

<GetRolePagePermissionsResponse xmlns="http://archer-tech.com/webservices/">

<GetRolePagePermissionsResult>**string** </GetRolePagePermissionsResult>

</GetRolePagePermissionsResponse>

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

<xpagesaccessroles_create>true</xpagesaccessroles_create>

<xpagesaccessroles_read>true</xpagesaccessroles_read>

<xpagesaccessroles_write>true</xpagesaccessroles_write>

<xpagesaccessroles_delete>false</xpagesaccessroles_delete>

</Page>

</PageList>
