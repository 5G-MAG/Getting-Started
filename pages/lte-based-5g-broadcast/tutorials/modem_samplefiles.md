---
layout: default
title: MBMS Modem - Sample Files
parent: Tutorials
grand_parent: 5G Broadcast - TV/Radio
has_children: false
nav_order: 0
---

# Tutorial - MBMS Modem with sample files

The rt-mbms-modem can be run with sample files. See [Sample Files](https://5g-mag.github.io/Getting-Started/pages/lte-based-5g-broadcast/additional/sample-files.html).

Before capturing or running a sample file, make sure that *MBMS Modem* isn't running in background. If it is, stop *MBMS Modem* with ``systemctl stop 5g-mag-rt-modem``.

## Capture a sample file

In order to capture sample files, you need to receive a 5G BC signal.

Run the command:

```
modem -w "PathToSample/samplefile.raw"
```

to capture the raw I/Q data from the SDR.

## Run a sample file

**Important**: For correct pre-configuring of the MBMS Modem at system startup, it has to be run through systemd once, see https://github.com/5G-MAG/rt-mbms-modem#configuration

Based on the structure of the Service Announcement file the configuration file in `/etc/5gmag-rt.conf` needs to be adjusted. For details refer to the corresponding [documentation](https://5g-mag.github.io/Getting-Started/pages/lte-based-5g-broadcast/additional/rt-common-shared/MBMS-service-announcement-files.html). 

If you like to start *MBMS Modem* with a downloaded sample file, you can run the following command:

```
modem -f "PathToSample/samplefile.raw" -b 10
```

> **Notice:** ``-b 10`` represents the used bandwith when the sample file was captured (see <a href="#Manual-startstop">Manual start/stop</a>). So for a 5 MHz bandwidth sample file you need to adjust the command to ``-b 5``
