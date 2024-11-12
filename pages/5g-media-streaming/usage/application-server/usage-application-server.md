---
layout: default
title: Application Server
parent: Usage
grand_parent: 5G Downlink Media Streaming
has_children: true
nav_order: 0
---

# Application Server

The 5GMS Application Server (AS) is a Network Function that forms part of the 5G Media Services framework as defined in
ETSI TS 126.501.

A 5GMS Downlink Application Server (5GMSd AS), which can be deployed in the 5G Core Network or in an External Data
Network, provides 5G Downlink Media Streaming services to 5GMSd Clients. This logical function embodies the data plane
aspects of the 5GMSd System that deals with proxying media content (similar to a Content Delivery Network). The content
is ingested from 5GMSd Application Providers at reference point M2d. Both push- and pull-based ingest methods are
supported, based on HTTP. Ingested content is distributed to 5GMSd clients at reference point M4d (after possible
manipulation by the 5GMSd AS). Standard pull-based content retrieval protocols (e.g. DASH) are supported at this
reference point.
