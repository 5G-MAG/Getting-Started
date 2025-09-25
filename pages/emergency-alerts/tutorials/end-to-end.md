---
layout: default
title: CBS over 5G Broadcast
parent: Tutorials
grand_parent: 5G Broadcast - Emergency Alerts
has_children: false
nav_order: 1
---

# Tutorial - Cell Broadcast emergency alerts over a 5G Broadcast transmitter

This tutorial describes a basic setup to deliver emergency alerts compliant with CBS over the rt-mbms-tx-for-qrd-and-crd from 5G-MAG Reference Tools.

## Architecture

TODO

## Requirements

The following components are required to setup the end to end chain for emergency alerts:

* A QRD or CRD device
* A Software Defined Radio (SDR) such as the [BladeRF](https://www.nuand.com/bladerf-2-0-micro/) with an antenna
  connected to the TX1 port
* A Linux machine running Ubuntu 22

## Installation

### Step 1: Install the 5G Broadcast Transmitter

Install the dependencies and SDR drivers for the transmitter as documented [here](https://github.com/5G-MAG/rt-mbms-tx-for-qrd-and-crd).

Next, clone the transmitter repository using the `emergency-alerts` branch:

```
git clone --recurse-submodules -b emergency-alerts https://github.com/5G-MAG/rt-mbms-tx-for-qrd-and-crd.git rt-mbms-tx-for-qrd-and-crd-emergency-alerts
```

Now build the transmitter running the following commands:

```
cd rt-mbms-tx-for-qrd-and-crd-emergency-alerts
git submodule update
mkdir build && cd build
cmake -GNinja ..
ninja
```

## Configuration

### Step 1: Configuration of the 5G Broadcast Transmitter

Follow the configuration instructions documented [here](https://github.com/5G-MAG/rt-mbms-tx-for-qrd-and-crd?tab=readme-ov-file#configuration-after-installation).
Make sure to adjust the `dl_freq` and the `dl_earfcn` in the `enb.conf` based on the frequency that your CRD or QRD device is operating on. To derive the right `dl_earfcn` you can use
this [tool](https://5g-tools.com/4g-lte-earfcn-calculator/). Note also that SoapySDR might detect the wrong output (e.g. an audio device instead of your SDR.). In that case make sure to use `device_name` and `device_args` to select the right output device.

Example configuration files are located under the directory Config-Templates. These will be called when running.

Copy the `bytecode` file to a foder `/home/fivegmag`.

```
cd ~/rt-mbms-tx-for-qrd-and-crd-emergency-alerts/Config-Template
cp bytecode /home/fivegmag/bytecode
```

## Running

### Step 1: Running the 5G Broadcast Transmitter

The MBMS-GW receives multicast packets on one tunnel interface, packages them to GTP-U-Packets and sends them to ENB over another tunnel interface. This command creates the sgi_mb interface.

```
sudo route add -net 239.11.4.0 netmask 255.255.255.0 dev sgi_mb
```

Start the MBMS Gateway, EPC and eNodeB in different terminals:

```
cd ~/rt-mbms-tx-for-qrd-and-crd-emergency-alerts/build 
sudo ./srsepc/src/srsmbms ../Config-Template/mbms.conf
```

```
cd ~/rt-mbms-tx-for-qrd-and-crd-emergency-alerts/build 
sudo ./srsepc/src/srsepc ../Config-Template/epc.conf
```

```
cd ~/rt-mbms-tx-for-qrd-and-crd-emergency-alerts/build 
sudo ./srsenb/src/srsenb ../Config-Template/enb.conf
```

Note that some of this files point to directories which should be adapted for your own setup. For instace `user_db.csv` inside `epc.conf` points to `db_file = /home/fivegmag/rt-mbms-tx-for-qrd-and-crd-emergency-alerts/Config-Template/user_db.csv`

### Step 2: Start the UE

Now that the transmitter is running you can turn on your phone. You should receive an alert shortly after the phone was
turned on. The output looks similar to this:

![App Playback](../../../assets/images/emergency-alerts/emergency-alert.jpg)

### Step 3: Changing the type of the alert

With the current implementation, the SIB 12 payload is static and defined in `Config-Templates/sib.conf.mbsfn`. To change the type
of the alert you need to open `Config-Templates/sib.conf.mbsfn` and change the `message_identifier`. A list of possible values is
defined in [3GPP TS 23.041](https://www.3gpp.org/dynareport/23041.htm) Section 9.4.1.2.2. For example:

```
sib12 =
{
    message_identifier = 0x1102;
    serial_number = 0x0001;
    data_coding_scheme = 01;
    warning_msg_segment_type = "lastSegment";
    warning_msg_segment_num = 0;
    warning_msg_segment_r9 = "01C576597E2EBBC7F950A8D168341A8D46A3D168341A8D46A3D168341A8D46A3D168341A8D46A3D168341A8D46A3D168341A8D46A3D168341A8D46A3D168341A8D46A3D168341A8D46A3D168341A8D46A3D1000A";
};
```
| message_identifier | Description |
| ------------------ | ----------- |
| 0x1100             | ETWS CBS Message Identifier for earthquake warning message |
| 0x1101             | ETWS CBS Message Identifier for tsunami warning message |
| 0x1102             | ETWS CBS Message Identifier for earthquake and tsunami combined warning message |
| 0x1104             | ETWS CBS Message Identifier for messages related to other emergency types |
| 0x1112-1130        | CMAS CBS Message Identifier |
| 0x1131-113B        | Non-ETWS CBS Message Identifier |

### Step 4: Triggering multiple alerts

To trigger a new alert the `serial_number` needs to be changed. At this point, there is no interface to change
the `serial_number` while the eNB is still running. You will need to change the `serial_number`
in `build/sib.conf.mbsfn` manually and then restart the eNB.
