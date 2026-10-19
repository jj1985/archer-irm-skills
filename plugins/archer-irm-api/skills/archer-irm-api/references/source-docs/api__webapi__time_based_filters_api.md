# Time-Based Filtering

For an advanced search to return search results to a level smaller than a single day, you can set time filters to your search criteria. Using specific filter operators and values, you can configure time filters, with or without dates. For more information on time-based filter searches, see [XML Formatting Guidelines for Search Input](xml_formatting_guidelines_for_search_input.htm).

Time-based filtering requires several rules and logic to determine the correct search results. The following general rules apply to the time filter options: 

  * The time filter options are available only when a Date field is configured to show time.
  * Unless a specific time is selected, the Archer uses the All Times option.
  * Where available, a specific time zone can be selected, or the local time zone of the user performing the search can be used when the search is saved and run by another user.
  * A time must be selected before a specific time zone can be selected.
  * Daylight savings time is accommodated.

The following table describes the other rules and logic by filter type. Filter Type |  Rules and Logic  
---|---  
Equals Does Not Equal |  If you enter 09/12/2012 1:15 p.m., the search returns records that meet that exact date and time for an Equals search, or records that do not equal that exact date and time for a Does Not Equal search. If the field is not configured to show time, you can only select a date. You must select a date before you can select a time. You must select a time in order to select a time zone. If you leave the date and time values empty, the results return all records that have blank values in the field on which the filter was configured. If a date is selected, but you do not select a time value, the filter acts as a date-only filter.  
Current   
(Minute or Hour) |  If you select the current hour, all records with a time in the current hour are included in the search results. For example, if the time value is 10:14, all records in the 10:00 hour are included. Time zone options are not available on this filter type. The local time zone of the user performing the search is used.  
Last  
(Minutes or Hours) |  If you filter "Last" "3" "Hours", the results include the previous 3 hours, but do not include the current hour.  The time zone options are not available on this filter type. The local time zone of the user performing the search is used. This filter types does not include the current minute or hour.  
Next  
(Minutes or Hours) |  If you filter "Next" "3" "Days", the results include the next 3 days, but not the current day. The time zone options are not available on this filter type. The local time zone of the user performing the search is used. This filter types does not include the current minute or hour.  
Greater Than Less Than |  If the field is not configured to show time, you can only select a date. You must select a date before you can select a time. If you leave the date and time values empty, the results return as blank values. If a date is selected, but you do not select a time value, the filter acts as a date-only filter.  
Between |  Search results include selected dates and times. You must select a date before you can select a time. You must select a time before you can select a specific time zone. You must select a date in each Date field. If a date is selected, but you do not select a time value, the filter acts as a date-only filter with selected dates included.  
Time Interval |  Search results include selected dates and times. You must select a time in both Time fields. You must select a time before you can select a specific time zone. You can configure the filter based on 2 Time values for all dates, or filter the search to a specific date range in addition to the time range. If you do not select dates, the filter is not restricted to a date range, and the Archer searches for all records that occur within the selected times, including the selected times.
