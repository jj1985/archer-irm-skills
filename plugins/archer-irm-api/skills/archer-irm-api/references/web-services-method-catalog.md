# Archer Web Services API (SOAP) - Method Catalog

Source: Archer API Help 2026.08 (help.archerirm.cloud/api_202608/content/api/webapi/). Generated from the per-method pages.

Endpoint pattern: `POST https://<host>/<instance>/ws/<class>.asmx` with header `SOAPAction: "http://archer-tech.com/webservices/<Method>"` (Module class uses namespace `http://tempuri.org/`). SOAP 1.1 and 1.2 are supported. Body element `<Method xmlns="http://archer-tech.com/webservices/">` with child elements named exactly as the parameters below, in order. The response is `<MethodResponse><MethodResult>...</MethodResult></MethodResponse>`; string results that are XML documents come back XML-escaped inside the result element and must be unescaped/parsed.

Privilege rule of thumb (from API Access Configuration page): Create* needs Create; Check/Does/Get/Lookup/Retrieve/Search need Read; Add/Associate/Bind/Change/Disassociate/Force/Set/Unbind/Update need Update; Delete/Remove/Terminate need Delete. Permissions are the same ones the user has in the Archer UI.

Status legend: **ok** = current; **deprecated** = still works, has a replacement; **disabled** = removed, call fails.

## Table of contents

