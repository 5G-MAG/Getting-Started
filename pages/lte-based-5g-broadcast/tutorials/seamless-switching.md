---
layout: default
title: Linux stack - Seamless switching
parent: Tutorials
parent: 5G Broadcast & MBMS
has_children: false
nav_order: 3
---

# Linux stack - Seamless switching

## Introduction

The goal of this documentation is to provide detailed information, the required steps and the resulting output by the
5G-MAG Reference Tools for seamless switching between content delivered via broadcast and via unicast. Note: By the time
this documentation is written the 5G-MAG Reference Tools support a dynamic switch for content packaged in the HLS
format. The support DASH content is work in progress. The final outcome is also illustrated in a short demo video that
can be found [here](https://www.youtube.com/watch?v=Jbir8B-gC4c).

## Background

### HTTP Live Streaming (HLS)

HTTP Live Streaming (HLS) is an HTTP-based adaptive bitrate streaming communications protocol developed by
Apple Inc. and released in 2009 [1].
HLS is based on master and media playlists (m3u8 files). The master playlist links to media playlists with the media
playlists describing the content. HLS is mainly used on Apple platforms due to native support. HLS typically uses the
Transport Stream (TS) media container, but also offers support for f-mp4/CMAF.

More information can be found in the IETF HLS specification:

* [RFC 8216 - HTTP Live Streaming](https://datatracker.ietf.org/doc/html/rfc8216)

### Unicast Delivery

Unicast delivery typically refers to delivery of media segments and manifest files using a one-to-one connection between
the client and the Content Delivery Network (CDN). In contrast to the delivery of media files via multicast and
broadcast each client is requesting and receiving the files individually. Classic DASH and HLS based unicast streaming
is often referred to as Over-the-Top (OTT) streaming.

### Multimedia Broadcast/Multicast Service (MBMS)

MBMS is a point-to-multipoint service in which data is transmitted from a single source entity to multiple recipients.
The MBMS bearer service offers two modes, namely broadcast mode and multicast mode. In the scope of the 5G-MAG Reference
Tools we focus on the broadcast mode.

More information about MBMS and the related interfaces and components can be found in the corresponding 3GPP and ETSI
specifications:

* [23.246 - Multimedia Broadcast/Multicast Service (MBMS); Architecture and functional description(Release 16)](https://www.3gpp.org/ftp/Specs/archive/23_series/23.246/)
* [26.347 - Multimedia Broadcast/Multicast Service (MBMS); Application Programming Interface and URL (Release 16)](https://www.3gpp.org/ftp/Specs/archive/26_series/26.347/)
* [26.346 - Multimedia Broadcast/Multicast Service (MBMS); Protocols and codecs(Release 16)](https://www.3gpp.org/ftp/Specs/archive/26_series/26.346)
* [29.116 - Representational state transfer over xMB reference point between content provider and BM-SC](https://www.3gpp.org/ftp/Specs/archive/29_series/29.116)
* [ETSI TS 123 246 - Multimedia Broadcast/Multicast Service (MBMS); Architecture and functional description ](https://www.etsi.org/deliver/etsi_ts/123200_123299/123246/)

### 5G-MAG Reference Tools

Detailed information about the architecture of the 5G-MAG Reference Tools can be found on the Wiki pages of the
different projects:

* [MBMS Modem](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/MBMS-Modem)
* [MBMS Middleware](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/MBMS-Middleware)
* [Webinterface](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Webinterface)

## Requirements

In order to enable dynamic with the 5G-MAG Reference Tools, we need to install and run the following components of the
5G-MAG Reference Tools:

* [MBMS Modem](https://github.com/5G-MAG/rt-mbms-modem) (**required, minimum version tbd**): The MBMS Modem builds the
  lower part of the 5G-MAG
  Reference Tools. Its main task is to convert a 5G BC input signal (received either as live I/Q raw data from the SDR
  or as prerecorded SDR sample file) to multicast IP packets on the output. The MBMS Modem can run as background process
  or can be started/stopped manually.
* [MBMS Middleware](https://github.com/5G-MAG/rt-mbms-mw) (**required, minimum version tbd**): The MBMS Middleware
  presents the heart of the
  5G-MAG Reference Tools. Its main task is to provide the best available content to the (internal or external)
  application at any time. If available, it combines content from (mobile) broadband, WiFi with the 5G broadcast content
  from the MBMS Modem using an advanced decision logic. The content is presented to the applications in the form of an
  intelligent edge cache ready for pickup via http(s). Internally, the MBMS Middleware uses
  the [5G-MAG Reference Tools FLUTE library](https://github.com/5G-MAG/rt-libflute) to decode FLUTE encoded manifest
  files and media segments.
* [RT Webinterace](https://github.com/5G-MAG/rt-wui) (optional): The 5G-MAG Reference Tools Webinterface (rt-wui)
  provides an optional graphical webinterface with a control display for each 5G-MAG Reference Tools process (MBMS
  Modem, MBMS Middleware). Its main purpose is to collect and display useful information from the MBMS Modem and the
  MBMS Middleware. The webinterface provides basic browser-based HLS playback of the HLS manifest and segments provided
  by the MBMS Middleare using [hls.js](https://github.com/video-dev/hls.js/).
* [HLS sample recording](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Sample-Files#hls-payload) (
  optional): In
  order to support application developers as well as 5G-MAG contributors for testing their improvements, ORS captured
  sample files ("raw data" = digitized I/Q data at LimeSDR Mini output) directly from a 5G BC transmitter.

## Basic workflow

As described in [Requirements](#Requirements) we need the MBMS Modem, the MBMS Middleware and a media player in order to
enable playback of HLS content in unicast and broadcast mode using the 5G-MAG Reference Tools. The basic interaction and
output of
these components is illustrated in the Figure below:

![Architecture](https://github.com/5G-MAG/Getting-Started/blob/main/media/architecture/5G-MAG%20RT%20Architecture%20Seamless%20Switching%20v8.drawio.png?raw=true)

The output of the SDR or the sample file serves as the input for the MBMS Modem. The MBMS Modem converts the input data
to a UDP multicast. The UDP multicast serves as the input for the MBMS Middleware. The FLUTE encoded content is decoded
in the MBMS Middleware using the [5G-MAG Reference Tools FLUTE library](https://github.com/5G-MAG/rt-libflute). Once the
manifest files and media segments are FLUTE decoded they are cached in the middleware and made available to the media
player via an Nginx proxy.

TBD: Unicast part

The media player itself is not aware that the content is provided via broadcast.

Note that in the illustration the media player is depicted as a separate component and not part of the web interface.

## Installation

Detailed installation instructions can be found in the respective Wiki documentation of the different projects. In order
to enable HLS playback via MBMS the following steps are required:

1. [Install the MBMS Modem (minimum version tbd)](https://github.com/5G-MAG/rt-mbms-modem#readme)
2. [Install the MBMS Middleware (minimum version tbd)](https://github.com/5G-MAG/rt-mbms-mw#readme)
3. [Install the Webinterface](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Webinterface#installation)
4. [Download an HLS sample file](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Sample-Files)

## Running the components

Once all the required components have been installed, we need to sequentially start all of them. Depending on the
concrete use case (either a live SDR input or a prerecorded sample file) the concrete calls are slightly different.

### Using a prerecorded sample file

This Section provides information on how to run the 5G-MAG Reference Tools using a prerecorded HLS sample file.

#### MBMS Modem

1. Follow the detailed instructions on how to configure multicast routing
   provided [here](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/mbms-modem#run-the-mbms-modem).
2. Stop and start the MBMS Modem as a service in order to generate or update the required configurations files. Note
   that this step might be required again after a reboot.
    - `systemctl stop 5g-mag-rt-modem`
    - `systemctl start 5g-mag-rt-modem`
3. Since we don't want to run the MBMS Modem as a service in the background but instead provide a prerecorded sample
   file, we need to make sure that the service is not running. Calling `systemctl stop 5g-mag-rt-modem` stops the
   service.
4. Start the MBMS Modem with a sample as
   specified [here](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/mbms-modem#run-a-sample-file). It is
   important to provide the right bandwidth to the MBMS Modem. Consequently, for a 5 MHz bandwidth sample file, the
   command looks like this: `./modem -f "PathToSample/samplefile.raw" -b 5`.

The final output on the terminal should now look like similar to the output below:

````
modem[7891]: 5g-mag-rt modem v1.1.1 starting up
modem[7891]: Initialising SDR
modem[7891]: Launching phy thread with realtime scheduling priority 10
modem[7891]: Launching phy thread with realtime scheduling priority 10
modem[7891]: Launching phy thread with realtime scheduling priority 10
modem[7891]: Launching phy thread with realtime scheduling priority 10
modem[7891]: Launching phy thread with realtime scheduling priority 10
modem[7891]: Raising main thread to realtime scheduling priority 20
modem[7891]: GPS data stream started
modem[7891]: TUN file descriptor 6
modem[7891]: Starting RESTful API handler at http://0.0.0.0:3010/modem-api/
modem[7891]: Phy: PSS/SSS detected: Mode FDD, PCI 333, CFO 0.18315084 KHz, CP Extended
modem[7891]: Phy: MIB Decoded. Mode FDD, PCI 333, PRB 25, Ports 1, CFO 0.18315084 KHz, SFN 0
modem[7891]: Decoded MIB at target sample rate, TTI is 120. Subframe synchronized.
modem[7891]: CINR 16.13 dB
modem[7891]: PDSCH: MCS 5, BLER 0.0, BER 0.0
modem[7891]: MCCH: MCS 2, BLER 0.0, BER 0.0
modem[7891]: MCH 0: MCS 16, BLER 0.0, BER 0.05661512027491409
modem[7891]:     MTCH 0: LCID 1, TMGI 0x00000009f165, 238.1.1.95:40085
modem[7891]:     MTCH 1: LCID 2, TMGI 0x00001009f165, 238.1.1.111:40101
modem[7891]: -----
````

#### MBMS Middleware

Now that the MBMS Modem is running and exposes the FLUTE encoded content via UDP multicast to the MBMS Middleware we can
start the latter as well. The MBMS Middleware listens to the local tun interface. Received multicast packets from the
Receive Process are FLUTE decoded and the files are stored in the cache.

In this example, we start the MBMS Middleware right from the build folder. That way potential debug output is directly
logged to the terminal.

1. Navigate to the build folder of the MBMS Middleware, for instance: `cd /home/user/rt-mbms-mw/build`
2. Start the middleware: `./mw`

The output should look like this:

````
mw[6611]: 5g-mag-rt mw v0.9.0 starting up
````

#### Webinterface

For the purpose of this documentation we use the Webinterface to monitor the MBMS Modem and the MBMS Middleware.
Moreover, we use the hls.js integration in the Webinterface to playback the final HLS stream. In order run the
Webinterface perform the steps
describe [here](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Webinterface#run-the-webinterface).

The Webinterface can also be started directly from its root folder:

1. cd `/home/user/rt-wui`
2. `node app.js`

### Using an SDR card

Todo

## Playback

The final playback is similar for both use cases _"Using an SDR card"_ and _"Using a prerecorded sample file"_.

### Webinterface

In order to use the webinterface for playback perform the following steps:

1. Navigate to `http://localhost` in your browser
2. Click `Middleware v.0.9.1` on the top right corner
3. Click on the play button below the stream information
4. An instance of hls.js is initialized playing the HLS stream

The output for step 3 and step 4 should look similar to this:

<img src="https://github.com/5G-MAG/Getting-Started/blob/main/media/wiki/rt-wui-mw-tab.jpg?raw=true" width="800">

<img src="https://github.com/5G-MAG/Getting-Started/blob/main/media/wiki/rt-wui-playback.jpg?raw=true" width="800">

### VLC

It is also possible to use other players like VLC. Simply paste the url to the `index.m3u8` into the VLC player. As an
example the URL can look the following: `http://localhost/f/00001009f165/index.m3u8`. Replace the `localhost` part with
the IP of the machine that is running the MBMS Middleware in order to access the stream from other machines in the same
network.

## Troubleshooting

### I/O errors in the MBMS Modem

If you encounter I/O errors in the MBMS Modem there are a few things to try:

1. Verify that the correct network interface is used to output the UDP multicast.
   See https://github.com/5G-MAG/Documentation-and-Architecture/wiki/mbms-modem#multicast-routing
2. Make sure to start/stop the MBMS Modem as a service before launching it from the `build` folder:
    - `systemctl start 5g-mag-rt-modem`
    - `systemctl stop 5g-mag-rt-modem`
3. Try starting the MBMS Modem with sudo rights: `sudo ./modem -f "PathToSample/samplefile.raw" -b 5

## References

[1] [https://en.wikipedia.org/wiki/HTTP_Live_Streaming](https://en.wikipedia.org/wiki/HTTP_Live_Streaming)
