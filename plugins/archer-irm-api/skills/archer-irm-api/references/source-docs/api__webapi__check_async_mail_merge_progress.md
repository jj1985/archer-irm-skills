# CheckAsyncMailMergeProgress

The CheckAsyncMailMergeProgress method returns the percentage in which the specified Mail Merge process is complete.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CheckAsyncMailMergeProgress method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
exportId |  Integer  |  Identifier returned by the [record.StartAsyncMailMerge](start_async_mail_merge.htm) method.  
  
**Output.** This method returns an integer value. This integer value represents a number between 0 and 100 which tells the percentage in which the specified Mail Merge is complete. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

int percentComplete = record.CheckAsyncMailProgress(sSessionToken, exportId);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CheckAsyncMailMergeProgress"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CheckAsyncMailMergeProgress xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<exportId>**int** </exportId>

</CheckAsyncMailMergeProgress>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CheckAsyncMailMergeProgressResponse xmlns="http://archer-tech.com/webservices/">

<CheckAsyncMailMergeProgressResult>**int** </CheckAsyncMailMergeProgressResult>

</CheckAsyncMailMergeProgressResponse>

</soap:Body>

</soap:Envelope>
