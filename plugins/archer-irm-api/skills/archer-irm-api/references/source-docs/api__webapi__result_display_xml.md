# Result Display (Legacy Search Input)  
  
The following table describes elements that are required unless otherwise stated. Element |  Description  
---|---  
Display |  **Sample:** <Display>

<Field id="7609" /> <Field id="7606" /> 
</Display> This element has no attributes, but it requires you to specify Field sub-elements.  
Field |  **Sample:** <Field id="7609" /> The Field element has just 1 attribute: id. The value of this attribute is the identification number of a field as shown in the Application Detail Report generated from Application Builder or seen using the [record.GetRecordbyId](getrecordbyid.htm)[ ](getrecordbyid.htm)method.  
KeywordModules |  **Sample:** <KeywordModules>

<Module id="101" /> 
</KeywordModules> This element has no attributes, but it requires you to specify Module sub-elements.  
Module |  **Sample:** <Module id="101" /> The Module element has just 1 attribute: id. The value of this attribute is the identification number of the application in which you want to search. To obtain the Module id, view the Application Detail Report in the Platform, and record the value of the Application ID. This value serves as the Module ID.  
Primary Sort  |  **Sample:** <PrimarySort id="7606" order="ASC" /> This element requires 2 attributes: 

  * id. This attribute is the Field id of the field that you want to use as the primary sort field in the results.
  * order. This attribute has 2 acceptable values that specify how you sort:
    * ASC (ascending sort order).
    * DESC (descending sort order).

  
Secondary Sort |  **Sample:** <SecondarySort id="7609" order="ASC" /> This is an optional element. It requires 2 attributes: 

  * id. This attribute is the Field id of the field that you want to use as the secondary sort field in the results.
  * order. This attribute has 2 acceptable values that specify how you sort:
    * ASC (ascending sort order).
    * DESC (descending sort order).

  
Display Format  |  **Sample:** <DisplayFormat value="3" /> This element defines how to format the results. Currently, the only value supported is 3 – Summary format.
