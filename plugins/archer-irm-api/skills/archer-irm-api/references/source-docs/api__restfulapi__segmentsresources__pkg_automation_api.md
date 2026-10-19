# Configure API Calls for Package Automation

To automate package creation, generation, upload, download, and installation, configure REST API calls similar to the examples below. The example code shows generic variables in italics, such as _ExampleSessionID_ , _ExampleDescription_ , and _ExampleGuid_. When you configure the API calls for your deployment, replace the variables with information specific to your environment and the task you want to automate.

For create, generate, and install API requests, copy the code generated from the Manage Packages page or the Import and Install Packages page in the user interface, which contains package-specific data in place of the example variables. For more information, see Automate Generation and Installation of Packages.

On this page

  * Create Package
    * Request Example
    * Request Header Example
    * Request Body Example
    * Response Example
  * Generate Package
    * Request Example
    * Request Header Example
    * Request Body Example
    * Response Example
  * Install Package
    * Request Example
    * Request Header Example
    * Request Body Example
    * Response Example
  * Upload Package
    * Request Example
    * Request Header Example
    * Request Body Example
    * Response Example
  * Download Package
    * Request Example
    * Request Header Example
    * Request Body Example
    * Response Example

## Create Package

To create a new package, configure an API call similar to the following example.

### Request Example

POST http://_ExampleWebServerIP_ /_ExampleArcherInstanceName_ /api/core/package/

### Request Header Example

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id=_ExampleSessionID_

Content-Type: application/json

Host: localhost

Content-Length: 0

### Request Body Example

{"Name":"_ExampleName_ ","Description":"_ExampleDescription_ ","PreparedBy":"_ExamplePreparedByText_ ","PackageObjects": [{"Guid":"_ExampleGuid1_ ","Type":"Application"},{"Guid":"_ExampleGuid2_ ","Type":"Application"}]

### Response Example

{  
"Links": [],  
"RequestedObject": {"Id": _ExampleID_},  
"IsSuccessful": true,  
"ValidationMessages": []  
}

## Generate Package

To generate a package, configure an API similar to the following example.

### Request Example

POST http://_ExampleWebServerIP_ /_ExampleArcherInstanceName_ /api/core/package/generate/_ExamplePackageID_

### Request Header Example

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id=_ExampleSessionID_

Content-Type: application/json

Host: localhost

Content-Length: 0

### Request Body Example

Not required.

### Response Example

{  
"Links": [],  
"RequestedObject": {},  
"IsSuccessful": true,  
"ValidationMessages": null  
}

## Install Package

To install a package, configure an API call similar to the following example.

### Request Example

POST http://_ExampleWebServerIP_ /_ExampleArcherInstanceName_ /api/core/package/install

{"PackageId":_ExamplePackageID_ ,"InactivateUnusedFields":false,"PrefixInactivatedFields":null,"InstallOptions":[

{"Guid":"_ExampleGuid1_ ","Name":"_ExampleName1_ ","Type":"Application","TranslationOption":1,"InstallMethod":2,"InstallOption":1},

{"Guid":"_ExampleGuid2_ ","Name":"_ExampleName2_ ","Type":"Application","TranslationOption":1,"InstallMethod":2,"InstallOption":1},

{"Guid":"_ExampleGuid3_ ","Name":"_ExampleName3_ ","Type":"GlobalReport","TranslationOption":1,"InstallMethod":2,"InstallOption":1},

{"Guid":"_ExampleGuid4_ ","Name":"_ExampleName4_ ","Type":"GlobalReport","TranslationOption":1,"InstallMethod":2,"InstallOption":1},

{"Guid":"_ExampleGuid5_ ","Name":"_ExampleName5_ ","Type":"SubForm","TranslationOption":1,"InstallMethod":2,"InstallOption":1}]}

### Request Header Example

Accept: application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id=_ExampleSessionID_

Content-Type: application/json

Host: localhost

Content-Length: 0

### Request Body Example

{"Name":"_ExampleName_ ","Description":"_ExampleDescription_ ","PreparedBy":"_ExamplePreparedByText_ ", "PackageObjects":[{"Guid":"_ExampleGuid6_ ","Type":"Application"}, {"Guid":"_ExampleGuid7_ ","Type":"Application"}]

### Response Example

{  
"Links": [],  
"RequestedObject": {},  
"IsSuccessful": true,  
"ValidationMessages": null  
}

## Upload Package

To upload a package, configure an API call similar to the following example.

### Request Example

POST http://_ExampleWebServerIP_ /_ExampleArcherInstanceName_ /api/core/package/upload

### Request Header Example

Content-Type: multipart/form-data; boundary=-------------------------acebdf13572468

Accept: application/zip,application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Authorization: Archer session-id=_ExampleSessionID_

Host: localhost

Content-Length: 2491925

### Request Body Example

\---------------------------acebdf13572468

Content-Disposition: form-data; name="_ExampleFieldName_ "; filename="_ExamplePackageName_.zip"

Content-Type: application/zip

<\--_ExampleFileBytes_ \-->

\---------------------------acebdf13572468--

### Response Example

{

"Links":[],

"RequestedObject":{"Id":_ExamplePackageID_},

"IsSuccessful":true,

"ValidationMessages":[]

}

## Download Package

To download a package, configure an API call similar to the following example.

### Request Example

GET http://_ExampleWebServerIP_ /_ExampleArcherInstanceName_ /api/core/package/download/_ExamplePackageID_

### Request Header Example

Content-Type: application/zip

Authorization: Archer session-id=_ExampleSessionID_

### Request Body Example

Not Required.

### Response Example

Response contains the requested package file.
