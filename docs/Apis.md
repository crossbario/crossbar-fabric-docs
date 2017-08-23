title: Crossbar.io Fabric Center API Reference
toc: [Documentation, API Reference]

# Crossbar.io Fabric Center API Reference

Crossbar.io Fabric Center (CFC) exposes a rich set of APIs to user management tools and applications.

Clients connect to CFC under one of two realms: the **Fabric realm** (`com.crossbario.fabric`), exposing the **[Global API](Global-Api.md)**:


2. **[Management API](Management-Api.md)** a specific, user created **management realm** (eg `com.example.my-mgmt-realm1`), exposing the

The former allows users to create new management realms, pair nodes with such realms and manage their user profiles.

The latter actually are for managing user nodes. Both Crossbar.io Fabric nodes and user management tools and apps connect to previously created management realms in regular operation.
