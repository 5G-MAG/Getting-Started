---
layout: default
title: Repositories
parent: V3C Immersive Platform
has_children: false
nav_order: 2
---
<img src="../../assets/images/Banner_Repositories.png" /> 

1. TOC
{:toc}

# High-level architecture

## V3C Immersive Platform

<img src="../../assets/images/projects/v3c_diagram.png" style="width: 80%">

# Repositories

<img src="../../assets/images/projects/v3c_repos.png" style="width: 80%">


---

## V3C Unity Player: [rt-v3c-unity-player](https://github.com/5G-MAG/rt-v3c-unity-player)
This project provides a Unity package to decode and play V3C contents in Unity, using the V3C Immersive Platform - Decoder Plugin. Also provided in that repository are V-PCC and MIV synthesizers plugins needed for the rendering of the V3C contents.
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-v3c-unity-player#readme)
* [Releases](https://github.com/5G-MAG/rt-v3c-unity-player/releases)

## V3C Decoder Plugin: [rt-v3c-decoder-plugin](https://github.com/5G-MAG/rt-v3c-decoder-plugin)
This project contains the entrypoints for decoding and viewing MPEG Immersive Video (MIV) and Video Point Cloud Compression (V-PCC) related to the V3C Immersive Platform.
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-v3c-decoder-plugin#readme)
* [Releases](https://github.com/5G-MAG/rt-v3c-decoder-plugin/releases)

## V3C Pre-encoded Test Content: [rt-v3c-content](https://github.com/5G-MAG/rt-v3c-content)
This folder contains the files to configure and test the V3CImmersivePlatform - Unity Player application.
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-v3c-content#readme)
* [Releases](https://github.com/5G-MAG/rt-v3c-content/releases)

## Auxiliary repositories
### Auxiliary tools common to various projects: [rt-common-shared](https://github.com/5G-MAG/rt-common-shared)
In the context of this project this repository is used for:
  - Installing the dependencies for the avcodec libraries: [https://github.com/5G-MAG/rt-common-shared/blob/main/avcodec-build/README.md](https://github.com/5G-MAG/rt-common-shared/blob/main/avcodec-build/README.md)
  - Installing a simple HTTP server based on express.js that can be used to statically host files for streaming: [https://github.com/5G-MAG/rt-common-shared/blob/main/simple-express-server/README.md](https://github.com/5G-MAG/rt-common-shared/blob/main/simple-express-server/README.md)
