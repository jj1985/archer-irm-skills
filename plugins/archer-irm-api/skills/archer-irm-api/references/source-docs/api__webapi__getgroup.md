# GetGroup

The GetGroup method returns the textual name of a groupId in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetGroup method are described in the following table. Parameter  | Data Type | Value  
---|---|---  
sessionToken  |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
groupId |  Integer |  Internal ID of the group as contained in the results of the [accesscontrol.  
LookupGroup](lookupgroup.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value is a text description of the group that appears in the GUI. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sGroupName = accesscontrol.GetGroup(sSessionToken, 123);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetGroup"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetGroup xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<groupId>**int** </groupId>

</GetGroup>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: length  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetGroupResponse xmlns="http://archer-tech.com/webservices/">

<GetGroupResult>**string** </GetGroupResult>

</GetGroupResponse>

</soap:Body>

</soap:Envelope>
