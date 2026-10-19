# GetModuleIdByGUID

The GetModuleIdByGUID method retrieves the ID for an application (module) in the system.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetModuleIdByGUID method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
instanceId |  String  |  ID of the instance that contains the application that you want to export. You can find this instance ID in the Control Panel.  
GUID |  String  |  GUID of the application for which you want to return an ID.  
  
**Output.** This method returns an integer, which is the assigned ID for the application to which the GUID belongs. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iModuleID = module.GetModuleIdByGUID(sSessionToken, “instance”,   
“7538F922-7794-11E2-BCD8-634F61887098”);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/module.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://tempuri.org/GetModuleIdByGUID"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetModuleIdByGUID xmlns="http://tempuri.org/">

<sessionToken>**string** </sessionToken>

<instanceId>**string** </instanceId>

<GUID>**string** </GUID>

</GetModuleIdByGUID>

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

<GetModuleIdByGUIDResponse xmlns="http://tempuri.org/">

<GetModuleIdByGUIDResult>**int** </GetModuleIdByGUIDResult>

</GetModuleIdByGUIDResponse>

</soap:Body>

</soap:Envelope>
