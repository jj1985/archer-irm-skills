# Configure Data Gateway Connections (RESTful API)

On this page

  * Data Gateway Overview
  * Get Connections
  * Add Connection
  * Edit Connection
  * Test Connection
  * Delete Connections
  * Get Field Maps
  * Add or Edit Field Maps
  * Revert Field Maps
  * Get Content Maps
  * Add or Edit Content Maps
  * Delete Content Maps by Connection and Content ID
  * Delete Content Map by Connection

## Data Gateway Overview

Data gateway enables Archer to connect to and interact with external data sets. By providing real-time visibility into external data sets, your organization can leverage Archer to analyze and understand risks that occur in large amounts of data. Data feeds copy information into an Archer database, while data gateway maps information from an external system directly to records within Archer applications. This allows you to use Archer to view and make real time edits to that external data. For example, you can sort through large amounts of vulnerability scan results to quickly identify the highest risk scans without wasting time duplicating the data or overflowing Archer database servers.

The data gateway API allows you to manage your connections and data through a data gateway connector. The following section details those commands and provides examples assuming the use of the Flexible SQL Connector is available out of the box. For more information about the Flexible SQL Connector, see Using the Flexible SQL Connector. The inputs to these commands vary depending upon your connector. For more information about how to code your own connector, see Creating a Data Gateway Connector.

Use the data pulled through data gateway in any application or questionnaire, including applications with multiple levels. For example, you may have an application with 2 levels that draws data from 2 different external data sets. You can accomplish this with 2 data gateway connections, 1 for each level, where the input property targetId identifies the level. For more information about leveled applications, see Applications.

The following table describes which actions are available: Resource |  URL |  $filter |  $select |  $top |  $skip |  $orderby  
---|---|---|---|---|---|---  
Get Connections |  /DataGateway/Connections  HTTP Verb: GET |  |  |  |  |   
Add Connection |  /DataGateway/Connections  HTTP Verb: POST |  |  |  |  |   
Edit Connection |  /DataGateway/Connections HTTP Verb: PUT |  |  |  |  |   
Test Connection |  /DataGateway/Connections/Test HTTP Verb: POST |  |  |  |  |   
Delete Connections |  /DataGateway/Connections HTTP Verb: DELETE |  |  |  |  |   
Get Field Maps |  /DataGateway/FieldMaps HTTP Verb: GET |  |  |  |  |   
Add or Edit Field Maps |  /DataGateway/FieldMaps HTTP Verb: PUT or POST |  |  |  |  |   
Revert Field Maps |  /DataGateway/FieldMaps HTTP Verb: PUT or POST |  |  |  |  |   
Get Content Maps |  /DataGateway/ContentMaps/?connection=*locationAlias* HTTP Verb: GET |  |  |  |  |   
Add or Edit Content Maps |  /DataGateway/ContentMaps HTTP Verb: PUT or POST |  |  |  |  |   
Delete Content Maps by Connection and Content ID |  /DataGateway/ContentMaps/Delete HTTP Verb: DELETE |  |  |  |  |   
Delete Content Maps by Connection |  /DataGateway/ContentMaps/DeleteAll/?connection=*locationAlias* HTTP Verb: DELETE |  |  |  |  |   
  
**Note:** All input property names are case insensitive. The input property values are case sensitive. 

## Get Connections

A data gateway connection provides a connection from an external system to Archer. This section explains how to get a listing of all connections currently available. The session token must be for a user who has access rights to data gateway.

Request

GET http://Archer/platformapi/DataGateway/Connections

GET http://Archer/platformapi/DataGateway/Connections?$filter=targetId%20eq%20530

**Note:** Use a filter to find a specific connection. See above for an example. This request returns the connection with a targetId of 530 and filters all other connections.

Request Header

Authorization: Archer session-id=*session token*

Request Body Example

This command does not require a specific body. However, you can use $filter to return information on a specific targetId. 

