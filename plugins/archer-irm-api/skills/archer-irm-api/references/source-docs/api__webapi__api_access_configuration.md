# API Access Configuration

All Web Services API calls require valid user credentials to be submitted before the calling application gains access. The privileges that you grant different users depend on the functions that they need to perform. 

**Important:** Web Services API privileges and Archer privileges are shared. For example, if a Platform user has Read privileges to a certain application, that user is now able to use Web Services API calls that require Read permissions for that application.

The following rules offer insight into the required level of access for a method:

  * Methods that start with Create require Create permissions.
  * Methods that start with the following words require Read permissions:
    * Check
    * Does
    * Get
    * Lookup
    * Retrieve
    * Search
  * Methods that start with the following words require Update permissions:
    * Add
    * Associate
    * Bind
    * Change
    * Disassociate
    * Force
    * Set
    * Unbind
    * Update
    * User
  * Methods that start with the following words require Delete permissions:
    * Delete
    * Remove
    * Terminate

For more information on the permissions required for each web services, see the individual web service methods.
