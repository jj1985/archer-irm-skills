# Components of a RESTful API Call

The Archer RESTful API can be used in a number of ways. An example is to use a text editing tool like Notepad to create a header and a wrapper. 

The following table describes the various components of a RESTful API call within Archer. Component |  Description |  Sample Code  
---|---|---  
Call the API |  Sets an HTTP Request. |  Sub CallTheArcherAPIFromVBS() End Sub  
Library |  Uses HTTP by using a library. |  Set MyRequest = CreateObject(”winHttp.WinHttpRequest.5.1”)  
Proxy |  Tells the call where to send the HTTP Request to. |  MyRequest.setProxy 2, “127.0.0.1:8888”  
Request |  Opens a request to send an API call to the server. |  MyRequest.Open “POST”, “http://123.1.123.10/archer/platformapi/core/security/login”  
Header |  Tells the server what to do with the API call once it is received. |  MyRequest.setRequestHeader “Accept”, “application/json,text/html,application/xhtml  
+xml,application/xml;q=0.9,*/*;q=0.8”  
MyRequest.setRequestHeader “Content-Type”, “application/json”  
Body |  The contents of the API call. |  requestBody =  
“{””InstanceName””:””Archer1,””Username””:””sysadmin””,””UserDomain””:”””,””Password””:””Archer2005””}”  
Submission |  A call to submit the body to the server. |  MyRequest.send requestBody  
Response |  Presenting the output from the server. |  Response = MyRequest.ResponseText  
token = Mid(Response, 48, 32) MsgBox token  
  
**Example:**

This particular sample finds the session token that the sysadmin user used to log in to the Archer session.

CallTheRestAPIFromVBS

Sub CallTheArcherAPIFromVBS()

Set MyRequest = CreateObject(WinHttp.WinHttpRequest.5.1”)

MyRequest.setProxy 2, “127.0.0.1:8888”

MyRequest.Open “POST”, “http://123.1.123.10/archer/platformapi/core/security/login”

MyRequest.setRequestHeader “Accept”, “application/json,text/html,application/xhtml  
+xml,application/xml;q=0.9,*/*;q=0.8”  
MyRequest.setRequestHeader “Content-Type”, “application/json”

requestBody =  
“{””InstanceName””:””Archer1,””Username””:””sysadmin””,””UserDomain””:”””,””Password””:””Archer2005””}”

MyRequest.send requestBody

Response = MyRequest.ResponseText  
token = Mid(Response, 48, 32)

MsgBox token

End Sub
