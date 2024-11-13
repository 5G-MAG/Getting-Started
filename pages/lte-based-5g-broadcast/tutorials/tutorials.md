---
layout: default
title: Tutorials
parent: 5G Broadcast - MBMS & LTE-based 5G Broadcast
has_children: true
nav_order: 4
---

# Tutorials

## Our video library

The section [DEVELOPER XCHANGES & TUTORIALS](https://www.5g-mag.com/tutorials) in the 5G-MAG website contains more
information and videos from the 5G-MAG Reference Tools developers on the usage of the tools. Some of the videos are also
available here:

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=slOCsL53O2W6WlIb&amp;list=PLFqKJZ78_IWWbdf4rZ_SS9W0dqpLhKZz8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Using the tools

### [Tutorial: Linux Stack - RTP Playback over 5G Broadcast](./rtp-playback-5gbc.html)

This tutorial provides guidelines how to setup the
5G-MAG Reference Tools to use an RTP stream which was received via 5G Broadcast, processed by
the [MBMS Modem](https://github.com/5G-MAG/rt-mbms-modem) and played in a third-party media player such as ffplay or
VLC.

### [Tutorial: Linux Stack - HLS Playback over 5G Broadcast](./hls-playback-5gbc.html)

This tutorial provides guidelines how to setup the
5G-MAG Reference Tools to use an HLS stream which was received via 5G Broadcast, processed by
the [MBMS Modem](https://github.com/5G-MAG/rt-mbms-modem) and played via dash.js or hls.js in
the [Web User Interface](https://github.com/5G-MAG/rt-wui).

### [Tutorial: Linux Stack - Seamless Switching between unicast and broadcast](./seamless-switching.html)

The goal of this documentation is to provide detailed information, the required steps and the resulting output by the
5G-MAG Reference Tools for seamless switching between content delivered via broadcast and via unicast. Note: By the time
this documentation is written the 5G-MAG Reference Tools support a dynamic switch for content packaged in the HLS
format. The support DASH content is work in progress.

### [Tutorial: Linux Stack - Configuration Guide](./configuration-guide.html)

This tutorial provides an overview of the different configuration options when running the Linux based 5G broadcast
stack. It highlights the required configuration options for the 5G Broadcast Service Announcements files and how to
configure the FLUTE ffmpeg watchfolder implementation for DASH, HLS and seamless switching.

### [Tutorial: Linux Stack - Docker](./docker-implementation.html)

We provide the implementation of the rt-mbms processes (5G broadcast receiver) as Docker containers. Details on how to
use the Docker setup can be found in this tutorial.

### [Tutorial: Android Middleware - Seamless Switching](./android-mw-seamless-switching.html)

This tutorial describes the end-to-end setup for seamless switching between 5G Broadcast and unicast delivery on an
Android device. It
utilizes [flute-ffmpeg](https://github.com/5G-MAG/rt-mbms-examples/tree/development/flute-ffmpeg), [rt-libflute](https://github.com/5G-MAG/rt-libflute)
and [rt-mbms-tx-for-qrd-and-crd](https://github.com/5G-MAG/rt-mbms-tx-for-qrd-and-crd) for the transmission of the
media data and the [rt-mbms-mw-android](https://github.com/5G-MAG/rt-mbms-mw-android) for the reception on the client-side.
