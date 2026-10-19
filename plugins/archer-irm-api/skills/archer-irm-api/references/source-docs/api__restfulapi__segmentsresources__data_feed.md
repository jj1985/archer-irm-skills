# Data Feed

The Data Feed segment is accessed through the Data Feed controller. Actions taken on a resource determine the type of action that can be performed. 

On this page

  * Execute Data Feed
    * Request
    * Request Header
    * Request Body
  * Get History Message for a History
    * Request
    * Request Header
  * Get Recent Run Detail for a Data Feed
    * Request
    * Request Header
    * Request Body
  * Get Run History for a Data Feed
    * Request
    * Request Header
    * Request Body

The following table describes which actions can be taken on the content all resource.  Resource |  URI |  $filter |  $select |  $top |  $skip |  $orderby  
---|---|---|---|---|---|---  
Execute Data Feed |  /datafeed/executedatafeed |  |  |  |  |   
Get History Message for History |  /datafeed/historymessage/historyId |  |  |  |  |   
Get Recent Run Detail |  /datafeed/getrecentrundetail |  |  |  |  |   
Get Run History |  /datafeed/history |  |  |  |  |   
  
## Execute Data Feed

The Execute Data Feed resource runs a data feed and any data feeds that may be referenced. The IsReferenceFeedsIncludedflag must be true before any referenced data feeds can run. If you want to run a single data feed without any referenced feeds, the flag must be set to false. The session token ID must be for a user who has access rights to run data feeds.

### Request

POST http://Archer/platformapi/core/datafeed/execution

### Request Header

Accept:application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

### Request Body

{"DataFeedGuid":"4685367E-E76E-4580-BDEC-83E98FF48A50","IsReferenceFeedsIncluded":false}

## Get History Message for a History

The Get History Message for a History resource retrieves a history message for a specific history ID.

### Request

POST http://Archer/platformapi/core/datafeed/historymessage/historyId

### Request Header

Accept:application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

## Get Recent Run Detail for a Data Feed

The Get Recent Run Detail for a Data Feed resource retrieves history information for the most recent data feed, including execution time, number of records created, updated or deleted, status, and whether the feed succeeded or failed.

The following table lists the data feed status codes that can appear in the request response and their corresponding definitions. Data Feed Status Code | Definition  
---|---  
1 |  Running  
2 |  Completed  
3 |  Faulted  
4 |  Warning  
5 |  Terminating  
6 |  Terminated  
7 |  Pending  
  
### Request

POST http://Archer/platformapi/core/datafeed/history/recent

### Request Header

Accept:application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

### Request Body

{"Guid":"4685367E-E76E-4580-BDEC-83E98FF48A50"}

## Get Run History for a Data Feed

The Get Run History for a Data Feed resource retrieves history information for a data feed, including execution time, number of records created, updated or deleted, status, and whether the feed succeeded or failed.

### Request

POST http://Archer/platformapi/core/datafeed/history

### Request Header

Accept:application/json,text/html,application/xhtml+xml,application/xml;q=.9,*/*;q=0.8

Authorization: Archer session-id="session token ID from login"

Content-Type: application/json

X-Http-Method-Override: GET

### Request Body

{"Guid":"4685367E-E76E-4580-BDEC-83E98FF48A50"}
