# GetUserContactInfo

The GetUserContactInfo method returns contact information for a specified user ID. This contact information includes the user e-mail addresses and phone numbers.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetUserContactInfo method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
userId |  Integer |  Internal ID of the user as returned by the [accesscontrol.LookupUserId](lookupuserid.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value is an XML string that contains contact information for the specified user. If there is a failure, the API issues an exception.

## Samples

Sample C# CAll

sUserData = accesscontrol.GetUserContactInfo(sSessionToken, 123);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetUserContactInfo"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetUserContactInfo xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<userId>**int** </userId>

</GetUserContactInfo>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetUserContactInfoResponse xmlns="http://archer-tech.com/webservices/">

<GetUserContactInfoResult>**string** </GetUserContactInfoResult>

</GetUserContactInfoResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<ContactInfos>

<ContactInfo>

<ContactTypeId>7</ContactTypeId>

<ContactInfo>jmiller@company-name.com</ContactInfo>

<ContactDefault>true</ContactDefault>

<Id>517535</Id>

<ContactSubTypeId>2</ContactSubTypeId>

<ContactSubTypeDesc>Business</ContactSubTypeDesc>

</ContactInfo>

<ContactInfo>

<ContactTypeId>9</ContactTypeId>

<ContactInfo>555-123-4567</ContactInfo>

<ContactDefault>false</ContactDefault>

<Id>713840</Id>

<ContactSubTypeId>2</ContactSubTypeId>

<ContactSubTypeDesc>Business</ContactSubTypeDesc>

</ContactInfo>

</ContactInfos>
