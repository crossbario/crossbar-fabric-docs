title: Global API
toc: [Documentation, API Reference, Global API]

# Global API

The global realm `com.crossbario.fabric` on Crossbar.io Fabric Center exposes the following APIs to clients.

---


## System API

Prefix: `crossbarfabriccenter.system.`

Status: **alpha**

* [ ] [crossbarfabriccenter.system.get_status](#crossbarfabriccentersystemget_status)
* [ ] [crossbarfabriccenter.system.on_tick](#crossbarfabriccentersystemon_tick)

---


## Management Realms API

Prefix: `crossbarfabriccenter.mrealm.`


### Management Realms API: Realms

Status: **alpha**

* [ ] [crossbarfabriccenter.mrealm.get_realms](#crossbarfabriccentermrealmget_realms)
* [ ] [crossbarfabriccenter.mrealm.get_realm](#crossbarfabriccentermrealmget_realm)
* [ ] [crossbarfabriccenter.mrealm.create_realm](#crossbarfabriccentermrealmcreate_realm)
* [ ] [crossbarfabriccenter.mrealm.delete_realm](#crossbarfabriccentermrealmdelete_realm)
* [ ] [crossbarfabriccenter.mrealm.on_realm_creating](#crossbarfabriccentermrealmon_realm_creating)
* [ ] [crossbarfabriccenter.mrealm.on_realm_created](#crossbarfabriccentermrealmon_realm_created)
* [ ] [crossbarfabriccenter.mrealm.on_realm_deleting](#crossbarfabriccentermrealmon_realm_deleting)
* [ ] [crossbarfabriccenter.mrealm.on_realm_deleted](#crossbarfabriccentermrealmon_realm_deleted)


### Management Realms API: Roles

Status: **under development**

* [ ] [crossbarfabriccenter.mrealm.get_roles](#crossbarfabriccentermrealmget_roles)
* [ ] [crossbarfabriccenter.mrealm.grant_role](#crossbarfabriccentermrealmgrant_role)
* [ ] [crossbarfabriccenter.mrealm.revoke_role](#crossbarfabriccentermrealmrevoke_role)
* [ ] [crossbarfabriccenter.mrealm.on_role_granted](#crossbarfabriccentermrealmon_role_granted)
* [ ] [crossbarfabriccenter.mrealm.on_role_revoked](#crossbarfabriccentermrealmon_role_revoked)


### Management Realms API: Nodes

Status: **alpha**

* [ ] [crossbarfabriccenter.mrealm.get_nodes](#crossbarfabriccentermrealmget_nodes)
* [ ] [crossbarfabriccenter.mrealm.get_node](#crossbarfabriccentermrealmget_node)
* [ ] [crossbarfabriccenter.mrealm.pair_node](#crossbarfabriccentermrealmpair_node)
* [ ] [crossbarfabriccenter.mrealm.unpair_node](#crossbarfabriccentermrealmunpair_node)
* [ ] [crossbarfabriccenter.mrealm.on_node_paired](#crossbarfabriccentermrealmon_node_paired)
* [ ] [crossbarfabriccenter.mrealm.on_node_unpaired](#crossbarfabriccentermrealmon_node_unpaired)

---


## Procedures Reference

Signature and descriptions of API procedures.

---


### crossbarfabriccenter.system.get_status

Return global CFC service status.

* **get_status** () -> status

where

* **status** (dict): service status information object:

```javascript
{
    // CFC version
    "version": "v17.8.1",

    // CFC global realm (being connected to)
    "realm": "com.crossbario.fabric",

    // CFC startup nonce
    "nonce": "ad80758d0c40098504aeb220022b84fc",

    // UTC system time (ISO 8601 format)
    "now": "2017-08-23T13:01:25.416Z",

    // CFC tick counter
    "tick": 982344
}
```

The startup nonce is a random value generated at CFC startup time and unchanged while running.

The CFC tick counter is started at a random integer value, and then incremented every 5 seconds.

---


### crossbarfabriccenter.mrealm.get_realms

Get list of names of management realms accessible to the user account.

* **get_realms** () -> [realm_name]

where

* **realm_name** (string): name of a management realm.

---


### crossbarfabriccenter.mrealm.get_realm

Return detailed information about a management realm.

* **get_realm** (realm_name) -> realm

where

* **realm_name** (string): name of the management realm to retrieve information for

and

* **realm** (dict): realm information object

---


### crossbarfabriccenter.mrealm.create_realm

Create a new management realm.

> Management realm names must be globally unique (within a given CFC installation)

* **create_realm** (realm_name) -> realm_created

where

* **realm_name** (string): name of the management realm to create

and

* **realm_created** (dict): realm creation information object

is returned:

```javscript
{
    // FIXME
}
```

The call does not return until the management realm has been completely created and all CFC side components for the management realm started.

When the new management realm *is being created*, an event

* **on_realm_creating** (realm_name)

is fired.

When the new management realm *has been completely created and started*, an event

* **on_realm_created** (realm_name, realm_created)

is fired.

---


### crossbarfabriccenter.mrealm.delete_realm

Delete an existing management realm.

Only owners of a management realm can delete the realm.

If the management realm currently has nodes paired, it cannot be deleted, unless `cascade=true` is used.

* **delete_realm** (realm_name, cascade) -> realm_deleted

where

* **realm_name** (string): name of the management realm to delete
* **cascade** (boolean): when the management realm to be deleted currently has nodes paired, automatically unpair the nodes (default: false)

and

* **realm_deleted** (dict): realm deletion information object

is returned:

```javscript
{
    // FIXME
}
```

The call does not return until the management realm has been completely deleted and all CFC side components for the management realm stopped.

When a management realm *is being deleted*, an event

* **on_realm_deleting** (realm_name)

is fired.

When the new management realm *has been completely stopped and deleted*, an event

* **on_realm_deleted** (realm_name, realm_deleted)

is fired.

---


### crossbarfabriccenter.mrealm.get_roles

Get all roles assigned to users on a given management realm.

* **get_roles** (realm_name) -> user_roles_map

where

* **realm_name** (string): the name of the management realm to get user roles for

and

* **user_roles_map** (dict): a mapping from user_ids (string) to list of roles (strings)

is returned.

---


### crossbarfabriccenter.mrealm.grant_role

Grant a role to a user on a management realm.

* **grant_role** (realm_name, user_id, role_name) -> role_granted

where

* **realm_name** (string): the name of the management realm on which to grant a role to a user
* **user_id** (string): the ID of the user to grant a role to
* **role_name** (string): the role to grant to the user (one of `[u'guest', u'developer', u'operator', u'admin', u'owner']`)

and

* **role_granted** (dict): role granted information object

is returned:

```javscript
{
    // FIXME
}
```

When the role has been granted successfully, an event

* **on_role_granted** (realm_name, user_id, role_granted)

is fired.

---


### crossbarfabriccenter.mrealm.revoke_role

Revoke a role from a user on a management realm.

* **revoke_role** (realm_name, user_id, role_name) -> role_revoked

where

* **realm_name** (string): the name of the management realm on which to revoke a role from a user
* **user_id** (string): the ID of the user to revoke the role from
* **role_name** (string): the role to revoke from the user (one of `[u'guest', u'developer', u'operator', u'admin', u'owner']`)

and

* **role_revoked** (dict): role revoked information object

is returned:

```javascript
{
    // FIXME
}
```

When the role has been revoked successfully, an event

* **on_role_revoked** (realm_name, user_id, role_revoked)

is fired.

---


### crossbarfabriccenter.mrealm.get_nodes

Get IDs of nodes currently paired with the management realm.

* **get_nodes** () -> [node_id]

where

* **node_id** (string): ID of a node (that is paired with the management realm)

is returned:

```javascript
["node1", "node2"]
```

> The order of IDs within the list returned is unspecified, but stable.

---


### crossbarfabriccenter.mrealm.get_node

Get detailed information about a node paired with the management realm.

* **get_node** (node_id) -> node

where

* **node_id** (string): ID of the node to get information for

and

* **node** (dict): node information object

is returned:

```javascript
{
    // FIXME
}
```

---


### crossbarfabriccenter.mrealm.pair_node

Pair a node with this management realm.

> Nodes are technically identified by their Ed25519 public key, and no two nodes will have the same public key. A given node can only be paired to (at most) one management realm at a time).

* **pair_node** (pubkey, realm_name, node_id, authextra) -> node_paired

where

* **pubkey** (string): the public key (Hex) of the node to pair
* **realm_name** (string): name of the management realm to pair the given node with
* **node_id** (string): the node ID to assign the node (this will be the `authid` under which the node will be authenticated)
* **authextra** (dict): optional extra information to store in CFC, and to hand out to the node when it is authenticating

and

* **node_paired** (dict): node paired information object

is returned:

```javscript
{
    // FIXME
}
```

When the node has been paired successfully, an event

* **on_node_paired** (realm_name, node_id, node_paired)

is fired.

---


### crossbarfabriccenter.mrealm.unpair_node

Unpair a node currently paired to a management realm from that realm.

* **unpair_node** (pubkey) -> node_unpaired

where

* **pubkey** (string): the public key (Hex) of the node to unpair

and

* **node_unpaired** (dict): node unpaired information object

is returned:

```javascript
{
    // FIXME
}
```

When the node has been unpaired successfully, an event

* **on_node_unpaired** (realm_name, node_id, node_unpaired)

is fired.

---


## Events Reference

Signature and descriptions of API events.

---


### crossbarfabriccenter.system.on_tick

CFC global status/heartbeat event generated every 5 seconds.

* **on_tick** (ticked)

where

* **ticked** (dict): ticked information:

```javascript
{
    // current CFC system time in ISO 8601 format
    "now": "2017-08-23T13:01:25.416Z",

    // CFC tick: initialized with a random integer when CFC starts,
    // and incremented every 5 seconds
    "tick": 89014
}
```

---


### crossbarfabriccenter.mrealm.on_realm_creating

Event generated when a management realm is being created and started.

* **on_realm_creating** (realm_name, realm_creating)

where

* **realm_name** (string): the name of the realm being created
* **realm_creating** (dict): realm creating information object:

```javascript
{
    // FIXME
}
```

---


### crossbarfabriccenter.mrealm.on_realm_created

Event generated when a management realm has been created and fully started.

* **on_realm_created** (realm_name, realm_created)

where

* **realm_name** (string): the name of the realm that was created
* **realm_created** (dict): realm created information object:

```javascript
{
    // FIXME
}
```

---


### crossbarfabriccenter.mrealm.on_realm_deleting

Event generated when a management realm is being stopped and deleted.

* **on_realm_deleting** (realm_name, realm_deleting)

where

* **realm_name** (string): the name of the realm that is being deleted
* **realm_deleting** (dict): realm deleting information object:

```javascript
{
    // FIXME
}
```

---


### crossbarfabriccenter.mrealm.on_realm_deleted

Event generated when a management realm has been fully stopped and deleted.

* **on_realm_deleted** (realm_name, realm_deleted)

where

* **realm_name** (string): the name of the realm that was deleted
* **realm_deleted** (dict): realm deleted information object:

```javascript
{
    // FIXME
}
```

---


### crossbarfabriccenter.mrealm.on_role_granted

Event generated when a role has been granted to a user on a management realm.

* **on_role_granted** (realm_name, user_id, role_granted)

where

* **realm_name** (string): the name of the realm on which a role was granted to a user
* **user_id** (string): the ID of the user a role was granted to
* **role_granted** (dict): role granted information object:

```javascript
{
    // FIXME
}
```

---


### crossbarfabriccenter.mrealm.on_role_revoked

Event generated when a role has been revoked from a user on a management realm.

* **on_role_revoked** (realm_name, user_id, role_revoked)

where

* **realm_name** (string): the name of the realm on which a role was revoked from a user
* **user_id** (string): the ID of the user a role was revoked from
* **role_revoked** (dict): role revoked information object:

```javascript
{
    // FIXME
}
```

---


### crossbarfabriccenter.mrealm.on_node_paired

Event generated when a node has been successfully paired with a management realm.

* **on_node_paired** (realm_name, node_id, node_paired)

where

* **realm_name** (string): name of the management realm the node was paired with
* **node_id** (string): the ID of the node was paired under
* **node_paired** (dict): node pairing information object:

```javascript
{
    // FIXME
}
```

---


### crossbarfabriccenter.mrealm.on_node_unpaired

Event generated when a node has been successfully unpaired from a management realm.

* **on_node_unpaired** (realm_name, node_id, node_unpaired)

where

* **realm_name** (string): name of the management realm the node was unpaired from
* **node_id** (string): the ID of the node was unpaired
* **node_unpaired** (dict): node unpairing information object:

```javascript
{
    // FIXME
}
```

---
