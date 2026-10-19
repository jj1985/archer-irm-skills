# LookupGroup

The LookupGroup method returns the XML structure of the specified group in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the LookupGroup method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
keyword |  String |  An exact match of the group name as returned by the [accesscontrol.GetGroup](getgroup.htm) method. **Note:** The keyword must be an exact match of the full name, not just a fragment.  
  
**Output.** This method returns a string. If the method is successful, the value is an XML string of the group. If there is a failure, the API issues an exception.

**Note:** If there is not a group with the name provided in the keyword attribute, an empty Groups element is returned.

## Samples

Sample C# Code

sGroupData = accesscontrol.LookupGroup(sSessionToken, “groupname”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/LookupGroup"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<LookupGroup xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<keyword>**string** </keyword>

</LookupGroup>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<LookupGroupResponse xmlns="http://archer-tech.com/webservices/">

<LookupGroupResult>**string** </LookupGroupResult>

</LookupGroupResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<Groups>

<Group>

<Id>1</Id>

<Name>Everyone</Name>

<Description>Everyone</Description>

</Group>

<Groups>
