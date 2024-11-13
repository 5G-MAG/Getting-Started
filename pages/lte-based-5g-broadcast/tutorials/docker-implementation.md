---
layout: default
title: Linux stack - Docker support
parent: Tutorials
grand_parent: 5G Broadcast - MBMS & LTE-based 5G Broadcast
has_children: false
nav_order: 4
---

# Linux stack - Docker support for rt-mbms client side

## Introduction

The repository contains the implementation of rt-mbms processes (5G broadcast receiver) in docker containers.
[rt-mbms-modem](https://github.com/5G-MAG/rt-mbms-modem), [rt-mbms-mw](https://github.com/5G-MAG/rt-mbms-mw), [rt-wui](https://github.com/5G-MAG/rt-wui)
and nginx are run in individual containers which interact each other using the native docker network.

## Pre-requisites

### Hardware requirements

It is hard to define system requirements because these depend e.g. on bandwidth (e.g., 5, 8, 10 MHz), modulation coding
scheme and other parameters. Generally, a CPU with 4 cores and 8 threads, 16 GB RAM and - in case a SDR and not just
sample files are used - an USB 3.0 port is necessary. Furthermore, HDMI, Wifi, LAN and sufficient SSD space (for sample
files,...) is recommended.

### Supported SDR

To use the rt-mbms processes in a live setup a SDR (software defined radio) is required.
[MBMS Modem](https://github.com/5G-MAG/rt-mbms-modem)
supports [SoapyAPI](https://github.com/pothosware/SoapySDR/wiki), thus any supported SDR should work with the 5G-MAG
Reference Tools (please keep in mind that not every SDR hardware is sufficient for receiving an 5G Broadcast signal (
e.g. bandwidth, sample rate...)).

We recommend using a LimeSDR or USRP n210 as in the current reference.

### OS

We recommend to use [Ubuntu 20.04 LTS (64 bit)](https://ubuntu.com/)

### Reference setups

#### Hardware Specs

* Intel NUC [Intel Provo Canyon BKNUC8V7PNH](https://www.amazon.de/gp/product/B08CNLFM1N/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)
* RAM    [Crucial RAM CT16G4SFRA266 16GB DDR4 2666 MHz CL19](https://www.amazon.de/gp/product/B08C4VKYFG/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1)
* SSD    [SanDisk Extreme PRO M.2 NVMe 3D SSD 500 GB interne SSD](https://www.amazon.de/gp/product/B07BSSFB4N/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
* Power cord    [LINDY 30406 - Power cord for notebooks (Schuko) 3m](https://www.amazon.de/gp/product/B00K65JGUY/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)

The full specification of the Intel NUC can be
found [here](https://ark.intel.com/content/www/us/en/ark/products/199110/intel-nuc-8-pro-kit-nuc8v7pnh.html).

#### Tested configurations

The 5G-MAG Reference Tools system was tested live, with sample files, with bandwidths 3, 5, 6, 7, 8 and 10 MHz, SCS 1.25
and 7.5 kHz with multiple services (RTP, HLS).

## Installation of rt-mbms-processes with Docker:

1. Install the docker engine.
2. Build the Docker Images
3. Running Containers
4. Execute the Containers

### Step 1: Installing Docker

[Dockerhub](https://docs.docker.com/engine/install/ubuntu/) hosts the docker engine repos which can be easily installed
locally to start working with docker.

**Alternatively**, easy to use shell script can be
found [here](https://github.com/5G-MAG/rt-mbms-modem/blob/development/dockerPrereq.sh)!

### Build Images

The files for the docker implementation are contained
in [rt-mbms-modem](https://github.com/5G-MAG/rt-mbms-modem/tree/development/modem), [rt-mbms-mw](https://github.com/5G-MAG/rt-mbms-mw/tree/development/middleware), [rt-wui](https://github.com/5G-MAG/rt-wui/tree/development/wui)
and [nginx](https://github.com/5G-MAG/rt-wui/tree/development/nginx).

The Dockerfile helps to create a docker image, which can be used to run the containers.

The command `docker build` uses by default the Dockerfile to create the image. For custom docker files go with    
`docker build -f /path/to/Dockerfile -t target_image_name /location/of/Dockerfile`

There is a build.sh script on each folder for easy access.

**Note:** Please edit the appropriate path to the sample files in the last line
of [startup](https://github.com/5G-MAG/rt-mbms-modem/tree/development/modem/scripts) script for modem process before
building the container.

### Running the containers

The modem, middleware, wui and nginx containers can be run using the run.sh script in their respective folders.

The run.sh script contains the `docker logs` command which helps the user to have an idea on what is happening inside
the containers.

**Note:** Please build docker images and run the containers in the order of

1. rt-mbms-modem
2. rt-mbms-mw
3. rt-wui
4. nginx respectively

The resulting IP addresses of the containers are

    Modem - 172.17.0.2
    mbms-mw - 172.17.0.3
    wui    - 172.17.0.4
    nginx  - 172.17.0.5

`sudo docker inspect container_name | grep IPAddress` returns the IP of the container.

If you have different IPs please configure the corresponding IPs in `5gmag-rt.conf` , wui and nginx config files.

### Executing the Containers

The docker exec commands helps you to get into the container.
`docker exec -it container_name /bin/bash`

The list of the containers (running or exited) can be viewed using :
`docker ps -a ` . The staus column shows the staus of each container.

A running container can be stopped using:
`docker stop container_name`

An exited or obsolete container can be removed using :
`docker rm container_name`  
