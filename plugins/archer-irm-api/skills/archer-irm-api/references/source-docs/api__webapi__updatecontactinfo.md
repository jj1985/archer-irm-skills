# UpdateContactInfo

The UpdateContactInfo method overwrites existing contact information, such as email addresses and phone numbers, with updated information on a user's account record. Before invoking this method, obtain your system's contact type IDs and contact subtype IDs using the following methods: 

  * [accesscontrol.GetContactTypes](getcontacttypes.htm)
  * [accesscontrol.GetContactSubTypes](getcontactsubtypes.htm)

**Important:** These IDs are required for the ContactInfo parameter.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateContactInfo method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
userId |  Integer |  Internal ID of the user returned by the [accesscontrol.LookupUserId](lookupuserid.htm) method.  
contactInfo |  String |  String that provides the following: 

  * The contact type ID for the contact type that you want to add as returned by the [accesscontrol.GetContactTypes](getcontacttypes.htm) method.
  * The contact subtype ID for the contact type that you want to add as returned by the [accesscontrol.GetContactSubTypes](getcontactsubtypes.htm) method.
  * The value to add for the contact type, either the e-mail address or phone number.
  * A true or false indicator that determines whether the contact value should be the default for the user's account. (This is only applicable if you are adding an email address.)

The following is a sample string for this parameter: <ContactInfo>

<ContactTypeId>7</ContactTypeId> <ContactSubTypeId>3</ContactSubTypeId> <ContactInfo>jmiller@company-name.com</ContactInfo> <ContactDefault>false </ContactDefault> 
</ContactInfo> In this example, the contact type ID of 7 indicates that the value is an email address. The contact subtype ID of 3 indicates that it is a home email address. The contact default flag of false indicates that the e-mail address is not the default address for the user account.   
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = access.UpdateContactInfo(sSessionToken, iUserID, sXML);

**Note:**

sXML = "<ContactInfo> <Id>" + sContactID + "</Id><ContactTypeId>7</ContactTypeId> <ContactSubTypeId>2</ContactSubTypeId> <ContactInfo>no-reply9@archerirm.com</ContactInfo> </ContactInfo>";

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateContactInfo"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateContactInfo xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<userId>**int** </userId>

<contactInfo>**string** </contactInfo>

</UpdateContactInfo>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length  
**

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateContactInfoResponse xmlns="http://archer-tech.com/webservices/">

<UpdateContactInfoResult>**int** </UpdateContactInfoResult>

</UpdateContactInfoResponse>

</soap:Body>

</soap:Envelope>
