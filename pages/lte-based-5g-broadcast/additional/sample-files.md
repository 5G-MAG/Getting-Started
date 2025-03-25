---
layout: default
title:  Sample files
parent: Additional Resources
grand_parent: 5G Broadcast (MBMS)
has_children: false
nav_order: 2
---
<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Sample files
In order to support application developers as well as 5G-MAG contributors for testing their improvements, ORS captured sample files ("raw data" = digitized I/Q data at [LimeSDR Mini](https://www.crowdsupply.com/lime-micro/limesdr-mini/) output) directly from a 5G BC transmitter. You can also capture sample files using the [capture command of the Receive Process](https://github.com/5G-MAG/rt-mbms-modem#capture-and-running-of-sample-files).

#### RTP payload:
3 MHz bandwidth, subcarrier spacing 1.25 kHz, Modulation Coding Scheme 16 (16QAM) with Payload 3.5 Mbit RTP:
* [3MHz_MCS16_1kHz25_RTP_3.5.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/3MHz_MCS16_1kHz25_RTP_3.5.raw) (7.9 GB)

5 MHz bandwidth, subcarrier spacing 1.25 kHz or 7.5 kHz, Modulation Coding Scheme 16 (16QAM) with Payload 3.5 Mbit RTP:
* [5MHz_MCS16_1kHz25_RTP_3.5.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/5MHz_MCS16_1kHz25_RTP_3.5.raw) (14.5 GB)
* [5MHz_MCS16_7kHz5_RTP_3.5.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/5MHz_MCS16_7kHz5_RTP_3.5.raw) (11.4 GB)

6 MHz bandwidth, subcarrier spacing 1.25 kHz, Modulation Coding Scheme 16 (16QAM) with Payload 3.5 Mbit RTP:
* [6MHz_MCS16_1kHz25_RTP_3.5.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/6MHz_MCS16_1kHz25_RTP_3.5.raw) (33.7 GB)

7 MHz bandwidth, subcarrier spacing 1.25 kHz, Modulation Coding Scheme 16 (16QAM) with Payload 3.5 Mbit RTP:
* [7MHz_MCS16_1kHz25_RTP_3.5.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/7MHz_MCS16_1kHz25_RTP_3.5.raw) (23.6 GB)

8 MHz bandwidth, subcarrier spacing 1.25 kHz, Modulation Coding Scheme 16 (16QAM) with Payload 3.5 Mbit RTP:
* [8MHz_MCS16_1kHz25_RTP_3.5.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/8MHz_MCS16_1kHz25_RTP_3.5.raw) (23.5 GB)

10 MHz bandwidth, subcarrier spacing 1.25 kHz, Modulation Coding Scheme 16 (16QAM) with Payload 3.5 Mbit RTP:
* [10MHz_MCS16_1kHz25_RTP_3.5.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/10MHz_MCS16_1kHz25_RTP_3.5.raw) (21.6 GB)

#### HLS payload:

3 MHz bandwidth, subcarrier spacing 1.25 kHz, Modulation Coding Scheme 16 (16QAM) with Payload HLS:
* [3MHz_MCS16_1kHz25_HLS_q6a.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/3MHz_MCS16_1kHz25_HLS_q6a.raw) (5.9 GB)

5 MHz bandwidth, subcarrier spacing 1.25 kHz, Modulation Coding Scheme 16 (16QAM) with Payload HLS:
* [5MHz_MCS16_1kHz25_HLS_q6a.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/5MHz_MCS16_1kHz25_HLS_q6a.raw) (12.2 GB)

8 MHz bandwidth, subcarrier spacing 1.25 kHz, Modulation Coding Scheme 16 (16QAM) with Payload HLS:
* [8MHz_MCS16_1kHz25_HLS_q6a.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/8MHz_MCS16_1kHz25_HLS_q6a.raw) (25.4 GB)

10 MHz bandwidth, subcarrier spacing 1.25 kHz, Modulation Coding Scheme 16 (16QAM) with Payload HLS:
* [10MHz_MCS16_1kHz25_HLS_q6a.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/10MHz_MCS16_1kHz25_HLS_q6a.raw) (17.6 GB)

#### DASH payload:
5 MHz bandwidth, subcarrier spacing 1.25 kHz, Modulation Coding Scheme 16 (16QAM) with Payload DASH:
* [5MHz_MCS16_1kHz25_DASH_q6a.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/5MHz_MCS16_1kHz25_DASH_q6a.raw) (10.4 GB)

#### Sample files for rt-mbms-modem development Rel14/Rel16 only:
* Rel.14 CAS [5MHz_MCS16_1kHz25_HLS_q4a_Rel14.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/5MHz_MCS16_1kHz25_HLS_q4a_Rel14.raw) (5.4 GB)
* Rel.16 CAS [5MHz_MCS16_1kHz25_HLS_q4a_Rel16.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/5MHz_MCS16_1kHz25_HLS_q4a_Rel16.raw) (5.1 GB) (PBCH Repetition, Aggregation Level 16, CFI-Indicator in MIB-MBMS)
  * **Note**: Release 16 is currently not supported in the rt-mbms-modem. This stream can be used for development purposes.
* Rel.16 CAS [8MHz_MCS16_1kHz25_Rel16.raw](https://obeca-testdaten.s3.eu-central-1.amazonaws.com/8MHz_MCS16_1kHz25_Rel16.raw) (13.4 GB) (PBCH Repetition, Aggregation Level 16, CFI-Indicator in MIB-MBMS)
  * **Note**: Release 16 is currently not supported in the rt-mbms-modem. This stream can be used for development purposes.
> Note: The sample files were captured in Nov 2021. An mp4 file of the movie [Big Buck Bunny](https://www.bigbuckbunny.org) (published under the [Creative Commons Attribution 3.0 license](https://creativecommons.org/licenses/by/3.0/), (c) copyright 2008, Blender Foundation / [www.bigbuckbunny.org](https://www.bigbuckbunny.org)) was looped to create RTP and HLS streams. Play duration of each sample file is 3-5 minutes.

If you need any further sample files, please get in contact with us **[reference-tools@5g-mag.com](mailto:reference-tools@5g-mag.com)**.
