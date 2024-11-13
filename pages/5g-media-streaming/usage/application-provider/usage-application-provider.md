---
layout: default
title: Application Provider
parent: Usage
grand_parent: 5G Downlink Media Streaming
has_children: true
nav_order: 1
---

# Application Provider

A 5GMS Application Provider uses the M1 interface of the Application Function to provision the network for media
streaming sessions that are operated by that 5GMS Application Provider. For downlink media streaming, these sessions may
be DASH streaming sessions, progressive download sessions, or any other type of media streaming or distribution (e.g.
HLS) sessions.

The 5G-MAG Reference Tools ship with multiple tools to interact with the 5GMS Application Function via the interface at
reference point M1.

## Command Line Interface Tools

The Python-based Command Line Interface tool for 5GMS management is a set of executable wrapper modules
built upon Python classes which interacts with the 5GMS Application Function's RESTful API at reference point M1 to
provision 5GMS services.

The installation instructions for the Command Line Interface Tool can be
found [here](https://github.com/5G-MAG/rt-5gms-application-provider/blob/development/python/README.md).

Instructions on how to use the CLI Tool can be found here:

* [Testing M1 with AF v1.2.x](../application-function/testing-m1-v120.html)
* [Testing M1 with AF v1.3.x](../application-function/testing-m1-v130.html)
* [Testing M1 with AF v1.4.x](../application-function/testing-m1-v141.html)

## Management UI

A web-based Graphical User Interface for 5GMS management that uses the CLI Python classes and interacts with
the 5GMS Application Function.

The installation instructions for the Management UI can be
found [here](https://github.com/5G-MAG/rt-5gms-application-provider/blob/development/management-ui/README.md).

A demo video showcasing the functionalities of the Management UI can be found below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qewsQhGi8aE?si=j3aNWafmMtynM0Yo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Postman Collection

Postman recipes to test the 5GMS Application Function's API at reference point M1. This is a collection of predefined
HTTP requests for every Application Function's RESTful endpoint, including environmental variables and requests payload.
The source files and the documentation are located in the postman folder of this repository.

The installation instructions for the Postman Collection can be
found [here](https://github.com/5G-MAG/rt-5gms-application-provider/blob/development/postman/README.md).

A detailed guide on how to use the Postman Collection together with the Application Function can be
found [here](../application-function/testing-postman.html).

## QoE Metrics Reporting UI

A web-based Graphical User Interface that parses a QoE Metrics Report provided in XML format and outputs its content in
graphical and tabular form.

The installation instructions for the QoE Metrics Reporting UI can be
found [here](https://github.com/5G-MAG/rt-5gms-application-provider/blob/master/qoe-metrics-reporting-ui/README.md).
