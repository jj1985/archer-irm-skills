# CreateRecord

The CreateRecord method creates a record using the specified values.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CreateRecord method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
moduleId |  Integer  |  Internal ID of an application as specified in the Application Builder Application Detail Report.  
fieldValues |  String  |  XML structure of the fields and values to add.  **Note:** For details about constructing this string, see [XML Formatting Guidelines for Field Input](xml_formatting_guidelines_for_field_input.htm).  
  
**Output.** This method returns an integer. If the method is successful, the value is the content ID of the newly created record. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iContentID = record.CreateRecord(sSessionToken, 17, sXML);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CreateRecord"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateRecord xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<moduleId>**int** </moduleId>

<fieldValues>**string** </fieldValues>

</CreateRecord>

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

<CreateRecordResponse xmlns="http://archer-tech.com/webservices/">

<CreateRecordResult>**int** </CreateRecordResult>

</CreateRecordResponse>

</soap:Body>

</soap:Envelope>

Sample XML Output

<?xml version="1.0" encoding="utf-8" ?>

<Record>

<Field id="9402" value="ABCDEFG 信息報이ÜФ LMNOP áòëæñü ÃÄÇËÑßÜ" />

<Field id="9405" value="áòëZZZæñü" />

<Field id="9403" value="Some in a text area" />

<Field id="9404" value="Other text in a rich text area" />

<Field id="9406" value="87654321" />

<Field id="9407" value="123.21" />

<Field id="9409" value="888" />

<Field id="9410" value="-88" />

<Field id="9408" value="4" />

<Field id="9411" value="12/21/2012" />

<Field id="9412" value="12/31/1999 1:59PM" />

<Field id="9416" value="523" />

<Field id="9418" value="1254" />

<Field id="9413" value="Search Engine" link="http://www.google.com" />

<Field id="9414" value="EMail" link="mailto:MyName@archerirm.com" />

<Field id="9415" value="191.167.0.255" />

<Field id="9429" value="0054:0230:0253:0511:0747:0066:0034:0023" />

<Field id="9430" value="64:0:594:0:677:46::" />

<Field id="9423" rowId="1253" columnId="730">

<MultiValue rowId="1254" columnId="728" />

<MultiValue rowId="1255" columnId="729" />

<MultiValue rowId="1256" columnId="730" />

</Field>

</Record>
