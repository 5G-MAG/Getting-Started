---
layout: default
title: Using the libraries
parent: Tutorials
grand_parent: 5GC Service Consumers
has_children: false
nav_order: 0
---

# Tutorial - Using the 5GC Service Consumer libraries

## Introduction

Consumption Collection and Reporting executes the collection of content consumption measurement logs
from the Media Player and sending of consumption reports to a 5GMSd AF about the currently consumed media
within the available presentation, about the UE capabilities and about the environment of the media session for
potential transport optimizations by the network or consumption report analysis.

To setup and enable Consumption Reporting we must first configure the 5GMS Application Function and the 5GMS Application
Server. Next, we start a 5GMS media streaming downlink session on the client-side. The resulting Consumption Reporting
reports can then be accessed from the local hard-drive.

## Setup the relevant Open5GS network functions

We recommend a local installation of Open5GS following the instructions provided [here](../../3gpp-ran-and-core-platforms/tutorials/5gnetwork.html).

Note that the tools interacting with MBS-related network functions will require installing such components from other 5G-MAG repositories.

The following are the requirements for the different tools:

* PCF Policy Authorization tool: Requires regular Open5GS v2.7.2

* TMGI Allocation/Deallocation tool: Requires the MBS components under the `5mbs` branch of 5G-MAG's Open5GS repository. This can be cloned with: `git clone --recurse-submodules -b 5mbs https://github.com/5G-MAG/open5gs.git ~/open5gs`. The MBS Transport Function can be installed from the [rt-mbs-transport-function](https://github.com/5G-MAG/rt-mbs-transport-function) repository.

* MBS Service tool: Requires the MBS components under the `5mbs` branch of 5G-MAG's Open5GS repository. This can be cloned with: `git clone --recurse-submodules -b 5mbs https://github.com/5G-MAG/open5gs.git ~/open5gs`. The MBS Transport Function can be installed from the [rt-mbs-transport-function](https://github.com/5G-MAG/rt-mbs-transport-function) repository.

In the following examples 127.0.0.10:7777 is used as the address and port number for the NRF API (Open5GS default). The address 12.34.56.78 is the UE's IP address as assigned by the 5G Core.

Please substitute these IP addresses for the ones you are using with your network.

## Using the PCF PolicyAuthorization tool

The PCF PolicyAuthorization tool can request a QoS policy and will then wait and report notifications for the QoS policy session.

The PCF PolicyAuthorization tool can be run with a command like (requests QoS settings for video Media-Type with a minimum guarenteed 2.5Mbps downlink):

```
/usr/local/bin/pcf-policyauthorization -a 12.34.56.78 -n 127.0.0.10:7777 -t video -d 2.5e6
```

Note: This will only work if you have defined a PCC Rule for 5QI 2 (video) defaults

To get the full command help for the PCF PolicyAuthorization tool use the command:

```
/usr/local/bin/pcf-policyauthorization -h
```

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
