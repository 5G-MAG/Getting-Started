---
layout: default
title: Repositories
parent: 5G Media Streaming
has_children: false
nav_order: 2
---

<img src="../../assets/images/Banner_Repositories.png" /> 

1. TOC
{:toc}

# Repositories

The following repositories are available. Please refer to the "Scope & Architecture" sections of the different projects for more context.

<img src="../../assets/images/projects/5gms_repos.png">

---

## 5GMS-Aware Application: [rt-5gms-application](https://github.com/5G-MAG/rt-5gms-application)
This repository holds applications that can be used to test and demonstrate other 5G-MAG Reference Tools related to 5GMS.
This is a list of the current applications available:

* 5GMSd-Aware Application: An Android application that serves as a reference implementation for 5GMS downlink media streaming. It uses the Media Stream Handler for playback and communication with the Media Session Handler.
* Exo DVB-I Player: This project uses the Android ExoPlayer and the DVB-I Reference Client functionality to provide the capabilities to select and play back media content.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-application#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-application/releases)

## 5GMS Media Session Handler: [rt-5gms-media-session-handler](https://github.com/5G-MAG/rt-5gms-media-session-handler)
The 5GMS Media Session Handler is a 5GMS Client component that forms part of the 5G Media Services framework as defined
in ETSI TS 126.501.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-media-session-handler#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-media-session-handler/releases)

## 5GMSd Media Stream Handler: [rt-5gms-media-stream-handler](https://github.com/5G-MAG/rt-5gms-media-stream-handler)
The 5GMS Media Stream Handler is a 5GMS client component that forms part of the 5G Media Services framework as defined in ETSI TS 126.501.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-media-stream-handler#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-media-stream-handler/releases)
* [Packages](https://github.com/orgs/5G-MAG/packages?repo_name=rt-5gms-media-stream-handler)

## 5GMSd Application Function: [rt-5gms-application-function](https://github.com/5G-MAG/rt-5gms-application-function)
The 5GMS Application Function (AF) is a Network Function that forms part of the 5G Media Services framework as defined in ETSI TS 126.501.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-application-function#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-application-function/releases)

## 5GMSd Application Server: [rt-5gms-application-server](https://github.com/5G-MAG/rt-5gms-application-server)
The 5GMS Application Server (AS) is a Network Function that forms part of the 5G Media Streaming framework as defined in ETSI TS 126.501.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-application-server#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-application-server/releases)

## 5GMS Application Provider: [rt-5gms-application-provider](https://github.com/5G-MAG/rt-5gms-application-provider)
This repository provides multiple tools to interact with the 5GMS Application Function.

The following tools are available:
* **Command Line Interface Tool** - Python-based Command Line Interface tool for 5GMS management
* **Management UI** - A web-based Graphical User Interface for 5GMS management that uses the aforementioned Python classes and interacts with the 5GMS Application Function
* **Postman Collection** - Postman recipes to test the 5GMS Application Function's API at reference point M1
* **QoE Metrics Reporting UI** - Web-based Graphical User Interface that parses a QoE Metrics Report provided in XML format and outputs its content in graphical and tabular form

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-application-provider#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-application-provider/releases)

---

## Auxiliary repositories

### 5GMS Common Android Library: [rt-5gms-common-android-library](https://github.com/5G-MAG/rt-5gms-common-android-library)
The 5GMS Common Library is an Android library that includes models and helper classes used within the different client-side Android applications such as the 5GMSd-Aware Application, 5GMSd Media Stream Handler and the 5GMSd Media Session Handler.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gms-common-android-library#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-common-android-library/releases)
* [Packages](https://github.com/orgs/5G-MAG/packages?repo_name=rt-5gms-common-android-library)

### 5GMS Examples: [rt-5gms-examples](https://github.com/5G-MAG/rt-5gms-examples)
This repository holds example projects that make use of other 5G-MAG repositories or provide additional functionalities to test and implement new features for 5GMS.

The following tools are available:
* **5G Media Streaming - Docker Compose Setup** - This project provides a docker-compose setup to run the 5GMS Application Function and the 5GMS Application Server components in a local container environment
* **Express Mock AF** - This project provides a very simple HTTP server that implements two routes.

Additional information:
* [Information](https://github.com/5G-MAG/rt-5gms-examples#readme)
* [Releases](https://github.com/5G-MAG/rt-5gms-examples/releases)

---

# Packages

This project also provides or makes use of the following packages GitHub Container packages.

## 5G Media Streaming

Components | Package
 --|--
 com.fivegmag.a5gmsmediastreamhandler | [https://github.com/5G-MAG/rt-5gms-media-stream-handler/packages/](https://github.com/5G-MAG/rt-5gms-media-stream-handler/packages/)
 com.fivegmag.a5gmscommonlibrary | [https://github.com/5G-MAG/rt-5gms-common-android-library/packages/](https://github.com/5G-MAG/rt-5gms-common-android-library/packages/)


