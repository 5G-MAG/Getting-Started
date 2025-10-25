---
layout: default
title: Tutorials
parent: 5G Broadcast - TV/Radio
has_children: true
nav_order: 3
---
<img src="../../assets/images/Banner_Tutorials.png" /> 

1. TOC
{:toc}

# How to use the Reference Tools

## Tutorials, Tests and Examples

### [Tutorial: Seamless Switching between Unicast and Broadcast (Android)](./tutorials/android-mw-seamless-switching.html)

This tutorial describes the end-to-end setup for seamless switching between 5G Broadcast and unicast delivery on an
Android device. It
utilizes [flute-ffmpeg](https://github.com/5G-MAG/rt-mbms-examples/tree/development/flute-ffmpeg), [rt-libflute](https://github.com/5G-MAG/rt-libflute)
and [rt-mbms-tx-for-qrd-and-crd](https://github.com/5G-MAG/rt-mbms-tx-for-qrd-and-crd) for the transmission of the
media data and the [rt-mbms-mw-android](https://github.com/5G-MAG/rt-mbms-mw-android) for the reception on the client-side.

### [Tutorial: SDR - HLS Playback over 5G Broadcast](./tutorials/hls-playback-5gbc.html)

This tutorial provides guidelines how to setup the
5G-MAG Reference Tools to use an HLS stream which was received via 5G Broadcast, processed by
the [MBMS Modem](https://github.com/5G-MAG/rt-mbms-modem) and played via dash.js or hls.js in
the [Web User Interface](https://github.com/5G-MAG/rt-wui).

### [Tutorial: SDR - RTP Playback over 5G Broadcast](./tutorials/rtp-playback-5gbc.html)

This tutorial provides guidelines how to setup the
5G-MAG Reference Tools to use an RTP stream which was received via 5G Broadcast, processed by
the [MBMS Modem](https://github.com/5G-MAG/rt-mbms-modem) and played in a third-party media player such as ffplay or
VLC.

### [Tutorial: MBMS Modem - Measurements & GPS](./tutorials/modem-samplefiles.html)

We provide information on the use of the rt-mbms-modem with sample files as input.

### [Tutorial: Docker support for rt-mbms client components (Linux)](./tutorials/docker-implementation.html)

We provide the implementation of the rt-mbms processes (5G broadcast receiver) as Docker containers. Details on how to
use the Docker setup can be found in this tutorial.

### [Tutorial: MBMS Modem - Measurements & GPS](./tutorials/modem-measurements.html)

We provide information on the use of the rt-mbms-modem to record data.

### [Tutorial: Configuration of Service Announcement](./tutorials/configuration-guide.html)

This tutorial provides an overview of the different configuration options when running the Linux based 5G broadcast
stack. It highlights the required configuration options for the 5G Broadcast Service Announcements files and how to
configure the FLUTE ffmpeg watchfolder implementation for DASH, HLS and seamless switching.

## Check our video library
Our [YouTube channel](https://www.youtube.com/@5GMAG) hosts some practical videos provided by developers on the use of the 5G-MAG Reference Tools.

Some of the videos are also available here:

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=slOCsL53O2W6WlIb&amp;list=PLFqKJZ78_IWWbdf4rZ_SS9W0dqpLhKZz8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
