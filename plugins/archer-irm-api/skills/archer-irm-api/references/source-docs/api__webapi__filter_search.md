# Filters 

The following table describes elements that define the filter criteria for the search. Use these elements with the [search.ExecuteSearch](executesearch.htm) method. These elements are optional. Element |  Description  
---|---  
Filter |  The Filter element is the root of the filter criteria. It takes no attributes. You can specify the sub-elements in this table under the Filter root element. **Note:** All special characters must be double XML-encoded. For example, ampersand (&) must be encoded as &amp;amp;. The following table lists special character symbols and their double XML-encoded values. |  Special Character |  Symbol |  Double XML-Encoded Value  
---|---|---  
Double Quotes |  " |  &amp;quot;  
Apostrophe |  ' |  &amp;#39;  
Less than |  < |  &amp;lt;  
Greater Than |  > |  &amp;gt;  
Ampersand |  & |  &amp;amp;  
OperatorLogic |  The advanced operator logic for the filter criteria. This element uses the same syntax as the Advanced Operator Logic field in the Filters section of the Search Records page.   
Conditions |  **Sample:** <Conditions>  

<NumericFilterCondition> <Operator>Equals</Operator> <Field>5</Field> <ParentField>8</ParentField> <Value>22.5</Value> </NumericFilterCondition> 
</Conditions> Specifies the filters to use in the search. This element requires 1 or more of the sub-elements defined in Conditions.   
  
Conditions

You must specify 1 or more Conditions sub-elements under the Filter root element.

The following table describes the Conditions sub-elements. Element |  Description  
---|---  
ContentFilterCondition |  **Sample:** <ContentFilterCondition>

<Level>1</Level> <Operator>Equals</Operator> <Values> <Value>1</Value> <Value>2</Value> </Values> 
</ContentFilterCondition> A filter condition using record content. This replicates the Filter by Record option in Search Records. The following table describes ContentFilterCondition sub-elements. |  Element |  Description  
---|---  
Level |  In a leveled application, the level in which the record resides.   
Operator |  The operator to use in this condition. Possible values:

  * Equals
  * DoesNotEqual

  
Values |  The records to evaluate in this condition. Use the Value sub-element to specify the SQL ID of each record.   
DateComparison  
FilterCondition |  **Sample:** <DateComparisonFilterCondition>

<Operator>Equals</Operator> <Field>5</Field> <ParentField>8</ParentField> <Value>1/1/2008</Value> <TimeZoneId>Central Standard Time</TimeZoneId> <IsTimeIncluded>TRUE</IsTimeIncluded> 
</DateComparisonFilterCondition> A filter condition that compares a date. The following table describes DateComparison  
FilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * Equals
  * DoesNotEqual
  * GreaterThan
  * LessThan
  * AfterToday
  * PriorToToday

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.  **Note:** This element is not required.  
Value |  The value to evaluate in this condition. This element is not used with the AfterToday and PriorToToday operators.   
TimeZoneId |  The ID of the time zone you are searching for. For additional information, see [Supported Time Zones](timezones.htm). **Note:** This element is only required if you are using Time-Based Filtering.  
IsTime  
Included |  Specifies whether to search for a time range or not. Possible values: 

  * TRUE
  * FALSE

**Note:** This element is only required if you are using Time-Based Filtering.  
DateRange  
FilterCondition |  **Sample:** <DateRangeFilterCondition>

<Operator>Between</Operator> <Field>5</Field> <ParentField>8</ParentField> <BeginValue>1/1/2008</BeginValue> <EndValue>1/2/2008</EndValue> <TimeZoneId>Central Standard Time</TimeZoneId> <IsTimeIncluded>TRUE</IsTimeIncluded> 
</DateRangeFilterCondition> A filter condition for date ranges. The following table describes DateRange  
FilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible value is: Between  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.   
BeginValue |  The first date in the range.  
EndValue |  The last date in the range.   
TimeZoneId |  The ID of the time zone you are searching for. For additional information, see [Supported Time Zones](timezones.htm). **Note:** This element is only required if you are using Time-Based Filtering.  
IsTimeIncluded |  Specifies whether to search for a time range or not. Possible values:

  * TRUE
  * FALSE

**Note:** This element is only required if you are using Time-Based Filtering.  
DateTimeRange  
FilterCondition |  **Sample:** <DateTimeRangeFilterCondition>

<Field>15176</Field> <BeginDate>7/7/2011</BeginDate> <BeginTime>00:00</BeginTime> <EndDate>7/14/2011</EndDate> <EndTime>15:00</EndTime> <TimeZoneId>Central Standard Time</TimeZoneId> <IsTimeIncluded>TRUE</IsTimeIncluded> 
</DateTimeRangeFilterCondition> A filter condition for date ranges. The following table describes DateTimeRange  
FilterCondition sub-elements. | Element | Description  
---|---  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
BeginDate |  The first date in the range.  
BeginTime |  The first time in the range.  
EndDate |  The last date in the range.  
EndTime |  The last time in the range.   
TimeZoneId |  The ID of the time zone you are searching for. For additional information, see [Supported Time Zones](timezones.htm). **Note:** This element is only required if you are using Time-Based Filtering.  
IsTimeIncluded |  Specifies whether to search for a time range or not. Possible values:

  * TRUE
  * FALSE

