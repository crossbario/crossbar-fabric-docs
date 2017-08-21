# Crossbar.io Fabric Public

The repository contains the public documentation (source), example source code and user issues for Crossbar.io Fabric:

* [Crossbar.io Fabric Documentation (Source)](docs)
* [Crossbar.io Fabric Examples](examples)
* [Crossbar.io Fabric Issue Tracker](https://github.com/crossbario/crossbar-fabric-public/issues)

---

## Getting Started

### Requirements

You will need

* Docker
* Python 3 (and [virtualenv](https://virtualenv.pypa.io/))

We will use Docker to start a Crossbar.io Fabric node locally. The node will connect to Crossbar.io Fabric Center, which allows the node to be managed and monitored remotely.

Management clients, such as Crossbar.io Fabric Shell, or custom user programs and scripts can connect to Crossbar.io Fabric Center to remotely and dynamically manage the Crossbar.io Fabric nodes connected to the respective management realm.


### Fabric Shell

[Crossbar.io Fabric Shell](https://github.com/crossbario/crossbar-fabric-shell) is a management client Python package that includes

* an interactive management shell
* a management client library

To install, create a new dedicated Python virtualenv, activate it and install Crossbar.io Fabric Shell [from PyPI](https://pypi.python.org/pypi/crossbarfabricshell) in there:

```console
virtualenv ~/.cbsh
source ~/.cbsh/bin/activate
pip install crossbarfabricshell
```

> Note: we do not recommend installing cbsh into a Python environment shared with other applications, or shared system wide. cbsh is well packaged and follows best practices, but we cannot support all combinations of dependencies. A Python virtualenv comes with a good compromise for isolation versus overhead.

Now register or login to Crossbar.io Fabric Center by running:

```console
cbsh auth
```

This will ask for an email address, and otherwise optionally allows to set a customer CFC URL, which should be left at default.

On a fresh system, the following files will be generated:

```console
(cpy362_1) oberstet@thinkpad-t430s:~$ ll ~/.cbf/
insgesamt 20
drwxrwxr-x  2 oberstet oberstet 4096 Aug 14 13:16 ./
drwxr-xr-x 94 oberstet oberstet 4096 Aug 20 21:49 ../
-rw-rw-r--  1 oberstet oberstet   78 Aug 14 13:16 config.ini
-rw-------  1 oberstet oberstet  332 Aug 14 13:16 default.priv
-rw-r--r--  1 oberstet oberstet  227 Aug 14 13:16 default.pub
```

The `default.priv` and `default.pub` are your private and public key files. Keep the `default.priv` safe!

The `config.ini` is the main cbsh configuration file:

```
(cpy362_1) oberstet@thinkpad-t430s:~$ cat ~/.cbf/config.ini
[default]

url=wss://fabric.crossbario.com/ws
privkey=default.priv
pubkey=default.pub
```

Lastly, an activation code will be sent to you by email. The activation code should arrive promptly, and you can go on providing the activation code you received on the command line:

```console
cbsh auth --code <YOUR ACTIVATION CODE>
```

When successful, this will print out a short welcome notice and then exit again.

That's it! You are authenticated, and the public key is known to CFC from now on. Which means, authentication when running cbsh, or other clients using your private key (`default.priv`) will successfully authenticate against CFC.

Now, start the shell in interactive mode:

```console
cbsh
```

This will bring up a full screen console mode interactive shell. You can now query, control and manage your Crossbar.io Fabric nodes. Please see below.


### Creating a management realm

To create a CFC management realm for your CF nodes, start cbsh and enter

    create management-realm <realm-name>

Here, chose a `<realm-name` for your management realm. The name must be unique globally within CFC.


### Fabric Nodes

Start a new Crossbar.io Fabric Docker container connecting to Crossbar.io Fabric Center (CFC):

    docker run -it --rm crossbario/crossbar-fabric:latest

When the node is started the first time, a new node public/private key pair is generated. Further, the node will first need to be paired with CFC.


### Pairing a node

To pair a CF node to a management realm, start cbsh and enter

    pair node <realm-name> <public-key> <node-id>

Chose your management realm name for `<realm-name>`.

Use your node's public key (in Hex) for `<public-key>` (the public key Hex value is printed to the log when the node starts).

Finally, chose a `<node-id>` the node should be assigned to. The node ID needs to be unique within the management realm.
