# GetContactSubTypes

The GetContactSubTypes method returns contact subtype IDs. The contact subtypes are Business, Home, Mobile, Assistant, Fax, and Pager.

The contact subtype IDs returned by this method can be used to add contact information to a user's account through the [accesscontrol.AddContactInfo](addcontactinfo.htm) method.

On this page

  * Usage
  * Sample

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetContactSubTypes method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken  |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.   
contactTypeId |  Integer |  **Note:** This parameter is no longer used. Use a value of “0”.  
  
**Output.** This method returns a string. If the method is successful, it returns a list of all contact subtype IDs and descriptions. If there is a failure, the API issues an exception.

## Sample

Sample C# Call

sContactSubTypes = accesscontrol.GetContactSubTypes(sSessionToken, 1);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: http://archer-tech.com/webservices/GetContactSubTypes  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetContactSubTypes xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<contactTypeId>**int** </contactTypeId>

</GetContactSubTypes>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetContactSubTypesResponse xmlns="http://archer-tech.com/webservices/">

<GetContactSubTypesResult>**string** </GetContactSubTypesResult>

</GetContactSubTypesResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<ContactSubTypes>

<ContactSubType>

<ContactSubTypeId>1</ContactSubTypeId>

<ContactSubTypeDescription>Assistant</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>2</ContactSubTypeId>

<ContactSubTypeDescription>Business</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>3</ContactSubTypeId>

<ContactSubTypeDescription>Business2</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>4</ContactSubTypeId>

<ContactSubTypeDescription>BusinessFax</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>5</ContactSubTypeId>

<ContactSubTypeDescription>Home</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>6</ContactSubTypeId>

<ContactSubTypeDescription>Home2</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>7</ContactSubTypeId>

<ContactSubTypeDescription>HomeFax</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>8</ContactSubTypeId>

<ContactSubTypeDescription>ISDN</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>9</ContactSubTypeId>

<ContactSubTypeDescription>Mobile</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>10</ContactSubTypeId>

<ContactSubTypeDescription>Mobile2</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>11</ContactSubTypeId>

<ContactSubTypeDescription>Other</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>12</ContactSubTypeId>

<ContactSubTypeDescription>Other2</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>13</ContactSubTypeId>

<ContactSubTypeDescription>OtherFax</ContactSubTypeDescription>

</ContactSubType>

<ContactSubType>

<ContactSubTypeId>14</ContactSubTypeId>

<ContactSubTypeDescription>Pager</ContactSubTypeDescription>

</ContactSubType>

</ContactSubTypes>
