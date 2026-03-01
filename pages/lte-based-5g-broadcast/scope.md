---
layout: default
title: Scope
parent: 5G Broadcast - TV/Radio
has_children: false
nav_order: 0
---

<img src="../../assets/images/Banner_5GBCTVR.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](../releases.html#project-5g-broadcast-tv-and-radio-hybrid-services){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Requirements](./requirements.html){: .btn .btn-blue }

# Scope

This page contains information such as the specifications within the scope of the tools and high-level architectures that bring context to their applicability.

## Technical Resources and Specifications

[Technical Resources](https://hub.5g-mag.com/Tech/pages/lte-based-5g-broadcast.html){: .btn .btn-blue } [Specifications](https://hub.5g-mag.com/Standards/pages/lte-based-5g-broadcast.html){: .btn .btn-blue }

# Features under implementation

## Support of features in rt-mbms-tx and rt-mbms-modem

### Release 14 features

| Feature                                          | rt-mbms-tx | rt-mbms-modem 
|--------------------------------------------------|------------|---------------|
| MBSFN subframes using SCS = 1.25 kHz             | ✅          | ✅             |
| MIB-MBMS                                         | ✅          | ✅             | 
| SIB1-MBMS                                        | ✅          | ✅             |
| MBMSInterestIndication RRC signalling procedure	 | To check   | To check      |

### Release 16 features

| Feature                                                                      | rt-mbms-tx | rt-mbms-modem 
|------------------------------------------------------------------------------|------------|---------------|
| MBSFN subframes using SCS = 0.37 kHz                                         | ❌          | ❌             |
| MBSFN subframes using SCS = 2.5 kHz	                                         | ❌          | ❌             |
| PDCCH enhancements: CFI indication in MIB to avoid the need to decode PCFICH | ❌          | ❌             |
| PDCCH enhancements: New aggregation level 16                                 | ❌          | ❌             |
| Repetition of PBCH                                                           | ❌          | ❌             |

### Release 17 features

| Feature                                                          | rt-mbms-tx | rt-mbms-modem 
|------------------------------------------------------------------|------------|---------------|
| PMCH bandwidth of 30, 35 and 40 PRBs (corresponding to 6/7/8MHz) | ❌          | ✅             |

## Support of features for rt-mbms-tx-for-qrd-and-crd

Note that the 5G Broadcast Transmitter for QRD and CRD is an extension of an MBMS-enabled eNodeB tailored to operate as
a 5G Broadcast transmitter. Only MBMS/Unicast-mixed cell is supported alongside pre-Rel-14 features. 

# High-level architectures

## 5G Broadcast with Multimedia delivery protocols

<img src="../../assets/images/projects/5gbc_diagram.png" style="width: 80%">

[5G Broadcast: Repositories](../lte-based-5g-broadcast/repositories.html){: .btn .btn-5gbc }
[Multimedia content delivery protocols: Repositories](../multimedia-content-delivery/repositories.html){: .btn .btn-md }
[Common Tools: Repositories](../common-tools/){: .btn .btn-common }

## 5G Downlink Media Streaming (5GMSd) over eMBMS

<img src="../../assets/images/projects/5gms_5gbc_diagram.png" style="width: 80%">

[5G Media Streaming: Repositories](../5g-media-streaming/repositories.html){: .btn .btn-5gms }
[5G Broadcast: Repositories](../lte-based-5g-broadcast/repositories.html){: .btn .btn-5gbc }
[Multimedia content delivery protocols: Repositories](../multimedia-content-delivery/repositories.html){: .btn .btn-md }
[3GPP RAN and Core Platforms: Repositories](../3gpp-ran-and-core-platforms/repositories.html){: .btn .btn-3gpp }
[Common Tools: Repositories](../common-tools/){: .btn .btn-common }
