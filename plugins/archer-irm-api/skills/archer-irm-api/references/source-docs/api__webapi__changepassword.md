# ChangePassword

The ChangePassword method sets the user password to the specified value.

**Note:** The provided password must meet the requirements specified in the user security parameter.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the ChangePassword method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
userId |  Integer  |  Internal ID of the user returned by the [accesscontrol.LookupUserId](lookupuserid.htm) method.   
password |  String |  Value that you want to assign as the password.   
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iReturnCode = accesscontrol.ChangePassword(sSessionToken, 123, “newpassword”);

Sample Request and Response

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: length

SOAPAction: http://archer-tech.com/webservices/ChangePassword  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<ChangePassword xmlns="http://archer-tech.com/webservices/">

<sessionToken>string</sessionToken>

<userId>int</userId>

<password>string</password>

</ChangePassword>

</soap:Body>

</soap:Envelope>

Sample Request and Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: length  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<ChangePasswordResponse xmlns="http://archer-tech.com/webservices/">

<ChangePasswordResult>**int** </ChangePasswordResult>

</ChangePasswordResponse>

</soap:Body>

</soap:Envelope>