Response Examples

  * [Successful](dg_ex/dg_ex_get_connect_res_success.txt "Successful")
  * [Unsuccessful due to data gateway not enabled](dg_ex/dg_ex_get_connect_res_notsucc_dg_disabled.txt "Unsuccessful due to data gateway not enabled")
    * **Note:** This example indicates that the data gateway requires enabling in the Archer Control Panel. For more information, see "Configuring an Instance for Using Data Gateway" in the [Archer Control Panel Help](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/platform_home.htm).

  * [Unsuccessful due to lack of permissions](dg_ex/dg_ex_get_connect_res_notsucc_no_perm.txt "Unsuccessful due to lack of permissions")
    * **Note:** This example indicates that the user's access role requires permissions to manipulate data gateway connections. For more information, see [Metadata Role](user_mgt/user_mgt_role.htm). 

## Add Connection

A data gateway connection provides a connection from an external system to Archer. This section explains how to add a new connection. The session token must be for a user who has access rights to data gateway.

Request

POST http://Archer/platformapi/DataGateway/Connections

Request Header 

Content-Type: application/json

Authorization: Archer session-id=*session token*

Request Body Example

  * [Add Connection Request Body](dg_ex/dg_ex_add_connect_req_body.txt "Add Connection Request Body")

This example body has the following inputs: Properties | Data Type |  Description  
---|---|---  
TargetId |  Integer |  Indicates the level of the application to add the new external connection.  
LocationAlias |  Character String Limit of 10 characters |  Indicates the name of the connector.  
  
This example body also uses the inputs of the Flexible SQL Connector. For more information, see Using the Flexible SQL Connector.

Response Example

  * [Add Connection Response](dg_ex/dg_ex_add_connect_res.txt "Add Connection Response")

## Edit Connection

A data gateway connection provides a connection from an external system to Archer. This section explains how to edit an existing connection. The session token must be for a user who has access rights to data gateway.

Request

PUT http://Archer/platformapi/DataGateway/Connections

Request Header

Content-Type: application/json

Authorization: Archer session-id=*session token*

Request Body Example

Edit connection uses the same request body as add connection with 1 addition, Connection ID. This property identifies the connection to be updated.

In addition, edit connection ignores references to the locationAlias and targetId properties in the request body. Otherwise, edit connection updates all other properties.

  * [Edit Connection Request Body](dg_ex/dg_ex_edit_connect_req_body.txt "Edit Connection Request Body")

Response Example

Responses to edit connection are the same as those for add connection.

## Test Connection

A data gateway connection links an external system to Archer. This explains how to test the linkage through your chosen connector. The Flexible SQL Connector supports this functionality. To use test connection with your connector, your connector must include the test connection functionality. For more information, see Creating a Data Gateway Connector. The session token must be for a user who has access rights to data gateway.

Request

POST http://Archer/platformapi/DataGateway/Connections/Test

Request Header

Content-Type: application/json

Authorization: Archer session-id=*session token*

Request Body Example

[Test Connection Body](dg_ex/dg_ex_test_body.txt)

Response Examples

  * [Successful](dg_ex/dg_ex_test_success.txt "Successful")
  * [Unsuccessful test](dg_ex/dg_ex_test_failed.txt). No connection established. The test failed. Check your connection properties and try again.
  * [Unsuccessful due to connector not configured to support test connection functionality](dg_ex/dg_ex_test_notsupported.txt)

Update your connector to include the test connection functionality. For more information, see [Creating a Data Gateway Connector](../../../Platform/Integration/int_dg_connector_creating.htm). 

  * [Unsuccessful due to data gateway not enabled](dg_ex/dg_ex_test_notsucc_dg_not_enabled.txt "Unsuccessful due to data gateway not enabled")

**Note:** This example indicates that the data gateway requires enabling in the Archer Control Panel. For more information, see "Configuring an Instance for Using Data Gateway" in the [Archer Control Panel Help](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/platform_home.htm). 

## Delete Connections

A data gateway connection provides a connection from an external system to Archer. This section explains how to remove an existing connection. This command removes the connection, resets all field maps, and content maps associated with it. Those Archer fields affected by command are left blank. The session token must be for a user who has access rights to data gateway.

Request

DELETE http://Archer/platformapi/DataGateway/Connections?connection=<LocationAlias>

Request Header

Authorization: Archer session-id=*session token*

Request Body Example

This command does not require a specific request body. 

