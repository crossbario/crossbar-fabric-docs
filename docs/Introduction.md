title: Introduction
toc: [Documentation, Introduction]

# Introduction

## What is Crossbar.io Fabric?

The Crossbar.io Fabric service builds on the [open source Crossbar.io messaging router](http://crossbar.io), and adds features for production deployments, such as remote management and monitoring.

Crossbar.io Fabric routers connect to the Crossbar.io Fabric Center online service.

Crossbar.io Fabric Center offers an API which allows the remote management and monitoring of the connected Crossbar.io Fabric routers.

This API can be accessed using the Crossbar.io Fabric Shell command line tool, or programmatically from your code.


## What can I do with this?

You can configure Crossbar.io Fabric nodes remotely - and at runtime.

Crossbar.io Fabric removes the need to restart the messaging router after each configuration change.

You can e.g.

* create or remove realms,
* start or stop a worker, and
* create or remove a role.

The API also allows remote retrieval of information about a node, e.g. get router worker logs.  

Remote access to the WAMP meta-API is also provided, so that you can, for example, get events about new session registrations.

## How do I access Crossbar.io Fabric?

There are presently two ways: using the Crossbar.io Fabric Shell, a command line interface, and raw access to the API from your code.

The shell still has limited functionality, but from code you can configure everything that you can control via the Crossbar.io configuration file.

We provide [numerous examples](Examples.md) for programmatic access.

Installation of the shell is covered in [Getting Started](Getting-Started.md).

## Getting Started

To get started, you need Docker and Python installed on your system, and then follow [these instructions](Getting-Started.md).


## Links

- [Getting started instructions](Getting-Started.md)
- [Examples](Examples.md)
- [background about Crossbar.io](http://crossbar.io)
