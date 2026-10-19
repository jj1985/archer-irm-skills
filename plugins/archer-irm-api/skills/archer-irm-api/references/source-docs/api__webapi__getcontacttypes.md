# GetContactTypes

The GetContactTypes method returns contact type IDs for the email and phone contact types. These contact type IDs can be used to add contact information to a user account through the [accesscontrol.AddContactInfo](addcontactinfo.htm) method.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameter.**

The parameter for the GetContactTypes method is described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken  |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value is the contact type ID for the email and phone contact types. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sContactTypes = accesscontrol.GetContactTypes(sSessionToken);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetContactTypes"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetContactTypes xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

</GetContactTypes>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetContactTypesResponse xmlns="http://archer-tech.com/webservices/">

<GetContactTypesResult>**string** </GetContactTypesResult>

</GetContactTypesResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<ContactTypes>

<ContactType>

<ContactTypeId>1</ContactTypeId>

<ContactTypeDescription>Work</ContactTypeDescription>

</ContactType>

<ContactType>

<ContactTypeId>2</ContactTypeId>

<ContactTypeDescription>Home</ContactTypeDescription>

</ContactType>

<ContactType>

<ContactTypeId>3</ContactTypeId>

<ContactTypeDescription>Cell</ContactTypeDescription>

</ContactType>

<ContactType>

<ContactTypeId>7</ContactTypeId>

<ContactTypeDescription>E-mail</ContactTypeDescription>

</ContactType>

<ContactType>

<ContactTypeId>9</ContactTypeId>

<ContactTypeDescription>Phone</ContactTypeDescription>

</ContactType>

</ContactTypes>