Response Examples

  * [Successful](dg_ex/dg_ex_del_connect_res_success.txt "Successful")
  * [Unsuccessful due to invalid locationAlias](dg_ex/dg_ex_del_connect_res_notsucc_invalid_loc_alias.txt "Unsuccessful due to invalid locationAlias")
  * [Unsuccessful due to data gateway not enabled](dg_ex/dg_ex_del_connect_res_notsucc_dg_disabled.txt "Unsuccessful due to data gateway not enabled")
  * [Unsuccessful due to lack of permissions](dg_ex/dg_ex_del_connect_res_notsucc_no_perm.txt "Unsuccessful due to lack of permissions")

**Note:** This example indicates that the user's access role requires permissions to manipulate data gateway connections. For more information, see [Metadata Role](user_mgt/user_mgt_role.htm). 

## Get Field Maps

A data gateway connection provides a connection from an external system to Archer. This section explains the API command to get existing external source fields and where they map to Archer fields. The session token must be for a user who has access rights to data gateway. 

Request

GET http://Archer/platformapi/DataGateway/FieldMaps

GET http://Archer/platformapi/DataGateway/FieldMaps?$filter=DataGatewayFieldMaps/any(dgfm:dgfm/Connections/any(conn:conn/Name%20eq%20%27SQLCON1%27))

**Note:** Use a filter to find field maps for a specific connection. See above for an example. This request returns the field maps for the connection named SQLCON1 and filters all other connections.

GET http://Archer/platformapi/DataGateway/FieldMaps?$filter=DataGatewayFieldMaps/any(dgfm:dgfm/targetId%20eq%20335)

**Note:** Use a filter to find field maps for a specific level. See above for an example. This request returns the field maps for the level ID of 335 and filters all other connections.

GET http://Archer/platformapi/DataGateway/FieldMaps?$filter=DataGatewayFieldMaps/any(dgfm:dgfm/targetId%20eq%20335)%20and%20DataGatewayFieldMaps/any(dgfm:dgfm/Connections/any(conn:conn/Name%20eq%20%27SQLCON1%27))

**Note:** Use a filter to find field maps for a specific connection and level. See above for an example. This request returns the field maps for the level ID of 335 and connections named SQLCON1, while filtering all other connections.

Request Header

Authorization: Archer session-id=*session token*

Request Body Example

This command does not require a specific body. However, you can use $filter to return information. There are 2 variables, you can filter on these separately or combined:

  * ConnectionName. This filters on field maps associated with a specific connection.
  * TargetId. This filters on those field maps within a specific level.

Response Examples

  * [Successful](dg_ex/dg_ex_get_field_map_res_success.txt "Successful")
  * [Partially successful due to non-existent $filter value](dg_ex/dg_ex_get_field_map_res_part_success.txt "Partially successful due to non-existent $filter value")
  * [Unsuccessful due to data gateway not enabled](dg_ex/dg_ex_get_field_map_res_notsucc_dg_not_enabled.txt "Unsuccessful due to data gateway not enabled")
    * **Note:** This example indicates that the data gateway requires enabling in the Archer Control Panel. For more information, see "Configuring an Instance for Using Data Gateway" in the [Archer Control Panel Help](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/platform_home.htm).

  * [Unsuccessful due to lack of permissions](dg_ex/dg_ex_get_field_map_res_notsucc_no_perm.txt "Unsuccessful due to lack of permissions")
    * **Note:** This example indicates that the user's access role requires permissions to manipulate data gateway connections. For more information, see [Metadata Role](user_mgt/user_mgt_role.htm). 

## Add or Edit Field Maps

A data gateway connection provides a connection from an external system to Archer. This section explains the API command to map external source fields to Archer fields. The session token must be for a user who has access rights to data gateway. 

Request

PUT http://Archer/platformapi/DataGateway/FieldMaps

POST http://Archer/platformapi/DataGateway/FieldMaps

Request Header

Content-Type: application/json

Authorization: Archer session-id=*session token*

Request Body Example

  * [Add or Edit Field Maps Request Body](dg_ex/dg_ex_add_edit_field_map_req_body.txt "Add or Edit Field Maps Request Body")

This example body has the following inputs: Properties | Data Type |  Description  
---|---|---  
TargetId |  Integer |  Indicates the level of the application to add the new external connection.  
Name |  Character String Limit of 10 characters |  Indicates the name of the connector.  
SourceFieldId |  Character String Limit of 256 characters |  Represents the string required for locating the field within the external resource.  
ArcherFieldId |  Integer |  Indicates the Field ID within Archer.  
  
