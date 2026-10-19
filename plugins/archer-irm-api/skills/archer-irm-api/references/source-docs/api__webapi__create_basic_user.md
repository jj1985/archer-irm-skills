# Create and Update a Basic User

The following C# code sample creates a user, changes the username, adds an email address, adds the user to a group, and assigns the user a role.

iUserID = access.CreateUserEx(sSessionToken, "First", "Middle", "Last",   
"Company", "Title", 2, "Address", "", "Central Standard Time", "en-US");

iReturnCode = access.ForcePasswordChange(sSessionToken, iUserID, false);

iReturnCode = access.ChangePassword(sSessionToken, iUserID, "NewPassword");

iReturnCode = access.AddUserToRole(sSessionToken, iUserID, 3);

iReturnCode = access.AddUserToGroup(sSessionToken, iUserID, 3);

iReturnCode = access.UpdateUserName(sSessionToken, iUserID, "LoginName");

sXML = "<ContactInfo><ContactTypeId>7</ContactTypeId>  
<ContactSubTypeId>2</ContactSubTypeId><ContactInfo>email@archerirm.com  
</ContactInfo></ContactInfo>";

iReturnCode = access.AddContactInfo(sSessionToken, iUserID, sXML);
