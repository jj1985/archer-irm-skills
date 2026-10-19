# CreateGroup

The CreateGroup method adds a group to the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CreateGroup method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken  |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.   
groupName |  String |  Name of the group to add.   
  
**Output.** This method returns an integer. If the method is successful, the value is the ID of the newly created group. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iGroupID = accesscontrol.CreateGroup(sSessionToken, “groupname”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CreateGroup"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateGroup xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<groupName>**string** </groupName>

</CreateGroup>

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

<CreateGroupResponse xmlns="http://archer-tech.com/webservices/">

<CreateGroupResult>**int** </CreateGroupResult>

</CreateGroupResponse>

</soap:Body>

</soap:Envelope>
