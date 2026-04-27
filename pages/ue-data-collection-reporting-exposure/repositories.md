---
layout: default
title: Repositories
parent: UE Data Collection
has_children: false
nav_order: 2
---

<img src="../../assets/images/Banner_UEDC.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](./repositories.html#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video } [Requirements](./requirements.html){: .btn .btn-blue }

# Software Repositories

The following repositories are available. Please refer to the "Scope" section of the different projects for more context.

{% include architecture_table.html ids="D1" %}

*Note: Auxiliary repositories are indicated with a dashed border.*

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
    {% for item in site.data.releases.projects["UE Data Collection"] %}
    <tr>
      <td><a href="https://github.com/5G-MAG/{{ item.short_name }}" class="btn btn-uedc">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn btn-uedc">{{ item.tag }}</a></td>
      <td><span class="date-cell-release {% if item.blink %}blink-animation{% endif %}"><strong>{{ item.date }}</strong></span></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---
# Packages

This project also provides or makes use of the following packages GitHub Container packages.

## UE Data Collection, Reporting and Event Exposure

Components | Package
 --|--
 DCAF | [https://github.com/5G-MAG/rt-data-collection-application-function/pkgs/container/data-collection-af](https://github.com/5G-MAG/rt-data-collection-application-function/pkgs/container/data-collection-af)
