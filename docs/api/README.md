title: API Reference
toc: [Documentation, APIs]

# API Reference

Crossbar.io Fabric Center (CFC) exposes a rich set of APIs to user management tools and applications.

Clients connect to CFC under one of two realms:

1. **[Global API](Global-API.md)** exposed on the CFC **global realm** (`com.crossbario.fabric`)

2. **[Management API](Management-API.md)** exposed on every user created **management realm** (eg `my-realm1`)

The former allows users to create new management realms, pair nodes with such realms and manage their user profiles.

The latter actually are for managing user nodes. Both Crossbar.io Fabric nodes and user management tools and apps connect to previously created management realms in regular operation.
