---
layout: default
title: Basic 5GMS Setup with 5G Network
parent: Tutorials
grand_parent: 5G Media Streaming
has_children: false
nav_order: 3
---

# Tutorial - 5G MSd: Basic End-to-End Setup with 5G Network

This guide describes how to setup and configure the 5G-MAG Reference Tools to create an end to end setup consisting of
the 5G Downlink Media Streaming components and a 5G Network based on Open5GS and srsRAN.

# 5G Network with COTS UE setup

To setup the 5G Network and connect a COTS device please refer to the [corresponding documentation](../../3gpp-ran-and-core-platforms/tutorials/5gnetwork.html).

# 5G Media Streaming setup

## Server-side Setup

### Step 0: Using a local server (Skip if your content is hosted in the internet)

#### Install the express.js webserver

The express.js webserver acts as our CDN for unicast delivery. To install the webserver follow the
instructions [here](https://github.com/5G-MAG/rt-common-shared/tree/main/simple-express-server).

#### Configure ffmpeg

First we configure the `ffmpeg` output. Navigate to `flute-ffmpeg/files` and open `ffmpeg-hls.sh` or `ffmpeg-dash.sh`
depending on the output format you want to create. Change the following
two lines and point them to the path of the local webserver installed previously. If there is no `watchfolder/hls` or
`watchfolder/dash`folder
on your webserver yet create that as well.

````
-hls_segment_filename /home/dsi/5gmag/simple-express-server/public/watchfolder/hls/stream_%v_data%02d.ts \
-var_stream_map "v:0,a:0" /home/dsi/5gmag/simple-express-server/public/watchfolder/hls/stream_%v.m3u8
````

#### Run ffmpeg and the express.js webserver

Navigate to `flute-ffmpeg/files` and run `sh ffmpeg-hls.sh` or `sh ffmpeg-dash.sh`.

#### Start the express.js webserver

Run `npm start` in `simple-express-server`. Our files created by `ffmpeg` are now hosted and available via unicast. Try
to query the master manifest to check for the availability of the files:

````
curl http://192.168.11.1:3333/watchfolder/hls/manifest.m3u8
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-STREAM-INF:BANDWIDTH=2305600,RESOLUTION=1280x720,CODECS="avc1.64001f,mp4a.40.2"
stream_0.m3u8
````

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

Note that you need to point the `ingestURL` of your `streams.json` to the URL of your webserver.

## Client-side Setup

As we are all set on the server-side now we can focus on the client side.

### Step 1: Installation, Configuration and Running the 5GMSd Client

Please follow the [instructions](end-to-end.html#client-side-setup) documented in
the [basic end-to-end guide](end-to-end.html) setup guide.
