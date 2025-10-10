---
layout: default
title: Using libscMBSMF
parent: Tutorials
grand_parent: 5GC Service Consumers
has_children: false
nav_order: 2
---

# Tutorial - Using the 5GC Service Consumer libraries: libscMBSMF

## Introduction

This tutorial provides information to test the 5GC Service Consumer libraries available in [rt-5gc-service-consumers](https://github.com/5G-MAG/rt-5gc-service-consumers) repository.

This collection of reusable service consumer libraries are designed to talk to the 5G Core Network Functions using some of their defined service interfaces. The command line tools below are provided to demonstrate the use of these service consumer libraries.

## Setup the relevant Open5GS network functions

We recommend a local installation of Open5GS following the instructions provided [here](../../3gpp-ran-and-core-platforms/tutorials/5gnetwork.html).

Note that the **TMGI Allocation/Deallocation tool** and the **MBS Service tool** requires the MBS components under the `5mbs` branch of 5G-MAG's Open5GS repository. This can be cloned with: `git clone --recurse-submodules -b 5mbs https://github.com/5G-MAG/open5gs.git ~/open5gs`. The MBS Transport Function can be installed from the [rt-mbs-transport-function](https://github.com/5G-MAG/rt-mbs-transport-function) repository.

In the following examples 127.0.0.10:7777 is used as the address and port number for the NRF API (Open5GS default). The address 12.34.56.78 is the UE's IP address as assigned by the 5G Core.

Please substitute these IP addresses for the ones you are using with your network.

## Using the TMGI Allocation/Deallocation tool

The TMGI Allocation and Deallocation tool can request the allocation or deallocation of a TMGI. It will then display the result and exit.

The TMGI Allocation and Deallocation tool can be run with an allocation command like:

```
/usr/local/bin/tmgi-tool -n 127.0.0.10:7777
```

...and a deallocation command like (for an allocated TMGI with PLMN of 001-01):

```
/usr/local/bin/tmgi-tool -d -p 001-01 -n 127.0.0.10:7777
```
To get the full command help for the TMGI Allocation and Deallocation tool use the command:

```
/usr/local/bin/tmgi-tool -h
```

## Using the MBS Service tool

The MBS Service tool will create an MBS Session and then report notifications for that MBS Session.

The MBS Service tool can be run with a command like:

```
/usr/local/bin/mbs-service-tool -TMu -S 192.168.0.1:232.0.0.59 -n 127.0.0.10:7777
```

To get the full command help for the MBS Service tool use the command:

```
/usr/local/bin/mbs-service-tool -h
```
