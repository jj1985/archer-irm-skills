# Search For a Filter  
  
On this page

  * Search for Comments
  * Search for Dates

## Search for Comments

The following XML code sample searches the available reports for the comments set below.

<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

<SearchReport>

<PageSize>100</PageSize>

<DisplayFields>

<DisplayField>9399</DisplayField>

<DisplayField>9402</DisplayField>

<DisplayField>9403</DisplayField>

<DisplayField>9405</DisplayField>

<DisplayField>9411</DisplayField>

<DisplayField>9413</DisplayField>

</DisplayFields>

<Criteria>

<ModuleCriteria>

<Module>331</Module>

<IsKeywordModule>false</IsKeywordModule>

<SortFields>

<SortField>

<Field>9399</Field>

<SortType>Ascending</SortType>

</SortField>

</SortFields>

</ModuleCriteria>

<Filter>

<Conditions>

<TextFilterCondition>

<Operator>Contains</Operator>

<Field>9402</Field>

<Value>A comment</Value>

</TextFilterCondition>

<TextFilterCondition>

<Operator>Contains</Operator>

<Field>9403</Field>

<Value>123 Lotus</Value>

</TextFilterCondition>

</Conditions>

<OperatorLogic>1 OR 2</OperatorLogic>

</Filter>

</Criteria>

</SearchReport>

## Search for Dates

The following XML code sample searches the available reports for the dates set below.

<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

<SearchReport>

<PageSize>100</PageSize>

<DisplayFields>

<DisplayField>9399</DisplayField>

<DisplayField>9411</DisplayField>

<DisplayField>9412</DisplayField>

</DisplayFields>

<Criteria>

<ModuleCriteria>

<Module>331</Module>

<IsKeywordModule>false</IsKeywordModule>

<SortFields>

<SortField>

<Field>9399</Field>

<SortType>Ascending</SortType>

</SortField>

</SortFields>

</ModuleCriteria>

<Filter>

<Conditions>

<DateComparisonFilterCondition>

<Operator>Equals</Operator>

<Field>9411</Field>

<Value>1/1/1980</Value>

</DateComparisonFilterCondition>

<DateComparisonFilterCondition>

<Operator>GreaterThan</Operator>

<Field>9412</Field>

<Value>01/01/2099</Value>

</DateComparisonFilterCondition>

</Conditions>

<OperatorLogic>1 AND 2</OperatorLogic>

</Filter>

</Criteria>

</SearchReport>
