# GetSecurityParameters

The GetSecurityParameters method returns a list of all of the security parameters and their corresponding IDs.

On this page

  * Usage
  * Samples

## Usage

**Privileges.** This method requires Read privileges.

**Parameter.**

The parameter for the GetSecurityParameters method is described in the following table. Parameter  |  Data Type |  Value  
---|---|---  
sessionToken |  String |  Valid sessionToken returned by the [general.CreateUserSession](createusersession.htm) method   
  
**Output.** This method returns a string. If the method is successful, the value is an XML string of all of the security parameters in the system. If there is a failure, the API issues an exception.

## Samples

Sample C# Call

sSecurity = accesscontrol.GetSecurityParameters(sSessionToken);

Sample Request

The following is a sample SOAP 1.1 request and response. The placeholders shown would be replaced with actual values. SOAP 1.2 also is supported.

POST /archer/ws/accesscontrol.asmx HTTP/1.1

Host: staging

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

SOAPAction: "http://archer-tech.com/webservices/GetSecurityParameters"  
  

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetSecurityParameters xmlns="http://archer-tech.com/webservices/">

<sessionToken>**string** </sessionToken>

</GetSecurityParameters>

</soap:Body>

</soap:Envelope>

Sample Response

HTTP/1.1 200 OK

Content-Type: text/xml; charset=utf-8

Content-Length: **length**

<?xml version="1.0" encoding="utf-8"?>

<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

<soap:Body>

<GetSecurityParametersResponse xmlns="http://archer-tech.com/webservices/">

<GetSecurityParametersResult>**string** </GetSecurityParametersResult>

</GetSecurityParametersResponse>

</soap:Body>

</soap:Envelope>

Sample String in the Response

<SecurityParameters>

<SecurityParameter>

<xcomp_sec_prm_id>2</xcomp_sec_prm_id>

<xcomp_sec_prm_name>Default Administrative User</xcomp_sec_prm_name>

<xcomp_sec_prm_desc>Default Administrative User Security Parameter</xcomp_sec_prm_desc>

<xcomp_sec_prm_min_pwd_length>8</xcomp_sec_prm_min_pwd_length>

<xcomp_sec_prm_pwd_alpha>4</xcomp_sec_prm_pwd_alpha>

<xcomp_sec_prm_pwd_numeric>3</xcomp_sec_prm_pwd_numeric>

<xcomp_sec_prm_pwd_change_days>90</xcomp_sec_prm_pwd_change_days>

<xcomp_sec_prm_grace_logins>5</xcomp_sec_prm_grace_logins>

<xcomp_sec_prm_max_attempts>3</xcomp_sec_prm_max_attempts>

<xcomp_sec_prm_lock_time>10</xcomp_sec_prm_lock_time>

<lock_time_interval_id>2</lock_time_interval_id>

<xcomp_sec_prm_timeout>60</xcomp_sec_prm_timeout>

<timout_time_interval_id>2</timout_time_interval_id>

<default_parameter>false</default_parameter>

<expiration_notice>0</expiration_notice>

<account_timeout>0</account_timeout>

<lock_timeframe>false</lock_timeframe>

<unlocked_from>1900-01-01T07:00:00.0000000-06:00</unlocked_from>

<unlocked_to>1900-01-01T19:00:00.0000000-06:00</unlocked_to>

<lock_days>false</lock_days>

<locked_day_flags>0</locked_day_flags>

<lock_dates>false</lock_dates>

</SecurityParameter>

</SecurityParameters>
