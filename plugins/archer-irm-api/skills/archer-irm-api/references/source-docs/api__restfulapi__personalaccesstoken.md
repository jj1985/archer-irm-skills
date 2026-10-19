# Personal Access Token RESTful API

## Personal Access Token Overview

Personal Access Tokens (PATs) provide a secure alternative user authentication process to traditional username and password methods.

The following table describes available API commands: Resource |  URL  
---|---  
Create PAT |  /api/V2/PersonalAccessToken/Create HTTP Verb: POST  
Revoke PAT |  /api/V2/PersonalAccessToken(<PATId>) HTTP Verb: DELETE  
Rotate PAT |  /api/V2/PersonalAccessToken(<PATId>)/Rotate HTTP Verb: POST  
Self-Rotate PAT |  /api/V2/PersonalAccessToken/SelfRotate HTTP Verb: POST  
Get PATs for a User |  /api/V2/PersonalAccessToken HTTP Verb: GET  
  
## Create Personal Access Token

Generates a new Personal Access Token for a specified user. Administrators can create tokens for any user. Non-administrators can only create their own tokens.

Request

POST /api/V2/PersonalAccessToken/Create

Request Header 

Content-Type: application/json

Authorization: Archer session-id="<SessionToken>"

Request Body Example

  * [Request Body](segmentsresources/pat_ex/pat_ex_add_connect_req_body.txt)

This example body has the following inputs: Properties | Data Type | Required |  Description  
---|---|---|---  
UserId |  Integer |  Yes |  The ID of the user for whom the PAT is being created.  
Name |  String |  Yes |  A descriptive name for the PAT.  
Description |  String |  No |  An optional description for the PAT.  
ExpirationDate |  String |  Yes |  The expiration date for the PAT, formatted as yyyy-MM-dd. Must be a future date, at least 1 day from the current date and no more than one year from the current date.  
  
Response Examples

  * [Successful](segmentsresources/pat_ex/pat_ex_text_success.txt "Successful")

## Revoke Personal Access Token

Revokes an existing Personal Access Token identified by its unique ID.

Request

DELETE /api/V2/PersonalAccessToken(<PATId>)

Request Header 

Content-Type: application/json

Authorization: Archer session-id="<SessionToken>"

This example has the following inputs: Properties | Data Type | Required |  Description  
---|---|---|---  
PATId |  Integer |  Yes |  The ID of the PAT to be revoked.  
  
Return Value

HTTP/1.1 200 OK

## Rotate Personal Access Token

Revokes an existing token and creates a new token assigned to the same user.

This operation is similar to Self-Rotate, but uses a token ID instead of the authenticated session.

Request

POST /api/V2/PersonalAccessToken(<PATId>)/Rotate

Request Header 

Content-Type: application/json

Authorization: Archer session-id="<SessionToken>" or "<PAT>"

Request Parameters (Body)

  * [Request Body (optional)](segmentsresources/pat_ex/pat_ex_new_exp_date_body.txt)

**Important:** It can be empty or contain an ExpirationDate.

This example body has the following inputs: Properties | Data Type | Required |  Description  
---|---|---|---  
PATId |  Integer |  Yes |  The ID of the Personal Access Token to be rotated.  
ExpirationDate |  String |  Yes |  The expiration date for the PAT, formatted as yyyy-MM-dd. Must be a future date, at least 1 day from the current date and no more than one year from the current date.  
  
Return Value

  * [Successful](segmentsresources/pat_ex/pat_ex_rotate_test_success.txt)

## Self-Rotate Personal Access Token

Rotates the Personal Access Token currently in use for authentication, creating a new token while revoking an existing one.

Request

POST /api/V2/PersonalAccessToken/SelfRotate

Request Header 

Content-Type: application/json

Authorization: Archer session-id="<PAT_To_Rotate>"

Request Parameters (Body)

  * [Request Body](segmentsresources/pat_ex/pat_ex_selfrotate_body.txt)

This example body has the following inputs: Properties | Data Type | Required |  Description  
---|---|---|---  
(Optional)ExpirationDate |  String |  No | The expiration date for the PAT, formatted as yyyy-MM-dd. If no new date is set, the token keeps the old expiry or takes the default one. The expiry should be within 1 day to 1 year from today.   
  
Return Value

  * [Successful](segmentsresources/pat_ex/pat_ex_selfrotate_success.txt)

## Get Personal Access Tokens for a User

Returns a list of all active Personal Access Tokens associated with a specified user.

Request

GET /api/V2/PersonalAccessToken?userId="<Integer>"

Request Header 

Content-Type: application/json

Authorization: Archer session-id="<SessionToken>"

This example has the following inputs: Properties | Data Type | Required |  Description  
---|---|---|---  
UserId |  Integer |  Yes |  The ID of the user whose PATs are to be retrieved.  
  
Return Value

  * [Successful](segmentsresources/pat_ex/pat_ex_getpat_success.txt)

