# CreateUserExWithPassword

CreateUserExWithPassword returns a user ID from the system. This method also enables you to set the time zone, locale, and password of the user account.

**Note:** This method generates a user name automatically and associates it with the account. You can modify it with the [accesscontrol.UpdateUserName](updateusername.htm) method.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Create privileges.

**Parameters.**

The parameters for the CreateUserExWithPassword method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken  |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method.  
firstName  |  String |  User first name.   
middleName |  String |  User middle name.  
lastName |  String |  User last name.  
companyName |  String |  User organization/company.  
title |  String |  User job title/function.  
securityParameter |  Integer |  Internal ID of the corresponding security parameter as contained in the results of the [accesscontrol.GetSecurityParameters](getsecurityparameters.htm) method.  
address |  String |  User location/mailing address.  
userDomain |  String |  User domain.  
timeZone |  String |  User time zone. Use the .NET time zone ID property. If this value is NULL or empty, the system uses the server default of the instance. For more information on supported time zones, see [Supported Time Zones](timezones.htm).  
locale |  String |  User locale. Use the .NET CultureInfo name property. For example, en-US. If this value is NULL or empty, the system uses the server default of the instance. For more information on supported locales, see [Supported Locales](locales.htm).   
password |  String |  User password.  
contactInfo |  String |  User contact information, including email address.  
sendNotification |  Boolean |  If true, sends an email notification to the new user with their credentials.  
  
**Important:** All parameters are required.

**Output.** This method returns an integer. If the method is successful, the value is the ID of the newly created user. If there is a failure, the API issues an exception.

## Samples

Sample C# Code

iUserID = accesscontrol.CreateUserExWithPassword(sSessionToken, “firstname”, “middlename”, “lastname”, “company”, “title”, 2, “address”, “domain”, "(UTC-06:00) Central Time (US & Canada)", "en-US"), "password", "MyName@email.com", "true";

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/CreateUserExWithPassword"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateUserExWithPassword xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<firstName>**string** </firstName>

<middleName>**string** </middleName>

<lastName>**string** </lastName>

<companyName>**string** </companyName>

<title>**string** </title>

<securityParameter>**int** </securityParameter>

<address>**string** </address>

<timeZone>**string** </timeZone>

<locale>**string** </locale>

<password>**string** </password>

<contactInfo>**string** </contactInfo>

<sendNotification>**boolean** </sendNotification>

</CreateUserExWithPassword>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<CreateUserExWithPasswordResponse xmlns="http://archer-tech.com/webservices/">

<CreateUserExWithPasswordResult>**int** </CreateUserExWithPasswordResult>

</CreateUserExWithPasswordResponse>

</soap:Body>

</soap:Envelope>
