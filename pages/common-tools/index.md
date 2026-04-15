---
layout: default
title: Common Tools
has_children: true
nav_order: 4
---

<style>
  /* Table Styles */
  .health-table {
    width: 100%; 
    border-collapse: collapse; 
    margin-top: 20px; 
    table-layout: fixed;
  }
  .health-table th {
    padding: 12px;
    text-align: left;
    border-bottom: 2px solid #eee;
    font-size: 0.75em;
    color: #666;
    text-transform: uppercase;
  }
  .health-table td {
    padding: 12px;
    border-bottom: 1px solid #eee;
    vertical-align: middle;
    font-size: 0.9em;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dot { height: 8px; width: 8px; border-radius: 50%; display: inline-block; margin-right: 5px; }
  .dot-green { background-color: #28a745; }
  .dot-orange { background-color: #fd7e14; }
  .dot-blue { background-color: #0366d6; }
  .stats-sub { font-size: 0.8em; color: #888; display: block; }

  /* Consistency for buttons */
  .btn-blue {
    background-color: #0366d6;
    color: white !important;
    padding: 8px 16px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.9em;
    display: inline-block;
  }
</style>

<img src="../../assets/images/Banner_CommonTools.png" /> 

[Scope](./index.html){: .btn .btn-blue } [Releases](./index.html#latest-releases){: .btn .btn-release }

# Common Tools: Information and Software Repositories

The following repositories are available. Please refer to the "Scope" section of the different projects for more context.

<img src="../../assets/images/projects/common_tools.png" style="width: 80%">

---

## Community Stats
> **Last Synced:** {{ site.data.community_stats.last_updated }}

{% capture table_header %}
  <thead>
    <tr>
      <th style="width: 25%;">Repository</th>
      <th style="width: 10%;">Stars</th>
      <th style="width: 10%;">Forks</th>
      <th style="width: 15%;">Views (Total)</th>
      <th style="width: 20%;">Clones (Total)</th>
      <th style="width: 20%;">Activity</th>
    </tr>
  </thead>
{% endcapture %}

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["Auxiliary Tools"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

## Auxiliary tools common to various projects
[rt-common-shared](https://github.com/5G-MAG/rt-common-shared){: .btn .btn-common } [Releases](../releases.html#auxiliary-tools-common-to-various-projects){: .btn .btn-release }

The following tools are available:

### 5G Media Streaming (5GMS): [https://github.com/5G-MAG/rt-common-shared/blob/main/5gms/](https://github.com/5G-MAG/rt-common-shared/blob/main/5gms/)

Includes example configurations and common scripts for the 5GMS (rt-5gms-*) Reference Tools. 

In particular, the `5G_APIs-overrides` directory contains files that can be used with the `open5gs-tools/scripts/generate_openapi` script to override or supplement the OpenAPI YAML files from the 5G_APIs repository.

### MBMS and LTE-based 5G Broadcast (MBMS): [https://github.com/5G-MAG/rt-common-shared/tree/main/mbms](https://github.com/5G-MAG/rt-common-shared/tree/main/mbms)

Includes example configurations for the LTE-based 5G Broadcast (rt-mbms-*) Reference Tools.

In particular, it includes information about the `ServiceAnnouncement(SA)` file also referred to as `bootstrap.multipart` in the context of 5G-MAG Reference Tools.

### Simple Express Server: [https://github.com/5G-MAG/rt-common-shared/blob/main/simple-express-server/README.md](https://github.com/5G-MAG/rt-common-shared/blob/main/simple-express-server/README.md)

Includes a simple HTTP server based on express.js that can be used to statically host files for streaming.

### Open5GS Tools: [https://github.com/5G-MAG/rt-common-shared/tree/main/open5gs-tools](https://github.com/5G-MAG/rt-common-shared/tree/main/open5gs-tools)

Includes scripts related to the OpenAPI generator.

### Data Reporting 5G_APIs overrides: [https://github.com/5G-MAG/rt-common-shared/tree/main/data-reporting/5G_APIs-overrides](https://github.com/5G-MAG/rt-common-shared/tree/main/data-reporting/5G_APIs-overrides)

Includes modified versions of the OpenAPI YAML files from the 5G_APIs repository specific to Data Reporting for use with a Data Collection Application Function.

### Avcodec build: [https://github.com/5G-MAG/rt-common-shared/blob/main/avcodec-build/README.md](https://github.com/5G-MAG/rt-common-shared/blob/main/avcodec-build/README.md)

Includes a helper script to build ffmpeg libraries for Android.

---

## Latest Releases

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 40%;">Repository</th>
      <th style="padding: 12px; width: 40%;">Version</th>
      <th style="padding: 12px; width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["Auxiliary Tools"] %}
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.short_name }}</a></td>
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td style="padding: 12px;">{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
