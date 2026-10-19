# Updating Locked Records (WS)

Archer has an important feature that prevents the updating or altering of a locked record. A record becomes locked when a user has opened it in Edit mode for the purpose of modifying it.

However, it is important to note that records can be updated through the RESTful and Web APIs, as well as through data feeds, even when a user has locked them. The following are examples of typical APIs that can update user-locked records:

  * PUT content (RESTful )
  * UpdateRecord (Web Services)
  * UpdateRecords (Web Services)

