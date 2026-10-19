# AddChildToGroup

The AddChildToGroup method creates a hierarchical parent-child relationship between 2 groups.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the AddChildToGroup method are described in the following table. Parameter |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
childGroupId |  Integer |  Internal ID of the child group returned by the [accesscontrol.LookupGroup](lookupgroup.htm) method.  
parentGroupId |  Integer |  Internal ID of the parent group as returned by the [accesscontrol.LookupGroup](lookupgroup.htm) method.  
  
**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = accesscontrol.AddChildToGroup(sSessionToken, 456, 789);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. (SOAP 1.2 also is supported.)

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/AddChildToGroup"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<AddChildToGroup xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<childGroupId>**int** </childGroupId>

<parentGroupId>**int** </parentGroupId>

</AddChildToGroup>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<AddChildToGroupResponse xmlns="http://archer-tech.com/webservices/">

<AddChildToGroupResult>**int** </AddChildToGroupResult>

</AddChildToGroupResponse>

</soap:Body>

</soap:Envelope>
