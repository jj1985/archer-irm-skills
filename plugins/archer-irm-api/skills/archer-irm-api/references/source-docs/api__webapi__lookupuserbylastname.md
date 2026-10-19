# LookupUserByLastName

The LookupUserByLastName method returns a list of users with the specified last name.

**Note:** This query attaches a wildcard to the end of the keyword, for example, "John" returns both Johnson and Johnston.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the LookupUserByLastName method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
keyword |  String |  Name or first part of a name for which you can search  
  
**Output.** This method returns a string. If the method is successful, the value is an XML string that contains the properties of each user whose last name meets the search criteria. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sUserList = accesscontrol.LookupUserByLastName(sSessionToken, “lastname”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/LookupUserByLastName"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<LookupUserByLastName xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<keyword>**string** </keyword>

</LookupUserByLastName>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<LookupUserByLastNameResponse xmlns="http://archer-tech.com/webservices/">

<LookupUserByLastNameResult>**string** </LookupUserByLastNameResult>

</LookupUserByLastNameResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<Return>

<User>

<row_num>1</row_num>

<ID>3</ID>

<LastName>Miller</LastName>

<FirstName>Jake</FirstName>

<AccountStatus>Active</AccountStatus>

<ParamName>General User Parameter</ParamName>

<SecurityID>1</SecurityID>

<LoggedIn>true</LoggedIn>

<username>jmiller</username>

</User>

</Return>
