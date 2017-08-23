title: Global API
toc: [Documentation, API Reference, Global API]

# Global API

The global realm `com.crossbario.fabric` on Crossbar.io Fabric Center exposes the following APIs to clients:

**Procedures**

* *System*
    * [crossbarfabriccenter.system.get_status](#crossbarfabriccentersystemget_status)
* *Management Realms*
    * [crossbarfabriccenter.mrealm.get_management_realms](#crossbarfabriccentermrealmget_management_realms)
    * [crossbarfabriccenter.mrealm.get_management_realm](#crossbarfabriccentermrealmget_management_realm)
    * [crossbarfabriccenter.mrealm.create_management_realm](#crossbarfabriccentermrealmcreate_management_realm)
    * [crossbarfabriccenter.mrealm.delete_management_realm](#crossbarfabriccentermrealmdelete_management_realm)
    * [crossbarfabriccenter.mrealm.get_realm_roles](#crossbarfabriccentermrealmget_realm_roles)
    * [crossbarfabriccenter.mrealm.grant_realm_role](#crossbarfabriccentermrealmgrant_realm_role)
    * [crossbarfabriccenter.mrealm.revoke_realm_role](#crossbarfabriccentermrealmrevoke_realm_role)
    * [crossbarfabriccenter.mrealm.get_nodes](#crossbarfabriccentermrealmget_nodes)
    * [crossbarfabriccenter.mrealm.get_node](#crossbarfabriccentermrealmget_node)
    * [crossbarfabriccenter.mrealm.pair_node](#crossbarfabriccentermrealmpair_node)
    * [crossbarfabriccenter.mrealm.unpair_node](#crossbarfabriccentermrealmunpair_node)

**Events**

* *System*
    * [crossbarfabriccenter.system.on_tick](#crossbarfabriccentersystemon_tick)
* *Management Realms*
    * [crossbarfabriccenter.mrealm.on_management_realm_creating](#crossbarfabriccentermrealmon_management_realm_creating)
    * [crossbarfabriccenter.mrealm.on_management_realm_created](#crossbarfabriccentermrealmon_management_realm_created)
    * [crossbarfabriccenter.mrealm.on_management_realm_deleting](#crossbarfabriccentermrealmon_management_realm_deleting)
    * [crossbarfabriccenter.mrealm.on_management_realm_deleted](#crossbarfabriccentermrealmon_management_realm_deleted)
    * [crossbarfabriccenter.mrealm.on_role_granted](#crossbarfabriccentermrealmon_role_granted)
    * [crossbarfabriccenter.mrealm.on_role_revoked](#crossbarfabriccentermrealmon_role_revoked)
    * [crossbarfabriccenter.mrealm.on_node_paired](#crossbarfabriccentermrealmon_node_paired)
    * [crossbarfabriccenter.mrealm.on_node_unpaired](#crossbarfabriccentermrealmon_node_unpaired)

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

    // UTC system time (ISO 8601 format)
    "now": "2017-08-23T13:01:25.416Z",

    // CFC startup time (ISO 8601 format)
    "started": "2017-05-23T13:01:25.416Z",

    // CFC uptime in seconds
    "uptime": 8123,

    // CFC tick counter
    "tick": 982344
}
```

---


### crossbarfabriccenter.mrealm.get_management_realms

Get list of names of management realms accessible to the user account.

* **get_management_realms** () -> [realm_name]

where

* **realm_name** (string): name of a management realm.

---


### crossbarfabriccenter.mrealm.get_management_realm

Return detailed information about a management realm.

* **get_management_realm** (realm_name) -> realm

where

* **realm_name** (string): name of the management realm to retrieve information for

and

* **realm** (dict): realm information object

---


### crossbarfabriccenter.mrealm.create_management_realm

Create a new management realm.

> Management realm names must be globally unique (within a given CFC installation)

* **create_management_realm** (realm_name) -> realm_created

where

* **realm_name** (string): name of the management realm to create

and

* **realm_created** (dict): realm creation information object

The call does not return until the management realm has been completely created and all CFC side components for the management realm started.

When the new management realm *is being created*, an event

* **on_management_realm_creating** (realm_name, realm_creating)

is fired.

When the new management realm *has been completely created and started*, an event

* **on_management_realm_created** (realm_name, realm_created)

is fired.

---


### crossbarfabriccenter.mrealm.delete_management_realm

Delete an existing management realm.

Only owners of a management realm can delete the realm.

If the management realm currently has nodes paired, it cannot be deleted, unless `cascade=true` is used.

* **delete_management_realm** (realm_name, cascade) -> realm_deleted

where

* **realm_name** (string): name of the management realm to delete
* **cascade** (boolean): when the management realm to be deleted currently has nodes paired, automatically unpair the nodes (default: false)

and

* **realm_deleted** (dict): realm deletion information object

The call does not return until the management realm has been completely deleted and all CFC side components for the management realm stopped.

When a management realm *is being deleted*, an event

* **on_management_realm_deleting** (realm_name, realm_deleting)

is fired.

When the new management realm *has been completely stopped and deleted*, an event

* **on_management_realm_deleted** (realm_name, realm_deleted)

is fired.

---


### crossbarfabriccenter.mrealm.get_realm_roles

Get all roles assigned to users on a given management realm.

* **get_realm_roles** (realm_name) -> user_roles_map

where

* **realm_name** (string): the name of the management realm to get user roles for

and

* **user_roles_map** (dict): a mapping from user_ids (string) to list of roles (strings)

is returned.

---


### crossbarfabriccenter.mrealm.grant_realm_role

Grant a role to a user on a management realm.

* **grant_realm_role** (realm_name, user_id, role_name) -> role_granted

where

* **realm_name** (string): the name of the management realm on which to grant a role to a user
* **user_id** (string): the ID of the user to grant a role to
* **role_name** (string): the role to grant to the user (one of `[u'guest', u'developer', u'operator', u'admin', u'owner']`)

and

* **role_granted** (dict): role granted information object

is returned.

When the role has been granted successfully, an event

* **on_role_granted** (realm_name, user_id, role_granted)

is fired.

---


### crossbarfabriccenter.mrealm.revoke_realm_role

Revoke a role from a user on a management realm.

* **grant_realm_role** (realm_name, user_id, role_name) -> role_granted

where

* **realm_name** (string): the name of the management realm on which to revoke a role from a user
* **user_id** (string): the ID of the user to revoke the role from
* **role_name** (string): the role to revoke from the user (one of `[u'guest', u'developer', u'operator', u'admin', u'owner']`)

and

* **role_revoked** (dict): role revoked information object

is returned.

When the role has been revoked successfully, an event

* **on_role_revoked** (realm_name, user_id, role_revoked)

is fired.

---


### crossbarfabriccenter.mrealm.get_nodes

Get IDs of nodes currently paired with the management realm.

* **get_nodes** () -> [node_id]

where

* **node_id** (string): ID of a node (that is paired with the management realm)

---


### crossbarfabriccenter.mrealm.get_node

Get detailed information about a node paired with the management realm.

* **get_node** (node_id) -> node

where

* **node_id** (string): ID of the node to get information for

and

* **node** (dict): node information object

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

* **ticked** (dict): ticked information

```javascript
{
    // current system time in ISO 8601 format
    "now": "2017-08-23T13:01:25.416Z",

    // tick count since system start
    "tick": 89014
}
```

---


### crossbarfabriccenter.mrealm.on_management_realm_creating

Event generated when a management realm is being created and started.

---


### crossbarfabriccenter.mrealm.on_management_realm_created

Event generated when a management realm has been created and fully started.

---


### crossbarfabriccenter.mrealm.on_management_realm_deleting

Event generated when a management realm is being stopped and deleted.

---


### crossbarfabriccenter.mrealm.on_management_realm_deleted

Event generated when a management realm has been fully stopped and deleted.

---


### crossbarfabriccenter.mrealm.on_role_granted

Event generated when a role has been granted to a user on a management realm.

---


### crossbarfabriccenter.mrealm.on_role_revoked

Event generated when a role has been revoked from a user on a management realm.

---


### crossbarfabriccenter.mrealm.on_node_paired

Event generated when a node has been successfully paired with a management realm.

---


### crossbarfabriccenter.mrealm.on_node_unpaired

Event generated when a node has been successfully unpaired from a management realm.

---
