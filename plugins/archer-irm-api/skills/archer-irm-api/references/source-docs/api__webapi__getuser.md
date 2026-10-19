# GetUser

The GetUser method returns user information for the specified user ID.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetUser method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
userId |  Integer |  Internal ID of the user as returned by the [accesscontrol.LookupUserId](lookupuserid.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value is an XML string that contains account information for the specified user. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

sUserData = accesscontrol.GetUser(sSessionToken, 123);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetUser"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetUser xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<userId>int</userId>

</GetUser>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetUserResponse xmlns="http://archer-tech.com/webservices/">

<GetUserResult>**string** </GetUserResult>

</GetUserResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<user>

<name first="Jake" middle="" last="Miller" />

<company name="" title="Helper" />

<system userName="jmiller" userId="1004" status="1" securityParameter="5" lastLogin="4/27/2005 4:45:00 PM" forcePasswordChange="False" />

<timeZone id="7" dst="true" />

<address />

<notes />

<contactItems>

<item id="1270" type="7" value="jmiller@xyzcompany.com" default="true" />

</contactItems>

<roles hasOverride="True">

<role id="6" name="Demo * Super Administrator" />

</roles>

<groups>

<group id="4" name="QA" />

</groups>

<subscriptions>

<template id="286" name="New Record Updates" />

</subscriptions>

</user>

**Note:** The subscriptions element only appears if there is a value assigned to it. 
