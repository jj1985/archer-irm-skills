# CreateQuestionnaireRecord

The CreateQuestionnaireRecord method creates a new questionnaire record within the specified questionnaire populating only the target cross-reference field.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CreateQuestionnaireRecord method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
questionnairModuleId |  Integer  |  Internal ID of the questionnaire as specified in the Application Builder Questionnaire Detail Report.  
targetContentId |  Integer  |  Internal ID of the target record within the specified target application as returned by the [search.ExecuteSearch](executesearch.htm) method.  
  
**Output.** This method returns an integer. If the method is successful, the value is the content ID of the newly created questionnaire record. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iContentID = record.CreateQuestionnaireRecord(sSessionToken, 266, 431);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /Archer/ws/record.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CreateQuestionnaireRecord"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateQuestionnaireRecord xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<questionnaireModuleId>**int** </questionnaireModuleId>

<targetContentId>**int** </targetContentId>

</CreateQuestionnaireRecord>

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

<CreateQuestionnaireRecordResponse xmlns="http://archer-tech.com/webservices/">

<CreateQuestionnaireRecordResult>**int** </CreateQuestionnaireRecordResult>

</CreateQuestionnaireRecordResponse>

</soap:Body>

</soap:Envelope>
