---
layout: default
title: Media Session Handler
parent: Usage
grand_parent: 5G Downlink Media Streaming
has_children: true
nav_order: 4
---

# Media Session Handler

The 5GMS Media Session Handler is a 5GMS Client component that forms part of the 5G Media Services framework as defined
in ETSI TS 126.501.

A Media Session Handler first retrieves its configuration (“Service Access Information”) from the 5GMSd AF at reference
point M5d and then uses this configuration information to activate and exploit the currently provisioned 5GMSd features.
In addition, the Media Session Handler exposes APIs via M6 to the 5GMSd-Aware Application and to the Media Player (for
downlink streaming).

More information about how to use the Media Session Handler together with other 5GMSd components can be found in
the [Tutorials](../../tutorials/tutorials.html) section.
