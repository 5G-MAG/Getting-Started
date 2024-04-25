---
layout: default
title:  GPS Time Synchonization for rt-mbms-modem
parent: Tutorials
grand_parent: MBMS and LTE-based 5G Broadcast
has_children: false
nav_order: 0
---

# GPS Time Synchonization for rt-mbms-modem

Preconditions: install, configure and enable ``gpsd`` by
following [this guide.](https://github.com/5G-MAG/rt-mbms-modem#measurement-recording-and-gps)

## Install chrony

````
sudo apt install chrony
````

## Edit ``/etc/chrony/chrony.conf``, and add the following line at the end:

````
refclock SHM 0  delay 0.5 refid NMEA
````

## Edit ``/etc/default/gpsd``, and add options '-n -b':

````
# Devices gpsd should collect to at boot time.
# They need to be read/writeable, either by user gpsd or the group dialout.
DEVICES="/dev/ttyACM0"
# Other options you want to pass to gpsd
GPSD_OPTIONS="-n -b"
````

## Restart gpsd and chrony:

````
sudo systemctl restart gpsd
sudo systemctl restart chrony
````

## Done!

You can check if chrony receives time data from your GPS devices with ``chronyc sources``

After around 30 seconds, you should see last sample data in the NMEA line, e.g:

````
210 Number of sources = 9
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
#- NMEA                          0   4   377    11    +73ms[  +73ms] +/-  251ms
^- pugot.canonical.com           2   6   377    53   +394us[ +394us] +/-   54ms
^+ chilipepper.canonical.com     2   6   377    54   +156us[ +185us] +/-   44ms
^- alphyn.canonical.com          2   6   377    52   +624us[ +624us] +/-  127ms
^+ golem.canonical.com           2   6   377    55   +324us[ +352us] +/-   53ms
^+ extern4.nemox.net             2   6   377    54   -177us[ -149us] +/-   48ms
^+ 194.112.182.172               2   6   377    55   -151us[ -123us] +/-   29ms
^* ntp.candystore.at             2   6   377    53   +132us[ +160us] +/-   23ms
^+ svn.mediainvent.at            2   6   377    55    -94us[  -66us] +/-   36ms
````
