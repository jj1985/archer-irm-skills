# PerformMailMerge  
  
The PerformMailMerge method performs a mail merge synchronously and returns an Microsoft Word document.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the PerformMailMerge method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
contentId |  Integer  |  Internal ID of a content record  
mailMergeTemplateId |  Integer |  Internal ID of a Mail Merge Template record  
  
**Output.** This method returns a byte array. If the method is successful, the byte array contains the contents of the Word document. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

byte[] doc = record.PerformMailMerge(sSessionToken, 17, 25);

using (FileStream fs = new FileStream(“C:\\\temp\\\mailmerge.doc”, FileMode.OpenOrCreate))

fs.Write(doc, 0, doc.Length);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/PerformMailMerge"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<PerformMailMerge xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<contentId>**int** </contentId>

<mailMergeTemplateId>**int** </mailMergeTemplateId>

</PerformMailMerge>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<PerformMailMergeResponse xmlns="http://archer-tech.com/webservices/">

<PerformMailMergeResult>**base64Binary** </PerformMailMergeResult>

</PerformMailMergeResponse>

</soap:Body>

</soap:Envelope>