This command works, if the following is true: 

  * The targetId matches an existing level within the Archer application. 
  * The Connection matches the level for the given archerFieldId. 
  * The targetId of the archerFieldId matches targetId in the input.
  * Flexible SQL connectors support the following field types: Date, IpAddress, Numeric, or Text.
  * Custom connectors support the following field types:
    * Attachment
    * Date
    * ExternalLinks
    * Image
    * IpAddress 
    * Matrix
    * Numeric
    * RecordPermissions
    * Scheduler/Appointment
    * Scheduler
    * Text 
    * Users/Groups Lists
    * ValuesList
    * Voting
  * The connection name is a valid connection.

Response Examples

  * [Successful](dg_ex/dg_ex_add_edit_field_map_res_success.txt "Successful")
    * A successful response returns successfully processed Archer Field IDs.

  * [Partially successful](dg_ex/dg_ex_add_edit_field_map_res_part_success.txt "Partially successful")
    * A partially successful response returns successfully processed Archer Field IDs and Field IDs that failed to process properly. The header for this example provided an invalid connection, or some Field IDs not associated with that connection.

    * To solve this problem, verify the following:
      * TargetId matches a level within Archer.

      * The archerFieldIds exist within the given Archer application.
  * [Unsuccessful due to unsupported field type](dg_ex/dg_ex_add_edit_field_map_res_notsucc_nosupport_field_type.txt "Unsuccessful due to unsupported field type")
  * [Unsuccessful due to data gateway not enabled](dg_ex/dg_ex_add_edit_field_map_res_notsucc_dg_disabled.txt "Unsuccessful due to data gateway not enabled")
    * **Note:** This example indicates that the data gateway requires enabling in the Archer Control Panel. For more information, see "Configuring an Instance for Using Data Gateway" in the [Archer Control Panel Help](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/platform_home.htm).

  * [Unsuccessful due to lack of permissions](dg_ex/dg_ex_add_edit_field_map_res_notsucc_no_perm.txt "Unsuccessful due to lack of permissions")
    * **Note:** This example indicates that the user's access role requires permissions to manipulate data gateway connections. For more information, see [Metadata Role](user_mgt/user_mgt_role.htm). 

## Revert Field Maps

A data gateway connection provides a connection from an external system to Archer. During set up, you can map external source fields to Archer fields. This section explains the API command to revert those field maps back to their original state, a field map to the Archer database. The content within Archer remains unaffected. The session token must be for a user who has access rights to data gateway. 

Request

POST http://Archer/platformapi/DataGateway/FieldMaps

PUT http://Archer/platformapi/DataGateway/FieldMaps

**Note:** In most cases, PUT adds information, and POST updates information. However for this command, either command reverts the field maps to Archer maps.

Request Header

Content-Type: application/json

Authorization: Archer session-id=*session token*

Request Body Example

  * [Revert Field Maps Request Body](dg_ex/dg_ex_rev_field_map_req_body.txt "Revert Field Maps Request Body")

This command works, if the following is true: 

  * The targetId matches an existing level within the Archer application. 
  * The connection targetId matches targetId in the input.
  * The connection name is a valid connection.

Response Examples

  * [Successful](dg_ex/dg_ex_rev_field_map_res_success.txt "Successful")
  * [Partially successful due to invalid connection or non-existent field map](dg_ex/dg_ex_rev_field_map_part_success.txt "Partially successful due to invalid connection or non-existent field map")
  * [Unsuccessful due to invalid target ID or connection name](dg_ex/dg_ex_rev_field_map_res_notsucc_invalid_connect_name.txt "Unsuccessful due to invalid target ID or connection name")
  * [Unsuccessful due to data gateway not enabled](dg_ex/dg_ex_rev_field_map_res_notsucc_dg_disabled.txt "Unsuccessful due to data gateway not enabled")
    * **Note:** This example indicates that the data gateway requires enabling in the Archer Control Panel. For more information, see "Configuring an Instance for Using Data Gateway" in the [Archer Control Panel Help](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/platform_home.htm).

  * [Unsuccessful due to lack of permissions](dg_ex/dg_ex_rev_field_map_res_notsucc_no_perm.txt "Unsuccessful due to lack of permissions")
    * **Note:** The previous example indicates that the user's access role requires permissions to manipulate data gateway connections. For more information, see [Metadata Role](user_mgt/user_mgt_role.htm). 

