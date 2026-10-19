# Module Definition

A module is an application or a questionnaire. This section specifies the module that you want to search. Use these elements with either the [search.ExecuteSearch](executesearch.htm) or [search.ExecuteStatisticSearch](executestatisticsearch.htm) methods.

The following table describes module elements. Element |  Description  
---|---  
ModuleCriteria |  The ModuleCriteria element is the root of the module definition and takes no attributes. You can specify the following sub-elements in this table under ModuleCriteria root element.  
Module |  **Sample:** <Module>764</Module> The GUID or SQL ID of the primary application or questionnaire to search.  
IsKeywordModule |  **Sample:** <IsKeywordModule>false</IsKeywordModule> Determines whether to search this module for keywords. Possible values: 

  * True
  * False

**Note:** This element is required if you are performing a keyword search. Otherwise, the default is false.   
Buildout  
Relationship |  **Sample:** <BuildoutRelationship>Union  
</BuildoutRelationship> Determines whether to search the module using an outer join (Union) or an inner join (Intersection). Possible values: 

  * Union
  * Intersection

**Note:** This element is not required. The default is Union.  
Leveled  
BuildoutOptions |  **Sample:** <LeveledBuildoutOptions>BuildUp  
</LeveledBuildoutOptions> When searching leveled modules, this element determines whether to search parent modules (build up). Possible value: BuildUp **Note:** This element is not required. The default is None.  
SortFields |  **Sample** : <SortFields>

<SortField> <Field>12972</Field> <SortType>Ascending</SortType> </SortField> 
</SortFields> Defines the sort criteria. The following table describes SortFields sub-elements. | Element | Description  
---|---  
SortField |  The container for each field to sort. It takes no attributes. You can specify the following sub-elements in this table under the SortField root element.  
Field |  The field to sort by. Use the GUID or the SQL field ID for that field. **Note:** If you supply multiple Field values, they are resolved in the order you entered them.  
SortType |  The type of sort for this field. Possible values: 

  * Ascending
  * Descending 

  
Children |  **Sample** : <Children>

<ModuleCriteria> <Module>765</Module> <IsKeywordModule>false</IsKeywordModule> <BuildoutRelationship>Union  
</BuildoutRelationship> <LeveledBuildoutOptions>BuildDown  
</LeveledBuildoutOptions> <SortFields> <SortField> <Field>12976</Field> <SortType>Ascending</SortType> </SortField> </SortFields> </ModuleCriteria> 
</Children> For modules that are related to other modules using a cross-reference field or a related-records relationship, the Children element defines each child module to include in the search. It takes the same elements as the module definition.
