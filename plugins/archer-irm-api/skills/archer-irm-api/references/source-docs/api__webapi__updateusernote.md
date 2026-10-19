# UpdateUserNote

The UpdateUserNote method overwrites the text value in a user's Additional Notes field with the provided value.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateUserNote method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
userId |  Integer |  Internal ID of the user as returned by the [accesscontrol.LookupUserId](lookupuserid.htm) method  
note |  String |  Text for the Additional Notes field  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = accesscontrol.UpdateUserNote(sSessionToken, 123, “notetext”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateUserNote"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateUserNote xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<userId>**int** </userId>

<note>**string** </note>

</UpdateUserNote>

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

<UpdateUserNoteResponse xmlns="http://archer-tech.com/webservices/">

<UpdateUserNoteResult>**int** </UpdateUserNoteResult>

</UpdateUserNoteResponse>

</soap:Body>

</soap:Envelope>
