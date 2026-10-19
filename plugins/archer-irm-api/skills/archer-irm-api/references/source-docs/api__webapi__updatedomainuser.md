# UpdateDomainUser

The UpdateDomainUser method allows you to modify the account properties for a user. Use this method to modify the First, middle, and last name, Company name, Title, Security parameter, Address, and Time zone of a user.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateDomainUser method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
userId |  String |  Internal ID of the user as returned by the [accessontrol.LookupUserId](lookupuserid.htm) method.  
firstName |  String  |  User first name.  
middleName |  String  |  User middle name.  
lastName |  String  |  User last name.  
companyName |  String  |  User organization or company.  
title  |  String  |  User job title or function.  
securityParameter |  Integer  |  Internal ID of the corresponding security parameter as contained in the results of the [accesscontrol.GetSecurityParameters](getsecurityparameters.htm) method.  
address  |  String  |  User location mailing address.  
timeZone |  Integer  |  **Important:** This parameter is disabled, but an integer must still be passed in the method. It is recommended to use 0.   
usersDomain |  String  |  Name of the domain to which the users and groups belong.  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = access.UpdateDomainUser(sSessionToken, iUserID, "WebAPI", "zMiddle", "Domain", "zCompany", "zTitle", 2, "zAddress", 7, "archerlab");

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateDomainUser"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateDomainUser xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<userId>**int** </userId>

<firstName>**string** </firstName>

<middleName>**string** </middleName>

<lastName>**string** </lastName>

<companyName>**string** </companyName>

<title>**string** </title>

<securityParameter>**int** </securityParameter>

<address>**string** </address>

<timeZone>**int** </timeZone>

<usersDomain>**string** </usersDomain>

</UpdateDomainUser>

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

<UpdateDomainUserResponse xmlns="http://archer-tech.com/webservices/">

<UpdateDomainUserResult>**int** </UpdateDomainUserResult>

</UpdateDomainUserResponse>

</soap:Body>

</soap:Envelope>
