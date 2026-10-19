# GetAttachmentFile

The GetAttachmentFile method returns all details of the specified file ID.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameters.**

The parameters for the GetAttachmentFile method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
SessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
fileId |  Integer  |  Internal ID of the file information to retrieve.  
  
**Output.** This method returns a string. If the file ID is not found, an empty string is returned. If the method is successful, the value is the XML structure of the requested file information. If there is a failure, the API issues an exception.

The XML structure is as follows:

<files><file id=”” name=”” length=””>(base64 encoded document}</file><files>

Where:

  * id is the file ID (expected to be the same value passed into the method)
  * name is the actual name of the file
  * length is the length of the file
  * value of the file node is the base 64 encoded document

## Samples

Sample C# Call

var xmlFile = record.GetAttachmentFile(session, 8);

XDocument fileDocument = XDocument.Parse(xmlFile);

XElement fileElement = fileDocument.Root.Descendants("file").FirstOrDefault();

XAttribute fileNameAttribute = fileElement.Attributes().FirstOrDefault(e => e.Name.LocalName.ToLower() == "name");

string fileName = Path.Combine("C:\\\temp", fileNameAttribute.Value);

byte[] filebytes = Convert.FromBase64String(fileElement.Value);

using (FileStream fs = new FileStream(fileName, FileMode.CreateNew, FileAccess.Write, FileShare.None))

fs.Write(filebytes. 0. filebytes.Length);

Sample Request

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: length

SOAPAction: "<http://archer-tech.com/webservices/GetAttachmentFile>"

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>" xmlns:xsd="<http://www.w3.org/2001/XMLSchema>" 

xmlns:soap="<http://schemas.xmlsoap.org/soap/envelope/>">

<soap:Body>

<GetAttachmentFile xmlns="<http://archer-tech.com/webservices/>">

<sessionToken>string</sessionToken>

<fileId>int</fileId>

</GetAttachmentFile>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: length

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>" xmlns:xsd="<http://www.w3.org/2001/XMLSchema>" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetAttachmentFileResponse xmlns="<http://archer-tech.com/webservices/>">

<GetAttachmentFileResult>string</GetAttachmentFileResult>

</GetAttachmentFileResponse>

</soap:Body>

</soap:Envelope>
