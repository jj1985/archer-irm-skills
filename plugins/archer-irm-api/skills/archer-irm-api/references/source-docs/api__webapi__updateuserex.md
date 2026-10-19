# UpdateUserEx

The UpdateUserEx method replaces the UpdateUser and UpdateDomainUser methods used in version 4.x. This method allows you to modify the account properties for a user. Use this method to modify the First, middle, and last name, Company name, Title, Security parameter, Address, Time zone, and Locale of a user.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateUserEx method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
userId |  Integer |  Internal ID of the user as returned by the [accesscontrol.LookupUserId](lookupuserid.htm) method.  
firstName |  String |  User first name.  
middleName |  String  |  User middle name.  
lastName  |  String  |  User last name.  
companyName |  String  |  User organization or company.  
title |  String  |  User job title or function.  
securityParameter |  Integer |  Internal ID of the corresponding Security Parameter as contained in the results of the [accesscontrol.GetSecurityParameters](getsecurityparameters.htm) method.  
address |  String  |  User location or mailing address.  
userDomain |  String  |  User domain.  **Note:** If this value is NULL or empty, the system replaces the current value with NULL.   
timeZone  |  String  |  User time zone. Use the .NET time zone ID property.  **Note:** If this value is NULL or empty, the system uses the server default of the instance. For more information supported time zones, see [Supported Time Zones](timezones.htm).  
locale |  String  |  User locale. Use the .NET CultureInfo name property, for example, en-US.  **Note:** If this value is NULL or empty, the system deletes the current value and uses the server default of the instance. For more information on supported locales, see [Supported Locales](locales.htm).   
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iReturnCode = access.UpdateUserEx(sSessionToken, iUserID, "WebAPI", "zMiddle", "Automation", "zCompany", "zTitle", 2, "zAddress", "", "Central Standard Time", "en-US");

Sample Request and Response

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateUser"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateUserEx xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<userId>**int** </userId>

<firstName>**string** </firstName>

<middleName>**string** </middleName>

<lastName>**string** </lastName>

<companyName>**string** </companyName>

<title>**string** </title>

<securityParameter>**int** </securityParameter>

<address>**string** </address>

<timeZone>**string** </timeZone>

<locale>**string** </locale>

</UpdateUserEx>

</soap:Body>

</soap:Envelope>

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length  
**

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateUserExResponse xmlns="http://archer-tech.com/webservices/">

<UpdateUserExResult>**int** </UpdateUserExResult>

</UpdateUserExResponse>

</soap:Body>

</soap:Envelope>
