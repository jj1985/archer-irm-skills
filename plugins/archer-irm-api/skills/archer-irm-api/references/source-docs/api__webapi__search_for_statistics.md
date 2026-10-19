# Search For Statistics

On this page

  * Sample Input
  * Sample Output

The following XML code sample performs a simple search: group by 1 field, count another.

## Sample Input

<?xml version="1.0" encoding="utf-16"?>

<SearchStatisticReport>

<PageSize>5</PageSize>

<Criteria>

<ModuleCriteria>

<Module>89</Module>

</ModuleCriteria>

<Filter>

<Conditions>

<TextFilterCondition>

<Operator>Contains</Operator>

<Field>675</Field>

<Value>GroupByAndCount</Value>

</TextFilterCondition>

</Conditions>

</Filter>

</Criteria>

<StatisticCriteria>

<StatisticSteps>

<StatisticStep>

<Field>698</Field>

<StepIndex>0</StepIndex>

<Name>Engagement Types</Name>

<StepType>GroupBy</StepType>

</StatisticStep>

<StatisticStep>

<Field>670</Field>

<StepIndex>1</StepIndex>

<Name>Count of Engagements</Name>

<StepType>Count</StepType>

</StatisticStep>

</StatisticSteps>

<SortSteps>

<SortStep>

<StepIndex>1</StepIndex>

<SortType>Descending</SortType>

</SortStep>

<SortStep>

<StepIndex>0</StepIndex>

<SortType>Ascending</SortType>

</SortStep>

</SortSteps>

<IncludeEmptyGroups>true</IncludeEmptyGroups>

</StatisticCriteria>

<ShowStatSummaries>false</ShowStatSummaries>

</SearchStatisticReport>

## Sample Output

<?xml version="1.0" encoding="utf-16"?>

<Groups count="16">

<Metadata>

<FieldDefinitions>

<FieldDefinition id="698" name="Engagement Type" alias="Engagement_Type" />

<FieldDefinition id="670" name="Budgeted Hours" alias="Budgeted_Hours" />

</FieldDefinitions>

</Metadata>

<Group FieldId="698" Value="Building maintenance">

<Aggregates>

<Aggregate FieldId="670" Count="10" />

</Aggregates>

</Group>

<Group FieldId="698" Value="Human Resources support">

<Aggregates>

<Aggregate FieldId="670" Count="6" />

</Aggregates>

</Group>

<Group FieldId="698" Value="Credit card production">

<Aggregates>

<Aggregate FieldId="670" Count="4" />

</Aggregates>

</Group>

<Group FieldId="698" Value="Call Center - inbound">

<Aggregates>

<Aggregate FieldId="670" Count="0" />

</Aggregates>

</Group>

<Group FieldId="698" Value="Call Center - outbound">

<Aggregates>

<Aggregate FieldId="670" Count="0" />

</Aggregates>

</Group>

</Groups>
