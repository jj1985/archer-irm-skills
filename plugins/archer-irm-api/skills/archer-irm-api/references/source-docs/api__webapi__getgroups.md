# GetGroups

The GetGroups method returns the ID, name, and description of all the groups in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameter.**

The parameter for the GetGroups method is described in the following table. Parameter |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value is an XML string that contains the ID, name, and description of each group. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sGroups = accesscontrol.GetGroups(sSessionToken);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetGroups"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

  * <soap:Body>

    * <GetGroups xmlns="http://archer-tech.com/webservices/">

      * <sessionToken>**string** </sessionToken>

</GetGroups>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

  * <soap:Body>

    * <GetGroupsResponse xmlns="http://archer-tech.com/webservices/">

      * <GetGroupsResult>**string** </GetGroupsResult>

</GetGroupsResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

iViews are only used in Classic Dashboards. See Archer Classic Experiences for more information.

<Groups>

  * <Group>

    * <Id>2</Id>

<Name>Administrators</Name>

<Description>Used to list all individuals that should have administration level rights in various applications to create reports and iViews.</Description>

</Group>

<Group>

    * <Id>1</Id>

<Name>Everyone</Name>

<Description>Everyone.</Description>

</Group>

</Groups>
