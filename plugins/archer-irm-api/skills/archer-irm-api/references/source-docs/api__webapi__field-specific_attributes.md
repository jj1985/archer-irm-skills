# Field-Specific Attributes

The following table describes the attributes and values the Web Services API returns for various field types. This table excludes the attributes described in [Common Attributes](common_attributes.htm). Field ID |  Field Name |  Example  
---|---|---  
1 |  Text |  **Sample XML:** <Field id="4918" type="1" value="&amp;lt;P&amp;gt;&amp;lt;U&amp;gt;Rich Text;&amp;lt;/U&amp;gt;&amp;lt;/P&amp;gt;" /> A Text field’s only other attribute is value. The value of the value attribute is ASCII text. If the Text field uses the Area control type, the value attribute can include HTML text.   
2 |  Numeric |  **Sample XML:** <Field id="4914" type="2" value="824024">

<UnitOfMeasure id="6" value="13" unitLabel="Miles" /> <UnitOfMeasure id="5" value="28" unitLabel="Feet" /> <UnitOfMeasure id="4" value="8" unitLabel="Inches" /> 
</Field> A Numeric field's only other attribute is value. The value of the value attribute is the number in the record. There are appropriate UnitOfMeasure sub-elements included within the field: 

  * In the Sample XML, the common attributes are removed from the field element, but the UnitOfMeasure elements are shown as they were received.
  * Even if the field does not use units of measure, you need to specify a closing tag for the Field element as opposed to representing it as an empty element.
  * You do not use UnitOfMeasure elements to create or update the field. 

  
3 |  Date |  **Sample XML:** <Field id="4905" type="3" value="7/8/1999 6:50 AM" /> A Date field's only other attribute is value. The value of the attribute is shown in the MM/DD/YYY HH:MM:SS AM or PM format, for example, 10/15/2003 4:19:04 PM.  
4 |  Values List |  **Sample XML:** <Field id="123" type="4" value="2">

<MultiValue value="3" /> <MultiValue value="4" /> 
</Field> A Values List field's only other attribute is value. It is populated with an integer representing the ID of the selected valuesListValue. If the field supports multiple selections (and the record has multiple selections specified), you specify additional selections with the MultiValue sub-element. Even if there is only a single value, you need to specify a closing tag for the Field element as opposed to representing it as an empty element.  
6 |  Tracking ID |  **Sample XML:** <Field id="123" type="6" value="123456" /> The value attribute is an integer that represents the value of the record's tracking ID. You can use the tracking ID in any method that requests a contentId; however, it cannot be modified.   
7 |  External Links |  **Sample XML:** <Field id="123" type="7" value="Archer" link=  
"http://staging/domains/archer/index.html">

<MultiValue value="Aquarium Advice" link="http://www.aquariumadvice.com/" /> 
</Field> The value attribute is the text that is displayed in the field, and the link attribute is the actual link value that you click to activate. If the record has multiple links, additional links are included using the MultiValue sub-element.  Even if there is only a single value, you need to specify a closing tag for the Field element as opposed to representing it as an empty element.   
8 |  User/Groups List |  **Sample XML:** <Field id="123" type="8">

<Groups> <Group id="123" name="Asset Administrators" desc="description" /> <Group id="345" name="Non-Asset Administrators" desc="" /> </Groups> <Users> <User firstName="Joe" lastName="User" id="123" /> </Users> 
</Field> The id attribute is the ID of the group or user. Under Groups, the desc attribute contains the description of the group as shown through the GUI (if defined). If there are no groups or users, the field does not come back. Similarly, if you do not have any of a particular type of value, for example, no user or no group, the corresponding element is omitted rather than returned empty. Each member must be included as a separate value. The id value is the userId (as returned by the [accesscontrol.LookupUserByFirstName](lookupuserbyfirstname.htm) method) or the groupId (as returned by the [accesscontrol.LookupGroup](lookupgroup.htm) method). The created or updated information is in the Users and Groups elements, not in the Field element.   
9 |  Cross-Reference |  **Sample XML:** <Field id="13115" guid="3abdaac6-18f4-431e-a263-f7aec27caf34" type="9">

<Reference id="269954">01 Information Access Control</Reference> <Reference id="270053">Title of My InfoSec Policy</Reference> 
</Field> The Cross-Reference field has the following attribute:

  * Reference id. The ID of the item referenced within the Cross-Reference field.

  
11 |  Attachment |  **Sample XML:** <Field id="4903" type="11" fileID="410" fileName="0001.xls" width="" height="">  
</Field> The Attachment field has the following attributes: 

  * fileID. The integer ID of the file within the document repository.
  * filename. The string name of the uploaded file.
  * width. Not populated for attachments.
  * height. Not populated for attachments.

