# Search by Time

The following 3 XML code samples utilize the [Time-Based Filters](time_based_filters_api.htm) found in Archer.

On this page

  * Time Based Filtering - Equals Operator / DateComparisionFilterCondition
  * Time Based Filtering - Between operator / DateRangeFilterCondition
  * Time Based Filtering - Time Interval Operator / DateTimeRangeFilterCondition

## Time Based Filtering - Equals Operator / DateComparisionFilterCondition

<SearchReport>

<PageSize>1000</PageSize>

<MaxRecordCount>1000</MaxRecordCount>

<DisplayFields>

<DisplayField>15116</DisplayField>

<DisplayField>15087</DisplayField>

<DisplayField>14903</DisplayField>

</DisplayFields>

<Criteria>

<ModuleCriteria>

<Module>410</Module>

<IsKeywordModule>False</IsKeywordModule>

<SortFields>

<SortField>

<Field>15116</Field>

<SortType>Ascending</SortType>

</SortField>

</SortFields>

</ModuleCriteria>

<Filter>

<OperatorLogic>1 OR NOT 2</OperatorLogic>

<Conditions>

<DateComparisonFilterCondition>

<Operator>Equals</Operator>

<Field>14903</Field>

<Value>11/1/2011 8:00 PM</Value>

<TimeZoneId>Central Standard Time</TimeZoneId>

<IsTimeIncluded>TRUE</IsTimeIncluded>

</DateComparisonFilterCondition>

<TextFilterCondition>

<Operator>DoesNotContain</Operator>

<Field>15087</Field>

<Value>Archer</Value>

</TextFilterCondition>

</Conditions>

</Filter>

</Criteria>

</SearchReport>

## Time Based Filtering - Between operator / DateRangeFilterCondition

<SearchReport>

<PageSize>1000</PageSize>

<MaxRecordCount>1000</MaxRecordCount>

<DisplayFields>

<DisplayField>15118</DisplayField>

<DisplayField>15089</DisplayField>

<DisplayField>15166</DisplayField>

</DisplayFields>

<Criteria>

<ModuleCriteria>

<Module>412</Module>

<IsKeywordModule>False</IsKeywordModule>

<SortFields>

<SortField>

<Field>15166</Field>

<SortType>Ascending</SortType>

</SortField>

</SortFields>

</ModuleCriteria>

<Filter>

<Conditions>

<DateRangeFilterCondition>

<Operator>Between</Operator>

<Field>15166</Field>

<BeginValue>2/15/2012 1:00 AM</BeginValue>

<EndValue>2/16/2012 10:00 PM</EndValue>

<TimeZoneId>Central Standard Time</TimeZoneId>

<IsTimeIncluded>TRUE</IsTimeIncluded>

</DateRangeFilterCondition>

</Conditions>

</Filter>

</Criteria>

</SearchReport>

## Time Based Filtering - Time Interval Operator / DateTimeRangeFilterCondition

<SearchReport>

<PageSize>1000</PageSize>

<MaxRecordCount>1000</MaxRecordCount>

<DisplayFields>

<DisplayField>15122</DisplayField>

<DisplayField>15093</DisplayField>

<DisplayField>15176</DisplayField>

</DisplayFields>

<Criteria>

<ModuleCriteria>

<Module>414</Module>

<IsKeywordModule>False</IsKeywordModule>

<SortFields>

<SortField>

<Field>15176</Field>

<SortType>Ascending</SortType>

</SortField>

</SortFields>

</ModuleCriteria>

<Filter>

<OperatorLogic>1 AND NOT 2</OperatorLogic>

<Conditions>

<DateTimeRangeFilterCondition>

<Field>15176</Field>

<BeginDate>7/7/2011</BeginDate>

<BeginTime>00:00</BeginTime>

<EndDate>7/14/2011</EndDate>

<EndTime>15:00</EndTime>

<TimeZoneId>Central Standard Time</TimeZoneId>

<IsTimeIncluded>TRUE</IsTimeIncluded>

</DateTimeRangeFilterCondition>

<NumericBetweenFilterCondition>

<Operator>Between</Operator>

<Field>15122</Field>

<BeginValue>894</BeginValue>

<EndValue>896</EndValue>

</NumericBetweenFilterCondition>

</Conditions>

</Filter>

</Criteria>

</SearchReport>
