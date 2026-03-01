---
layout: default
title: SDR Platforms srsRAN
parent: Tutorials
grand_parent: 3GPP RAN and Core
has_children: false
nav_order: 0
---

<img src="../../../assets/images/Banner_3GPP_Platforms.png" /> 

# Tutorial - SDR Platforms for srsRAN

This page collects instructions to install and run some SDR Platforms which developers have used to build demonstrators for the 5G Broadcast project, which work for srsRAN

The following instructions have been tested to work in Ubuntu 22.04 LTS.

## Install SDR drivers

````
sudo apt install libsoapysdr-dev soapysdr-tools
````

## Using BladeRF with Soapy

For BladeRF the relevant package is named *soapysdr-module-bladerf*. Install it by running:
````
sudo apt install soapysdr-module-bladerf
````
Finally, install the BladeRF firmware:
````
sudo add-apt-repository ppa:nuandllc/bladerf
sudo apt-get update
sudo apt-get install bladerf
````

## Using LimeSDR with Soapy

Lime Suite needs to be built from source at a specific commit. *Do not* use the package available through apt, as the version it packages does not seem to work reliably with LimeSDR Minis and causes calibration errors and unreliable reception. Please follow these steps:

```
cd ~
git clone https://github.com/myriadrf/LimeSuite.git
cd LimeSuite/
git checkout 28031bfcffe1e8fa393c7db88d4fe370fb4c67ea
mkdir buildir
cd buildir
cmake -G Ninja ..
ninja
sudo ninja install
sudo ldconfig
```

## Using HackRF One with Soapy
It should be noted that the HackRF One is a half-duplex SDR and has issues synchronising using the internal clock, documented [here](https://hackrf.readthedocs.io/en/latest/clocking.html). Synchronisation can be achieved by providing an external CLKIN signal using e,g, Keysight 33120A configured to output a 10 MHz sine wave with amplitude 1.5 Vpp and offset 0.75 V (as it is an high impedance input). Alternatively, a simpler option is to install [this component](https://www.nooelec.com/store/tiny-tcxo.html) following [these instructions](https://f1atb.fr/index.php/2020/05/26/tcxo-installation-on-hackrf/). You may also want to install some [RF shielding](https://hackaday.io/project/158323/instructions).

For HackRF One , install by running:
````
sudo apt install hackrf soapysdr-module-hackrf
````
Plug in your HackRF and verify it is recognised using: 
````
hackrf_info
````
Example output:
```
hackrf_info version: unknown
libhackrf version: unknown (0.5)
Found HackRF
Index: 0
Serial number: 0000000000000000xxxxxxxxxxxxxxxx
Board ID Number: 2 (HackRF One)
Firmware Version: 2018.01.1 (API:1.02)
Part ID Number: 0xa000cb3c 0x0066435f
```

## Adjusting configuration for rt-mbms-modem
Note: After installing rt-mbms-modem using the instructions below you must modify the rt-mbms configuration parameter in `/etc/5gmag-rt.conf`:

Example for BladeRF:
```
device_args = "driver=bladerf";
antenna = "RX"
```

Example for LimeSDR:
```
device_args = "driver=lime";
antenna = "LNAW";
```

Example for HackRF:
```
device_args = "driver=hackrf";
antenna = "TX/RX";
```

## Check SDR availability
Check if the SDR can be found on your system

```
SoapySDRUtil --find
```

Example for BladeRF:
```
######################################################
##     Soapy SDR -- the SDR abstraction library     ##
######################################################
Found device 2
  backend = libusb
  device = 0x02:0x09
  driver = bladerf
  instance = 0
  label = BladeRF #0 [ANY]
  serial = ANY
```

Example for LimeSDR:
```
######################################################
##     Soapy SDR -- the SDR abstraction library     ##
######################################################

Found device 0
  addr = 24607:1027
  driver = lime
  label = LimeSDR Mini [USB 2.0] 1D587FCA09A966
  media = USB 2.0
  module = FT601
  name = LimeSDR Mini
  serial = 1D587FCA09A966
```

Example for HackRF One:
```
######################################################
##     Soapy SDR -- the SDR abstraction library     ##
######################################################

Found device 3
  device = HackRF One
  driver = hackrf
  label = HackRF One #0 75b068dc3_______
  part_id = a000cb3c0066435f
  serial = 000000000000000075b068dc3_______
  version = 2018.01.1
  
```

## Other SDRs

While we've only tested with Lime- and Blade-SDRs, Soapy supports a wide range of SDR devices, which should therefore also be usable with 5gmag-rt-modem if they support the high bandwidth/sample rates required for FeMBMS decoding.

You can find more info on device support at https://github.com/pothosware/SoapySDR/wiki

Running ``apt search soapysdr-module`` lists all available modules.

If you successfully (or unsuccessfully) try 5gmag-rt-modem with another SDR, please let us know! 


## Troubleshooting

When running the command ``SoapySDRUtil --find`` you might get a duplicate entry error:
```
######################################################
##     Soapy SDR -- the SDR abstraction library     ##
######################################################

[ERROR] SoapySDR::loadModule(/usr/local/lib/SoapySDR/modules0.7/libLMS7Support.so)
  duplicate entry for lime (/usr/lib/x86_64-linux-gnu/SoapySDR/modules0.7/libLMS7Support.so)
```
This is because a duplicate limesuite apt package has incorrectly been installed when installing the Soapy module and LimeSuite. You can identify this package by running the command:
```
$ sudo apt list --installed | grep lime
< ... >
liblimesuite20.01-1/focal,now 20.01.0+dfsg-2 amd64 [installed,automatic]
```
You can fix this issue by deleting this package:
```
sudo apt remove liblimesuite20.01-1
```
