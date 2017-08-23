# Accounts Realm API

The global **accounts realm** (`com.crossbario.fabric`) on Crossbar.io Fabric Center exposes the following API to clients:

* [General](#general)
    * [crossbarfabriccenter.account.get_status](#crossbarfabriccenterserviceget_status)
* [Management Realms](#management-realms)
    * [crossbarfabriccenter.account.get_management_realms](#crossbarfabriccenteraccountget_management_realms)
    * [crossbarfabriccenter.account.get_management_realm](#crossbarfabriccenteraccountget_management_realm)
    * [crossbarfabriccenter.account.create_management_realm](#crossbarfabriccenteraccountcreate_management_realm)
    * [crossbarfabriccenter.account.delete_management_realm](#crossbarfabriccenteraccountdelete_management_realm)
    * [crossbarfabriccenter.account.get_realm_roles](#crossbarfabriccenteraccountget_realm_roles)
    * [crossbarfabriccenter.account.grant_realm_role](#crossbarfabriccenteraccountgrant_realm_role)
    * [crossbarfabriccenter.account.revoke_realm_role](#crossbarfabriccenteraccountrevoke_realm_role)
    * [crossbarfabriccenter.account.get_nodes](#crossbarfabriccenteraccountget_nodes)
    * [crossbarfabriccenter.account.get_node](#crossbarfabriccenteraccountget_node)
    * [crossbarfabriccenter.account.pair_node](#crossbarfabriccenteraccountpair_node)
    * [crossbarfabriccenter.account.unpair_node](#crossbarfabriccenteraccountunpair_node)

---


## Procedures Reference

Signature and descriptions of API procedures.

---


### crossbarfabriccenter.account.get_status

Return global account service status information.

* **get_status** () -> status

where

* **status** (dict): status information object

---


### crossbarfabriccenter.account.get_management_realms

Get list of names of management realms accessible to the user account.

* **get_management_realms** () -> [realm_name]

where

* **realm_name** (string): name of a management realm.

---


### crossbarfabriccenter.account.get_management_realm

Return detailed information about a management realm.

* **get_management_realm** (realm_name) -> realm

where

* **realm_name** (string): name of the management realm to retrieve information for

and

* **realm** (dict): realm information object

---


### crossbarfabriccenter.account.create_management_realm

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


### crossbarfabriccenter.account.delete_management_realm

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


### crossbarfabriccenter.account.get_realm_roles

Get all roles


### crossbarfabriccenter.account.grant_realm_role

### crossbarfabriccenter.account.revoke_realm_role


### crossbarfabriccenter.account.get_nodes

Get IDs of nodes currently paired with the management realm.

* **get_nodes** () -> [node_id]

where

* **node_id** (string): ID of a node (that is paired with the management realm)

---


### crossbarfabriccenter.account.get_node

Get detailed information about a node paired with the management realm.

* **get_node** (node_id) -> node

where

* **node_id** (string): ID of the node to get information for

and

* **node** (dict): node information object

---


### crossbarfabriccenter.account.pair_node

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


### crossbarfabriccenter.account.unpair_node

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
