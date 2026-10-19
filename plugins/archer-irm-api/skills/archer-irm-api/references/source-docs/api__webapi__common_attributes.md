# Common Attributes

The following attributes are common to all field types: 

  * id. The id attribute of every field element represents the unique ID (identification code) of the field. This information is documented in the Application Detail Report in the Application Builder, and it is also visible in the results of the [record.GetRecordById method](getrecordbyid.htm).
  * type. The type attribute of every field element represents the type of field as documented in the second column of the [Field-Specific Attributes](field-specific_attributes.htm) table. The value is an integer representation of the type as reported within the Application Builder.
  * createDate. The createDate attribute shows when the field's value was first entered. The value of the attribute is shown in the MM/DD/YYY HH:MM:SS AM or PM format, for example, 10/15/2003 4:19:04 PM.
  * updateDate. The updateDate attribute shows when the field's value was last modified. The value of the attribute is shown in the MM/DD/YYY HH:MM:SS AM or PM format, for example, 11/24/2003 8:11:23 AM.
  * createLogin. The createLogin attribute shows the userId of the user who created the record. The value of the attribute is an integer, for example, 791.
  * updateLogin. The updateLogin attribute shows the userId of the user who last modified the field. The value of the attribute is an integer, for example, 1004.

