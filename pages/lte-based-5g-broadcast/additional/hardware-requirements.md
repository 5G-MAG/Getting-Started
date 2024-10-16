---
layout: default
title:  Hardware requirements
parent: Additional Resources
grand_parent: 5G Broadcast - MBMS & LTE-based 5G Broadcast
has_children: false
nav_order: 1
---

# Hardware requirements
## Table of content
* <a href="#hardware-requirements"> Hardware requirements</a>
* <a href="#supported-sdr"> Supported SDR</a>
* <a href="#os"> OS</a>
* <a href="#reference-setups"> Reference setups</a>

## Hardware requirements

It is hard to define system requirements because these depend e.g. on bandwidth (e.g., 5, 8, 10 MHz), modulation coding
scheme and other parameters. Generally, a CPU with 4 cores and 8 threads, 16 GB RAM and - in case a SDR and not just
sample files are used - an USB 3.0 port is necessary. Furthermore, HDMI, Wifi, LAN and sufficient SSD space (for sample
files,...) is recommended.

If you want to be sure that everything is working, we recommend to use our reference system.
> **Note** We would appreciate if you let us know about your setup to list it below. Drop us a mail [reference-tools@5g-mag.com](mailto:reference-tools@5g-mag.com).

## Supported SDR

To use the 5G-MAG Reference Tools in a live setup a SDR (software defined radio) is required.

5G-MAG Reference Tools *[MBMS Modem](MBMS-Modem)* supports [SoapyAPI](https://github.com/pothosware/SoapySDR/wiki), thus any
supported SDR should work with the 5G-MAG Reference Tools (please keep in mind that not every SDR hardware is sufficient for receiving an 5G
Broadcast signal (e.g. bandwidth, sample rate...)).

We recommend using a [LimeSDR Mini](https://limemicro.com/products/boards/limesdr-mini/)
or [BladeRF 2.0 Micro XA4](https://www.nuand.com/product/bladeRF-xA4). A [HackRF One](https://greatscottgadgets.com/hackrf/one/) can also be used.
Each has to be connected via USB to the computer and to your antenna via SMA connector.

* LimeSDR Mini can be ordered e.g. at [CrowdSupply](https://www.crowdsupply.com/lime-micro/limesdr-mini/)  for around
  160 EUR
* BladeRF can be ordered e.g. at [nuand](https://www.nuand.com/product/bladeRF-xA4) for around 480 EUR.
* HackRF One are widely available. Please see [their website](https://greatscottgadgets.com/hackrf/one/) for availability, typically around 250 EUR.
* Ettus USRP N310
* Ettus USRP B210

> **Note** If you are using another SDR, please let us know that we can update the list above. Drop us a mail [reference-tools@5g-mag.com](mailto:reference-tools@5g-mag.com).

> **Note** If you only want to test with sample files, a SDR is NOT required.

## OS

We recommend to use [Ubuntu 20.04 LTS (64 bit)](https://ubuntu.com/), but if you build everything from source, also
other OS should work (e.g., Ubuntu 18, Debian, Raspbian...)
> **Note** We would appreciate if you let us know about your setup to list it below. Drop us a mail [reference-tools@5g-mag.com](mailto:reference-tools@5g-mag.com).

## Reference setups

### 5G-MAG Reference Tools system

#### Specs

<p align="center"><img src="https://github.com/5G-MAG/Documentation-and-Architecture/blob/main/media/wiki/reference-ors.png"></p>

| Component | Part | Approx. price (EUR) |
| ------------- |-------------|-------------|
| Intel NUC | <a href="https://www.amazon.de/gp/product/B08CNLFM1N/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1" target="_blank">Intel Provo Canyon BKNUC8V7PNH</a> | 600 |
| RAM | <a href="https://www.amazon.de/gp/product/B08C4VKYFG/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1" target="_blank">Crucial RAM CT16G4SFRA266 16GB DDR4 2666 MHz CL19</a> | 60 |
| SSD| <a href="https://www.amazon.de/gp/product/B07BSSFB4N/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1" target="_blank">SanDisk Extreme PRO M.2 NVMe 3D SSD 500 GB interne SSD</a> | 70 |
| Power cord| <a href="https://www.amazon.de/gp/product/B00K65JGUY/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1" target="_blank">LINDY 30406 - Power cord for notebooks (Schuko) 3m</a> | 10 |
| _Optional:_ |
| _
Display_|  <a href="https://www.amazon.de/gp/product/B08B67KJ75/ref=ppx_yo_dt_b_asin_title_o00_s02?ie=UTF8&psc=1" target="_blank">Capacitive display 7" IPS 1024x600</a> | 70 |

The full specification of the Intel NUC can be
found [here](https://ark.intel.com/content/www/us/en/ark/products/199110/intel-nuc-8-pro-kit-nuc8v7pnh.html).

If you want to fully integrate the SDR into the NUC as seen on the picture
above: [5G-MAG Reference Tools casing](https://github.com/johannmika/obeca-ors-casing)

#### Testcases

The 5G-MAG Reference Tools system was tested live, with sample files, with bandwidths 3, 5, 6, 7, 8 and 10 MHz, SCS 1.25 and 7.5 kHz and
modulation coding schemes (MCS) 1-26 with multiple services (RTP, HLS). Max CPU (2 services, 10 MHz, MCS26) was below
60%.

### VM

#### Specs

Ubuntu 20 with Hyper-V on Windows 10.

#### Testcases

We tested the build process and sample files (1 RTP service, 5 MHz).
