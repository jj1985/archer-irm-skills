# XML Formatting Guidelines for Search Input  
  
**Important:** To reference a field in the search parameters, it is recommended to use the GUID for that field instead of the SQL field ID. The GUID is listed in the Application Detail Report as well as in Application Builder, by opening the Manage Field page for that field. The GUID is displayed on the General tab in the ID field.

**Note:** Any search that returns a <metadata> section now includes the field ID, name, and GUID for each field.

The following table describes the elements used to form the search inputs. Element |  Description  
---|---  
SearchReport  |  The SearchReport element is the root of the search XML document for searches that use the [search.ExecuteSearch](executesearch.htm) method. It takes no attributes.   
SearchStatisticReport  |  The SearchStatisticReport element is the root of the search XML document for searches that use the [search.ExecuteStatisticSearch](executestatisticsearch.htm) method. It takes no attributes.   
  
For a description of the sub-elements that you can specify under the SearchReport and SearchStatisticReport elements, see the following topics: 

  * [General Settings](general_settings.htm)
  * [Result Display](result_display.htm)
  * [Search Criteria](search_criteria.htm)
  * [Keywords Search](keywords_search.htm)
  * [Filters](filter_search.htm)
  * [Statistics Criteria](statistics_criteria.htm)
  * [Module Definition](module_definition.htm)

