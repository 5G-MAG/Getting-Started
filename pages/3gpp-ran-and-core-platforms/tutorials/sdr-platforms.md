---
layout: default
title: SDR for 5G Broadcast
parent: Tutorials
grand_parent: 3GPP RAN and Core Platforms
has_children: false
nav_order: 0
---

# Tutorial - SDR Platforms for 5G Broadcast

This page collects instructions to install and run some SDR Platforms which developers have used to build demonstrators for the 5G Broadcast project.

## Blade RF

The following instructions have been tested to work in Ubuntu 22.04 LTS.

### Install SDR drivers

````
sudo apt install libsoapysdr-dev soapysdr-tools
````

### Using BladeRF with Soapy

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

### Check SDR availability
Check if the SDR can be found on your system
````
SoapySDRUtil --find
````

The output should look like this:
````
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
````
