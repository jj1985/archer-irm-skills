# GetUserListCount

The GetUserListCount method returns the total number of non-deleted users in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameter.**

The parameter for the GetUserListCount method is described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
  
**Output.** This method returns an integer. If the method is successful, the value is the number of non-deleted users in the system. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iUserCount = accesscontrol.GetUserListCount(sSessionToken);

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

<GetUserListCount xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

</GetUserListCount>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetUserListCountResponse xmlns="http://archer-tech.com/webservices/">

<GetUserListCountResult>**int** </GetUserListCountResult>

</GetUserListCountResponse>

</soap:Body>

</soap:Envelope>
