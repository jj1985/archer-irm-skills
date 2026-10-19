# RemoveUserFromGroup

The RemoveUserFromGroup method removes a user from the specified group.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Delete privileges.

**Parameters.**

The parameters for the RemoveUserFromGroup method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
userId |  Integer |  Internal ID of the user returned by the [accesscontrol.LookupUserId](lookupuserid.htm) method  
groupId |  Integer |  Internal ID of the group as contained in the results of the [accesscontrol.  
LookupGroup](lookupgroup.htm) method  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = accesscontrol.RemoveUserFromGroup(sSessionToken, 123, 456);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/RemoveUserFromGroup"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<RemoveUserFromGroup xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<userId>**int** </userId>

<groupId>**int** </groupId>

</RemoveUserFromGroup>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<RemoveUserFromGroupResponse xmlns="http://archer-tech.com/webservices/">

<RemoveUserFromGroupResult>**int** </RemoveUserFromGroupResult>

</RemoveUserFromGroupResponse>

</soap:Body>

</soap:Envelope>
