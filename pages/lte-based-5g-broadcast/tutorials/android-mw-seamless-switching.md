---
layout: default
title: Android Middleware - Seamless Switching
parent: Tutorials
grand_parent: MBMS and LTE-based 5G Broadcast
has_children: false
---

# Tutorial - Android Middleware - Seamless Switching

## Introduction

This tutorial describes the end-to-end setup for seamless switching between 5G Broadcast and unicast delivery on an
Android device. The basic architecture of the setup is depicted in the Figure below:

![Android Seamless Switching](../../../assets/images/5gbc/android-seamless-switching-architecture.png)

We use `ffmpeg` to create an HLS livestream from a plain .mp4 file. The resulting manifest files and media segments are
stored on a folder located on a simple `express.js webserver`. From this webserver the files are accessible to media
players
located in the same network. This setup corresponds to a classic OTT and CDN based workflow. As an example, the HLS
stream can be played natively in a Safari Web-browser by simply pasting the URL to the primary or the media playlist
into the URL address bar.

Whenever a new file is added to the `watchfolder` located on the webserver, a background process called `flute-ffmpeg`
is
notified. `flute-ffmpeg` uses the `rt-libflute` library to FLUTE encode the files and sends them via a dedicated network
tunnel to the `srsmbms` process. `srsmbms` acts as an MBMS gateway and exposes the `sgi_mb` interface for that reason.
The `rt-mbms-tx-for-qrd-and-crd` repository acts as a 5G Broadcast transmitter hosting the `srsmbms`, `srsepc`
and `srsenb` processes. It is based on srsRAN with additional changes from 5G-MAG to support LTE-based 5G Broadcast
transmission.

Finally on the receiver side the `rt-mbms-mw-android` is running on a QRD or CRD device. It is responsible for receiving
the media files delivered via 5G Broadcast. The files are exposed to a media player such as the Exoplayer via a local
webserver. In cases in which no 5G Broadcast is available the Android Middleware fetches the required manifest and media
files directly from the CDN via unicast and exposed them again via the local webserver. From a media player's
perspective it does not matter if the files hosted on the local webserver have been received via unicast or via 5G
broadcast. It is simply consuming the files via standard HTTP requests to `localhost`. That way the Android MW can
dynamically switch between broadcast and unicast delivery based on the availability of the respective delivery
mechanism.

## Requirements

To replicate the setup described in this tutorial the following components are required:

* An Ubuntu 22 system to install and host ffmpeg, an express.js webserver, the flute-ffmpeg repository as well as our
  5G-MAG QRD and CRD transmitter.
* A Software Defined Radio (SDR) such as the BladeRF with an antenna for transmission of the 5G Broadcast signal
* A QRD or CRD device operating in Receive-only mode (ROM) to receive the 5G Broadcast transmission and run the 5G-MAG
  MBMS Android Middleware.

A photo of the basic setup is depicted below:

![Basic Setup](../../../assets/images/5gbc/5gbc-basic-setup.png)