If the record has multiple attachments, additional attachments are included using the MultiValue sub-element.  Even if there is only a single value,you need to specify a closing tag for the Field element as opposed to representing it as an empty element.  The Attachment field type is not supported for creating or updating records.   
12 |  Image |  **Sample XML:** <Field id="4908" type="12" fileID="411" fileName="0001.jpg" width="100" height="100"></Field> The Image field has the following attributes: 

  * fileID. The integer ID of the file within the document repository.
  * fileName. The string name of the uploaded file.
  * width. The width of the image as defined in Application Builder.
  * height. The height of the image as defined in Application Builder.

If the record has multiple images, additional images are included using the MultiValue sub-element. The Image field type is not supported for creating or updating records.   
14 |  Cross-Application Status Tracking |  The API does not support this field type.  The 1001 CAST field type is supported from its parent application, for example, from Assets, not Vulnerabilities.  
15 |  Record Permission |  This is the same as field type 8—User/Groups List.  
16 |  Matrix |  **Sample XML:** <Field id="7766" type="16" rowId="17729" rowValueName="High" rowValueColor="" rowValueSecondColor="" columnId="17726 columnValueName="Confidentiality" columnValueColor="" columnValueColor2="" >  

<MultiValue rowId="17731" rowValueName="Low" rowValueColor="" rowValueSecondColor="" columnId="17726" columnValueName="Confidentiality" columnValueColor="" columnValueColor2="" /> <MultiValue rowId="17730" rowValueName="Medium" rowValueColor="" rowValueSecondColor="" columnId="17726" columnValueName="Confidentiality" columnValueColor="" columnValueColor2="" /> 
</Field> The Matrix field has the following attributes: 

  * rowId. The integer ID of the row within the matrix.
  * rowValueName. The string name of the row.
  * rowValueColor. Contains the color (if specified) of the value.
  * rowValueSecondColor. A deprecated attribute.
  * columnId. The integer ID of the column within the matrix.
  * columnValueName. The string name of the column.
  * columnValueColor. Contains the color (if specified) of the value.
  * columnValueSecondColor. A deprecated attribute.

The column and row IDs are important for adding or updating records.   
19 |  IP Address |  **Sample XML:** <Field id="123" type="19" value="a.b.c.d" /> The value attribute must be a valid IPv4 address in the standard 4 octet format or IPv6 address.  
20 |  Record Status |  **Sample XML:** <Field id="123" type="20" value="New" /> The value attribute is either "New" or "Updated".  
21 |  First Published Date |  **Sample XML:** <Field id="7608" type="21" value="12/12/2003 2:28 PM" />  
22 |  Last Updated Date |  **Sample XML:** <Field id="7608" type="22" value="12/12/2003 2:28 PM" />  
  
The following table describes information about more fields. Field ID | Field Name | Example  
---|---|---  
1001 |  CAST |  **Sample XML:** <Field id="7612" type="1001" childFieldId="7611" childModuleId="540" childModuleName="Questionaire" moduleSearchPageNum="i6031" moduleSearchViewId="1" totalCount="11">

<RecordValue selectValueId="1692" selectValueName="AcceptRisk" selectValueDefaultFlag="False" selectValueColor="#004400" count="1" /> <RecordValue selectValueId="1693" selectValueName="Alternate Solution" selectValueDefaultFlag="False" selectValueColor="#66AAFF" count="1" /> <RecordValue selectValueId="1694" selectValueName="Implemented" selectValueDefaultFlag="False" selectValueColor="#33BB00" count="3" /> <RecordValue selectValueId="1695" selectValueName="Not Applicable" selectValueDefaultFlag="False" selectValueColor="#000000" count="0" /> <RecordValue selectValueId="1696" selectValueName="Not Implemented" selectValueDefaultFlag="True" selectValueColor="#990055" count="1" /> <RecordValue selectValueId="1697" selectValueName="Time Extension" selectValueDefaultFlag="False" selectValueColor="#665533" count="1" /> 
</Field>  
|  |  The Field element supports the following attributes: 

  * childFieldId. The integer ID of the field in the child application.
  * childModuleId. The integer ID of the child application used for finding the related records by querying the child application.
  * childModuleName. The string name of the child application.
  * moduleSearchPageNum. An integer for the search characteristics. It has no practical application within the API. 
  * moduleSearchViewId. An integer specifying how the results are displayed. It has no practical application within the API.
  * totalCount. An integer for the calculated value that appears in the Total for the record.

The RecordValue element supports the following attributes: 

  * selectValueId. The integer ID of the corresponding values list value.
  * selectValueName. The string value that is displayed for this values list value.
  * selectValueDefaultFlag. A Boolean indicating whether or not this values list item is the default value for the list.
  * selectValueColor. A string containing the value for the display color of the item. It has no practical application within the API.
  * count. An integer specifying how many related records are set to this value. 

