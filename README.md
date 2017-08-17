# Crossbar.io Fabric Documentation and Examples

The repository also contains the documentation (source) and example code for Crossbar.io Fabric:

* [Crossbar.io Fabric Documentation (Source)](https://github.com/crossbario/crossbar-fabric-docs/wiki)
* [Crossbar.io Fabric Examples](examples)

## Getting Started

### Python

You will need Python 3 and virtualenv.

### Fabric Shell

Create a new dedicated Python virtualenv for Crossbar.io Fabric Shell:

```console
virtualenv ~/.cbsh
source ~/.cbsh/bin/activate
pip install crossbarfabricshell
```

Now register or login to Crossbar.io Fabric Center:

```console
cbsh auth
```

An activation code will be sent by email to you.

Go on providing the activation code you received:

```console
cbsh auth --code ...
```

That's it! You are now authenticated.

Started the shell in interactive mode:

```console
cbsh
```


### Creating a management realm

To create a CFC management realm for your CF node, start cbsh and enter

    create management-realm my-realm-1


### Docker

You will need Docker.


### Fabric Nodes

Start a new Crossbar.io Fabric Docker container connecting to Crossbar.io Fabric Center (CFC):

    docker run -it --rm crossbario/crossbar-fabric:latest

When the node is started the first time, a new node public/private key pair is generated. Further, the node will first need to be paired with CFC.


### Pairing a node

To pair a CF node to a management realm, start cbsh and enter

    pair node my-realm-1 78aaf7... my-node-1
