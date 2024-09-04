---
layout: default
title:  Basic 5GMS Setup with 5G Network
parent: Tutorials
grand_parent: 5G Downlink Media Streaming
has_children: false
nav_order: 1
---

# Tutorial - 5G MSd: Basic End-to-End Setup with 5G Network
This guide describes how to setup and configure the 5G-MAG Reference Tools to create an end to end setup consisting of the 5G Downlink Media Streaming components and a 5G Network based on Open5GS and srsRAN.

# 5G Network with COTS UE setup
For details please refer to the [corresponding documentation](../../5g-core-network-components/tutorials/5gnetwork.html)

# 5G Media Streaming setup
## Server-side Setup

### Step 1: Install the Application Function

For details please refer to the [corresponding section](end-to-end.html#1-installing-the-application-function) in
the [basic end-to-end guide](end-to-end.html).

### Step 2: Install the Application Server

For details please refer to the [corresponding section](end-to-end.html#2-installing-the-application-server) in
the [basic end-to-end guide](end-to-end.html).

### Step 3: Start the Application Server

For details please refer to the [corresponding section](end-to-end.html#3-running-the-application-server) in
the [basic end-to-end guide](end-to-end.html).

### Step 4: Basic Configuration of the Application Function

Follow the [basic configuration steps](end-to-end.html#configuration-of-the-af) documented in
the [basic end-to-end guide](end-to-end.html).

### Step 5: Start the Application Function

Follow the [command](end-to-end.html#starting-the-af) documented in the [basic end-to-end guide](end-to-end.html).

### Step 6: Basic configuration of the Application Function

Follow the [steps](end-to-end.html#creating-a-content-hosting-configuration) to create a content hosting configuration
and a provisioning session using the `msaf-configuration` tool.

## Client-side Setup

As we are all set on the server-side now we can focus on the client side.

### Step 1: Installation, Configuration and Running the 5GMSd Client

Please follow the [instructions](end-to-end.html#client-side-setup) documented in
the [basic end-to-end guide](end-to-end.html) setup guide.
