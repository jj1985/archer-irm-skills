# GetGroupInformation

The GetGroupInformation method returns group information for a specified group ID.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetGroupInformation method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
groupId |  Integer |  Internal ID of the group as contained in the results of the [accesscontrol.  
LookupGroup](lookupgroup.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value is an XML string that contains the group ID, name, description, parent information, child information, and group membership. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sGroupInfo = accesscontrol.GetGroupInformation(sSessionToken, iGroupID);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetGroupInformation"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetGroupInformation xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<groupId>**int** </groupId>

</GetGroupInformation>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetGroupInformationResponse xmlns="http://archer-tech.com/webservices/">

<GetGroupInformationResult>**string** </GetGroupInformationResult>

</GetGroupInformationResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<Group>

<Id>1</Id>

<Name>Everyone</Name>

<Description>Everyone</Description>

<Parents></Parents>

<Children><Groups /></Children>

</Group>

Sample Results Showing Child Groups, Parent Groups, and Members

<Group>

<Id>5</Id>

<Name>Group A1</Name>

<Description>This is test group A1</Description>

<Parents>

<Group>

<Id>4</Id>

<Name>Group A</Name>

<Description>This is test group A.</Description>

</Group>

</Parents>

<Children>

<Groups>

<Group>

<Id>8</Id>

<Name>Group A11</Name>

<Description>This is a child of Group A1.</Description>

</Group>

</Groups>

</Children>

<Members>

<Groups>

<Group>

<Id>8</Id>

<Name>Group A11</Name>

</Group>

</Groups>

<Users>

<User>

<Id>1037</Id>

<Name>Jones, Renee</Name>

</User>

<User>

<Id>2</Id>

<Name>Tester1, Tester1</Name>

</User>

</Users>

</Members>

</Group>
