# GetValuesListItem

The GetValuesListItem method retrieves the properties of the specified valuesListValueId, including the value name, description, numeric value, default setting, and text color.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetValuesListItem method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
valuesListValueId |  Integer |  Internal ID of the specific values list value, as returned by the [field.LookupListValue](lookuplistvalue.htm) method  
  
**Output.** This method returns a string. If the method is successful, the value represents the XML structure of the values list properties. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

sValuesList = field.GetValuesListItem(sSessionToken, 468);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/field.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetValuesListItem"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetValuesListItem xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<valuesListValueId>**int** </valuesListValueId>

</GetValuesListItem>

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

<GetValuesListItemResponse xmlns="http://archer-tech.com/webservices/">

<GetValuesListItemResult>**string** </GetValuesListItemResult>

</GetValuesListItemResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<SelectDefValues>

<SelectDefValue>

<select_id>3599</select_id>

<guid>dba485b3-b0fc-4eaf-b413-493c3e4df594</guid>

<Name>Draft</Name>

<select_value_desc />

<AssociativeFlag>true</AssociativeFlag>

<create_date>2006-03-20T10:03:25.1530000-06:00</create_date>

<create_login>188247</create_login>

<update_date>2006-08-21T15:25:42.1170000-05:00</update_date>

<update_login>188247 </update_login>

<select_value_color />

<DefaultFlag>false</DefaultFlag>

<system>false</system>

<NumericValue>1.000000</NumericValue>

</SelectDefValue>

</SelectDefValues>
