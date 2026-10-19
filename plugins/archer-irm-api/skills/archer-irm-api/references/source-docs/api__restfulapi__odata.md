#  Open Data Protocol (OData)

The implementation of OData involves a custom processor that is accessible to each controller class derived from ArcherApiController. Because metadata and content are returned through different processes, the application of OData to these 2 different data sets varies. OData queries are normally passed on the request URI in a query string. This query is a supported use of OData in the Archer API. All queries must be passed in the request body.

On this page

  * OData for MetaData - Projecting
  * OData for MetaData - Sorting
  * OData for MetaData - Paging and Limiting Results
  * OData for Content - Projecting
  * OData for Content - Paging and Limiting Results

## OData for MetaData - Projecting

Projecting is accomplished through the use of the OData $select keyword. This keyword allows the caller to specify which properties of the response object are to be included in the response.

The following example is of a valid OData select to return only the Name and Description properties of a response:

{"Value":"?$select=Name,Description"}

Projecting is supported by most of the URIs in the API.

## OData for MetaData - Sorting

Sorting is accomplished through the use of the OData $orderby keyword. This keyword takes a property as an argument, together with ascending (asc) (the default) or descending (desc). 

The following OData query will sort results in descending order by the value of the property boo:

{"Value":"?$orderby=boo desc"}

## OData for MetaData - Paging and Limiting Results

Results can be paged using a combination of the OData keywords $top and $skip. 

  * $top sets the page size of the current request.
  * $skip selects the correct page. 

For example, assume that a particular request will return 1000 results. If you wanted the results to come back in 50 record pages and wanted to retrieve page 3, your OData query should look like this:

{"Value":"?$top=50&$skip=100"}

This query skips the first 100 records and returns the next 50, effectively returning page 3.

It is possible through configuration to set a page size on the server. Configuring the server for a usable page size limits the ability of the client to request a larger result set through an OData query. While this is limiting, it is a good idea for security reasons to configure a server side page size to the maximum size you want to allow. Doing so may prevent a scenario where a client inadvertently requests an unacceptably large number of records and monopolizes server resources with the request. It could also combat a malicious request intended to perpetrate a DOS by requesting a very large data set in a single page.

OData for Content

## OData for Content - Projecting

Projecting the results of content requests is supported, but is subject to limitations similar to those of filtering. Projecting properties within a collection is not supported by OData. Projecting certain fields in a content record is not currently supported.

## OData for Content - Paging and Limiting Results

$top, $skip, and $orderby are all fully supported when retrieving content for a reference field. 
