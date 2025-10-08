---
layout: default
title: Scope
parent: 5G Multicast Broadcast Services
has_children: false
nav_order: 0
---

<img src="../../assets/images/Banner_Scope.png" /> 

1. TOC
{:toc}

This page contains information such as the specifications within the scope of the tools, high-level architecture, APIs under implementation,...

# Specifications
Visit the [Standards repository](https://5g-mag.github.io/Standards/pages/5g-multicast-broadcast-services.html) for more details on the specifications within the scope of the tools.

# High-level architecture

## 5G Multicast Broadcast Services (MBS)

<img src="../../assets/images/projects/mbs_diagram.png" style="width: 80%">

 * Check [here](./repositories.html) to access the repositories for **5G Multicast Broadcast Services (MBS)**
 * Check [here](../3gpp-ran-and-core-platforms/repositories.html) to access the repositories for **3GPP RAN and Core Platforms**

## 5G Media Streaming (5GMS) over 5G Multicast Broadcast Services (MBS)

<img src="../../assets/images/projects/5gms_mbs_diagram.png" style="width: 80%">

 * Check [here](./repositories.html) to access the repositories for **5G Multicast Broadcast Services (MBS)**
 * Check [here](../3gpp-ran-and-core-platforms/repositories.html) to access the repositories for **3GPP RAN and Core Platforms**
 * Check [here](../5g-media-streaming/repositories.html) to access the repositories for **5G Media Streaming**

# Features under implementation

## MBS development over Open5GS

The 5G-MAG Reference Tools for MBS currently target:
- MBS Session provisioning in the MB-SMF (e.g. by an MBSF) via reference point Nmb1.
- Direct multicast data ingest by the MB-UPF from an AF/AS via reference point N6mb.
- Shared delivery of multicast packets from the MB-UPF via individual GTP-U tunnels to one or more gNodeBs in the 5G Core.
- Point-to-Multipoint (PTM) delivery of multicast packets from a gNodeB to UEs via the RAN.

The 5G-MAG Reference Tools for **MBS User Services** add the following functionality:
- MBSTF Distribution Session management (e.g. by an MBSF) via reference point Nmb2.
- Ingest of objects by the MBSTF from the MBS Application Provider (AF/AS) via reference point Nmb8, using either a pull- or push-based object acquisition method.
- Delivery of ingested objects in a FLUTE Session multicast sent as multicast ALC packets from an MBSTF to an MB-UPF via a reference point Nmb9 unicast tunnel.

The following features are supported:
- `MB-SMF TMGI Service API` (Following 3GPP TS 29.532 V17.4.0)
  - TMGI Allocate Service operation
  - TMGI Deallocate Service operation
- `MB-SMF MBS Session Service API` (Following 3GPP TS 29.532 - Release 17.4.0)
  - MBS Session Create Service operation
  - MBS Session Release Service operation
- `MB-SMF PFCP Session Establishment extensions` (Following 3GPP TS 29.244 - Release 17.9.0)
  - PFCP Session Establishment Request extensions
- `MB-UPF PFCP Session Establishment extensions` (Following 3GPP TS 29.244 - Release 17.9.0)
  - PFCP Session Establishment Response extensions
- `Multicast/Broadcast Service Transport Services (MBSTF)` (Following 3GPP TS 29.581 V18.5.0)
  - Object distribution method
    - **Single shot operating mode**: Individual objects are sent once in a FLUTE Session by the MBSTF
      - Pull-based object acquisition (MBSTF pulls objects from a media server)
      - Push-based object acquisition (objects are pushed into the MBSTF)
    - **Streaming operating mode**: Objects are scheduled and sent in real time according to a presentation manifest, such as a DASH MPD.
      - Pull-based object acquisition (MBSTF pulls a Service Entry Point object, such as a presentation manifest, and then schedules the pulling of further objects, such as media segments and updates of the presentation manifest)
      - Push-based object acquisition (MBSTF waits for a Service Entry Point object, such as a presentation manifest, to be pushed to it, and then schedules the pulling of media segment objects)
      - For this operating mode, the supported Service Entry Point formats are:
         - MPEG-DASH MPD (live profile only).

The following features are not yet supported:
- `AMF MBS Broadcast Service API` (Following 3GPP TS 29.518 V17.11.0)
  - MBS Broadcast ContextCreate Service operation
  - MBS Broadcast ContextRelease Service operation
- `AMF NGAP extensions` (Following 3GPP TS 38.413 - Release 17.6.0)
  - BROADCAST SESSION SETUP REQUEST
- `gNB NGAP extensions` (Following 3GPP TS 38.413 - Release 17.6.0)
  - BROADCAST SESSION SETUP RESPONSE
- `NRF NFDiscovery Service API extensions` (Following 3GPP TS 29.510 - Release 17.11.0)
  - MB-SMF TMGI Service API extensions
  - MB-SMF MBS Session Service API extensions
  - AMF MBS Broadcast Service API extensions
- `MBSTF Distribution Session management` (Following 3GPP TS 29.581 V18.5.0)
  - **Packet distribution method**
    - Use direct multicast packet ingest by the MB-UPF at reference point N6mb instead for now.
  - **Object distribution method**
    - **Collection operating mode**: One or more objects described by a simple manifest are sent once in the FLUTE Session.
    - **Carousel operating mode**: One or more objects described by a simple manifest are repeatedly sent in the FLUTE Session according to a schedule.
    - **Streaming operating mode**: Objects are sent in a FLUTE Session in real time according to a schedule specified in a streaming presentation manifest.
      - Presentation manifest types other than MPEG-DASH MPD (live profile).
  - Status notification subscription

