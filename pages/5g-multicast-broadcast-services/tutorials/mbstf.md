---
layout: default
title: Initial MBS Transport Services support
parent: Tutorials
grand_parent: 5G Multicast Broadcast (MBS)
has_children: false
nav_order: 2
---

# Initial MBS Transport Services support

This tutorial showcases the current features present in the 5G-MAG MBSTF implementation. You can check out the videos to
see more details or follow the write-up tutorial.

## Tutorial videos

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSc6fcO6cvo?si=4-uf_4Cn6i1J9Cs6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Prerequisites

This tutorial assumes that you have cloned and built the [rt-mbs-transport-function repository](https://github.com/5G-MAG/rt-mbs-transport-function).

## Description

In this tutorial we will configure the MBSTF with a variety of MBS Distribution Session types. This tutorial will also cover optional integration with the MB-SMF and MB-UPF.

### Step 1: (Optional) Create an MBS Session on the MB-UPF with UDP tunnel

Start the NRF, SCP, MB-UPF and MB-SMF docker components.

Copy this Nmbsmf_MBSSession *CreateReqData* JSON object into a file called `create-mbs-session.json`:
```json
{
  "mbsSession": {
    "mbsSessionId": {
      "ssm": {
        "sourceIpAddr": {
          "ipv4Addr": "127.0.0.1"
        },
        "destIpAddr": {
          "ipv4Addr": "232.0.0.1"
        }
      }
    },
    "tmgiAllocReq": true,
    "serviceType": "MULTICAST",
    "ingressTunAddrReq": true,
    "activityStatus": "ACTIVE",
    "anyUeInd": true
  }
}
```

Then we send this file to the MB-SMF to request a new MBS session:
```sh
curl --http2-prior-knowledge -H 'Content-Type: application/json' --data @create-mbs-session.json http://127.0.0.4:7777/nmbsmf-mbssession/v1/mbs-sessions
```

The response will contain the UDP tunnel details at JSON path `.mbsSession.ingressTunAddr`. These will need to be substituted in the `.distSession.mbUpfTunAddr` object in the Distribution Session JSON objects in the following steps in order to direct the output to the MB-UPF.

### Step 2: Create a single shot MBS Distribution Session for pull operation

### Step 3: Create a single shot MBS Distribution Session for push operation

### Step 4: Create a streaming MBS Distribution Session for pull operation on the DASH manifest

### Step 5: Create a streaming MBS Distribution Session for push operation on the DASH manifest