## Get Content Maps

A data gateway connection provides a connection from an external system to Archer. This section explains the API command to retrieve external source content mapped to content within Archer. The session token must be for a user who has access rights to data gateway.

Request

GET http://Archer/platformapi/DataGateway/ContentMaps/?connection=*locationAlias* 

GET http://Archer/platformapi/DataGateway/ContentMaps/?connection=*locationAlias*&$top=50&$skip=100

**Note:** The last example displays 50 content maps starting with the 101st content map. 

Request Header

Authorization: Archer session-id=*session token*

Request Body Example

While this command does not require a distinct body, it does require a variable in the link. LocationAlias, a string of up to 10 characters, indicates the name of the connector.

By default, this command returns the first 100 content maps available for the given connector. 

Other available parameters are:

  * $top: sets the number of content maps returned for the current request. The maximum value is 1000. 
  * $skip: begins displaying at the specified number of content maps. The default value is 0.

For more information on how these commands work, see[ Open Data Protocol (OData).](../odata.htm)

Response Examples

  * [Successful](dg_ex/dg_ex_get_content_map_res_success.txt "Successful")
  * [Unsuccessful due to invalid connection name](dg_ex/dg_ex_get_content_map_res_notsucc_invalid_connect_name.txt "Unsuccessful due to invalid connection name")
  * [Unsuccessful due to data gateway not enabled](dg_ex/dg_ex_get_content_map_res_notsucc_dg_disabled.txt "Unsuccessful due to data gateway not enabled")
    * **Note:** This example indicates that the data gateway requires enabling in the Archer Control Panel. For more information, see "Configuring an Instance for Using Data Gateway" in the [Archer Control Panel Help](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/platform_home.htm). 

  * [Unsuccessful due to lack of permissions](dg_ex/dg_ex_get_content_map_res_notsucc_no_perm.txt "Unsuccessful due to lack of permissions")
    * **Note:** This example indicates that the user's access role requires permissions to manipulate data gateway connections. For more information, see [Metadata Role](user_mgt/user_mgt_role.htm). 

## Add or Edit Content Maps

A data gateway connection provides a connection from an external system to Archer. This section explains the API command to map external source content within the fields to content within Archer fields. The session token must be for a user who has access rights to data gateway.

Request

PUT http://Archer/platformapi/DataGateway/ContentMaps

POST http://Archer/platformapi/DataGateway/ContentMaps

Request Header

Content-Type: application/json

Authorization: Archer session-id=*session token*

Request Body Example

  * [Add or Edit Content Maps Request Body](dg_ex/dg_ex_add_edit_content_map_req_body.txt "Add or Edit Content Maps Request Body")

This example body has the following inputs: Properties | Data Type |  Description  
---|---|---  
TargetId |  Integer |  Indicates the level of the application to add the new external connection  
LocationAlias |  Character String Limit of 10 characters |  Indicates the name of the connector  
ContentMaps |  |  Lists all the content to map with this command  
TrackingId |  Integer |  Indicates the Archer ContentId  
ContentPartId |  Character String Limit of 100 characters |  Indicates a unique identifier for content from the external system  
  
This command works, if trackingId and locationAlias are on the same level as indicated by the targetId. 

Response Examples

  * [Successful](dg_ex/dg_ex_add_edit_content_map_res_success.txt "Successful")
  * [Partially successful](dg_ex/dg_ex_add_edit_content_map_res_part_success.txt "Partially successful")
  * [Unsuccessful due to invalid locationAlias for indicated level](dg_ex/dg_ex_add_edit_content_map_res_notsucc_invalid_loc_alias.txt "Unsuccessful due to invalid LocationAlias for indicated level")
  * [Unsuccessful due to invalid trackingId for indicated level](dg_ex/dg_ex_add_edit_content_map_res_notsucc_invalid_track_id.txt "Unsuccessful due to invalid TrackingID for indicated level")
  * [Unsuccessful due to data gateway not enabled](dg_ex/dg_ex_add_edit_content_map_res_notsucc_dg_disabled.txt "Unsuccessful due to data gateway not enabled")
    * **Note:** The previous example indicates that the data gateway requires enabling in the Archer Control Panel. For more information, see "Configuring an Instance for Using Data Gateway" in the [Archer Control Panel Help](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/platform_home.htm). 

  * [Unsuccessful due to lack of permissions](dg_ex/dg_ex_add_edit_content_map_res_notsucc_no_perm.txt "Unsuccessful due to lack of permissions")
    * **Note:** The previous example indicates that the user's access role requires permissions to manipulate data gateway connections. For more information, see [Metadata Role](user_mgt/user_mgt_role.htm). 

