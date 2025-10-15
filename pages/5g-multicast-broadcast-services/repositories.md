---
layout: default
title: Repositories
parent: 5G Multicast Broadcast Services
has_children: false
nav_order: 2
---
<img src="../../assets/images/Banner_Repositories.png" /> 

1. TOC
{:toc}

# Repositories

The following repositories are available. Please refer to the "Scope & Architecture" sections of the different projects for more context.

<img src="../../assets/images/projects/mbs_repos.png">

---

## 5G UE (with MBS components): [srsRAN_4G (5mbs branch)](https://github.com/5G-MAG/srsRAN_4G/tree/5mbs)
This is a branch of srsRAN_4G which contains a basic implementation of an MBS-capable UE.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/srsRAN_4G/tree/5mbs)

## NG-RAN (with MBS components): [rt-srsRAN_Project (5mbs branch)](https://github.com/5G-MAG/rt-srsRAN_Project/tree/5mbs)
This is a branch of srsRAN_Project which contains a basic implementation of an MBS-capable NG-RAN.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-srsRAN_Project/tree/5mbs)

## 5GC (with MBS components): [open5gs/tree/5mbs (5mbs branch)](https://github.com/5G-MAG/open5gs/tree/5mbs)
This is a branch of Open5GS which contains implementations of 5GC NFs related to MBS.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/open5gs/tree/5mbs)
* [Packages](https://github.com/orgs/5G-MAG/packages?repo_name=open5gs)

## MBS User Services: MBS Function (MBSF): [https://github.com/5G-MAG/rt-mbs-function](https://github.com/5G-MAG/rt-mbs-function)
This repository provides a 5G MBS Function which forms part of the MBS User Services. This NF provides the interface designated as Nmb10 in the 3GPP TS 29.580 specification.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbs-function)
* [Releases](https://github.com/5G-MAG/rt-mbs-function/releases)

https://github.com/orgs/5G-MAG/packages?repo_name=rt-mbs-transport-function
## MBS User Services: MBS Transport Function (MBSTF): [https://github.com/5G-MAG/rt-mbs-transport-function](https://github.com/5G-MAG/rt-mbs-transport-function)
This repository provides a 5G MBS Transport Function which forms part of the MBS User Services. This NF provides the interfaces designated as Nmb2, Nmb8 and Nmb9 in the 3GPP TS 29.581 V18.5.0 specification.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbs-transport-function)
* [Releases](https://github.com/5G-MAG/rt-mbs-transport-function/releases)
* [Packages](https://github.com/orgs/5G-MAG/packages?repo_name=rt-mbs-transport-function)

---

## Auxiliary repositories:

### MBS Examples: [rt-mbs-examples](https://github.com/5G-MAG/rt-mbs-examples)
This repository contains Docker Compose components to deploy several network functions related to MBS.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbs-examples#readme)
* [Packages](https://github.com/orgs/5G-MAG/packages?repo_name=rt-mbs-examples)

---

# Packages

This project also provides or makes use of the following packages GitHub Container packages. Images and docker compose deployments for MBS are located in the following repository: [https://github.com/5G-MAG/rt-mbs-examples](https://github.com/5G-MAG/rt-mbs-examples)

## Standard Open5GS packages:

Components | Package
 --|--
 NRF | [https://github.com/5G-MAG/open5gs/pkgs/container/nrf](https://github.com/5G-MAG/open5gs/pkgs/container/nrf)
 UDM | [https://github.com/5G-MAG/open5gs/pkgs/container/udm](https://github.com/5G-MAG/open5gs/pkgs/container/udm)
 PCF | [https://github.com/5G-MAG/open5gs/pkgs/container/pcf](https://github.com/5G-MAG/open5gs/pkgs/container/pcf)
 WebUI | [https://github.com/5G-MAG/open5gs/pkgs/container/webui](https://github.com/5G-MAG/open5gs/pkgs/container/webui)
 BSF | [https://github.com/5G-MAG/open5gs/pkgs/container/bsf](https://github.com/5G-MAG/open5gs/pkgs/container/bsf)
 UDR | [https://github.com/5G-MAG/open5gs/pkgs/container/udr](https://github.com/5G-MAG/open5gs/pkgs/container/udr)
 NSSF | [https://github.com/5G-MAG/open5gs/pkgs/container/nssf](https://github.com/5G-MAG/open5gs/pkgs/container/nssf)
 AUSF | [https://github.com/5G-MAG/open5gs/pkgs/container/ausf](https://github.com/5G-MAG/open5gs/pkgs/container/ausf)
 SMF | [https://github.com/5G-MAG/open5gs/pkgs/container/smf](https://github.com/5G-MAG/open5gs/pkgs/container/smf)
 UPF | [https://github.com/5G-MAG/open5gs/pkgs/container/upf](https://github.com/5G-MAG/open5gs/pkgs/container/upf)
 AMF | [https://github.com/5G-MAG/open5gs/pkgs/container/amf](https://github.com/5G-MAG/open5gs/pkgs/container/amf)
 SCP | [https://github.com/5G-MAG/open5gs/pkgs/container/scp](https://github.com/5G-MAG/open5gs/pkgs/container/scp)
 SEPP | [https://github.com/5G-MAG/open5gs/pkgs/container/sepp](https://github.com/5G-MAG/open5gs/pkgs/container/sepp)

## MBS related packages:

Components | Package
 --|--
 UPF and MB-UPF | [https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/upf_mb-upf](https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/upf_mb-upf)
 Test AF/AS for MBS | [https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/test_mbs_af_as](https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/test_mbs_af_as)
 SMF and MB-SMF | [https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/smf_mb-smf](https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/smf_mb-smf)
 gNB with MBS | [https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/gnb_with_mbs](https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/gnb_with_mbs)
 AMF with MBS | [https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/amf_with_mbs](https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/amf_with_mbs)
 UE with MBS | [https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/ue_with_mbs](https://github.com/5G-MAG/rt-mbs-examples/pkgs/container/ue_with_mbs)

## MBS User Services related packages:

Components | Package
 --|--
 MBSTF | [https://github.com/5G-MAG/rt-mbs-transport-function/pkgs/container/mbstf](https://github.com/5G-MAG/rt-mbs-transport-function/pkgs/container/mbstf)