**Note:** This element is only required if you are using Time-Based Filtering.  
DateOffset  
FilterCondition |  **Sample:** <DateOffsetFilterCondition>

<Operator>LastXDays</Operator> <Field>5</Field> <ParentField>8</ParentField> <Value>22</Value> <TimeZoneId>Central Standard Time</TimeZoneId> <IsTimeIncluded>TRUE</IsTimeIncluded> 
</DateOffsetFilterCondition> A filter condition before or after the current date. The following table describes DateOffset  
FilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * LastXDays
  * LastXMonths
  * LastXQuarters
  * LastXYears
  * NextXDays
  * NextXMonths
  * NextXQuarters
  * NextXYears

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.   
Value |  The number of days, months, quarters, or years before or after the current date.  **Important:** The value must be an integer.   
TimeZoneId |  The ID of the time zone you are searching for. For additional information, see [Supported Time Zones](timezones.htm). **Note:** This element is only required if you are using Time-Based Filtering.  
IsTime  
Included |  Specifies whether to search for a time range or not. Possible values:

  * TRUE
  * FALSE

**Note:** This element is only required if you are using Time-Based Filtering.  
CurrentDate  
FilterCondition |  **Sample** : <CurrentDateFilterCondition>

<Operator>CurrentDay</Operator> <Field>5</Field> <ParentField>8</ParentField> <TimeZoneId>Central Standard Time</TimeZoneId> <IsTimeIncluded>TRUE</IsTimeIncluded> 
</CurrentDateFilterCondition> A filter condition using the current date. The following table describes CurrentDate  
FilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * CurrentDay
  * CurrentMonth
  * CurrentQuarter
  * CurrentYear

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
Value |  The subform if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.  
TimeZoneId |  The ID of the time zone you are searching for. For additional information, see [Supported Time Zones](timezones.htm). **Note:** This element is only required if you are using Time-Based Filtering.  
IsTimeIncluded |  Specifies whether to search for a time range or not. Possible values:

  * TRUE
  * FALSE

**Note:** This element is only required if you are using Time-Based Filtering.  
NumericFilterCondition |  **Sample:** <NumericFilterCondition>

<Operator>Equals</Operator> <Field>5</Field> <ParentField>8</ParentField> <Value>22.5</Value> 
</NumericFilterCondition> A filter condition using numeric fields. The following table describes NumericFilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * Equals
  * NotEqual
  * GreaterThan
  * LessThan

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.   
Value |  The value to evaluate.   
NumericRange  
FilterCondition |  **Sample:** <NumericRangeFilterCondition>

<Operator>Contains</Operator> <Field>5</Field> <ParentField>8</ParentField> <Values> <Value>1</Value> <Value>2</Value> </Values> 
</NumericRangeFilterCondition> A filter condition using ranges of numbers. The following table describes NumericRange  
FilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * Contains
  * DoesNotContain

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.   
Value |  The numeric ranges that you want to evaluate in this condition. Use the Value sub-element to specify the IDs of the numeric ranges.  
NumericBetween  
FilterCondition |  **Sample** : <NumericBetweenFilterCondition>

<Operator>Between</Operator> <Field>5</Field> <ParentField>8</ParentField> <BeginValue>5.1</BeginValue> <EndValue>8.2</EndValue> 
</NumericBetweenFilterCondition> A filter condition specifying values within a numeric range. The following table describes NumericBetween  
FilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible value is: Between  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.   
BeginValue |  The first value in the range.  
EndValue |  The last value in the range.  
RecordStatus  
FilterCondition |  **Sample** : <RecordStatusFilterCondition>

<Operator>DoesNotEqual</Operator> <Field>5</Field> <RecordStatusType>New</RecordStatusType> 
</RecordStatusFilterCondition> A filter condition using the record status. The following table describes RecordStatus  
FilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values:

  * Equals
  * DoesNotEqual

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.   
RecordStatusType |  The record status type that you want to evaluate in this condition. Possible values are: 

  * New
  * Updated

  
ValueListFilterCondition |  **Sample:** <ValueListFilterCondition>

<Operator>Contains</Operator> <Field>5</Field> <IsNoSelectionIncluded>True  
</IsNoSelectionIncluded> <Values> <Value>1</Value> <Value>2</Value> </Values> 
</ValueListFilterCondition> A filter condition using a values list. The following table describes ValueListFilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * Equals
  * DoesNotEqual
  * Contains
  * DoesNotContain

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
IsNoSelectionIncluded |  Specifies whether to return records without a value selected in that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.  
IncludeChildren |  Specifies whether to include child records for the chosen by the values in the Value element.  
Value |  The values to evaluate in this condition. Use the select value id for each select value.  
UserGroup  
FilterCondition |  **Sample:** <UserGroupFilterCondition>

