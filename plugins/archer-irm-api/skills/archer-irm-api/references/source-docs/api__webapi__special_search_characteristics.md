# Special Search Characteristics

The following table describes optional elements that can be used to allow non-default searching. Element |  Description  
---|---  
Content Review |  **Sample:** <Workflow value="1" /> When set to "1", the value attribute allows you to configure the search to return records that are enrolled in workflow. Setting the value attribute to "0" has the same result as omitting the element.   
Published |  **Sample:** <Published value="1" /> When set to "1", the value attribute allows you to configure the search to return records that are published (the same as omitting the element). Setting the value attribute to "0" excludes any published records from the results.  
MyRecord |  **Sample:** <MyRecord value="1" /> When set to "1", the value attribute allows you to configure the search to return all records. Setting the value attribute to "0" excludes any records that are not owned by or permissioned to the application account, which is the same as omitting the element. This element is useful when searching applications with record permissions. To use this ability (value="1"), you must configure the account with an access role for which the Members of this role can view all records in associated applications. 
