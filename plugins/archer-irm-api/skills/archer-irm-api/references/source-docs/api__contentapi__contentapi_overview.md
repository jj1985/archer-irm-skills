# Archer Content API

The Archer Content API acts as a translation layer that takes Archer Metadata and Content and converts them into logical entities so that those entities can be consumed in the same way that they are by users in the UI.

For information on Archer RESTful API see the Archer API Help on the [Archer Help Center](https://help.archerirm.cloud/archer_suite_help/Default.htm "Archer Help Center").

The UI is composed of 2 main area are:

  * End-user area. This area provides the translation and presents risk and compliance entities to the end users. Here you see lists of risks, business units, and vulnerabilities.

  * Administrator area. This is where administrators create instances of Archer domain objects to represent risk and compliance entities. Here see lists of applications, fields, and layouts. 

Record data fields are often stored in multiple places in the Archer database, but displayed in the end-user UI as field data on one screen. 

The available data that a Content API user can interact with is based on the permissions assigned to the user's session token. 

**Important:** In Archer Content API you cannot update a content record with the same values that are currently in the record. If you attempt to do this, the action fails and the message HTTP 400 displays.
