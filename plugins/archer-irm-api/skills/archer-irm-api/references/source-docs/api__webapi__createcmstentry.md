# CreateCMSTEntry

The CreateCMSTEntry method assigns a value to a relationship between 2 records.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CreateCMSTEntry method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
contentId |  Integer  |  Internal ID of a record within the source application (that is, the application in which the CAST field was defined), as returned by the [search.ExecuteSearch](executesearch.htm) method.  
fieldId |  Integer  |  Internal ID of the CAST field within the source application (that is, the application in which the CAST field was defined). You can obtain the field ID from the Application Detail Report in Application Builder. Field IDs are also provided in the results of the [record.GetRecordById](getrecordbyid.htm) method.  
parentId |  Integer  |  Internal ID of the content record in the related application (that is, the application that was specified when configuring the CAST field in the source application), as returned by the [search.ExecuteSearch](executesearch.htm) method.  
valueId |  Integer  |  Internal ID of the specific values list value that you want to modify, as returned by the [field.LookupListValue](lookuplistvalue.htm) method.  
comments  |  String  |  Notes regarding the assignment of the above value.  
  
**Note:** The contentId and parentId parameters must have a relationship as defined by the Cross-Application Status Tracking field configuration in the Application Builder.

**Output.** This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = rec.CreateCMSTEntry(sSessionToken, iContentIDinIncidentsApplication, iCASTFieldIDinIncidentsApplication, iContentIDinResponseProceduresApplication, iValuesListValueIDToSet, "Hello World");

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CreateCMSTEntry"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateCMSTEntry xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<contentId>**int** </contentId>

<fieldId>**int** </fieldId>

<parentId>**int** </parentId>

<valueId>**int** </valueId>

<comments>**string** </comments>

</CreateCMSTEntry>

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

<CreateCMSTEntryResponse xmlns="http://archer-tech.com/webservices/">

<CreateCMSTEntryResult>**int** </CreateCMSTEntryResult>

</CreateCMSTEntryResponse>

</soap:Body>

</soap:Envelope>
