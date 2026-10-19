# Filter  
  
The following table describes the optional elements that allow you to filter your results. Each element is a nested structure containing information. Element |  Description  
---|---  
Matching |  **Sample:** <Matching>

<Field id="7612"> <Include noValues="1"> <Value value="1740" /> </Include> </Field> 
</Matching> The Matching element allows you to create filters based on records with specific values-list values. It supports 1 or more Field child elements. If you do not want to use this type of filter, omit the whole Matching element rather than including an empty 1. The following table describes the Field, Include and Exclude, and Value elements. |  Element |  Description  
---|---  
Field |  The Field element has an id attribute that holds the identification number of the field in which to use the filter. Typically, this support is limited to values list fields. The Field element requires at least 1 of its 2 child elements: Include and Exclude.  
Include   
and  
Exclude  |  Each of these elements has a noValues attribute that allows you specify the No Selection value. Setting the value to 0 omits those records from the element. A value of 1 includes the records. Additionally, each of these supports (and requires) a Value child element.   
Value |  The Value element has a required attribute of the same name: value using lowercase letters. Use the [ValuesListValueId](getvalueslistitem.htm) of the item on which you want to filter.
