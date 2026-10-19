# GetUserList

The GetUserList method returns a list of all users in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameter.**

The parameter for the GetUserList method is described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value is an XML string that contains the ID, name, role, status, security parameter, and "logged on" indicator for every user in the company. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sUserData = accesscontrol.GetUserList(sSessionToken, 123);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetUserList"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetUserList xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

</GetUserList>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetUserListResponse xmlns="http://archer-tech.com/webservices/">

<GetUserListResult>**string** </GetUserListResult>

</GetUserListResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<Return>

<User>

<row_num>4</row_num>

<ID>11</ID>

<LastName>Jones</LastName>

<FirstName>Renee</FirstName>

<AccountStatus>Active</AccountStatus>

<ParamName>Default Administrative User</ParamName>

<SecurityID>2</SecurityID>

<LoggedIn>false</LoggedIn>

<username>rjones</username>

</User>

<User>

<row_num>8</row_num>

<ID>14</ID>

<LastName>Miller</LastName>

<FirstName>Jake</FirstName>

<AccountStatus>Active</AccountStatus>

<ParamName>General User Parameter</ParamName>

<SecurityID>1</SecurityID>

<LoggedIn>true</LoggedIn>

<username>jmiller</username>

</User>

</Return>
