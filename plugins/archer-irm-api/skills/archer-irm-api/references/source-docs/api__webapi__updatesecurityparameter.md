# UpdateSecurityParameter

The UpdateSecurityParameter method allows you to modify an existing security parameter.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Update privileges.

**Parameters.**

The parameters for the UpdateSecurityParameter method are described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method  
securityParameterId |  Integer |  Internal ID of the security parameter returned in the xcomp_sec_prm_id element after calling [accesscontrol.GetSecurityParameters](getsecurityparameters.htm)  
name |  String |  Name of the security parameter  
Description  |  String  |  Description of the security parameter  
minPasswordLength  |  Integer |  Minimum number of characters required in the password  
MinPasswordCharacters  |  Integer |  Minimum number of alpha characters required in the password  
minPasswordNumerals  |  Integer |  Minimum number of numeric characters required in the password  
passwordLifetime  |  Integer |  Length of time in days that a password is valid  
graceLogins  |  Integer |  Maximum number of grace logons allowed after a password lifetime has expired  
maxRetries |  Integer |  Maximum number of times a user can unsuccessfully attempt to log on to the system before the account is put into a locked state  
lockDuration |  Integer |  Duration that a user's account remains in a locked state after surpassing the maximum number of retries  
lockIntervalType |  Integer |  Type of lock duration (1=Hours, 2=Minutes, and 3=Days).   
sessionTimeout |  Integer |  Duration of inactivity after which a user's session times out. The unit of measure is set in the timeoutIntervalType method  
passwordHistoryCheckDepth |  Integer |  Number of previous passwords to keep track and restrict reuse  
expiratonNotice |  Integer |  Number of days before a password's expiration that a warning is displayed  
accountTimeout |  Integer |  Number of days after which an account's status automatically is changed to inactive. 0 = none or never automatically deactivates  
timeoutIntervalType |  Integer |  Unit of measure for sessionTimeout (1=Hours, 2=Minutes, and 3=Days).  
pinTimeout |  Integer |  Maximum length of time a PIN remains active before the PIN expires.  
pinTimeoutType |  Integer |  Type of PIN timeout (1=Hours, 2=Minutes, and 3=Days).  
pinMaxResendAttempts |  Integer |  Number of times users can request a PIN before the system prevents them from requesting additional PINs.  
pinResendLockTimeout |  Integer |  Lockout period before users can request a PIN after they exceed their maximum PIN request limit.  
pinResendLockTimeoutType |  Integer |  Type of Resend PIN Lock Timeout (1=Hours, 2=Minutes, and 3=Days).  
  
**Output.** This method returns an integer. If the method was successful, the value is 1. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

iReturnCode = accesscontrol.UpdateSecurityParameter(sSessionToken, iSecParmID, “newname”, “newdescription”, 6, 2, 2, 11, 17, 7, 1, 1, 31, 7, 3, 23, 1);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/UpdateSecurityParameter"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<UpdateSecurityParameter xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

<securityParameterId>**int** </securityParameterId>

<name>**string** </name>

<description>**string** </description>

<minPasswordLength>**int** </minPasswordLength>

<minPasswordCharacters>**int** </minPasswordCharacters>

<minPasswordNumerals>**int** </minPasswordNumerals>

<passwordLifetime>**int** </passwordLifetime>

<graceLogins>**int** </graceLogins>

<maxRetries>**int** </maxRetries>

<lockDuration>**int** </lockDuration>

<lockIntervalType>**int** </lockIntervalType>

<sessionTimeout>**int** </sessionTimeout>

<passwordHistoryCheckDepth>**int** </passwordHistoryCheckDepth>

<expirationNotice>**int** </expirationNotice>

<accountTimeout>**int** </accountTimeout>

<timeoutIntervalType>**int** </timeoutIntervalType>

<pinTimeout>**int** </pinTimeout>

<pinTimeoutType>**int** </pinTimeoutType>

<pinMaxResendAttempts>**int** </pinMaxResendAttempts>

<pinResendLockTimeout>**int** </pinResendLockTimeout>

<pinResendLockTimeoutType>**int** </pinResendLockTimeoutType>

</UpdateSecurityParameter>

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

<UpdateSecurityParameterResponse xmlns="http://archer-tech.com/webservices/">

<UpdateSecurityParameterResult>**int** </UpdateSecurityParameterResult>

</UpdateSecurityParameterResponse>

</soap:Body>

</soap:Envelope>
