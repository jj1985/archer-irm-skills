# XML Formatting Guidelines for Field Input

Much of the content data that is exchanged between the Web Services API and third-party applications is formatted using XML. This section provides the details of the XML format for the different field types when you use the [record.CreateRecord](createrecord.htm), [record.CreateSubformRecord](createsubformrecord.htm), and [record.UpdateRecord](updaterecord.htm) methods.

Adhere to the following guidelines when you construct XML to create or update records: 

  * The information that the API returns when you use the [record.GetRecordById](getrecordbyid.htm) or [search.RetrieveSearchResultsPage](retrievesearchresultspage.htm) is different. 
  * The ID attribute of every field element represents the unique ID of the field as documented in the Application Detail Report or in the results of the [record.GetRecordById](getrecordbyid.htm) method.
  * The type attribute of every field element represents the unique ID of the field type as documented in the Type ID column in the following table.
  * To create or update records in a leveled application, all of the fields in your XML structure must reside within a single data level. If you have fields from 2 or more levels, you receive an error message.
  * If you configure a Text, Numeric, Date, or Values List field as a calculated field, you cannot input data or select values in the field through the API. The field is read only.
  * If a Record Permissions field is configured to use permission rules rather than to allow manual selection, you cannot select users or groups on the field through the API. The field is read only.
  * Some fields support the MultiValue element as a way to provide multiple values. If you include a single value only, do not include the MultiValue sub-element and make the regular element empty.
  * To create or update multiple records with [record. CreateRecords](createrecords.htm) or [record.UpdateRecords](updaterecords.htm), use the same XML input defined in this section and wrap the collection of individual records with the **< Records></Records>** tags.
  * The XML elements that you provide can contain extra attribute-value pairs. The API uses only the required attribute-value pairs as documented in the following table.

The following table provides examples of XML for field input. Field ID |  Field Name |  Example  
---|---|---  
1 |  Text |  **Sample XML:** <Field id="9402" value="ABCDEFG hijk LMNOP qrstuvwxyz ÃÄÇËÑßÜ áòëæñü 信息報이ÜФ " /> The value attribute is in UTF-8 or UTF-16 when you use the Field control type. **Sample XML:** <Field id="9403" value="&lt;p&gt;1234 Main Street&lt;br&gt;Anytown, AA 12345&lt;/p&gt;" /> If you are use the Area control type, you can insert encoded HTML text.  
  
2 |  Numeric |  **Sample XML:** <Field id="123" value="125.75" /> If you have units of measure turned on, you express the value in the quantity of the smallest unit of measure, for example, 39 inches instead of 3 feet, 3 inches.   
3 |  Date |  **Sample XML:** <Field id="9412" value="12/31/2099 11:59AM" /> <Field id="9411" value="01/01/1980" /> If you specify the field as Date-only, and you do not specify the time, the API defaults to 12:00 AM.  **Note:** To pass in a date field null value, enter a value of "0". For example:  
  
<Field id="42065" value="0" />  
4 |  Values List |  **Sample XML:** <Field id="123" value="2">

<MultiValue value="3" /> <MultiValue value="4" /> 
</Field> The value attribute is the integer ID of the value (within the values list) as returned by the [field.LookUpListValue](lookuplistvalue.htm) method.  **Important:** If the values list supports the use of other type values, supply the value of the value that is enabled for other text, along with the other text in an attribute called otherText. For example:  
  
<Field id=\"4871\" value=\"4181\" type=\"4\" otherText=\"MyTextItem\" /> **Note:** To pass in a values list null value, enter a value of "0". For example:  
  
<Field id="8323" type="4" value="0"></Field>  
7 |  External Links |  **Sample XML:** <Field id="123" value="Archer" link=  
"http://staging/domains/archer/index.html">

<MultiValue value="Aquarium Advice" link="http://www.aquariumadvice.com/" /> 
</Field> The value attribute is the text that is displayed in the field. The link attribute is the actual link value that you click to activate.   
8 |  User/  
Groups List |  **Sample XML:** <Field id="123" >

<Groups> <Group id="123" /> <Group id="345" /> </Groups> <Users> <User id="123" /> <User id="234" /> </Users> 
</Field> If you do not have any of either type of value, that is, no user or no group, you can omit that corresponding element (groups or users) rather than including an empty 1. Each member must be included as a separate value. The ID value is the userId (as returned by the [accesscontrol.LookupUserByFirstName](lookupuserbyfirstname.htm) method) or the groupId (as returned by the [accesscontrol.LookupGroup](lookupgroup.htm) method).  
9 |  Cross-Reference  |  **Sample XML:** <Field id="123" value="1000" >

<MultiValue value="1001" /> <MultiValue value="1002" /> 
</Field> The API populates the value attribute with the contentId of the related record as returned by a search, for example, [search.ExecuteSearch](executesearch.htm).   
11 |  Attachment |  The API does not support this field type.  
12 |  Image |  The API does not support this field type.  
14 |  Cross-Application Status Tracking |  CAST values are set using the [record.CreateCMSTEntry](createcmstentry.htm) method.  
15 |  Record Permission |  Same as field type 8—**User/Groups List**. Remember to change the type attribute from 8 to 15. To create or update records through the API, select users or groups in a **Record Permissions** field that are not included in the field's available values. For example, you can configure the **Record Permissions** to show Jake Miller and Renee Jones as the only values available for selection. Alternatively, you can select Tim Lee as the value for the field through the API.   
16 |  Matrix |  **Sample XML:** <Field id="123" rowId="100" columnId="101" >

<MultiValue rowId="100" columnId="102" /> 
</Field>  
18 |  Cross-Reference (internal relationship) |  **Sample XML** : <Field id="123" value="1000" >

<MultiValue value="1001" /> <MultiValue value="1002" /> 
</Field> The value attribute is the record ID as returned by a search, for example, [search.ExecuteSearch](executesearch.htm).   
19 |  IP Address |  **Sample XML** : <Field id="9415" value="a.b.c.d" /> You can express the IP address value as a standard IP-V4 address with 4 octets. **Sample XML** : <Field id="9424" value="a:b:c:d:e:f:g:h" /> <Field id="9425" value="a:b:c:d:e:f::" /> You can also express the IP address value as an IP-V6 address in both full and short form. 
