# AddUsersToGroup

The AddUsersToGroup method adds a user to a specified group.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The following table describes the parameters for the AddUserToGroup method. Parameter  | Data Type | Value  
---|---|---  
sessionToken  |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
userIds |  Integer  |  Internal IDs of the users returned by the [accesscontrol.LookupGroup](lookupgroup.htm) method.  
groupId |  Integer  |  Internal ID of the group as contained in the results of the [accesscontrol.LookupGroup](lookupgroup.htm) method.  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iReturnCode = accesscontrol.AddUsersToGroup(sSessionToken, iListIDs.ToArray(), 456);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. (SOAP 1.2 also is supported.)

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: length

SOAPAction: "http://archer-tech.com/webservices/AddUserToGroup"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<AddUsersToGroup xmlns="http://archer-tech.com/webservices/">

<sessionToken>string</sessionToken>

<userIds>

<int>int</int>

<int>int</int>

<int>int</int>

</userIds>

<groupId>int</groupId>

</AddUsersToGroup>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: length  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<AddUsersToGroupResponse xmlns="http://archer-tech.com/webservices/">

<AddUsersToGroupResult>int</AddUsersToGroupResult>

</AddUsersToGroupResponse>

</soap:Body>

</soap:Envelope>
