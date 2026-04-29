---
layout: default
title: Repositories
parent: 5G Multicast Broadcast Services
has_children: false
nav_order: 2
---

<img src="../../assets/images/Banner_5MBS.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Packages](./packages.html){: .btn .btn-blue } [Releases](./repositories.html#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video }

# Software Repositories

The following repositories are available. Please refer to the "Scope" section of the different projects for more context.

{% include architecture_table.html ids="M1,M2,M3,M4,M5,M6" %}

*Note: Auxiliary repositories are indicated with a dashed border.*

---

## 5G UE (with MBS components)
[srsRAN_4G (5mbs branch)](https://github.com/5G-MAG/srsRAN_4G/tree/5mbs){: .btn .btn-5mbs }

This is a branch of srsRAN_4G which contains a basic implementation of an MBS-capable UE.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/srsRAN_4G/tree/5mbs)

## NG-RAN (with MBS components)
[rt-srsRAN_Project (5mbs branch)](https://github.com/5G-MAG/rt-srsRAN_Project/tree/5mbs){: .btn .btn-5mbs }

This is a branch of srsRAN_Project which contains a basic implementation of an MBS-capable NG-RAN.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-srsRAN_Project/tree/5mbs)

## 5GC (with MBS components)
[open5gs/tree/5mbs (5mbs branch)](https://github.com/5G-MAG/open5gs/tree/5mbs){: .btn .btn-5mbs }

This is a branch of Open5GS which contains implementations of 5GC NFs related to MBS.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/open5gs/tree/5mbs)
* [Packages](https://github.com/orgs/5G-MAG/packages?repo_name=open5gs)

## MBS User Services: MBS Function (MBSF)
[https://github.com/5G-MAG/rt-mbs-function](https://github.com/5G-MAG/rt-mbs-function){: .btn .btn-5mbs }

This repository provides a 5G MBS Function which forms part of the MBS User Services. This NF provides the interface designated as Nmb10 in the 3GPP TS 29.580 specification.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbs-function)
* [Releases](https://github.com/5G-MAG/rt-mbs-function/releases)

## MBS User Services: MBS Transport Function (MBSTF)
[https://github.com/5G-MAG/rt-mbs-transport-function](https://github.com/5G-MAG/rt-mbs-transport-function){: .btn .btn-5mbs }

This repository provides a 5G MBS Transport Function which forms part of the MBS User Services. This NF provides the interfaces designated as Nmb2, Nmb8 and Nmb9 in the 3GPP TS 29.581 V18.5.0 specification.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbs-transport-function)
* [Releases](https://github.com/5G-MAG/rt-mbs-transport-function/releases)
* [Packages](https://github.com/orgs/5G-MAG/packages?repo_name=rt-mbs-transport-function)

---

## Auxiliary repositories:

### MBS Examples
[rt-mbs-examples](https://github.com/5G-MAG/rt-mbs-examples){: .btn .btn-5mbs }

This repository contains Docker Compose components to deploy several network functions related to MBS.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-mbs-examples#readme)
* [Packages](https://github.com/orgs/5G-MAG/packages?repo_name=rt-mbs-examples)
* [Docker](https://github.com/5G-MAG/rt-mbs-examples/tree/development/images)

---

## Latest Releases

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["5G Multicast Broadcast"] %}
    <tr>
      <td><a href="https://github.com/5G-MAG/{{ item.short_name }}" class="btn btn-5mbs">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn btn-5mbs">{{ item.tag }}</a></td>
      <td><span class="date-cell-release {% if item.blink %}blink-animation{% endif %}"><strong>{{ item.date }}</strong></span></td>
    </tr>
    {% endfor %}
  </tbody>
</table>
