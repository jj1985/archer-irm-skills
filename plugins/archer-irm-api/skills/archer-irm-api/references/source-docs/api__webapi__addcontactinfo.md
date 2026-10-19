# AddContactInfo

The AddContactInfo method adds contact information, such as email addresses and phone numbers to a user account. Before invoking this method, obtain your system contact type and subtype IDs using the following methods: 

  * [accesscontrol.GetContactTypes](getcontacttypes.htm)  

  * [accesscontrol.GetContactSubTypes](getcontactsubtypes.htm)

**Important:** The IDs are required for the contactInfo parameter.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the AddContactInfo method are described in the following table. Parameter |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
userId |  Integer  |  Internal ID of the user returned by the [accesscontrol.LookupGroup](lookupgroup.htm) method.  
contactInfo |  String |  String that provides the following: 

  * The contact type ID for the contact type that you want to add as returned by the [accesscontrol.GetContacttypes](getcontacttypes.htm) method.
  * The contact subtype ID for the contact type that you want to add as returned by the [accesscontrol.GetContactSubTypes](getcontactsubtypes.htm) method.
  * The value to add for the contact type (e-mail address or phone number).
  * A true or false indicator that determines whether the contact value should be the default for the user account. This is only applicable if you are adding an e-mail address.

The following text is a sample string for this parameter. The contact type ID of 7 indicates that the value is an e-mail address. The contact subtype ID of 3 indicates that it is a home e-mail address. The contact default flag of false indicates that the e-mail address is not the default address for the user account.  
<ContactInfo>

<ContactTypeId>7</ContactTypeId><ContactSubTypeId>3</ContactSubTypeId><ContactInfo>jmiller@company-name.com</ContactInfo><ContactDefault>false</ContactDefault>
</ContactInfo>  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = accesscontrol.AddContactInfo(sSessionToken, 123, sXML);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: length

SOAPAction: "http://archer-tech.com/webservices/AddContactInfo"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<AddContactInfo xmlns="http://archer-tech.com/webservices/">

<sessionToken>string</sessionToken>

<userId>int</userId>

<contactInfo>string</contactInfo>

</AddContactInfo>

</soap:Body>

</soap:Envelope>  

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: length  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<AddContactInfoResponse xmlns="http://archer-tech.com/webservices/">

<AddContactInfoResult>int</AddContactInfoResult>

</AddContactInfoResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<ContactInfo>

<ContactTypeId>1</ContactTypeId>

<ContactSubTypeId>9</ContactSubTypeId>

<ContactInfo>913-555-1212</ContactInfo>

</ContactInfo>