<Operator>Contains</Operator> <Field>5</Field> <IsNoSelectionIncluded>True  
</IsNoSelectionIncluded> <Groups> <Group>1</Group> <Group>2</Group> </Groups> <Users> <User>1</User> <User>2</User> </Users> 
</UserGroupFilterCondition> A filter condition using user groups. The following table describes UserGroup  
FilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * Equals
  * DoesNotEqual
  * Contains
  * DoesNotContain
  * AfterToday
  * PriorToToday

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.   
IsNo  
Selection  
Included |  Specifies whether to return records without a value selected in that field.  
Groups |  The group to evaluate in this condition. Use the Group sub-element to specify the SQL ID of each group to include in the filter.   
Users |  The users to evaluate in this condition. Use the User sub-element to specify the SQL ID of each user to include in the filter.   
TextFilterCondition |  **Sample** : <TextFilterCondition>

<Operator>Contains</Operator> <Field>5</Field> <Value>Hello &amp;amp; Goodbye</Value> 
</TextFilterCondition> A filter condition using text. The following table describes TextFilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * Equals
  * DoesNotEqual
  * Contains
  * DoesNotContain

  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.  **Note:** This element is not required.  
Value |  The text to evaluate in this condition. **Note:** All special characters must be double XML-encoded. For example, ampersand (&) must be encoded as &amp;amp;  
MatrixFilterCondition |  **Sample** : <MatrixFilterCondition>

<Operator>Contains</Operator> <Field>5</Field> <IsNoSelectionIncluded>True  
</IsNoSelectionIncluded> <Row id="1"> <Column>5</Column> <Column>6</Column> </Row> <Row id="2"> <Column>7</Column> <Column>9</Column> </Row> 
</MatrixFilterCondition> A filter condition using the matrix field. The following table describes MatrixFilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * Equals
  * DoesNotEqual
  * Contains
  * DoesNotContain

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
IsNoSelectionIncluded |  Specifies whether to return records without a value selected in that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.   
Row id="SQL_ID" |  The row to evaluate. Specify the SQL ID of the row. This element uses the Column sub-element to specify the SQL ID of column within the row.   
Column |  The column to evaluate. Specify the SQL ID of the column within the row.  
ReferenceFilterCondition |  **Sample** : <ReferenceFilterCondition>

<Operator>Contains</Operator> <Field>5</Field> <IsNoSelectionIncluded>False  
</IsNoSelectionIncluded> <Level id="1"> <Content>5</Content> <Content>6</Content> </Level> <Level id="2"> <Content>7</Content> <Content>9</Content> </Level> 
</ReferenceFilterCondition> A filter condition using a reference field. The following table describes ReferenceFilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * Equals
  * DoesNotEqual
  * Contains
  * DoesNotContain

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.  **Note:** This element is not required.  
IsNoSelectionIncluded |  Specifies whether to return records without a value selected in that field.  
Level |  The SQL ID of the level in which the record resides. All applications have at least 1 level. The Level element uses the Content sub-element to specify the SQL ID of the content.   
Content |  The SQL ID of the content in the specified level.   
IpAddressFilterCondition |  **Sample using IPv4 address:** <IpAddressFilterCondition>

<Field>5</Field> <Operator>Equals</Operator> <Octet1>a</Octet1> <Octet2>b</Octet2> <Octet3>c</Octet3> <Octet4>d</Octet4> 
</IpAddressFilterCondition> **Sample using IPv6 address:** <IpAddressFilterCondition>

<Field>5</Field> <Operator>Equals</Operator> <Value>ab::cd</Value> 
</IpAddressFilterCondition> A filter condition using IP address. To filter multiple addresses, define multiple IpAddressFilterCondition nodes and join them using the OperatorLogic element. The following table describes IpAddressFilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values:

  * Equals
  * DoesNotEqual

For IPv4 addresses, use the following sub-elements to specify the IP address: 

  * Octet1
  * Octet2
  * Octet3
  * Octet4

For IPv6 addresses, use the following sub-element to specify the IP address in short or long notation: Value **Note:** The Value sub-element can also be used for IPv4 addresses.   
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.   
CastFilterCondition |  **Sample** : <CastFilterCondition>

<Operator>Contains</Operator> <Field>5</Field> <Value>12</Value> 
</CastFilterCondition> A filter condition using CAST fields. The following table describes CastFilterCondition sub-elements. | Element | Description  
---|---  
Operator |  The operator to use in this condition. Possible values: 

  * Equals
  * DoesNotEqual
  * Contains
  * DoesNotContain

  
Field |  The field to evaluate. Use the GUID or the SQL field ID for that field.  
ParentField |  The subform field if the field to evaluate is within a subform. Use the GUID or the SQL field ID for that subform.   
Value |  The values list to evaluate in this condition. Use the GUID or the SQL field ID for that values list. 
