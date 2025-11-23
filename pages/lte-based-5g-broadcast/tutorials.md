---
layout: default
title: Tutorials
parent: 5G Broadcast - TV/Radio
has_children: true
nav_order: 4
---

<img src="../../assets/images/Banner_5GBCTVR.png" /> 

[Scope & Architectures](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [Features](./features.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](../releases.html#project-5g-broadcast-tv-and-radio-hybrid-services){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-blue } [Requirements](./requirements.html){: .btn .btn-blue }

# Tutorials, Tests and Examples

## [Tutorial: Seamless Switching between Unicast and Broadcast (Android)](./tutorials/android-mw-seamless-switching.html)

This tutorial describes the end-to-end setup for seamless switching between 5G Broadcast and unicast delivery on an
Android device. It
utilizes [flute-ffmpeg](https://github.com/5G-MAG/rt-mbms-examples/tree/development/flute-ffmpeg), [rt-libflute](https://github.com/5G-MAG/rt-libflute)
and [rt-mbms-tx-for-qrd-and-crd](https://github.com/5G-MAG/rt-mbms-tx-for-qrd-and-crd) for the transmission of the
media data and the [rt-mbms-mw-android](https://github.com/5G-MAG/rt-mbms-mw-android) for the reception on the client-side.

## [Tutorial: SDR - HLS Playback over 5G Broadcast](./tutorials/hls-playback-5gbc.html)

This tutorial provides guidelines how to setup the
5G-MAG Reference Tools to use an HLS stream which was received via 5G Broadcast, processed by
the [MBMS Modem](https://github.com/5G-MAG/rt-mbms-modem) and played via dash.js or hls.js in
the [Web User Interface](https://github.com/5G-MAG/rt-wui).

## [Tutorial: SDR - RTP Playback over 5G Broadcast](./tutorials/rtp-playback-5gbc.html)

This tutorial provides guidelines how to setup the
5G-MAG Reference Tools to use an RTP stream which was received via 5G Broadcast, processed by
the [MBMS Modem](https://github.com/5G-MAG/rt-mbms-modem) and played in a third-party media player such as ffplay or
VLC.

## [Tutorial: MBMS Modem - Measurements & GPS](./tutorials/modem-samplefiles.html)

We provide information on the use of the rt-mbms-modem with sample files as input.

## [Tutorial: Docker support for rt-mbms client components (Linux)](./tutorials/docker-implementation.html)

We provide the implementation of the rt-mbms processes (5G broadcast receiver) as Docker containers. Details on how to
use the Docker setup can be found in this tutorial.

## [Tutorial: MBMS Modem - Measurements & GPS](./tutorials/modem-measurements.html)

We provide information on the use of the rt-mbms-modem to record data.

## [Tutorial: Configuration of Service Announcement](./tutorials/configuration-guide.html)

This tutorial provides an overview of the different configuration options when running the Linux based 5G broadcast
stack. It highlights the required configuration options for the 5G Broadcast Service Announcements files and how to
configure the FLUTE ffmpeg watchfolder implementation for DASH, HLS and seamless switching.

# Video Library
Our [YouTube channel](https://www.youtube.com/@5GMAG) hosts some practical videos provided by developers on the use of the 5G-MAG Reference Tools.

Some of the videos are also available here:

## The Nakolos Core - Interoperability with 5G-MAG Reference Tools
<iframe width="560" height="315" src="https://www.youtube.com/embed/3iIichQmjBg?si=-SE8OXcYA1jIrJXs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 5G Broadcast at FOKUS Media Web Symposium 2024
<iframe width="560" height="315" src="https://www.youtube.com/embed/dZaUAhYZTUU?si=SiKKCLAZhcjyJ1B3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Updates on the rt-mbms Web Interface and Modem
<iframe width="560" height="315" src="https://www.youtube.com/embed/gzHBEYRDXCU?si=yqi865ngqoGxYx83" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 5G Broadcast supported by 5G-MAG Reference Tools
<iframe width="560" height="315" src="https://www.youtube.com/embed/TtM98uZxHuc?si=bIUGVTgT247X2T3R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Closing the gap towards a 5G Broadcast Rel-16 open-source transmitter
<iframe width="560" height="315" src="https://www.youtube.com/embed/O_MfEE5KG6o?si=XBuMZ_hsOHBnzgZl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 5G Broadcast-Broadband Seamless Switching
<iframe width="560" height="315" src="https://www.youtube.com/embed/Jbir8B-gC4c?si=4GCTkNGfAyBGiLpY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
