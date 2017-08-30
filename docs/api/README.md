title: APIs
toc: [Documentation, APIs]

# APIs

Crossbar.io Fabric Center (CFC) exposes a rich set of APIs to user management tools and applications.

## API Reference

Clients connect to CFC under one of the following two realms, and depending on which of the two kinds of realm the client connects to, a different API is exposed:

* **[Global API](Global-API.md)** exposed on the CFC **global realm** (`com.crossbario.fabric`)
* **[Management API](Management-API.md)** exposed on every user created **management realm** (eg `my-realm1`)

The former allows users to create new management realms, pair nodes with such realms and manage their user profiles.

The latter actually are for managing user nodes. Both Crossbar.io Fabric nodes and user management tools and apps connect to previously created management realms in regular operation.

## Namespaces and Licenses

For an overview of the different API namespaces available in Crossbar.io OSS, Crossbar.io Fabric and Crossbar.io Fabric Center, and the respective API licenses that apply, please see:

* **[Namespaces and Licenses](Namespaces-and-Licenses.md)**

---
