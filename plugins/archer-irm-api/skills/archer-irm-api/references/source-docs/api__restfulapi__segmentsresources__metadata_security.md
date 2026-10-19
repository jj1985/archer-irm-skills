# Metadata Security

On this page

  * Create a security parameter
    * Security parameter values
  * Delete a security parameter
  * Get all security parameters
  * Get security parameter by ID
  * Update a security parameter

The Security Parameter segment is accessed through the System controller, which includes the following resources:

## Create a security parameter

The Create a security parameter resource creates a security parameter. 

### Security parameter values

The following table shows the valid security parameter values when creating a security parameter. Parameter |  Valid Value  
---|---  
LockoutPeriodType |  1 - (Hours), 2 - (Minutes), 3 - (Days)  
SessionTimeoutType:  |  1 - (Hours), 2 - (Minutes), 3 - (Days)  
DisallowedSessionDaysType:  |  1 - (Sunday), 2 - (Monday), 4 - (Tuesday), 8 - (Wednesday), 16 - (Thursday), 32 - (Friday), 64 - (Saturday)  
  
Request

POST http://Archer/platformapi/core/system/securityparameter

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{"Name":"Test Security Param","Description":"test sec","MinPasswordLength":9,"AlphaCharsRequired":2,"NumericCharsRequired":1,"UppercaseCharsRequired":1,"LowercaseCharsRequired":1,"SpecialCharsRequired":1,"PasswordChangeInterval":90,"PasswordChangeLimit":false,"GraceLogins":3,"MaximumFailedLoginAttempts":3,"PreviousPasswordsDisallowed":10,"LockoutPeriod":999,"LockoutPeriodType":3,"SessionTimeout":10,"SessionTimeoutType":2,"StaticSessionTimeout":null,"PasswordExpirationNotice":30,"AutomaticAccountDeactivation":0,"IsLimitByTimeFrame":false,"PermittedFromTime":"2015-03-05T08:00:00","PermittedToTime":"2015-03-05T10:00:00","IsDisallowedByDays":true,"DisallowedSessionDays":[2,3],"IsDisallowedByDates":true,"DisallowedDates":[{"LockedDate":"2015-04-01T00:00:00"},{"LockedDate":"2015-05-01T00:00:00"}],"Default":false,"TimeZoneCode":"Central Standard Time","SecurityParameterType":2}

## Delete a security parameter

The Delete a security parameter resource deletes a security parameter. 

Request

DELETE http://Archer/platformapi/core/system/securityparameter/*securityparameterid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

## Get all security parameters

The Get all security parameters resource retrieves all security parameters for the current Archer instance. 

Request

POST http://Archer/platformapi/core/system/securityparameter

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

## Get security parameter by ID

The Get security parameter by ID resource retrieves a security parameter by the specified ID.

Request

POST http://Archer/platformapi/core/system/securityparameter/*securityparameterid*

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

X-Http-Method-Override: GET

## Update a security parameter

The Update a security parameter resource updates a security parameter. 

Request

PUT http://Archer/platformapi/core/system/securityparameter

Request Header

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id="*SessionToken"

Content-Type: application/json

Request Body

{“Id”:23,”Alias”:”Test_Sec1”,”GUID”:”4B31AEEB-A85D-4665-B33F-E3CC79021228”,"Name":"Test Security Param","Description":"test sec","MinPasswordLength":9,"AlphaCharsRequired":2,"NumericCharsRequired":1,"UppercaseCharsRequired":1,"LowercaseCharsRequired":1,"SpecialCharsRequired":1,"PasswordChangeInterval":90,"PasswordChangeLimit":false,"GraceLogins":3,"MaximumFailedLoginAttempts":3,"PreviousPasswordsDisallowed":10,"LockoutPeriod":999,"LockoutPeriodType":3,"SessionTimeout":10,"SessionTimeoutType":2,"StaticSessionTimeout":null,"PasswordExpirationNotice":30,"AutomaticAccountDeactivation":0,"IsLimitByTimeFrame":false,"PermittedFromTime":"2015-03-05T08:00:00","PermittedToTime":"2015-03-05T10:00:00","IsDisallowedByDays":true,"DisallowedSessionDays":[2,3],"IsDisallowedByDates":true,"DisallowedDates":[{"LockedDate":"2015-04-01T00:00:00"},{"LockedDate":"2015-05-01T00:00:00"}],"Default":false,"TimeZonCode":"Central Standard Time","SecurityParameterType":2}
