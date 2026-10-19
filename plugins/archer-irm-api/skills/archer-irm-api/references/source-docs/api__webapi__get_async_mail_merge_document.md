# GetAsyncMailMergeDocument

The GetAsyncMailMergeDocument method retrieves the asynchronous mail merge MS Word document.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the GetAsyncMailMergeDocument method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
exportId |  Integer  |  Identifier returned by the [record.StartAsyncMailMerge](start_async_mail_merge.htm) method  
  
**Output.** This method returns a byte array. If the Mail Merge process is not complete, it returns null. If the Mail Merge process is complete and no failure occured, the byte array contains the contents of the MS Word document. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

byte[] doc;

do

{

doc = record.GetAsyncMailMergeDocument(sSessionToken, exportId);

} while (doc == null);

using (FileStream fs = new FileStream(“C:\\\temp\\\mailmerge.doc”, FileMode.OpenOrCreate))

fs.Write(doc, 0, doc.Length);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetAsyncMailMergeDocument"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetAsyncMailMergeDocument xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<exportId>**int** </exportId>

</GetAsyncMailMergeDocument>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: application/soap+xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">

<soap12:Body>

<GetAsyncMailMergeDocumentResponse xmlns="http://archer-tech.com/webservices/">

<GetAsyncMailMergeDocumentResult>**base64Binary** </GetAsyncMailMergeDocumentResult>

</GetAsyncMailMergeDocumentResponse>

</soap12:Body>

</soap12:Envelope>
