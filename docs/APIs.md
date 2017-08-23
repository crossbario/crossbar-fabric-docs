title: Crossbar.io Fabric Center API Reference
toc: [Documentation, APIs]

# Crossbar.io Fabric Center API Reference

Crossbar.io Fabric Center (CFC) exposes a rich set of APIs to user management tools and applications.

Clients connect to CFC under one of two realms:

1. the CFC **global realm** (`com.crossbario.fabric`), exposing the **[Global API](Global-Api.md)**:

2. a user created **management realm** (eg `com.example.my-mgmt-realm1`), exposing the **[Management API](Management-Api.md)**

The former allows users to create new management realms, pair nodes with such realms and manage their user profiles.

The latter actually are for managing user nodes. Both Crossbar.io Fabric nodes and user management tools and apps connect to previously created management realms in regular operation.
