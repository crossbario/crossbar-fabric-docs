title: Getting Started
toc: [Documentation, Getting Started]

# Getting Started

This section explains how to run register with the Crossbar.io Fabric Center online service (CFC), get and run a Crossbar.io Fabric instance, pair that instance with the Crossbar.io Fabric Center service, as well as some basic example configuration actions.


## Basic Concepts

You register with the CFC via the Crossbar.io Fabric Shell. This also handles the authentication for the examples contained in this repository.

Open source versions of Crossbar.io cannot connect to the CFC. This requires a closed source version, Crossbar.io Fabric.

Within the CFC, you can create multiple management realms (but need to create only a single one initially). Crossbar.io Fabric nodes connect to a specific management realm.

You can then access and manage the Crossbar.io Fabric nodes via the CFC API.

The Crossbar.io Fabric Shell as well as the included example code use this API.

## Requirements

You will need

* Docker
* Python 3 (and [virtualenv](https://virtualenv.pypa.io/))

installed on your machine.

Everything here assumes a Linux/\*nix machine. (Things may work on other systems, but are not tested by us.)

## Fabric Nodes

We provide a Docker image of Crossbar.io Fabric.

Start a Crossbar.io Fabric Docker container which connects to the CFC:

    docker run -it --rm crossbario/crossbar-fabric:latest

> Note: above will pull the Crossbar.io Fabric Docker image for x86-64. For ARM (32 bit) based devices like the Pi, use the `crossbario/crossbar-fabric-armhf` image. For ARM 64 bit based devices, use the `crossbario/crossbar-fabric-aarch64` image.

As the node is started the first time, a new node public/private key pair is generated.

This key pair is then used when authenticating to CFC.

The node public key needs to be assigned to a management realm ("paire").

Pairing a node with a management realm can be done via Crossbar.io Fabric Shell and programatically via the CFC API today, and we are working on a Web user interface.


## Fabric Shell

[Crossbar.io Fabric Shell](https://github.com/crossbario/crossbar-fabric-shell) is a management client Python package that includes

* an interactive management shell
* a management client library

We'll go throught the steps of

* installing the shell
* creating a CFC user account
* pairing the Crossbar.io Fabric node we just started
* getting basic information about this node


### Installation

To install Python 3 and virtualenv (on Debian/Ubuntu):

```console
sudo apt-get install -y python3 python3-pip python3-venv
```

To install, create a new dedicated Python virtualenv, activate it and install Crossbar.io Fabric Shell [from PyPI](https://pypi.python.org/pypi/crossbarfabricshell) in there:

```console
virtualenv ~/.cbsh
source ~/.cbsh/bin/activate
pip install crossbarfabricshell
```

> Note: we do not recommend installing cbsh into a Python environment shared with other applications, or shared system wide. cbsh is well packaged and follows best practices, but we cannot support all combinations of dependencies. A Python virtualenv comes with a good compromise for isolation versus overhead.

### Registration

Now register for Crossbar.io Fabric Center by running:

```console
cbsh auth
```

This will ask for an email address, to which an activation code is sent.

It will also create a pair of public an private key files and the default configuration:

```console
(cpy362_1) oberstet@thinkpad-t430s:~$ ll ~/.cbf/
insgesamt 20
drwxrwxr-x  2 oberstet oberstet 4096 Aug 14 13:16 ./
drwxr-xr-x 94 oberstet oberstet 4096 Aug 20 21:49 ../
-rw-rw-r--  1 oberstet oberstet   78 Aug 14 13:16 config.ini
-rw-------  1 oberstet oberstet  332 Aug 14 13:16 default.priv
-rw-r--r--  1 oberstet oberstet  227 Aug 14 13:16 default.pub
```

Keep the `default.priv` private key file safe!

Once you've received the activation code, authenticate yourself by doing:

```console
cbsh auth --code <YOUR ACTIVATION CODE>
```

When successful, this will print out a short welcome notice and then exit again.

For subsequent access, the shell will use the private key.

### Starting the shell

Start the shell in interactive mode:

```console
cbsh
```

This will bring up a full screen console mode interactive shell.


### Creating a Management Realm

To create a CFC management realm for your CF nodes, start cbsh and enter

    create management-realm <realm-name>

Here, chose a `<realm-name` for your management realm. The name must be unique globally within CFC.


### Pairing a node

To pair a CF node to a management realm, start cbsh and enter

    pair node <public-key> <realm-name> <node-id>

Your node's public key Hex value (to use as <public-key>) is printed to the log when the node starts.

Use the name of the management realm you just created for `<realm-name>`.

Finally, chose a `<node-id>` the node should be assigned to. The node ID needs to be unique within the management realm.


### Managing the node

The Crossbar.ioi Fabric node you have paired only has the node controller running.

In order for it to perform any WAMP routing function, you need to start a router worker in the node.

The Crossbar.io Fabric Shell is still mostly under construction, so for the time being you need to access the Crossbar.io Fabric service API from code.
