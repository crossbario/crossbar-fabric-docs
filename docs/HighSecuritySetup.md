# High Security Setup

The following describes a high-security, best-practice system setup of Crossbar.io Fabric and application components.


## Backend Application Components

Backend application components are WAMP components (often Autobahn based) that are run in the backend parts of an application, often on cloud systems, that is system which are reachable in the public Internet.

To integrate backend application components into the overall system, two things are needed:

- they need to run somewhere/somehow and also be started by someone
- they need to connect (and possibly authenticate) to Crossbar.io Fabric nodes


### Dockerizing Components

The recommended setup runs backend application components in Docker containers.

Each backend application component is run in a separate Docker container, and the container image is derived of one of the official Autobahn Docker images.

The actual application code and any additional dependencies can be included in the user Docker image deriving of one of the official Autobahn images.

Using Docker in this way comes with a couple of benefits:

- exactly reproducible deployment of your components
- run-time isolation in both security and resource consumption
- allows simple and complete network isolation (see below)


### Network and Disk Isolation

When backend application components provide business logic only, and do not need to talk to the outside world other than via WAMP and Crossbar.io, then there is no need for the backend component to be given _any_ network access.

Such backend components do not need to listen for incoming network connections, nor do they need to establish outgoing network connections (other than WAMP, and for that, see below).

To achieve this kind of full network isolation is easy using Docker, since when starting the backend application component in a Docker container without providing a network for the container to connect to, no networking (other than loopback) will be possible for the backend application component.


### Router Connection and Authentication

So how does the backend application component connect to Crossbar.io, given that we have denied it _any_ kind of network access - even to another container (such as Crossbar.io) running on the same host!

**Unix domain sockets (UDS)** are like network sockets, but do not exist in an IP namespace, but reside in the filesystem namespace.

And because of that, permissions to Unix domain sockets can be controlled and enforced using filesystem permissions.

Further, because we start the backend application component in a Docker container, we need to explicitly mount the Unix domain socket path into the Docker container when starting.

To take this approach further, **recommended is running one separate Unix domain socket for each backend application component** co-residing on the host that runs the Crossbar.io Fabric node the component is supposed to connect to.

When doing so, an additional benefit becomes obvious: because now Crossbar.io Fabric essentially runs a separate transport for each backend application component, it automatically knows that it must be that component that is connecting. In other words, **backend application components are implicitly authenticated**.

For the WAMP transport type used with backend application components, recommended is:

* RawSocket using CBOR
* no TLS

In this case, TLS is not required, as the traffic between the backend application component and Crossbar.io runs over a UDS, which means through kernel, and protected from other user processes anyways.


## Static Web Content

Crossbar.io Fabric, when used as a simple Web server for static content is [pretty fast](https://github.com/crossbario/crossbar-examples/tree/master/benchmark/web). Nginx is faster of course. Then who needs to push millions of Web requests per second?

However, the point is not being able to saturate a 10GbE link using a couple of cores on a single box in a data-center anyways.

The point with bringing static Web content to the masses with low latency (!) is that you probably want a CDN.

CDNs deliver static content like nothing else. And this part of your traffic is now completely managed by the CDN (= their problem!), including fighting off DDoS attacks on a large scale.
