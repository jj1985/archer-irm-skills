# Keyword Search  
  
If you are using any keyword searching, you must include the Keywords element. If you are searching using filters, you can omit this sub-element.

The following table describes the Keywords element. Element |  Description  
---|---  
Keywords |  **Sample:** <Keywords value="password" /> The Keywords element has 1 attribute: value. Specify search keywords for the value attribute as you would if searching within the application. This element supports all query types supported in the application, for example, “important document", document*, receive~, important AND document. The API separates search terms with the OR operator by default. **Note:** To search for a quoted search string, for example, "password validation" to return records that contain a specific phrase only, format the element as follows:  
  
<Keywords value=" &quot; password validation &quot; " />
