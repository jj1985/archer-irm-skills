# General Settings

The following table describes elements that define general settings for the search. Use these elements with either the [search.ExecuteSearch](executesearch.htm) or [search.ExecuteStatisticSearch](executestatisticsearch.htm) methods. Element |  Description  
---|---  
PageSize |  **Sample:** <PageSize>100</PageSize> The number of records to return per page in the search results. **Note:** This element is required.  
MaxRecordCount  |  **Sample:** <MaxRecordCount>1000000</MaxRecordCount> The maximum number of records to return in the search results.  **Note:** This element is not required. Use this element with the [search.ExecuteSearch](executesearch.htm) method only.   
ShowStatSummaries |  **Sample:** <ShowStatSummaries>true</ShowStatSummaries> Determines whether to return a grand total for the aggregated values in each grouping.  **Note:** This element is not required. Use this element with the [search.ExecuteStatisticSearch](executestatisticsearch.htm) method only. The default value is false. 
