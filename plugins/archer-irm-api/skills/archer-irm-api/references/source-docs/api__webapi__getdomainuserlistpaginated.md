# GetDomainUserListPaginated

The GetDomainUserListPaginated method returns a listing of all users in the system and allows you to specify the page size and desired page to be returned, thereby reducing the number of users returned per call.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetDomainUserListPaginated method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
pageSize |  Integer  |  Number of users to return on each page.  
page |  Integer  |  Page of the user list that you want to return.  **Note:** Page numbering begins with 1.  
userDomain |  String  |  Name of the domain to which the users and groups belong.  
  
**Output.** This method returns an string. If the method is successful, the value is an XML string that contains the ID, name, role, status, security parameter, and "logged on" indicator for the users on the specified page of results. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sUserPage = accesscontrol.GetDomainUserListPaginated(sSessionToken, 100, 1, “domain”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetDomainUserListPaginated"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetDomainUserListPaginated xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<pageSize>**int** </pageSize>

<page>**int** </page>

<usersDomain>**string** </usersDomain>

</GetDomainUserListPaginated>

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

<GetDomainUserListPaginatedResponse xmlns="http://archer-tech.com/webservices/">

<GetDomainUserListPaginatedResult>**string** </GetDomainUserListPaginatedResult>

</GetDomainUserListPaginatedResponse>

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
