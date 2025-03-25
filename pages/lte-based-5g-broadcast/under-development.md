---
layout: default
title: Under Development
parent: 5G Broadcast (MBMS)
has_children: false
nav_order: 0
---

# Under Development

## Specifications

Visit the [Standards repository](https://5g-mag.github.io/Standards/pages/lte-based-5g-broadcast.html) for details.

## High-level architecture

### High-level architecture: 5G Broadcast with Multimedia delivery protocols

<img src="../../assets/images/projects/5gbc_diagram.png" style="width: 80%">

 * Check [here](./repositories.html) to access the repositories for 5G Broadcast
 * Check [here](../multimedia-content-delivery/repositories.html) to access the repositories for Multimedia Content Delivery Protocols

### High-level architecture: 5G Downlink Media Streaming (5GMSd) over eMBMS

<img src="../../assets/images/projects/5gms_5gbc_diagram.png" style="width: 80%">

 * Check [here](./repositories.html) to access the repositories for 5G Broadcast
 * Check [here](../5g-media-streaming/repositories.html) to access the repositories for 5G Downlink Media Streaming
 * Check [here](../3gpp-ran-and-core-platforms/repositories.html) to access the repositories for 3GPP RAN and Core Platforms
 * Check [here](../multimedia-content-delivery/repositories.html) to access the repositories for Multimedia Content Delivery Protocols

# List of features under implementation

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
