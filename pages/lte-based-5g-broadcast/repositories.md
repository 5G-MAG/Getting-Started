---
layout: default
title: Repositories
parent: 5G Broadcast - TV/Radio
has_children: false
nav_order: 2
---
<img src="../../assets/images/Banner_Repositories.png" /> 

1. TOC
{:toc}

# High-level architecture

## 5G Broadcast with Multimedia delivery protocols

<img src="../../assets/images/projects/5gbc_diagram.png" style="width: 80%">

 * Check [here](../multimedia-content-delivery/repositories.html) to access the repositories for Multimedia Content Delivery Protocols

## 5G Downlink Media Streaming (5GMSd) over eMBMS

<img src="../../assets/images/projects/5gms_5gbc_diagram.png" style="width: 80%">

 * Check [here](../5g-media-streaming/repositories.html) to access the repositories for 5G Downlink Media Streaming
 * Check [here](../3gpp-ran-and-core-platforms/repositories.html) to access the repositories for 3GPP RAN and Core Platforms
 * Check [here](../multimedia-content-delivery/repositories.html) to access the repositories for Multimedia Content Delivery Protocols

# Repositories

<img src="../../assets/images/projects/5gbc_repos.png" style="width: 80%">

Note that 5G Broadcast makes use of other repositories:

 * Check [here](../3gpp-ran-and-core-platforms/repositories.html#access-to-the-3gpp-ran-and-core-platforms-repositories) to access the repositories for 3GPP RAN and Core Platforms
 * Check [here](../multimedia-content-delivery/repositories.html#access-to-the-multimedia-content-delivery-repositories) to access the repositories for Multimedia content delivery

## 5G Broadcast Transmitter for MBMS-dedicated cells and basic MBMS gateway: [rt-mbms-tx](https://github.com/5G-MAG/rt-mbms-tx)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbms-tx#readme)
* [Releases](https://github.com/5G-MAG/rt-mbms-tx/releases)

## 5G Broadcast Transmitter for QRD (Qualcomm Reference Design) and CRD (Commercial Research Device): [rt-mbms-tx-for-qrd-and-crd](https://github.com/5G-MAG/rt-mbms-tx-for-qrd-and-crd)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbms-tx-for-qrd-and-crd#readme)

## MBMS Modem: [rt-mbms-modem](https://github.com/5G-MAG/rt-mbms-modem)
The MBMS Modem main task is to convert a 5G BC input signal (received either as live I/Q raw data from the SDR or as prerecorded SDR sample file) to multicast IP packets on the output. The MBMS Modem can run as background process or can be started/stopped manually.
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbms-modem#readme)
* [Releases](https://github.com/5G-MAG/rt-mbms-modem/releases)
* [Docker](https://github.com/5G-MAG/rt-mbms-modem/tree/development/modem)

## MBMS Middleware: [rt-mbms-mw](https://github.com/5G-MAG/rt-mbms-mw)
The MBMS Middleware main task is to provide the best available content to the (internal or external) application at any time. If available, it combines content from (mobile) broadband, WiFi with the 5G broadcast content from the MBMS Modem using an advanced decision logic. The content is presented to the applications in the form of an intelligent edge cache ready for pickup via http(s). Internally, the MBMS Middleware uses the 5G-MAG Reference Tools FLUTE library to decode FLUTE encoded manifest files and media segments.
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbms-mw#readme)
* [Releases](https://github.com/5G-MAG/rt-mbms-mw/releases)
* [Docker](https://github.com/5G-MAG/rt-mbms-mw/tree/development/middleware)

## MBMS Middleware for Android: [rt-mbms-mw-android](https://github.com/5G-MAG/rt-mbms-mw-android)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbms-mw-android#readme)
* [Releases](https://github.com/5G-MAG/rt-mbms-mw-android/releases)

---

## Auxiliary repositories

### Tools common to various projects: [rt-common-shared](https://github.com/5G-MAG/rt-common-shared)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-common-shared#readme)

### MBMS Web User Interface: [rt-mbms-wui](https://github.com/5G-MAG/rt-wui)
The 5G-MAG Reference Tools Webinterface (rt-wui) provides an optional graphical webinterface with a control display for each 5G-MAG Reference Tools process (MBMS Modem, MBMS Middleware). Its main purpose is to collect and display useful information from the MBMS Modem and the MBMS Middleware. The webinterface provides basic browser-based HLS playback of the HLS manifest and segments provided by the MBMS Middleare using hls.js.
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-wui#readme)
* [Releases](https://github.com/5G-MAG/rt-wui/releases)
* [Docker](https://github.com/5G-MAG/rt-wui/tree/development/wui)

### MBMS Examples: [rt-mbms-examples](https://github.com/5G-MAG/rt-mbms-examples)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbms-examples#readme)
* [Releases](https://github.com/5G-MAG/rt-mbms-examples/releases)
