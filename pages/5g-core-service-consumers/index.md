---
layout: default
title: 5GC Service Consumers
parent: The Projects
has_children: true
nav_order: 6
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

</style>

<img src="../../assets/images/Banner_5GC.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](./repositories.html#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video } [Requirements](./requirements.html){: .btn .btn-blue }

# 5G Core Service Consumers - Reference Tools Project

Explore this slide deck for a concise introduction and a set of essential resources to help you get started. For deeper detail—including the scope of the reference tools, development roadmaps, and release information—use the navigation menu above or to the side. There you’ll also find direct links to the GitHub repositories and hands‑on tutorials designed to support you as you build, test, and deploy the reference tools.

## Project Overview

<iframe width="60%" height="560" src="../../docs/Reference_Tools_5GC_Service_Consumers.pdf"></iframe>

[Download the slidedeck of this Project](../../docs/Reference_Tools_5GC_Service_Consumers.pdf){: .btn .btn-blue }

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
    {% for item in site.data.community_stats.projects["5G Core Service Consumers"] %}
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
