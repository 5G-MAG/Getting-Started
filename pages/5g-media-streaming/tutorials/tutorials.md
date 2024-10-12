---
layout: default
title: Tutorials
parent: 5G Downlink Media Streaming
has_children: true
nav_order: 5
---

# Tutorials

## Our video library
The section [DEVELOPER XCHANGES & TUTORIALS](https://www.5g-mag.com/tutorials) in the 5G-MAG website contains more information and videos from the 5G-MAG Reference Tools developers on the usage of the tools. Some of the videos are also available here:

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=AmxsuFLQ8V_PZD0G&amp;list=PLFqKJZ78_IWUibB6dMiabaVNDFLSGBWlx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Using the tools
### [Tutorial: Basic 5G Media Streaming end-to-end setup](./end-to-end.html)
This guide describes how to setup and configure the 5G-MAG Reference Tools - 5G Downlink Media Streaming components to create an end to end setup using Application Function, Application Server, 5GMSd Aware Application, Media Session Handler, Media Stream Handler and Common Android Library.

### [Tutorial: Basic 5G Media Streaming end-to-end setup with 5G network and COTS UE](./end-to-end-with-5g.html)
This guide describes how to setup and configure the 5G-MAG Reference Tools to create an end to end setup consisting of the 5G Downlink Media Streaming components and a 5G Network based on Open5GS and srsRAN.

### [Tutorial: 5G Media Streaming with Consumption Reporting](./consumption-reporting.html)
Consumption Collection and Reporting executes the collection of content consumption measurement logs from the Media Player and sending of consumption reports to a 5GMSd AF about the currently consumed media within the available presentation, about the UE capabilities and about the environment of the media session for potential transport optimizations by the network or consumption report analysis.

### [Tutorial: 5G Media Streaming with QoE Metrics Reporting](./metrics-reporting.html)
QoE Metrics Reporting allows the Quality of Experience of media streaming sessions to be logged by the 5GMS System and exposed for analysis. The 5G-MAG Reference Tools support the scenario in which the metrics collection and reporting is configured by the 5GMSd Application Function. The metrics configuration provided by the 5GMSd AF to the 5GMSd client comprises instructions and rules regarding metrics collection (i.e. measurement and logging) and reporting for different schemes. Each metrics scheme requires the 5GMSd Client to perform metrics collection and subsequent metrics reporting to the 5GMSd AF according to the configuration rules of that scheme. In the simplest case the resulting QoE metrics reports are then saved to disk by the 5GMS Application Function.
