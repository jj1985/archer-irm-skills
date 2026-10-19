# GetUserDefaultEMail

The GetUserDefaultEMail method returns the text value in a user's default email address field.

**Note:** The method may return an empty string if no email address is defined.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetUserDefaultEMail method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
userId |  Integer |  Internal ID of the user as returned by the [accesscontrol.LookupUserId](lookupuserid.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value is the contents of the default email address. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sEmailGet = accesscontrol.GetUserDefaultEMail(sSessionToken, 123);

Sample Request 

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetUserDefaultEMail"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetUserDefaultEMail xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<userId>**int** </userId>

</GetUserDefaultEMail>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetUserDefaultEMailResponse xmlns="http://archer-tech.com/webservices/">

<GetUserDefaultEMailResult>**string** </GetUserDefaultEMailResult>

</GetUserDefaultEMailResponse>

</soap:Body>

</soap:Envelope>
