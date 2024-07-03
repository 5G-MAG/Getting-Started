---
layout: default
title:  RTP Playback over 5G Broadcast
parent: Tutorials
grand_parent: MBMS and LTE-based 5G Broadcast
has_children: false
---

# Tutorial - RTP Playback over 5G Broadcast

## Introduction

The goal of this documentation is to provide a use-case oriented information, i.e., the required steps to setup the 5G-MAG Reference Tools to use an RTP stream which was received via 5G Broadcast [1], processed by the [MBMS Modem](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/MBMS-Modem) and played in a third-party media player such as ffplay or VLC. 

## Background

### Real-Time Transport Protocol (RTP)
The Real-Time Transport Protocol (RTP) is a network protocol for delivering audio and video data via unicast or multicast over IP-based networks.

More information can be found in the IETF RTP specification:

* [RTP: A Transport Protocol for Real-Time Applications](https://datatracker.ietf.org/doc/html/rfc3550)

### Multimedia Broadcast/Multicast Service (MBMS)

MBMS is a point-to-multipoint service in which data is transmitted from a single source entity to multiple recipients.
The MBMS bearer service offers two modes, namely broadcast mode and multicast mode. This use-case focus on the broadcast reception mode (5G Broadcast).

More information about MBMS and the related interfaces and components can be found in the corresponding 3GPP and ETSI
specifications:

* [23.246 - Multimedia Broadcast/Multicast Service (MBMS); Architecture and functional description(Release 16)](https://www.3gpp.org/ftp/Specs/archive/23_series/23.246/)
* [26.347 - Multimedia Broadcast/Multicast Service (MBMS); Application Programming Interface and URL (Release 16)](https://www.3gpp.org/ftp/Specs/archive/26_series/26.347/)
* [26.346 - Multimedia Broadcast/Multicast Service (MBMS); Protocols and codecs(Release 16)](https://www.3gpp.org/ftp/Specs/archive/26_series/26.346)
* [29.116 - Representational state transfer over xMB reference point between content provider and BM-SC](https://www.3gpp.org/ftp/Specs/archive/29_series/29.116)
* [ETSI TS 123 246 - Multimedia Broadcast/Multicast Service (MBMS); Architecture and functional description ](https://www.etsi.org/deliver/etsi_ts/123200_123299/123246/)

### 5G-MAG Reference Tools 

Detailed information about the architecture of the 5G-MAG Reference Tools and how the MBMS broadcast mode is implemented can
be found on the Wiki pages of the different projects:

* [MBMS Modem](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/MBMS-Modem)
* [Webinterface](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Webinterface)

## Requirements

In order to be able to play an RTP stream which is received by 5G Broadcast, we need to install and run the following components of the 5G-MAG Reference Tools (make sure you have the suggested [hardware](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Hardware-Requirements#hardware-requirements) and [OS](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Hardware-Requirements#os) ready):


| Component  | Required/Optional | Min version  | Description |
| ------------- | ------------- | ------------- | ------------- |
| [MBMS Modem](https://github.com/5G-MAG/rt-mbms-modem) | Required | v1.1.1  | The MBMS Modem builds the lower part of the 5G-MAG Reference Tools. Its main task is to convert a 5G BC input signal (received either as live I/Q raw data from the SDR or as prerecorded SDR sample file) to multicast IP packets on the output. The MBMS Modem can run as a background process or can be started/stopped manually. |
| [RTP sample recording](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Sample-Files#rtp-payload)  | Optional (setup requires either a sample recording or a SDR) | / | In order to support application developers as well as 5G-MAG contributors for testing their improvements, ORS captured sample files ("raw data" = digitized I/Q data at LimeSDR Mini output) directly from a 5G BC transmitter.
| Software Defined Radio (SDR) | Optional (setup requires either a sample recoding or a SDR) | / | In case you are able to receive 5G Broadcast live signals, you need a Software Defined Radio (SDR) to convert the radio signal to a digitized I/Q data to feed the MBMS modem. A list of working SDRs can be found [here](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Hardware-Requirements#supported-sdr)
| Video Player | Required | / | For playback of the UDP multicast that is exposed by the MBMS modem we need a player that can handle UDP multicast inputs. As part of this tutorial, we will demonstrate playback in the [VLC Media Player](https://www.videolan.org/vlc/) and [ffplay](https://ffmpeg.org/download.html)


## Basic workflow

As described in [Requirements](#Requirements) we need the MBMS Modem, the MBMS Middleware and a media player in order to
enable playback of HLS content in broadcast mode using the 5G-MAG Reference Tools. The basic interaction and output of
these components are illustrated in the Figure below:

![Architecture](https://github.com/5G-MAG/Getting-Started/blob/main/media/architecture/5G-MAG%20RT%20Architecture%20RTP%20example.drawio.png?raw=true)

The output of the SDR or the sample file serves as the input for the MBMS Modem. The MBMS Modem converts the input data
to a UDP multicast. The UDP multicast can be played directly in ffplay or VLC. 

## Installation

Detailed installation instructions can be found in the respective Wiki documentation of the different projects. In order
to enable RTP playback via MBMS the following steps are required:

1. [Install the MBMS Modem](https://github.com/5G-MAG/rt-mbms-modem#readme)
2. Install at least one of the following media players:
   - [Install VLC](https://www.videolan.org/vlc/#download)
   - [Install ffplay](https://linuxize.com/post/how-to-install-ffmpeg-on-ubuntu-20-04/)
3. [Download an RTP sample file](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Sample-Files#rtp-payload) or setup an RTP live stream on your transmitting infrastructure. 

## Running the components

Once all the required components have been installed, we need to sequentially start all of them. Depending on the
concrete use case (either a live SDR input or a prerecorded sample file) the concrete calls are slightly different. 

### Using a prerecorded sample file
This Section provides information on how to run the 5G-MAG Reference Tools using a prerecorded HLS sample file.

#### MBMS Modem
1. Follow the detailed instructions on how to configure multicast routing provided [here](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/mbms-modem#run-the-mbms-modem).
2. Stop and start the MBMS Modem as a service in order to generate or update the required configurations files. Note that this step might be required again after a reboot. 
   - `systemctl stop 5gmag-rt-modem`
   - `systemctl start 5gmag-rt-modem`
3. Since we don't want to run the MBMS Modem as a service in the background but instead provide a prerecorded sample file, we need to make sure that the service is not running. Calling `systemctl stop 5g-mag-rt-modem` stops the service. 
4. Start the MBMS Modem with a sample as specified [here](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/mbms-modem#run-a-sample-file). It is important to provide the right bandwidth to the MBMS Modem. Consequently, for a 5 MHz bandwidth sample file, the command looks like this: `sudo ./modem -f "PathToSample/5MHz_MCS16_1kHz25_RTP_3.5.raw" -b 5`. 

The final output on the terminal should now look similar to the output below:
````
modem[10498]: Phy: PSS/SSS detected: Mode FDD, PCI 333, CFO 0.20108362 KHz, CP Extended
modem[10498]: Phy: MIB Decoded. Mode FDD, PCI 333, PRB 25, Ports 1, CFO 0.20108362 KHz, SFN 528
modem[10498]: Decoded MIB at target sample rate, TTI is 5360. Subframe synchronized.
modem[10498]: CINR 20.82 dB
modem[10498]: PDSCH: MCS 5, BLER 0.0, BER 0.0
modem[10498]: MCCH: MCS 2, BLER 0.0, BER 0.0
modem[10498]: MCH 0: MCS 16, BLER 0.0, BER 0.05661512027491409
modem[10498]:     MTCH 0: LCID 1, TMGI 0x00000309f165, 238.1.1.95:40085
modem[10498]:     MTCH 1: LCID 2, TMGI 0x00001009f165, 239.11.4.10:5520
modem[10498]: -----
modem[10498]: CINR 18.12 dB
modem[10498]: PDSCH: MCS 5, BLER 0.0, BER 0.0
modem[10498]: MCCH: MCS 2, BLER 0.0, BER 0.0
modem[10498]: MCH 0: MCS 16, BLER 0.0, BER 0.04579037800687285
modem[10498]:     MTCH 0: LCID 1, TMGI 0x00000309f165, 238.1.1.95:40085
modem[10498]:     MTCH 1: LCID 2, TMGI 0x00001009f165, 239.11.4.10:5520
modem[10498]: -----
````

### Using an SDR card

Todo

## Playback
The final playback is similar for both use cases _"Using an SDR card"_ and _"Using a prerecorded sample file"_.

### Playback url
To identify the correct multicast address for playback, navigate to the terminal in which the modem process is running and check the log output. Next to the `TMGI` information, the multicast addresses are listed:

````
modem[10498]: CINR 20.38 dB
modem[10498]: PDSCH: MCS 5, BLER 0.0, BER 0.0
modem[10498]: MCCH: MCS 2, BLER 0.0, BER 0.0
modem[10498]: MCH 0: MCS 16, BLER 0.0, BER 0.0468213058419244
modem[10498]:     MTCH 0: LCID 1, TMGI 0x00000309f165, **238.1.1.95:40085**
modem[10498]:     MTCH 1: LCID 2, TMGI 0x00001009f165, **239.11.4.10:5520**
modem[10498]: -----
````
In this case, we see two addresses, `238.1.1.95:40085` and `239.11.4.10:5520`. 

### ffplay
To play the stream in ffplay run the following steps

1. Open a new terminal
2. Start ffplay specifying the address to the multicast stream: `ffplay udp://239.11.4.10:5520`

The output should look like this:

<img src="https://github.com/5G-MAG/Getting-Started/blob/main/media/wiki/ffplay-rtp.png?raw=true" width="800">

### VLC
It is also possible to use VLC for playback:

1. Open VLC
2. Navigate to `Media > Open Network Stream`
3. Enter the stream url `rtp://@239.11.4.10:5520`
4. Press play

The output should look like this:

<img src="https://github.com/5G-MAG/Getting-Started/blob/main/media/wiki/rtp-vlc.png?raw=true" width="800">

## Troubleshooting

### I/O errors in the MBMS Modem
If you encounter I/O errors in the MBMS Modem, there are a few things to try:

1. Verify that the correct network interface is used to output the UDP multicast. See https://github.com/5G-MAG/Documentation-and-Architecture/wiki/mbms-modem#multicast-routing
2. Make sure to start/stop the MBMS Modem as a service before launching it from the `build` folder: 
   - `systemctl start 5g-mag-rt-modem`
   - `systemctl stop 5g-mag-rt-modem`
3. Try starting the MBMS Modem with sudo rights: `sudo ./modem -f "PathToSample/samplefile.raw" -b 5


## References

[1] [LTE-based 5G Terrestrial Broadcast](https://github.com/5G-MAG/Documentation-and-Architecture#lte-based-5g-terrestrial-broadcast) <br />