## Delete Content Maps by Connection and Content ID

A data gateway connection provides a connection from an external system to Archer. During set up, you can map external source content to Archer content. This section explains the API command to remove this map by connection and content ID. The content within Archer fields becomes blank. The session token must be for a user who has access rights to data gateway.

Request

DELETE http://Archer/platformapi/DataGateway/ContentMaps/Delete

Request Header

Content-Type: application/json

Authorization: Archer session-id=*session token*

Request Body Example

  * [Delete Content Maps by Connection and Content ID Request Body](dg_ex/dg_ex_del_content_map_connect_contentid_req_body.txt "Delete Content Maps by Connection and Content ID Request Body")

This example body has the following inputs: Properties | Data Type |  Description  
---|---|---  
LocationAlias |  Character String Limit of 10 characters |  Indicates the name of the connector  
ContentMaps |  |  Lists all the content to map with this command  
TrackingId |  Integer |  Indicates the Archer contentId  
  
This command works, if the locationAlias and trackingId pairing exists.

Response Examples

  * [Successful](dg_ex/dg_ex_del_content_map_connect_contentid_res_success.txt "Successful")
  * [Partially successful due to valid and invalid trackingIds](dg_ex/dg_ex_del_content_map_connect_contentid_res_part_success.txt "Partially successful due to valid and invalid trackingIDs")
  * [Unsuccessful due to invalid locationAlias](dg_ex/dg_ex_del_content_map_connect_contentid_res_notsucc_invalid_loc_alias.txt "Unsuccessful due to invalid LocationAlias")
  * [Unsuccessful due to data gateway not enabled](dg_ex/dg_ex_del_content_map_connect_contentid_res_notsucc_dg_disabled.txt "Unsuccessful due to data gateway not enabled")
  * [Unsuccessful due to lack of permissions](dg_ex/dg_ex_del_content_map_connect_contentid_res_notsucc_no_perm.txt "Unsuccessful due to lack of permissions")

## Delete Content Map by Connection

A data gateway connection provides a connection from an external system to Archer. During set up, you can map external source content to Archer content. This section explains the API command to remove this map by connection. The content within each Archer field associated with the given connection becomes blank. The session token must be for a user who has access rights to data gateway.

Request

DELETE http://Archer/platformapi/DataGateway/ContentMaps/DeleteAll/?connection=*locationAlias*

Request Header

Content-Type: application/json

Authorization: Archer session-id=*session token*

Request Body Example

While this command does not require a distinct body, it does require a variable in the link. LocationAlias, a string of up to 10 characters, indicates the name of the connector.

Response Examples

  * [Successful](dg_ex/dg_ex_del_content_map_connect_name_res_success.txt "Successful")
    * A successful response provides the job ID added to the asychronous job to the Job Engine Manager. For more information about asynchronous job processing, see "Managing Asynchronous Job Processing" in the [Archer Control Panel Help](https://help.archerirm.cloud/archer_suite_help/en-us/Content/PortalHome/platform_home.htm).

  * [Unsuccessful due to invalid locationAlias](dg_ex/dg_ex_del_content_map_connect_name_res_notsucc_invalid_loc_alias.txt "Unsuccessful due to invalid LocationAlias")
  * [Unsuccessful due to data gateway not enabled](dg_ex/dg_ex_del_content_map_connect_name_res_notsucc_dg_disabled.txt "Unsuccessful due to data gateway not enabled")
  * [Unsuccessful due to lack of permissions](dg_ex/dg_ex_del_content_map_connect_name_res_notsucc_no_perm.txt "Unsuccessful due to lack of permissions")