- [Access Control (accesscontrol.asmx)](#accesscontrol)
- [Access Role (accessrole.asmx)](#accessrole)
- [Field (field.asmx)](#field)
- [General (general.asmx)](#general)
- [Module (module.asmx)](#module)
- [Record (record.asmx)](#record)
- [Search (search.asmx)](#search)
- [Technology (technology.asmx) - ALL DISABLED](#technology)

## Access Control (accesscontrol.asmx)
<a id="accesscontrol"></a>

### accesscontrol.AddChildToGroup  (ok)
The AddChildToGroup method creates a hierarchical parent-child relationship between 2 groups.
- Privileges: This method requires Update privileges.
- Signature: `AddChildToGroup(sessionToken: String, childGroupId: Integer, parentGroupId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `childGroupId` (Integer): Internal ID of the child group returned by the accesscontrol.LookupGroup method.
  - `parentGroupId` (Integer): Internal ID of the parent group as returned by the accesscontrol.LookupGroup method.
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.AddContactInfo  (ok)
The AddContactInfo method adds contact information, such as email addresses and phone numbers to a user account. Before invoking this method, obtain your system contact type and subtype IDs using the following methods: accesscontrol.GetContactTypes accesscontrol.GetContactSubTypes
- Privileges: This method requires Update privileges.
- Signature: `AddContactInfo(sessionToken: String, userId: Integer, contactInfo: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `userId` (Integer): Internal ID of the user returned by the accesscontrol.LookupGroup method.
  - `contactInfo` (String): String that provides the following: The contact type ID for the contact type that you want to add as returned by the accesscontrol.GetContacttypes method. The contact subtype ID for the contact type that you want to add as returned by the accesscontrol.GetContactSubTypes method. The value to add for the contact type (e-mail address or phone number). A true or false indicator that determines whether the contact value should be the default for the user account. This is only applicable if you are adding an e-mail address. The following text is a sample string for this parameter. The contact type ID of 7 indicates that the value is an e-mail address. The contact subtype ID of 3 indicates that it is a home e-mail address. The contact default flag of false indicates that the e-mail address is not the default address for the user account. <ContactInfo> <ContactTypeId>7</ContactTypeId> <ContactSubTypeId>3</ContactSubTypeId> <ContactInfo>jmiller@company-name.com</ContactInfo> <ContactDefault>false</ContactDefault> </ContactInfo>
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.AddUserToGroup  (ok)
The AddUserToGroup method adds a user to a specified group.
- Privileges: This method requires Update privileges.
- Signature: `AddUserToGroup(sessionToken: String, userId: Integer, groupId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `userId` (Integer): Internal ID of the user being added to the group.
  - `groupId` (Integer): Internal ID of the group as contained in the results of the accesscontrol.LookupGroup method.
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.AddUserToRole  (ok)
The AddUserToRole method adds a user to a specific access role.
- Privileges: This method requires Update privileges.
- Signature: `AddUserToRole(sessionToken: String, userId: Integer, roleId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `userId` (Integer): Internal ID of the user returned by the accesscontrol.LookupGroup method.
  - `roleId` (Integer): Internal ID of the access role to which you want to add the user as contained in the results of the accessrole.GetRoles method.
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.AddUsersToGroup  (ok)
The AddUsersToGroup method adds a user to a specified group.
- Privileges: This method requires Update privileges.
- Signature: `AddUsersToGroup(sessionToken: String, userIds: Integer, groupId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `userIds` (Integer): Internal IDs of the users returned by the accesscontrol.LookupGroup method.
  - `groupId` (Integer): Internal ID of the group as contained in the results of the accesscontrol.LookupGroup method.
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.ChangePassword  (ok)
The ChangePassword method sets the user password to the specified value.
- Privileges: This method requires Update privileges.
- Signature: `ChangePassword(sessionToken: String, userId: Integer, password: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `userId` (Integer): Internal ID of the user returned by the accesscontrol.LookupUserId method.
  - `password` (String): Value that you want to assign as the password.
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.CreateExtendedSecurityParameter  (ok)
The CreateExtendedSecurityParameter method allows you to create a new security parameter in the system. This method differs from the CreateSecurityParameter method in that it includes the following parameters: Uppercase Characters Required Lowercase Characters Required Special Characters Required
- Privileges: This method requires Create privileges.
- Signature: `CreateExtendedSecurityParameter(sessionToken: String, name: String, description: String, minPasswordLength: Integer, minPasswordCharacters: Integer, passwordLifetime: Integer, graceLogins: Integer, maxRetries: Integer, lockDuration: Integer, lockIntervalType: Integer, sessionTimeout: Integer, passwordHistoryCheckDepth: Integer, expirationNotice: Integer, accountTimeout: Integer, timeoutIntervalType: Integer, minUppercaseCharacters: Integer, minLowercaseCharacters: Integer, minSpecialCharacters: Integer, pinTimeout: Integer, pinTimeoutType: Integer, pinMaxResendAttempts: Integer, pinResendLockTimeout: Integer, pinResendLockTimeoutType: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `name` (String): Name of the security parameter.
  - `description` (String): Description of the security parameter.
  - `minPasswordLength` (Integer): Minimum number of characters required for user passwords.
  - `minPasswordCharacters` (Integer): Minimum number of alpha characters required for user passwords.
  - `passwordLifetime` (Integer): Number of days before a user is required to change his or her password.
  - `graceLogins` (Integer): Maximum number of grace logons allowed after a password has expired.
  - `maxRetries` (Integer): Maximum number of times a user can unsuccessfully attempt to log on to the system before the account is put into a locked state.
  - `lockDuration` (Integer): Duration that a user account remains in a locked state after surpassing the maximum number of logon attempts. The unit of measure is set in the lockIntervalType parameter.
  - `lockIntervalType` (Integer): Type of lock duration (1=Hours, 2=Minutes, and 3=Days).
  - `sessionTimeout` (Integer): Idle time-out period for a user session. The unit of measure is set in the timeoutIntervalType parameter.
  - `passwordHistoryCheckDepth` (Integer): Number of previous passwords to track. Users are not permitted to reuse these tracked passwords.
  - `expirationNotice` (Integer): Number of days before a password's expiration that a warning is displayed.
  - `accountTimeout` (Integer): Number of days after which an account's status automatically is changed to inactive if the user has not logged on (0 = none or never automatically deactivates).
  - `timeoutIntervalType` (Integer): Unit of measure for sessionTimeout (1=Hours, 2=Minutes, and 3=Days).
  - `minUppercaseCharacters` (Integer): Number of uppercase characters that must be contained in a user password.
  - `minLowercaseCharacters` (Integer): Number of lowercase characters that must be contained in a user password.
  - `minSpecialCharacters` (Integer): Number of special characters that must be contained in a user's password. Special characters can include: ` ~ ! @ # $ % ^ & * ( ) _ + - = { } | : " < > ? [ ] \ ; ’ , . /
  - `pinTimeout` (Integer): Maximum length of time a PIN remains active before the PIN expires.
  - `pinTimeoutType` (Integer): Type of PIN timeout (1=Hours, 2=Minutes, and 3=Days).
  - `pinMaxResendAttempts` (Integer): Number of times users can request a PIN before the system prevents them from requesting additional PINs.
  - `pinResendLockTimeout` (Integer): Lockout period before users can request a PIN after they exceed their maximum PIN request limit.
  - `pinResendLockTimeoutType` (Integer): Type of Resend PIN Lock Timeout (1=Hours, 2=Minutes, and 3=Days).
- Output: This method returns an integer. If the method is successful, the value is the ID of the newly created security parameter. If there is a failure, the API issues an exception.

### accesscontrol.CreateGroup  (ok)
The CreateGroup method adds a group to the system.
- Privileges: This method requires Create privileges.
- Signature: `CreateGroup(sessionToken: String, groupName: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `groupName` (String): Name of the group to add.
- Output: This method returns an integer. If the method is successful, the value is the ID of the newly created group. If there is a failure, the API issues an exception.

### accesscontrol.CreateSecurityParameter  (ok)
The CreateSecurityParameter method allows you to create a new security parameter.
- Privileges: This method requires Create privileges.
- Signature: `CreateSecurityParameter(sessionToken: String, name: String, description: String, minPasswordLength: Integer, minPasswordCharacters: Integer, minPasswordNumerals: Integer, passwordLifetime: Integer, graceLogins: Integer, maxRetries: Integer, lockDuration: Integer, lockIntervalType: Integer, sessionTimeout: Integer, passwordHistoryCheckDepth: Integer, expirationNotice: Integer, accountTimeout: Integer, timeoutIntervalType: Integer, pinTimeout: Integer, pinTimeoutType: Integer, pinMaxResendAttempts: Integer, pinResendLockTimeout: Integer, pinResendLockTimeoutType: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `name` (String): Name of the security parameter.
  - `description` (String): Description of the security parameter.
  - `minPasswordLength` (Integer): Minimum number of characters required for user passwords.
  - `minPasswordCharacters` (Integer): Minimum number of alpha characters required for user passwords.
  - `minPasswordNumerals` (Integer): Minimum number of numeric characters required for user passwords.
  - `passwordLifetime` (Integer): Number of days before a user is required to change his or her password.
  - `graceLogins` (Integer): Maximum number of grace logons allowed after a password has expired.
  - `maxRetries` (Integer): Maximum number of times a user can unsuccessfully attempt to log on to the system before the account is put into a locked state.
  - `lockDuration` (Integer): Duration that a user account remains in a locked state after surpassing the maximum number of logon attempts. The unit of measure is set in the lockIntervalType parameter.
  - `lockIntervalType` (Integer): Type of lock duration (1=Hours, 2=Minutes, and 3=Days).
  - `sessionTimeout` (Integer): Idle time-out period for a user session. The unit of measure is set in the timeoutIntervalType parameter.
  - `passwordHistoryCheckDepth` (Integer): Number of previous passwords to track. Users are not permitted to reuse these tracked passwords.
  - `expirationNotice` (Integer): Number of days before a password's expiration that a warning is displayed.
  - `accountTimeout` (Integer): Number of days after which an account status automatically is changed to inactive if the user has not logged on (0 = none or never automatically deactivates).
  - `timeoutIntervalType` (Integer): Unit of measure for sessionTimeout (1=Hours, 2=Minutes, and 3=Days).
  - `pinTimeout` (Integer): Maximum length of time a PIN remains active before the PIN expires.
  - `pinTimeoutType` (Integer): Type of PIN timeout (1=Hours, 2=Minutes, and 3=Days).
  - `pinMaxResendAttempts` (Integer): Number of times users can request a PIN before the system prevents them from requesting additional PINs.
  - `pinResendLockTimeout` (Integer): Lockout period before users can request a PIN after they exceed their maximum PIN request limit.
  - `pinResendLockTimeoutType` (Integer): Type of Resend PIN Lock Timeout (1=Hours, 2=Minutes, and 3=Days).
- Output: This method returns an integer. If the method is successful, the value is the ID of the newly created security parameter. If there is a failure, the API issues an exception.

### accesscontrol.CreateUserEx  (ok)
The CreateUserEx method replaces the CreateUser and CreateDomainUser methods used in version 4.x. CreateUserEx returns a user ID from the system. This method also enables you to set the time zone and locale of the user account.
- Privileges: This method requires Create privileges.
- Signature: `CreateUserEx(sessionToken: String, firstName: String, middleName: String, lastName: String, companyName: String, title: String, securityParameter: Integer, address: String, userDomain: String, timeZone: String, Locale: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `firstName` (String): User first name
  - `middleName` (String): User middle name
  - `lastName` (String): User last name
  - `companyName` (String): User organization/company
  - `title` (String): User job title/function
  - `securityParameter` (Integer): Internal ID of the corresponding security parameter as contained in the results of the accesscontrol.GetSecurityParameters method
  - `address` (String): User location/mailing address
  - `userDomain` (String): User domain
  - `timeZone` (String): User time zone. Use the .NET time zone ID property. If this value is NULL or empty, the system uses the server default of the instance. For more information on supported time zones, see Supported Time Zones .
  - `Locale` (String): User locale. Use the .NET CultureInfo name property. For example, en-US. If this value is NULL or empty, the system uses the server default of the instance. For more information on supported locales, see Supported Locales .
- Output: This method returns an integer. If the method is successful, the value is the ID of the newly created user. If there is a failure, the API issues an exception.

### accesscontrol.CreateUserExWithPassword  (ok)
CreateUserExWithPassword returns a user ID from the system. This method also enables you to set the time zone, locale, and password of the user account.
- Privileges: This method requires Create privileges.
- Signature: `CreateUserExWithPassword(sessionToken: String, firstName: String, middleName: String, lastName: String, companyName: String, title: String, securityParameter: Integer, address: String, userDomain: String, timeZone: String, locale: String, password: String, contactInfo: String, sendNotification: Boolean)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `firstName` (String): User first name.
  - `middleName` (String): User middle name.
  - `lastName` (String): User last name.
  - `companyName` (String): User organization/company.
  - `title` (String): User job title/function.
  - `securityParameter` (Integer): Internal ID of the corresponding security parameter as contained in the results of the accesscontrol.GetSecurityParameters method.
  - `address` (String): User location/mailing address.
  - `userDomain` (String): User domain.
  - `timeZone` (String): User time zone. Use the .NET time zone ID property. If this value is NULL or empty, the system uses the server default of the instance. For more information on supported time zones, see Supported Time Zones .
  - `locale` (String): User locale. Use the .NET CultureInfo name property. For example, en-US. If this value is NULL or empty, the system uses the server default of the instance. For more information on supported locales, see Supported Locales .
  - `password` (String): User password.
  - `contactInfo` (String): User contact information, including email address.
  - `sendNotification` (Boolean): If true, sends an email notification to the new user with their credentials.
- Output: This method returns an integer. If the method is successful, the value is the ID of the newly created user. If there is a failure, the API issues an exception.

### accesscontrol.DeleteContactInfo  (ok)
The DeleteContactInfo method removes a specific aspect of user contact information within the system.
- Privileges: This method requires Delete privileges.
- Signature: `DeleteContactInfo(sessionToken: String, userID: String, contactRecordID: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userID` (String): Internal ID of the user as returned by the accesscontrol.LookupGroup method
  - `contactRecordID` (String): Internal ID of the contact information field as contained in the results of the accesscontrol.GetUserContactInfo method
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.DeleteGroup  (ok)
The DeleteGroup method removes the specified group from the system.
- Privileges: This method requires Delete privileges.
- Signature: `DeleteGroup(sessionToken: String, groupID: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `groupID` (Integer): Internal ID of the group as contained in the results of the accesscontrol.LookupGroup method
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.DeleteSecurityParameter  (ok)
The DeleteSecurityParameter method removes a security parameter from the system.
- Privileges: This method requires Delete privileges.
- Signature: `DeleteSecurityParameter(sessionToken: String, securityParameterId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `securityParameterId` (Integer): Internal ID of the security parameter as contained in the results of the accesscontrol.GetSecurityParameters method
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.DeleteUser  (ok)
The DeleteUser method removes a user from the system.
- Privileges: This method requires Delete privileges.
- Signature: `DeleteUser(sessionToken: String, userId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user as returned by the accesscontrol.LookupUserId method
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.DoesDomainUserExist  (ok)
The DoesDomainUserExist method returns a Boolean indicating whether the specified user exists.
- Signature: `DoesDomainUserExist(sessionToken: String, username: String, usersDomain: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `username` (String): User name to search
  - `usersDomain` (String): Name of the domain to which the users and groups belong
- Output: This method returns a Boolean value. If the user exists, it is set to true, and if the user does not exist, it is set to false. If there is a failure, the API issues an exception.

### accesscontrol.DoesUserExist  (ok)
The DoesUserExist method returns a Boolean value indicating whether the specified user exists.
- Privileges: This method requires Read privileges.
- Signature: `DoesUserExist(sessionToken: String, userName: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userName` (Integer): User name to search
- Output: This method returns a Boolean value. If the user exists, it is set to true, and if the user does not exist, it is set to false. If there is a failure, the API issues an exception.

### accesscontrol.ForcePasswordChange  (ok)
The ForcePasswordChange method sets the status of the Force Password Change property for a specified user.
- Privileges: This method requires Update privileges.
- Signature: `ForcePasswordChange(sessionToken: String, userID: Integer, forcePasswordchange: Boolean)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userID` (Integer): Internal ID of the user as returned by the accesscontrol.LookupUserId method
  - `forcePasswordchange` (Boolean): Setting of the Force Password Change property
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.GetContactSubTypes  (ok)
The GetContactSubTypes method returns contact subtype IDs. The contact subtypes are Business, Home, Mobile, Assistant, Fax, and Pager.
- Privileges: This method requires Read privileges.
- Signature: `GetContactSubTypes(sessionToken: String, contactTypeId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `contactTypeId` (Integer): Note: This parameter is no longer used. Use a value of “0”.
- Output: This method returns a string. If the method is successful, it returns a list of all contact subtype IDs and descriptions. If there is a failure, the API issues an exception.

### accesscontrol.GetContactTypes  (ok)
The GetContactTypes method returns contact type IDs for the email and phone contact types. These contact type IDs can be used to add contact information to a user account through the accesscontrol.AddContactInfo method.
- Privileges: This method requires Read privileges.
- Signature: `GetContactTypes(sessionToken: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
- Output: This method returns a string. If the method is successful, the value is the contact type ID for the email and phone contact types. If there is a failure, the API issues an exception.

### accesscontrol.GetDomainUserList  (ok)
The GetDomainUserList method returns a listing of all users in the system.
- Privileges: This method requires Read privileges.
- Signature: `GetDomainUserList(sessionToken: String, usersDomain: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `usersDomain` (String): Name of the domain to which the users and groups belong
- Output: This method returns a string. If the method is successful, the value is an XML string that contains the ID, name, role, status, security parameter, and "logged on" indicator for every user in the company. If there is a failure, the API issues an exception.

### accesscontrol.GetDomainUserListCount  (ok)
The GetDomainUserListCount method returns the total number of non-deleted users in the system.
- Privileges: This method requires Read privileges.
- Signature: `GetDomainUserListCount(sessionToken: String, usersDomain: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `usersDomain` (String): Name of the domain to which the users and groups belong
- Output: This method returns an integer. If the method is successful, the value is the number of non-deleted users in the system. If there is a failure, the API issues an exception.

### accesscontrol.GetDomainUserListPaginated  (ok)
The GetDomainUserListPaginated method returns a listing of all users in the system and allows you to specify the page size and desired page to be returned, thereby reducing the number of users returned per call.
- Privileges: This method requires Read privileges.
- Signature: `GetDomainUserListPaginated(sessionToken: String, pageSize: Integer, page: Integer, userDomain: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `pageSize` (Integer): Number of users to return on each page.
  - `page` (Integer): Page of the user list that you want to return. Note: Page numbering begins with 1.
  - `userDomain` (String): Name of the domain to which the users and groups belong.
- Output: This method returns an string. If the method is successful, the value is an XML string that contains the ID, name, role, status, security parameter, and "logged on" indicator for the users on the specified page of results. If there is a failure, the API issues an exception.

### accesscontrol.GetGroup  (ok)
The GetGroup method returns the textual name of a groupId in the system.
- Privileges: This method requires Read privileges.
- Signature: `GetGroup(sessionToken: String, groupId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `groupId` (Integer): Internal ID of the group as contained in the results of the accesscontrol. LookupGroup method
- Output: This method returns a string. If the method is successful, the value is a text description of the group that appears in the GUI. If there is a failure, the API issues an exception.

### accesscontrol.GetGroupInformation  (ok)
The GetGroupInformation method returns group information for a specified group ID.
- Privileges: This method requires Read privileges.
- Signature: `GetGroupInformation(sessionToken: String, groupId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `groupId` (Integer): Internal ID of the group as contained in the results of the accesscontrol. LookupGroup method
- Output: This method returns a string. If the method is successful, the value is an XML string that contains the group ID, name, description, parent information, child information, and group membership. If there is a failure, the API issues an exception.

### accesscontrol.GetGroups  (ok)
The GetGroups method returns the ID, name, and description of all the groups in the system.
- Privileges: This method requires Read privileges.
- Signature: `GetGroups(sessionToken: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
- Output: This method returns a string. If the method is successful, the value is an XML string that contains the ID, name, and description of each group. If there is a failure, the API issues an exception.

### accesscontrol.GetSecurityParameterName  (ok)
The GetSecurityParameterName method returns the textual name of a security parameter defined in the system.
- Privileges: This method requires Read privileges.
- Signature: `GetSecurityParameterName(sessionToken: String, securityParameters: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `securityParameters` (Integer): Internal ID of the security parameter as contained in the results of the accesscontrol.GetSecurityParameters method
- Output: This method returns a string. If the method is successful, the value is a text description of the security parameter's name as it appears in the GUI. If there is a failure, the API issues an exception.

### accesscontrol.GetSecurityParameters  (ok)
The GetSecurityParameters method returns a list of all of the security parameters and their corresponding IDs.
- Privileges: This method requires Read privileges.
- Signature: `GetSecurityParameters(sessionToken: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
- Output: This method returns a string. If the method is successful, the value is an XML string of all of the security parameters in the system. If there is a failure, the API issues an exception.

### accesscontrol.GetUser  (ok)
The GetUser method returns user information for the specified user ID.
- Privileges: This method requires Read privileges.
- Signature: `GetUser(sessionToken: String, userId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user as returned by the accesscontrol.LookupUserId method
- Output: This method returns a string. If the method is successful, the value is an XML string that contains account information for the specified user. If there is a failure, the API issues an exception.

### accesscontrol.GetUserContactInfo  (ok)
The GetUserContactInfo method returns contact information for a specified user ID. This contact information includes the user e-mail addresses and phone numbers.
- Privileges: This method requires Read privileges.
- Signature: `GetUserContactInfo(sessionToken: String, userId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user as returned by the accesscontrol.LookupUserId method
- Output: This method returns a string. If the method is successful, the value is an XML string that contains contact information for the specified user. If there is a failure, the API issues an exception.

### accesscontrol.GetUserDefaultEMail  (ok)
The GetUserDefaultEMail method returns the text value in a user's default email address field.
- Privileges: This method requires Read privileges.
- Signature: `GetUserDefaultEMail(sessionToken: String, userId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user as returned by the accesscontrol.LookupUserId method
- Output: This method returns a string. If the method is successful, the value is the contents of the default email address. If there is a failure, the API issues an exception.

### accesscontrol.GetUserList  (ok)
The GetUserList method returns a list of all users in the system.
- Privileges: This method requires Read privileges.
- Signature: `GetUserList(sessionToken: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
- Output: This method returns a string. If the method is successful, the value is an XML string that contains the ID, name, role, status, security parameter, and "logged on" indicator for every user in the company. If there is a failure, the API issues an exception.

### accesscontrol.GetUserListCount  (ok)
The GetUserListCount method returns the total number of non-deleted users in the system.
- Privileges: This method requires Read privileges.
- Signature: `GetUserListCount(sessionToken: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
- Output: This method returns an integer. If the method is successful, the value is the number of non-deleted users in the system. If there is a failure, the API issues an exception.

### accesscontrol.GetUserListPaginated  (ok)
The GetUserListPaginated method returns a list of all users in the system and allows you to specify the page size and desired page to be returned, thereby reducing the number of users returned per call.
- Privileges: This method requires Read privileges.
- Signature: `GetUserListPaginated(sessionToken: String, pageSize: Integer, Page: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `pageSize` (Integer): Number of users to return on each page.
  - `Page` (Integer): Page of the user list that you want to return. Note: Page numbering begins with 1.
- Output: This method returns a string. If the method is successful, the value is an XML string that contains the ID, name, role, status, security parameter, and "logged on" indicator for the users on the specified page of results. If there is a failure, the API issues an exception.

### accesscontrol.LookupDomainUserByFirstName  (ok)
The LookupDomainUserByFirstName method returns an XML structure containing users with a specified first name.
- Privileges: This method requires Read privileges.
- Signature: `LookupDomainUserByFirstName(sessionToken: String, keyword: String, userDomain: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `keyword` (String): Provides the name or first part of a name for which you can search
  - `userDomain` (String): Name of the domain to which the users and groups belong
- Output: This method returns a string. If the method is successful, the value is an XML string that contains the properties of each user whose first name meets the search criteria. If there is a failure, the API issues an exception.

### accesscontrol.LookupDomainUserByLastName  (ok)
The LookupDomainUserByLastName method returns a list of users with the specified last name.
- Privileges: This method requires Read privileges.
- Signature: `LookupDomainUserByLastName(sessionToken: String, keyword: String, userDomain: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `keyword` (String): Provides the name or first part of a name for which you can search
  - `userDomain` (String): Name of the domain to which the users and groups belong
- Output: This method returns a string. If the method was successful, the value is an XML string that contains the properties of each user whose last name meets the search criteria. If there is a failure, the API issues an exception.

### accesscontrol.LookupDomainUserId  (ok)
The LookupDomainUserId method returns a user’s ID from the system.
- Privileges: This method requires Read privileges.
- Signature: `LookupDomainUserId(sessionToken: String, username: String, userDomain: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `username` (String): Provides the user name of the user as returned by the accesscontrol. LookupUserName method
  - `userDomain` (String): Name of the domain to which the users and groups belong
- Output: This method returns an integer. If the method is successful, the value is the corresponding user ID. If there is a failure, the API issues an exception.

### accesscontrol.LookupEveryoneGroup  (ok)
The LookupEveryoneGroup method returns the groupId of the Everyone group.
- Privileges: This method requires Read privileges.
- Signature: `LookupEveryoneGroup(sessionToken: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
- Output: This method returns an integer. If the method is successful, the value is the ID of the Everyone group. If there is a failure, the API issues an exception.

### accesscontrol.LookupGroup  (ok)
The LookupGroup method returns the XML structure of the specified group in the system.
- Privileges: This method requires Read privileges.
- Signature: `LookupGroup(sessionToken: String, keyword: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `keyword` (String): An exact match of the group name as returned by the accesscontrol.GetGroup method. Note: The keyword must be an exact match of the full name, not just a fragment.
- Output: This method returns a string. If the method is successful, the value is an XML string of the group. If there is a failure, the API issues an exception.

### accesscontrol.LookupUserByFirstName  (ok)
The LookupUserByFirstName method returns an XML structure containing users with the specified first name.
- Privileges: This method requires Read privileges.
- Signature: `LookupUserByFirstName(sessionToken: String, keyword: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `keyword` (String): Name or first part of a name for which you can search
- Output: This method returns a string. If the method is successful, the value is an XML string that contains the properties of each user whose first name meets the search criteria. If there is a failure, the API issues an exception.

### accesscontrol.LookupUserByLastName  (ok)
The LookupUserByLastName method returns a list of users with the specified last name.
- Privileges: This method requires Read privileges.
- Signature: `LookupUserByLastName(sessionToken: String, keyword: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `keyword` (String): Name or first part of a name for which you can search
- Output: This method returns a string. If the method is successful, the value is an XML string that contains the properties of each user whose last name meets the search criteria. If there is a failure, the API issues an exception.

### accesscontrol.LookupUserId  (ok)
The LookupUserId method returns a user ID from the system.
- Privileges: This method requires Read privileges.
- Signature: `LookupUserId(sessionToken: String, userName: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userName` (String): Provides the user name of the user as returned by the accesscontrol.LookupUserName method
- Output: This method returns an integer. If the method is successful, the value is the corresponding user ID. If there is a failure, the API issues an exception.

### accesscontrol.LookupUserName  (ok)
The LookupUserName method returns a user name from the system.
- Privileges: This method requires Read privileges.
- Signature: `LookupUserName(sessionToken: String, userId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user as returned by the accesscontrol.LookupUserId method
- Output: This method returns a string. If the method is successful, the value is the corresponding user name. If there is a failure, the API issues an exception.

### accesscontrol.RemoveChildFromGroup  (ok)
The RemoveChildFromGroup method removes the parent-child relationship between 2 groups.
- Privileges: This method requires Delete privileges.
- Signature: `RemoveChildFromGroup(sessionToken: String, childGroupId: Integer, parentGroupId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `childGroupId` (Integer): Internal ID of the child group returned by the accesscontrol.LookupGroup method
  - `parentGroupId` (Integer): Internal ID of the parent group as contained in the results of the accesscontrol. LookupGroup method
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.RemoveUserFromGroup  (ok)
The RemoveUserFromGroup method removes a user from the specified group.
- Privileges: This method requires Delete privileges.
- Signature: `RemoveUserFromGroup(sessionToken: String, userId: Integer, groupId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user returned by the accesscontrol.LookupUserId method
  - `groupId` (Integer): Internal ID of the group as contained in the results of the accesscontrol. LookupGroup method
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.RemoveUserFromRole  (ok)
The RemoveUserFromRole method removes a user from a specific access role.
- Privileges: This method requires Delete privileges.
- Signature: `RemoveUserFromRole(sessionToken: String, userId: Integer, roleId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user returned by the accesscontrol.LookupUserId method
  - `roleId` (Integer): Internal ID of the access role from which the user should be removed as contained in the results of the accessrole.GetRoles method
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.SetUserDefaultEmail  (ok)
The SetUserDefaultEmail method modifies a user's default email and creates 1 when necessary.
- Privileges: This method requires Update privileges.
- Signature: `SetUserDefaultEmail(sessionToken: String, userId: Integer, email_address: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user returned by the accesscontrol.LookupUserId method
  - `email_address` (String): Email address that you want to set as the default
- Output: This method returns an integer. If the method is successful, the returned value is an integer. If there is a failure, the API issues an exception.

### accesscontrol.UpdateContactInfo  (ok)
The UpdateContactInfo method overwrites existing contact information, such as email addresses and phone numbers, with updated information on a user's account record. Before invoking this method, obtain your system's contact type IDs and contact subtype IDs using the following methods: accesscontrol.GetContactTypes accesscontrol.GetContactSubTypes
- Privileges: This method requires Update privileges.
- Signature: `UpdateContactInfo(sessionToken: String, userId: Integer, contactInfo: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `userId` (Integer): Internal ID of the user returned by the accesscontrol.LookupUserId method.
  - `contactInfo` (String): String that provides the following: The contact type ID for the contact type that you want to add as returned by the accesscontrol.GetContactTypes method. The contact subtype ID for the contact type that you want to add as returned by the accesscontrol.GetContactSubTypes method. The value to add for the contact type, either the e-mail address or phone number. A true or false indicator that determines whether the contact value should be the default for the user's account. (This is only applicable if you are adding an email address.) The following is a sample string for this parameter: <ContactInfo> <ContactTypeId>7</ContactTypeId> <ContactSubTypeId>3</ContactSubTypeId> <ContactInfo>jmiller@company-name.com</ContactInfo> <ContactDefault>false </ContactDefault> </ContactInfo> In this example, the contact type ID of 7 indicates that the value is an email address. The contact subtype ID of 3 indicates that it is a home email address. The contact default flag of false indicates that the e-mail address is not the default address for the user account.
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.UpdateDomainUser  (ok)
The UpdateDomainUser method allows you to modify the account properties for a user. Use this method to modify the First, middle, and last name, Company name, Title, Security parameter, Address, and Time zone of a user.
- Privileges: This method requires Update privileges.
- Signature: `UpdateDomainUser(sessionToken: String, userId: String, firstName: String, middleName: String, lastName: String, companyName: String, title: String, securityParameter: Integer, address: String, timeZone: Integer, usersDomain: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `userId` (String): Internal ID of the user as returned by the accessontrol.LookupUserId method.
  - `firstName` (String): User first name.
  - `middleName` (String): User middle name.
  - `lastName` (String): User last name.
  - `companyName` (String): User organization or company.
  - `title` (String): User job title or function.
  - `securityParameter` (Integer): Internal ID of the corresponding security parameter as contained in the results of the accesscontrol.GetSecurityParameters method.
  - `address` (String): User location mailing address.
  - `timeZone` (Integer): Important: This parameter is disabled, but an integer must still be passed in the method. It is recommended to use 0.
  - `usersDomain` (String): Name of the domain to which the users and groups belong.
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.UpdateExtendedSecurityParameter  (ok)
The UpdateExtendedSecurityParameter method allows you to modify an existing security parameter. This method differs from the UpdateSecurityParameter method in that it includes the following parameters: Uppercase Characters Required Lowercase Characters Required Special Characters Required
- Privileges: This method requires Update privileges.
- Signature: `UpdateExtendedSecurityParameter(sessionToken: String, securityParameterId: Integer, name: String, description: String, minPasswordLength: Integer, MinPasswordCharacters: Integer, minPasswordNumerals: Integer, passwordLifetime: Integer, graceLogins: Integer, maxRetries: Integer, lockDuration: Integer, lockIntervalType: Integer, sessionTimeout: Integer, passwordHistoryCheckDepth: Integer, expiratonNotice: Integer, accountTimeout: Integer, timeoutIntervalType: Integer, minUppercaseCharacters: Integer, minLowercaseCharacters: Integer, minSpecialCharacters: Integer, pinTimeout: Integer, pinTimeoutType: Integer, pinMaxResendAttempts: Integer, pinResendLockTimeout: Integer, pinResendLockTimeoutType: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `securityParameterId` (Integer): Internal ID of the security parameter returned in the xcomp_sec_prm_id element after calling accesscontrol.GetSecurityParameters .
  - `name` (String): Name of the security parameter.
  - `description` (String): Description of the security parameter.
  - `minPasswordLength` (Integer): Minimum number of characters required in the password.
  - `MinPasswordCharacters` (Integer): Minimum number of alpha characters required in the password.
  - `minPasswordNumerals` (Integer): Minimum number of numeric characters required in the password.
  - `passwordLifetime` (Integer): Length of time in days that a password is valid.
  - `graceLogins` (Integer): Maximum number of grace logons allowed after a password lifetime has expired.
  - `maxRetries` (Integer): Maximum number of times a user can unsuccessfully attempt to log on to the system before the account is put into a locked state.
  - `lockDuration` (Integer): Duration that a user account remains in a locked state after surpassing the maximum number of retries.
  - `lockIntervalType` (Integer): Type of lock duration (1=Hours, 2=Minutes, and 3=Days).
  - `sessionTimeout` (Integer): Duration of inactivity after which a user session times out. Note: The unit of measure is set in the timeoutIntervalType element.
  - `passwordHistoryCheckDepth` (Integer): Number of previous passwords to keep track of and to restrict the reuse of.
  - `expiratonNotice` (Integer): Number of days before a password's expiration that a warning is displayed.
  - `accountTimeout` (Integer): Number of days after which an account status is automatically changed to inactive. 0 = none or never automatically deactivates
  - `timeoutIntervalType` (Integer): Unit of measure for sessionTimeout (1=Hours, 2=Minutes, and 3=Days).
  - `minUppercaseCharacters` (Integer): Number of uppercase characters that must be contained in a user password.
  - `minLowercaseCharacters` (Integer): Number of lowercase characters that must be contained in a user password.
  - `minSpecialCharacters` (Integer): Number of special characters that must be contained in a user's password. Special characters can include: ` ~ ! @ # $ % ^ & * ( ) _ + - = { } | : " < > ? [ ] \ ; ’ , . /
  - `pinTimeout` (Integer): Maximum length of time a PIN remains active before the PIN expires.
  - `pinTimeoutType` (Integer): Type of PIN timeout (1=Hours, 2=Minutes, and 3=Days).
  - `pinMaxResendAttempts` (Integer): Number of times users can request a PIN before the system prevents them from requesting additional PINs.
  - `pinResendLockTimeout` (Integer): Lockout period before users can request a PIN after they exceed their maximum PIN request limit.
  - `pinResendLockTimeoutType` (Integer): Type of Resend PIN Lock Timeout (1=Hours, 2=Minutes, and 3=Days).
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.UpdateGroup  (ok)
The UpdateGroup method modifies the name of a group in the system.
- Privileges: This method requires Update privileges.
- Signature: `UpdateGroup(sessionToken: String, groupId: Integer, groupName: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `groupId` (Integer): Internal ID of the group as contained in the results of the accesscontrol. LookupGroup method
  - `groupName` (String): New group name
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.UpdateSecurityParameter  (ok)
The UpdateSecurityParameter method allows you to modify an existing security parameter.
- Privileges: This method requires Update privileges.
- Signature: `UpdateSecurityParameter(sessionToken: String, securityParameterId: Integer, name: String, Description: String, minPasswordLength: Integer, MinPasswordCharacters: Integer, minPasswordNumerals: Integer, passwordLifetime: Integer, graceLogins: Integer, maxRetries: Integer, lockDuration: Integer, lockIntervalType: Integer, sessionTimeout: Integer, passwordHistoryCheckDepth: Integer, expiratonNotice: Integer, accountTimeout: Integer, timeoutIntervalType: Integer, pinTimeout: Integer, pinTimeoutType: Integer, pinMaxResendAttempts: Integer, pinResendLockTimeout: Integer, pinResendLockTimeoutType: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `securityParameterId` (Integer): Internal ID of the security parameter returned in the xcomp_sec_prm_id element after calling accesscontrol.GetSecurityParameters
  - `name` (String): Name of the security parameter
  - `Description` (String): Description of the security parameter
  - `minPasswordLength` (Integer): Minimum number of characters required in the password
  - `MinPasswordCharacters` (Integer): Minimum number of alpha characters required in the password
  - `minPasswordNumerals` (Integer): Minimum number of numeric characters required in the password
  - `passwordLifetime` (Integer): Length of time in days that a password is valid
  - `graceLogins` (Integer): Maximum number of grace logons allowed after a password lifetime has expired
  - `maxRetries` (Integer): Maximum number of times a user can unsuccessfully attempt to log on to the system before the account is put into a locked state
  - `lockDuration` (Integer): Duration that a user's account remains in a locked state after surpassing the maximum number of retries
  - `lockIntervalType` (Integer): Type of lock duration (1=Hours, 2=Minutes, and 3=Days).
  - `sessionTimeout` (Integer): Duration of inactivity after which a user's session times out. The unit of measure is set in the timeoutIntervalType method
  - `passwordHistoryCheckDepth` (Integer): Number of previous passwords to keep track and restrict reuse
  - `expiratonNotice` (Integer): Number of days before a password's expiration that a warning is displayed
  - `accountTimeout` (Integer): Number of days after which an account's status automatically is changed to inactive. 0 = none or never automatically deactivates
  - `timeoutIntervalType` (Integer): Unit of measure for sessionTimeout (1=Hours, 2=Minutes, and 3=Days).
  - `pinTimeout` (Integer): Maximum length of time a PIN remains active before the PIN expires.
  - `pinTimeoutType` (Integer): Type of PIN timeout (1=Hours, 2=Minutes, and 3=Days).
  - `pinMaxResendAttempts` (Integer): Number of times users can request a PIN before the system prevents them from requesting additional PINs.
  - `pinResendLockTimeout` (Integer): Lockout period before users can request a PIN after they exceed their maximum PIN request limit.
  - `pinResendLockTimeoutType` (Integer): Type of Resend PIN Lock Timeout (1=Hours, 2=Minutes, and 3=Days).
- Output: This method returns an integer. If the method was successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.UpdateUserAccountStatus  (ok)
The UpdateUserAccountStatus method modifies the status of a user's account.
- Privileges: This method requires Update privileges.
- Signature: `UpdateUserAccountStatus(sessionToken: String, userId: Integer, accountStatus: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user as returned by the accesscontrol.LookupUserId method
  - `accountStatus` (Integer): Integer that sets the account status Note: 1 = Active, 2 = Inactive, and 3 = Locked
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.UpdateUserEx  (ok)
The UpdateUserEx method replaces the UpdateUser and UpdateDomainUser methods used in version 4.x. This method allows you to modify the account properties for a user. Use this method to modify the First, middle, and last name, Company name, Title, Security parameter, Address, Time zone, and Locale of a user.
- Privileges: This method requires Update privileges.
- Signature: `UpdateUserEx(sessionToken: String, userId: Integer, firstName: String, middleName: String, lastName: String, companyName: String, title: String, securityParameter: Integer, address: String, userDomain: String, timeZone: String, locale: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `userId` (Integer): Internal ID of the user as returned by the accesscontrol.LookupUserId method.
  - `firstName` (String): User first name.
  - `middleName` (String): User middle name.
  - `lastName` (String): User last name.
  - `companyName` (String): User organization or company.
  - `title` (String): User job title or function.
  - `securityParameter` (Integer): Internal ID of the corresponding Security Parameter as contained in the results of the accesscontrol.GetSecurityParameters method.
  - `address` (String): User location or mailing address.
  - `userDomain` (String): User domain. Note: If this value is NULL or empty, the system replaces the current value with NULL.
  - `timeZone` (String): User time zone. Use the .NET time zone ID property. Note: If this value is NULL or empty, the system uses the server default of the instance. For more information supported time zones, see Supported Time Zones .
  - `locale` (String): User locale. Use the .NET CultureInfo name property, for example, en-US. Note: If this value is NULL or empty, the system deletes the current value and uses the server default of the instance. For more information on supported locales, see Supported Locales .
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accesscontrol.UpdateUserName  (ok)
The UpdateUserName method sets the user name to the specified value.
- Privileges: This method requires Update privileges.
- Signature: `UpdateUserName(sessionToken: String, userId: Integer, userName: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user as returned by the accesscontrol.LookupUserId method
  - `userName` (String): User name
- Output: This method returns an integer. If the method is successful, the value is 1 and if no change was made, the value is 0. If there is a failure, the API issues an exception.

### accesscontrol.UpdateUserNote  (ok)
The UpdateUserNote method overwrites the text value in a user's Additional Notes field with the provided value.
- Privileges: This method requires Update privileges.
- Signature: `UpdateUserNote(sessionToken: String, userId: Integer, note: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `userId` (Integer): Internal ID of the user as returned by the accesscontrol.LookupUserId method
  - `note` (String): Text for the Additional Notes field
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Access Role (accessrole.asmx)
<a id="accessrole"></a>

### accessrole.CreateRole  (ok)
The CreateRole method creates an access role in the system.
- Privileges: This method requires Create privileges.
- Signature: `CreateRole(sessionToken: String, roleName: String, roleDesc: String, defaultFlag: Boolean, requiredFlag: Boolean)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `roleName` (String): Role name
  - `roleDesc` (String): Role descriptio
  - `defaultFlag` (Boolean): Indicates whether the role is the default role
  - `requiredFlag` (Boolean): Indicates whether members of the role can view all records in the applications for which they have at least Read access rights
- Output: This method returns an integer. If the method is successful, the value is the role ID. If there is a failure, the API issues an exception.

### accessrole.DeleteRole  (ok)
The DeleteRole method deletes an access role in the system.
- Privileges: This method requires Delete privileges.
- Signature: `DeleteRole(sessionToken: String, roleId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `roleId` (Integer): Internal ID of the role to be deleted
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### accessrole.GetRole  (ok)
The GetRole method retrieves an access role in the system.
- Privileges: This method requires Read privileges.
- Signature: `GetRole(sessionToken: String, roleId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `roleId` (Integer): Internal ID of the role to be deleted
- Output: This method returns a string. The value is an XML string containing the role ID, company ID, role name, role description, required flag, and default flag. If there is a failure, the API issues an exception.

### accessrole.GetRoleDependencies  (ok)
The GetRoleDependencies method retrieves all the dependencies for the specified role. The dependencies are the users and groups that are only assigned to the access role.
- Privileges: This method requires Read privileges.
- Signature: `GetRoleDependencies(sessionToken: String, roleId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `roleId` (Integer): Internal ID of the role for which to return the dependencies
- Output: This method returns a string. The value is an XML string containing all of the access role dependencies (users and groups) in the system. If there is a failure, the API issues an exception.

### accessrole.GetRolePagePermissions  (ok)
The GetRolePagePermissions method retrieves all the page permissions (Create, Read, Write, and Delete) for the specified role.
- Privileges: This method requires Read privileges.
- Signature: `GetRolePagePermissions(sessionToken: String, roleId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `roleId` (Integer): Internal ID of the role for which to return the dependencies

### accessrole.GetRolePagePermissionsForModule  (ok)
The GetRolePagePermissionsForModule method retrieves all of the Read/Write/Delete page permissions for the specified role and application.
- Privileges: This method requires Read privileges.
- Signature: `GetRolePagePermissionsForModule(sessionToken: String, roleId: Integer, moduleId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `roleId` (Integer): Internal ID of the role for which to return the dependencies
  - `moduleId` (Integer): Internal ID of the application for which to return the role page permissions

### accessrole.GetRoles  (ok)
The GetRoles method retrieves all of the access roles in the system.
- Privileges: This method requires Read privileges.
- Signature: `GetRoles(sessionToken: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
- Output: This method returns an XML string containing all of the access roles in the system. Each access role contains the role ID, company ID, role name, role description, required flag, and default flag. If there is a failure, the API issues an exception.

### accessrole.UpdateRole  (ok)
The UpdateRole method updates an access role in the system.
- Privileges: This method requires Update privileges.
- Signature: `UpdateRole(sessionToken: String, roleId: Integer, moduleId: Integer, roleName: String, roleDesc: String, defaultFlag: Boolean, requiredFlag: Boolean)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `roleId` (Integer): Internal ID of the role to update
  - `moduleId` (Integer): Internal ID of the application for which to return the role page permissions
  - `roleName` (String): New role name
  - `roleDesc` (String): New role description
  - `defaultFlag` (Boolean): Indicates if the role is the default role
  - `requiredFlag` (Boolean): Indicates if members of the role can view all records in the applications for which they have at least Read access rights
- Output: This method returns an integer. If the method was successful, the value is 1. If there is a failure, the API issues an exception.

### accessrole.UpdateRolePagePermissions2  (ok)
The UpdateRolePagePermissions2 method updates the page permissions (Create, Read, Update, and Delete) for the specified role and page.
- Privileges: This method requires Update privileges.
- Signature: `UpdateRolePagePermissions2(sessionToken: String, roleId: Integer, pageId: Integer, create: Boolean, read: Boolean, update: Boolean, delete: Boolean)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `roleId` (Integer): Internal ID of the role for which to update the page permissions
  - `pageId` (Integer): Internal ID of the page for which to update the page permissions
  - `create` (Boolean): Create page permission
  - `read` (Boolean): Read page permission
  - `update` (Boolean): Update page permission
  - `delete` (Boolean): Delete page permission
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Field (field.asmx)
<a id="field"></a>

### field.CreateValuesListItemWithNumericValue  (ok)
The CreateValuesListItemWithNumericValue method creates a values list item with an associated numeric value. For example, you could create the value "High" with a numeric value of 10 using this method.
- Privileges: This method requires Create privileges.
- Signature: `CreateValuesListItemWithNumericValue(sessionToken: String, valuesListId Integer: Integer, valuesListItemName: String, valuesListItemNumericValue: Decimal)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `valuesListId Integer` (Integer): Internal ID of the specific values list for which you want to create a value as included in the results of the field.GetValueListForField method
  - `valuesListItemName` (String): Value to add
  - `valuesListItemNumericValue` (Decimal): Numeric value to associate with the values list item
- Output: This method returns an integer. If the method was successful, the value is 1. If there is a failure, the API issues an exception.

### field.CreateValuesListValue  (ok)
The CreateValuesListValue method creates a values list item within the specified valuesListId.
- Privileges: This method requires Create privileges.
- Signature: `CreateValuesListValue(sessionToken: String, valuesListId Integer: Integer, valuesListItemName: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `valuesListId Integer` (Integer): Internal ID of the specific values list for which you want to create a value as included in the results of the field.GetValueListForField method
  - `valuesListItemName` (String): Value to add
- Output: This method returns an integer. The value is the ID of the values list item in the system. If there is a failure, the API issues an exception.

### field.DeleteValuesListValue  (ok)
The DeleteValuesListValue method removes the specified values list item.
- Privileges: This method requires Delete privileges.
- Signature: `DeleteValuesListValue(sessionToken: String, valuesListId: Integer, valuesListValueId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `valuesListId` (Integer): Internal ID of the specific values list that you want to delete as included in the results of the field.GetValueListForField method
  - `valuesListValueId` (Integer): Internal ID of the specific values list value that you want to delete as returned by the field.LookupListValue method
- Output: This method returns an integer. The value is 1 if the method was successful. The API issues an exception if there is a failure.

### field.GetFieldIdByGUID  (ok)
The GetFieldIDByGUID method returns the Field ID of the field associated with the specified GUID.
- Privileges: This method requires Read privileges.
- Signature: `GetFieldIdByGUID(sessionToken: String, GUID: String, valuesListValueId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `GUID` (String): GUID for the desired field. Note: This value can be found by reviewing the Application Field Detail report within the Archer Platform and copying the GUID for the desired field.
  - `valuesListValueId` (Integer): Internal ID of the specific values list value you want to delete as returned by the field.LookupListValue method.
- Output: This method returns an integer. If the method was successful, the value is the ID of the field associated with the GUID. If there is a failure, the API issues an exception.

### field.GetValueListForField  (ok)
The GetValueListForField returns the values list for the specified field.
- Privileges: This method requires Read privileges.
- Signature: `GetValueListForField(sessionToken: String, fieldId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `fieldId` (Integer): Internal ID of the Values List field. Note: The ID of a field can be determined by reviewing the Application Detail Report from within Application Builder or by invoking the record.GetRecordById method and reviewing the mappings.
- Output: This method returns a string. The value is an XML string containing all available values list items (ID, Value, and Description) in the values list. Second-level items are nested within the first-level SelectDefValue element. If there is a failure, the API issues an exception.

### field.GetValuesList  (ok)
The GetValuesList method returns the first level of values for the specified values list.
- Privileges: This method requires Read privileges.
- Signature: `GetValuesList(sessionToken: String, valuesListId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `valuesListId` (Integer): Internal ID of the specific values list you want to retrieve as included in the results of the field.GetValueListForField method
- Output: This method returns a string. The value is an XML string containing all of the top-level items (ID, Value, and Description) in the values list. If there is a failure, the API issues an exception.

### field.GetValuesListIdByGUID  (ok)
The GetValuesListIdByGUID method returns the values list ID of the global values list associated with the specified GUID.
- Privileges: This method requires Read privileges.
- Signature: `GetValuesListIdByGUID(sessionToken: String, GUID: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `GUID` (String): The GUID for the desired values list. Note: This value can be found by reviewing the Manage Global Values Lists page for the desired global values list and copying the GUID.
- Output: This method returns an integer. If the method is successful, the value is the ID of the global values list associated with the GUID. If there is a failure, the API issues an exception.

### field.GetValuesListItem  (ok)
The GetValuesListItem method retrieves the properties of the specified valuesListValueId, including the value name, description, numeric value, default setting, and text color.
- Privileges: This method requires Read privileges.
- Signature: `GetValuesListItem(sessionToken: String, valuesListValueId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `valuesListValueId` (Integer): Internal ID of the specific values list value, as returned by the field.LookupListValue method
- Output: This method returns a string. If the method is successful, the value represents the XML structure of the values list properties. If there is a failure, the API issues an exception.

### field.GetValuesListValue  (ok)
The GetValuesListValue method retrieves the text value of the specified valuesListValueId.
- Privileges: This method requires Read privileges.
- Signature: `GetValuesListValue(sessionToken: String, valuesListValueId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `valuesListValueId` (Integer): Internal ID of the specific values list value, as returned by the field.LookupListValue method, whose text value you want to retrieve
- Output: This method returns a string. If the method is successful, the value represents the text value of the values list item. If there is a failure, the API issues an exception.

### field.GetValuesListValueIdByGUID  (ok)
The GetValuesListValueIDByGUID method returns the ID of the values list value associated with the specified GUID.
- Privileges: This method requires Read privileges.
- Signature: `GetValuesListValueIdByGUID(sessionToken: String, GUID: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `GUID` (String): The GUID for the desired values list value
- Output: This method returns an integer. If the method is successful, the value is the ID of the values list value associated with the GUID. If there is a failure, the API issues an exception.

### field.LookupListValue  (ok)
The LookupListValue method returns the ID of the values list item containing the search string.
- Privileges: This method requires Read privileges.
- Signature: `LookupListValue(sessionToken: String, fieldId: Integer, keyword: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `fieldId` (Integer): Internal ID of the field using the values list you want to query
  - `keyword` (String): A keyword for which to search in the values list
- Output: This method returns an integer. The value is the ID of the values list item in the system. If there is a failure, the API issues an exception.

### field.UpdateValuesListItemWithNumericValue  (ok)
The UpdateValuesListItemWithNumericValue method enables you to update the text value and numeric value of a values list item. It also enables you to associate a numeric value with a values list item that does not currently have an assigned numeric value.
- Privileges: This method requires Update privileges.
- Signature: `UpdateValuesListItemWithNumericValue(sessionToken: String, valuesListItemId: Integer, valuesListItemNumericValue: Decimal)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `valuesListItemId` (Integer): Internal ID of the specific values list value that you want to modify as returned by the field.LookupListValue method.
  - `valuesListItemNumericValue` (Decimal): Numeric value that you want to associate with the values list item. Note: This can be a positive, negative, or decimal value.
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### field.UpdateValuesListNumericValueToNull  (ok)
The UpdateValuesListNumericValueToNull method sets the numeric value associated with the specified valuesListValueID to null.
- Privileges: This method requires Update privileges.
- Signature: `UpdateValuesListNumericValueToNull(sessionToken: String, valuesListItemId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `valuesListItemId` (Integer): Internal ID of the specific values list value that you want to modify as returned by the field.LookupListValue method
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### field.UpdateValuesListValue  (ok)
The UpdateValuesListValue method modifies the text value of the specified valuesListValueId.
- Privileges: This method requires Update privileges.
- Signature: `UpdateValuesListValue(sessionToken: String, valuesListValueId: Integer, valuesListValueName: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `valuesListValueId` (Integer): Internal ID of the specific values list value that you want to modify as returned by the field.LookupListValue method
  - `valuesListValueName` (String): Value that you want to assign the specified values list value
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## General (general.asmx)
<a id="general"></a>

### general.CreateDomainUserSessionFromInstance  (ok)
The CreateDomainUserSessionFromInstance method creates a session using the specified credentials.
- Privileges: This method requires Read privileges.
- Signature: `CreateDomainUserSessionFromInstance(username: String, instanceName: String, password: String, usersDomain: String)`
- Parameters:
  - `username` (String): Name of the instance where the session should be created.
  - `instanceName` (String): Company identification number.
  - `password` (String): User password.
  - `usersDomain` (String): Name of the domain to which the users and groups belong.
- Output: This method returns a string. If the method is successful, the value is a 32-character alphanumeric sessionToken. If there is a failure, the API issues an exception.

### general.CreateUserSessionFromInstance  (ok)
The CreateUserSessionFromInstance method creates a session using the specified credentials.
- Privileges: This method requires Read privileges.
- Signature: `CreateUserSessionFromInstance(userName: String, instanceName: String, password: String)`
- Parameters:
  - `userName` (String): Valid user name to log on with that has permissions to the appropriate API pages
  - `instanceName` (String): Name of the instance in which the session should be created
  - `password` (String): User password
- Output: This method returns a string. If the method is successful, the value is a 32-character alphanumeric sessionToken. If there is a failure, the API issues an exception.

### general.TerminateSession  (ok)
The TerminateSession method expires the specified session.
- Privileges: This method requires Delete privileges.
- Signature: `TerminateSession(sessionToken: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

## Module (module.asmx)
<a id="module"></a>

### module.GetModuleIdByGUID  (ok)
The GetModuleIdByGUID method retrieves the ID for an application (module) in the system.
- Privileges: This method requires Read privileges.
- Signature: `GetModuleIdByGUID(sessionToken: String, instanceId: String, GUID: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `instanceId` (String): ID of the instance that contains the application that you want to export. You can find this instance ID in the Control Panel.
  - `GUID` (String): GUID of the application for which you want to return an ID.
- Output: This method returns an integer, which is the assigned ID for the application to which the GUID belongs. If there is a failure, the API issues an exception.

## Record (record.asmx)
<a id="record"></a>

### record.CheckAsyncMailMergeProgress  (ok)
The CheckAsyncMailMergeProgress method returns the percentage in which the specified Mail Merge process is complete.
- Privileges: This method requires Create privileges.
- Signature: `CheckAsyncMailMergeProgress(sessionToken: String, exportId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `exportId` (Integer): Identifier returned by the record.StartAsyncMailMerge method.
- Output: This method returns an integer value. This integer value represents a number between 0 and 100 which tells the percentage in which the specified Mail Merge is complete. If there is a failure, the API issues an exception.

### record.CreateCMSTEntry  (ok)
The CreateCMSTEntry method assigns a value to a relationship between 2 records.
- Privileges: This method requires Create privileges.
- Signature: `CreateCMSTEntry(sessionToken: String, contentId: Integer, fieldId: Integer, parentId: Integer, valueId: Integer, comments: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `contentId` (Integer): Internal ID of a record within the source application (that is, the application in which the CAST field was defined), as returned by the search.ExecuteSearch method.
  - `fieldId` (Integer): Internal ID of the CAST field within the source application (that is, the application in which the CAST field was defined). You can obtain the field ID from the Application Detail Report in Application Builder. Field IDs are also provided in the results of the record.GetRecordById method.
  - `parentId` (Integer): Internal ID of the content record in the related application (that is, the application that was specified when configuring the CAST field in the source application), as returned by the search.ExecuteSearch method.
  - `valueId` (Integer): Internal ID of the specific values list value that you want to modify, as returned by the field.LookupListValue method.
  - `comments` (String): Notes regarding the assignment of the above value.
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### record.CreateQuestionnaireRecord  (ok)
The CreateQuestionnaireRecord method creates a new questionnaire record within the specified questionnaire populating only the target cross-reference field.
- Privileges: This method requires Create privileges.
- Signature: `CreateQuestionnaireRecord(sessionToken: String, questionnairModuleId: Integer, targetContentId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `questionnairModuleId` (Integer): Internal ID of the questionnaire as specified in the Application Builder Questionnaire Detail Report.
  - `targetContentId` (Integer): Internal ID of the target record within the specified target application as returned by the search.ExecuteSearch method.
- Output: This method returns an integer. If the method is successful, the value is the content ID of the newly created questionnaire record. If there is a failure, the API issues an exception.

### record.CreateRecord  (ok)
The CreateRecord method creates a record using the specified values.
- Privileges: This method requires Create privileges.
- Signature: `CreateRecord(sessionToken: String, moduleId: Integer, fieldValues: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `moduleId` (Integer): Internal ID of an application as specified in the Application Builder Application Detail Report.
  - `fieldValues` (String): XML structure of the fields and values to add. Note: For details about constructing this string, see XML Formatting Guidelines for Field Input .
- Output: This method returns an integer. If the method is successful, the value is the content ID of the newly created record. If there is a failure, the API issues an exception.

### record.CreateRecords  (ok)
The CreateRecords method enables the bulk creation of records in an application. When adding contact records, this method adds the user record when the User Account is selected and the user has rights to manage users.
- Privileges: This method requires Create privileges.
- Signature: `CreateRecords(sessionToken: String, moduleId: Integer, contentRecords: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `moduleId` (Integer): Internal ID of an application as specified in the Application Builder Application Detail Report
  - `contentRecords` (String): XML structure of the records to add Note: For details about constructing this string, see XML Formatting Guidelines for Field Input .
- Output: This method returns a string. If the method is successful, the string contains an XML list of the content IDs for the newly created records. If there is a failure, the API issues an exception.

### record.CreateSubformRecord  (ok)
The CreateSubformRecord method creates a sub-form record using the specified values. When you save the sub-form, the API returns the sub-form content ID, which you then use when saving the parent record.
- Privileges: This method requires Create privileges.
- Signature: `CreateSubformRecord(sessionToken: String, subformModuleId: Integer, subformFieldID: Integer, fieldValues: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `subformModuleId` (Integer): Internal ID of the sub-form as specified in the Application Builder Sub-Form Detail Report
  - `subformFieldID` (Integer): Internal ID of the Sub-Form field as specified in the Application Builder Application Detail Report
  - `fieldValues` (String): XML structure of the fields and values to add Note: For details about constructing this string, see XML Formatting Guidelines for Field Input .
- Output: This method returns an integer. If the method is successful, the value is the content ID of the newly created sub-form record. If there is a failure, the API issues an exception.

### record.DeleteRecord  (ok)
The DeleteRecord method removes the specified record from the system. When deleting a record, this method also deletes the associated subform.
- Privileges: This method requires Delete privileges.
- Signature: `DeleteRecord(sessionToken: String, moduleId: Integer, contentId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `moduleId` (Integer): Internal ID of an application as specified in the Application Builder Application Detail Report
  - `contentId` (Integer): Internal ID of a record within the specified application as returned by the search.ExecuteSearch method
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### record.GetAccessHistory  (ok)
The GetAccessHistory method returns access history data for a specific record in a specified application.
- Privileges: This method requires Read privileges.
- Signature: `GetAccessHistory(sessionToken: String, contentId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `contentId` (Integer): Internal ID of a record within the specified application as returned by the search.ExecuteSearch method
- Output: This method returns a string. If the method is successful, the value is an XML string that contains access history data for the specific record. If there is a failure, the API issues an exception.

### record.GetAsyncMailMergeDocument  (ok)
The GetAsyncMailMergeDocument method retrieves the asynchronous mail merge MS Word document.
- Privileges: This method requires Create privileges.
- Signature: `GetAsyncMailMergeDocument(sessionToken: String, exportId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `exportId` (Integer): Identifier returned by the record.StartAsyncMailMerge method
- Output: This method returns a byte array. If the Mail Merge process is not complete, it returns null. If the Mail Merge process is complete and no failure occured, the byte array contains the contents of the MS Word document. If there is a failure, the API issues an exception.

### record.GetAttachmentFile  (ok)
The GetAttachmentFile method returns all details of the specified file ID.
- Privileges: This method requires Read privileges.
- Signature: `GetAttachmentFile(SessionToken: String, fileId: Integer)`
- Parameters:
  - `SessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `fileId` (Integer): Internal ID of the file information to retrieve.
- Output: This method returns a string. If the file ID is not found, an empty string is returned. If the method is successful, the value is the XML structure of the requested file information. If there is a failure, the API issues an exception.

### record.GetChildRecordIds  (ok)
The GetChildRecordIds method retrieves a list of records related to the given top-level contentId by a locked cross-reference that is bound to the second level.
- Privileges: This method requires Read privileges.
- Signature: `GetChildRecordIds(sessionToken: String, moduleId: Integer, contentId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `moduleId` (Integer): Internal ID of a parent-level record as returned by the search.ExecuteSearch method
  - `contentId` (Integer): Internal ID of a parent-level record as returned by the search.ExecuteSearch method
- Output: This method returns a string. The value is an XML string containing a list of IDs.

### record.GetRecordById  (ok)
The GetRecordById method returns all details of the specified record. The search filters are based on the specified option setting: System ID or Application ID.
- Privileges: This method requires Read privileges.
- Signature: `GetRecordById(sessionToken: String, moduleId: Integer, contentId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `moduleId` (Integer): Internal ID of an application as specified in the Application Builder Application Detail Report Note: This parameter has no effect on the function of the GetRecordById method.
  - `contentId` (Integer): Internal ID of a record within the specified application as returned by the search.ExecuteSearch method
- Output: This method returns a string. If the method is successful, the value is the XML structure of the requested record. If there is a failure, the API issues an exception.

### record.PerformMailMerge  (ok)
The PerformMailMerge method performs a mail merge synchronously and returns an Microsoft Word document.
- Privileges: This method requires Create privileges.
- Signature: `PerformMailMerge(sessionToken: String, contentId: Integer, mailMergeTemplateId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `contentId` (Integer): Internal ID of a content record
  - `mailMergeTemplateId` (Integer): Internal ID of a Mail Merge Template record
- Output: This method returns a byte array. If the method is successful, the byte array contains the contents of the Word document. If there is a failure, the API issues an exception.

### record.StartAsyncMailMerge  (ok)
The StartAsyncMailMerge method performs a mail merge asynchronously.
- Privileges: This method requires Create privileges.
- Signature: `StartAsyncMailMerge(sessionToken: String, contentId: Integer, mailMergeTemplateId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `contentId` (Integer): Internal ID of a content record
  - `mailMergeTemplateId` (Integer): Internal ID of a Mail Merge Template record
- Output: This method returns an integer. This integer value is used to identify this particular execution of the Mail Merge process. If there is a failure, the API issues an exception.

### record.UpdateRecord  (ok)
The UpdateRecord method modifies the specified record.
- Privileges: This method requires Update privileges.
- Signature: `UpdateRecord(sessionToken: String, moduleId: Integer, contentId: Integer, fieldValues: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `moduleId` (Integer): ID of an application as specified in the Application Builder Application Detail Report.
  - `contentId` (Integer): System ID for the record within the specified application as returned by the search.ExecuteSearch method. This is a unique value used throughout all of Archer , and not the Field Specific Attribute Tracking ID. Note: This cannot be an Application ID.
  - `fieldValues` (String): XML string of the fields and values to modify. Note: For details about constructing this string, see XML Formatting Guidelines for Field Input .
- Output: This method returns an integer. If the method is successful, the value is 1. If there is a failure, the API issues an exception.

### record.UpdateRecords  (ok)
The UpdateRecords method enables the bulk update of records in an application.
- Privileges: This method requires Update privileges.
- Signature: `UpdateRecords(sessionToken: String, moduleId: Integer, contentRecords: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `moduleId` (Integer): ID of an application as specified in the Application Builder Application Detail Report.
  - `contentRecords` (String): XML structure of the records to modify. Note: For details about constructing this string, see XML Formatting Guidelines for Field Input .
- Output: This method returns an XML string indicating the records that failed to update.

## Search (search.asmx)
<a id="search"></a>

### search.ExecuteQuickSearchWithModuleIds  (ok)
The ExecuteQuickSearchWithModuleIds method runs a keyword search on the specified applications or questionnaires.
- Privileges: This method requires Read privileges.
- Signature: `ExecuteQuickSearchWithModuleIds(sessionToken: String, moduleIds: String, keywords: String, pageNumber: Integer, pageSize: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `moduleIds` (String): Internal IDs of the applications or questionnaires that you want to query
  - `keywords` (String): Search keywords as you would enter them if searching in the application or questionnaire
  - `pageNumber` (Integer): Integer of the page (1,2,3,…,n) of search results to return
  - `pageSize` (Integer): Number of records to display per page of search results
- Output: This method returns a string. The value is an XML string containing the fields of records in the specified applications or questionnaires matching the specific keywords.

### search.ExecuteQuickSearchWithSolutionId  (ok)
The ExecuteQuickSearchWithSolutionId method runs a keyword search on the specified solution.
- Privileges: This method requires Read privileges.
- Signature: `ExecuteQuickSearchWithSolutionId(sessionToken: String, solutionId: Integer, keywords: String, pageNumber: Integer, pageSize: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `solutionId` (Integer): Internal ID of the solution that you want to query
  - `keywords` (String): Search keywords as you would enter them if searching in the solution
  - `pageNumber` (Integer): Integer of the page (1,2,3,…,n) of search results to return
  - `pageSize` (Integer): Number of records to display per page of search results
- Output: This method returns a string. The value is an XML string containing the fields of records in the specified solution matching the specific keywords.

### search.ExecuteSearch  (ok)
The ExecuteSearch method runs a search according to custom criteria.
- Privileges: This method requires Read privileges.
- Signature: `ExecuteSearch(sessionToken: String, searchOptions: String, pageNumber: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `searchOptions` (String): XML string that provides the search criteria. Note: For details about constructing this string, see XML Formatting Guidelines for 5.x Search Input .
  - `pageNumber` (Integer): Integer of the page (1,2,3,...,n) of search results to return
- Output: This method returns a string. The value is an XML string containing the fields of records matching the search criteria.

### search.ExecuteStatisticSearch  (ok)
The ExecuteStatisticSearch method runs a statistics search according to custom criteria.
- Privileges: This method requires Read privileges.
- Signature: `ExecuteStatisticSearch(sessionToken: String, searchOptions: String, pageNumber: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `searchOptions` (String): XML string that provides the search criteria Note: For details about constructing this string, see XML Formatting Guidelines for Search Input .
  - `pageNumber` (Integer): Integer of the page (1,2,3,...,n) of search results to return.
- Output: This method returns a string. The value is an XML string containing the fields of records matching the statistics search criteria.

### search.ExecuteStatisticSearchByReport  (ok)
The ExecuteStatisticSearchByReport method runs a statistics search according to custom criteria.
- Privileges: This method requires Read privileges.
- Signature: `ExecuteStatisticSearchByReport(sessionToken: String, reportIdOrGuid: String, pageNumber: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `reportIdOrGuid` (String): Internal ID or GUID of the report whose records you want to query
  - `pageNumber` (Integer): Integer of the page (1,2,3,...,n) of search results to return
- Output: This method returns a string. The value is an XML string containing the fields of records matching the statistics search criteria.

### search.GetReports  (ok)
The GetReports method returns all reports and their associated report GUIDs that the user making the API call has permissions to.
- Privileges: This method requires Read privileges.
- Signature: `GetReports(sessionToken: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
- Output: This method returns a string. The value is an XML string containing the information from the reports and their corresponding GUIDs.

### search.GetSearchOptions  (ok)
The GetSearchOptions method returns a search string based upon the criteria entered. The returned search string can then be used by search.ExecuteSearch .
- Privileges: This method requires Read privileges.
- Signature: `GetSearchOptions(sessionToken: String, searchReportId: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `searchReportId` (Integer): The ID number of the report for which you are searching. Important: Statistics reports are not supported.
- Output: This method returns a string. The value is an XML string that can be used as the searchOptions parameter in search.ExecuteSearch . If there is an error, the returned value will either be “NULL”, or an empty string.

### search.GetSearchOptionsByGuid  (ok)
The GetSearchOptionsByGuid method returns a search string based upon the criteria entered. The returned search string can then be used by search.ExecuteSearch .
- Privileges: This method requires Read privileges.
- Signature: `GetSearchOptionsByGuid(sessionToken: String, searchReportGuid: String)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method.
  - `searchReportGuid` (String): The GUID of the report for which you are searching. Important: Statistics reports are not supported. Note: You can use search.GetReports to find a specific report GUID.
- Output: This method returns a string. The value is an XML string that can be used as the searchOptions parameter in search.ExecuteSearch . If there is an error, the returned value will either be “NULL” or an empty string.

### search.SearchRecordsByReport  (ok)
The SearchRecordsByReport method runs a search of records according to the specified report ID or report GUID.
- Privileges: This method requires Read privileges.
- Signature: `SearchRecordsByReport(sessionToken: String, reportIdOrGuid: String, pageNumber: Integer)`
- Parameters:
  - `sessionToken` (String): Valid sessionToken returned by the general.CreateUserSession method
  - `reportIdOrGuid` (String): Internal ID or GUID of the report whose records you want to query
  - `pageNumber` (Integer): Integer of the page (1,2,3,…,n) of search results to return
- Output: This method returns a string. The value is an XML string containing the fields of records matching the report ID or GUID.
