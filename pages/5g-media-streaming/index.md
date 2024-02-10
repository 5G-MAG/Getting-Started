---
layout: default
title: 5G Downlink Media Streaming
has_children: true
toc: false
---

# Project: 5G Downlink Media Streaming (5GMSd)
<iframe width="100%" height="440" src="https://drive.google.com/file/d/105dQMUHnuKxIwn8K7z5rvuPLMU85FQUc/preview"></iframe>

***

## 📑 Specifications and architecture
* Information about relevant specifications can be found at the [Standards Wiki](https://github.com/5G-MAG/Standards/wiki/5G-Downlink-Media-Streaming-Architecture-(5GMSd):-Relevant-Specifications)

***

## 🚧 On-going projects

### 5GMS: Basic Media stream handling (MVP#1)
The main objective for MVP#1 is to implement a starting point for 5G Media Streaming with DASH-based media streaming using 5GMS formats and protocols as the basis. This includes a basic Media Player talking to a simple 5GMS Application Server.
* [Kanban board](https://github.com/orgs/5G-MAG/projects/3)

### 5GMS: Media session handling (MVP#2)
The 5GMSd Media Session Handler retrieves Service Access Information from a 5GMSd Application Function (5GMSd AF) via reference point M5d.
* [Kanban board](https://github.com/orgs/5G-MAG/projects/4)

### 5GMS: M1d Provisioning
Implementation of 5GMSd Provisioning (M1d) APIs
* [Kanban board](https://github.com/orgs/5G-MAG/projects/8)

### 5GMS: M3 Link  (AF to AS RESTful OpenAPI)
Configuration of the 5GMS Application Server by the 5GMS Application Function via an RESTful OpenAPI interface.
* [Kanban board](https://github.com/orgs/5G-MAG/projects/6)

### 5GMS: Network Assistance and Dynamic Policies features
Addition of Network Assistance and Dynamic Policies features to the 5GMS components, including integration with the BSF and PCF via new, reusable service consumer libraries.
* [Kanban board](https://github.com/orgs/5G-MAG/projects/11)

### 5GMS: QoE metrics collection and reporting feature
Everything required for the provisioning of QoE metrics collection and reporting in the 5GMS AF as well as the collection of QoE by the 5GMS Client and the reporting of QoE metrics by the Media Session Handler to the 5GMS AF.
* [Kanban board](https://github.com/orgs/5G-MAG/projects/12)

### 5GMS: Consumption collection and reporting feature
Everything required for the provisioning of media consumption collection and reporting in the 5GMS AF as well as the collection of consumption reports by the 5GMS Client and the reporting by the Media Session Handler to the 5GMS AF.
* [Kanban board](https://github.com/orgs/5G-MAG/projects/16)

### 5GMS: TS 26.512 V17.5.0 uplift
* [Kanban board](https://github.com/orgs/5G-MAG/projects/18)

### 5GMS: Cloud infrastructure
* [Kanban board](https://github.com/orgs/5G-MAG/projects/21)

### 5GMS: DVB-I Service using 5G Media Streaming
* [Kanban board](https://github.com/orgs/5G-MAG/projects/23)

***

## ▶️ Using the tools
Check the [TUTORIALS & DEVELOPER XCHANGES](https://www.5g-mag.com/tutorials) and check the wikis below for more information
* [End to End Setup for 5G Downlink Media Streaming (Android)](https://github.com/5G-MAG/Getting-Started/wiki/Use-Case:-5G-Downlink-Media-Streaming-End-to-End-Setup)
***

## ⭐ Related repositories
* Check the Repositories relevant to 5GMSd: Code, releases, packages, dockers, guidelines,...

Please note that 5G Media Streaming makes use of other generic 5G Core Network components: https://github.com/5G-MAG/Getting-Started/wiki/5G-Core-Network

### 5GMSd Application Function: [rt-5gms-application-function](https://github.com/5G-MAG/rt-5gms-application-function)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-application-function#readme)
* [Guidelines, development and testing](https://github.com/5G-MAG/rt-5gms-application-function/wiki)
* [Releases](https://github.com/5G-MAG/rt-5gms-application-function/releases)
* [Projects](https://github.com/5G-MAG/rt-5gms-application-function/projects?query=is%3Aopen)

### 5GMSd Application Server: [rt-5gms-application-server](https://github.com/5G-MAG/rt-5gms-application-server)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-application-server#readme)
* [Guidelines, development and testing](https://github.com/5G-MAG/rt-5gms-application-server/wiki)
* [Releases](https://github.com/5G-MAG/rt-5gms-application-server/releases)
* [Projects](https://github.com/5G-MAG/rt-5gms-application-server/projects?query=is%3Aopen)

### 5GMSd Media Session Handler: [rt-5gms-media-session-handler](https://github.com/5G-MAG/rt-5gms-media-session-handler)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-media-session-handler#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-media-session-handler/releases)

### 5GMSd Media Stream Handler: [rt-5gms-media-stream-handler](https://github.com/5G-MAG/rt-5gms-media-stream-handler)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-media-stream-handler#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-media-stream-handler/releases)
* [Packages](https://github.com/orgs/5G-MAG/packages?repo_name=rt-5gms-media-stream-handler)

### 5GMSd-Aware Applications: [rt-5gms-application](https://github.com/5G-MAG/rt-5gms-application)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-application#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-application/releases)

## Auxiliary repositories

### 5GMSd Common Android Library: [rt-5gms-common-android-library](https://github.com/5G-MAG/rt-5gms-common-android-library)
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-common-android-library#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-common-android-library/releases)
* [Packages](https://github.com/orgs/5G-MAG/packages?repo_name=rt-5gms-common-android-library)

### 5GMSd Examples: [rt-5gms-examples](https://github.com/5G-MAG/rt-5gms-examples)
* [Information](https://github.com/5G-MAG/rt-5gms-examples#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-examples/releases)

### Tools common to various projects: [rt-common-shared](https://github.com/5G-MAG/rt-common-shared)
* [Information](https://github.com/5G-MAG/rt-common-shared#readme)
***
