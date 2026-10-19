# Using the RESTful API

On this page

  * Components of a RESTful API Call
  * Determine Application GUIDs (RESTful)
  * Determine System IDs (RESTful)
  * Updating Locked Records (RESTful)

## Components of a RESTful API Call

The Archer RESTful API can be used in a number of ways. An example is to use a text editing tool like Notepad to create a header and a wrapper. 

The following table describes the various components of a RESTful API call within Archer. Component |  Description |  Sample Code  
---|---|---  
Call the API |  Sets an HTTP Request. |  Sub CallTheArcherAPIFromVBS() End Sub  
Library |  Uses HTTP by using a library. |  Set MyRequest = CreateObject(”winHttp.WinHttpRequest.5.1”)  
Proxy |  Tells the call where to send the HTTP Request to. |  MyRequest.setProxy 2, “staging:8888”  
Request |  Opens a request to send an API call to the server. |  MyRequest.Open “POST”, “http://staging/archer/platformapi/core/security/login”  
Header |  Tells the server what to do with the API call once it is received. |  MyRequest.setRequestHeader “Accept”, “application/json,text/html,application/xhtml  
+xml,application/xml;q=0.9,*/*;q=0.8”  
MyRequest.setRequestHeader “Content-Type”, “application/json”  
Body |  The contents of the API call. |  requestBody =  
“{””InstanceName””:””Archer1,””Username””:””sysadmin””,””UserDomain””:”””,””Password””:””Archer2005””}” requestBody =  
“{””InstanceName””:””<instance>,””Username””:””<username>””,””UserDomain””:”””,””Password””:””<password>””}”  
Submission |  A call to submit the body to the server. |  MyRequest.send requestBody  
Response |  Presenting the output from the server. |  Response = MyRequest.ResponseText  
token = Mid(Response, 48, 32) MsgBox token  
  
**Example:**

This particular sample finds the session token that the sysadmin user used to log in to the Archer session.

CallTheRestAPIFromVBS

Sub CallTheArcherAPIFromVBS()

Set MyRequest = CreateObject(WinHttp.WinHttpRequest.5.1”)

MyRequest.setProxy 2, “staging:8888”

MyRequest.Open “POST”, “http://staging/archer/platformapi/core/security/login”

MyRequest.setRequestHeader “Accept”, “application/json,text/html,application/xhtml  
+xml,application/xml;q=0.9,*/*;q=0.8”  
MyRequest.setRequestHeader “Content-Type”, “application/json”

requestBody =  
“{””InstanceName””:””<instance>,””Username””:””<username>””,””UserDomain””:”””,””Password””:””<password>””}”

MyRequest.send requestBody

Response = MyRequest.ResponseText  
token = Mid(Response, 48, 32)

MsgBox token

End Sub

## Determine Application GUIDs (RESTful)

Some methods require an application Globally Unique Identifier (GUID) as a parameter. 

Determine the application GUID  

  1. Go to the Manage Applications page.

     1. From the menu, click .
     2. Under Application Builder, click Applications. 
  2. In the Applications section, click the name of the application for which you want the GUID. 
  3. In the General Information section, the ID field contains the application GUID.

## Determine System IDs (RESTful)

Some methods require a system ID as a parameter. Use the following procedure to find a Field ID, Application IDs, and Values List IDs.

Determine system IDs  

  1. Go to the Manage Applications page.

     1. From the menu, click .
     2. Under Application Builder, click Applications. 
  2. In the Applications section, click the name of the application that contains the field for which you want the ID. 
  3. Click the Fields tab. 
  4. In the Fields section, hover over the name of the appropriate field. 

The ID of the field displays in the bottom of the Manage Applications window.

## Updating Locked Records (RESTful)

Archer has an important feature that prevents the updating or altering of a locked record. A record becomes locked when a user has opened it in Edit mode for the purpose of modifying it.

However, it is important to note that records can be updated through the RESTful and Web APIs, as well as through data feeds, even when a user has locked them. The following are examples of typical APIs that can update user-locked records:

  * PUT content (RESTful )
  * UpdateRecord (Web Services)
  * UpdateRecords (Web Services)

