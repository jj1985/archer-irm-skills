# Statistics Criteria

The following table describes elements that define the statistics criteria. Use these elements with the [search.ExecuteStatisticSearch](executestatisticsearch.htm) method. Element |  Description  
---|---  
StatisticCriteria |  The StatisticCriteria element is the root of the module definition. It takes no attributes. You can specify the following sub-elements in this table under the StatisticCriteria root element.  
IncludeEmptyGroups |  **Sample:** <IncludeEmptyGroups>false</IncludeEmptyGroups> Determines whether to include empty groups in the search criteria.  **Note:** This element is not required. The default value is false.  
StatisticStep |  **Sample:** <StatisticSteps>

<StatisticStep> <Field>1</Field> <StepIndex>0</StepIndex> <Name>Display Name</Name> <StepType>GroupByDateRange</StepType> <Action>GroupByDay</Action> </StatisticStep> 
</StatisticSteps> Determines the fields to include in the results and how to sort the data. The following table describes StatisticSteps sub-elements. | Element | Description  
---|---  
StatisticsStep |  The root of the step criteria for each step.   
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
StepIndex |  An integer value that identifies the order in which this step should be evaluated. The first step must be 0.  **Note:** This value is also referenced in the SortSteps element.  
Name |  The name to display in the results.   
StepType |  Determines how this step is evaluated. Possible values: 

  * Count
  * DateAggregate
  * GroupBy
  * GroupByDateRange
  * GroupByHierarchicalValuesList
  * GroupByMatrix 
  * NumericAggregate

  
DepthField |  The depth of the hierarchy to group by. **Important:** If you are using the GroupByHierarchicalValuesList StepType, you must use this element. **Note:** This value is zero-based. This means that if you want to group by the first level of the hierarchy, you must set the value to 0 (instead of 1).  
Action |  The action to take for certain step types. If the StepType is GroupByDateRange, specify the following: 

  * GroupByDay
  * GroupByWeek
  * GroupByMonth
  * GroupByQuarter
  * GroupByYear

If the StepType is DateAggregate, specify the following: 

  * Min
  * Max

If the StepType is GroupByMatrix, specify:

  * Row
  * Column 

If the StepType is NumericAggregate, specify the following: 

  * Average
  * Min 
  * Max
  * Sum
  * Median
  * Mode

  
SortSteps |  **Sample** : <SortSteps>

<SortStep> <StepIndex>0</StepIndex> <SortType>Ascending</SortType> </SortStep> 
</SortSteps> Determines the order in which the data is sorted in the results. The following table describes SortSteps sub-elements. | Element | Description  
---|---  
SortStep |  The root of the sort criteria for the step. This element requires the sub-elements StepIndex and SortType.  
StepIndex |  Determines which step to sort. This value corresponds with the value in the StepIndex sub-element of the StatisticsStep element. **Note:** The first value is 0.  
SortType |  The type of sort. Possible values: 

  * Ascending
  * Descending 

