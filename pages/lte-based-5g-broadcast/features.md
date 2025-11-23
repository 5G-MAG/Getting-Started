---
layout: default
title: Features
parent: 5G Broadcast - TV/Radio
has_children: false
nav_order: 2
---

<img src="../../assets/images/Banner_5GBCTVR.png" /> 

[Scope & Architectures](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [Features](./features.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](../releases.html#project-5g-broadcast-tv-and-radio-hybrid-services){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-blue } [Requirements](./requirements.html){: .btn .btn-blue }

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
