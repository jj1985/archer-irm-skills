# Result Display (Search Input)

The following table describes elements that define result display settings for the search. Use these elements with the [search.ExecuteSearch](executesearch.htm) method.

**Important:** You can use only 1 of these elements, not both.

Element |  Description  
---|---  
DisplayFields |  **Sample:** <DisplayFields>

<DisplayField>12972</DisplayField> <DisplayField>{0BDF0A10-F0FF-43B9-869B-6F5A00BF1DCC}</DisplayField> 
</DisplayFields> The fields to display in the search results.  **Note:** This element requires the DisplayFieldsub-element to specify each field to display. Use the GUID or SQL field ID for the field.  
ContainedDisplayFields  |  **Sample** : <ContainedDisplayFields>

<ContainedDisplayField> <Field>12977</Field> <DisplayFields> <DisplayField>12972</DisplayField> </DisplayFields> </ContainedDisplayField> 
</ContainedDisplayFields> Defines how to display lists of values returned from a field. This element is used for searches within fields that contain other fields, such as sub-forms or history log fields. The following table describes ContainedDisplayeFields sub-elements. | Element | Details  
---|---  
ContainedDisplayField |  The root of the display criteria for each set of parent and child fields to display.  **Note:** This element requires the Field and DisplayFields sub-elements.   
Field |  The field that contains the lists of values that you want to display.  **Note:** Use the GUID or the SQL field ID for the field.  
DisplayFields |  The fields to display for the search.  **Note:** This element requires the DisplayField sub-element to specify each field to display. Use the GUID or the SQL field ID for the field.
