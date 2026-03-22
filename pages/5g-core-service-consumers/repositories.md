---
layout: default
title: Repositories
parent: 5GC Service Consumers
has_children: false
nav_order: 3
---

<img src="../../assets/images/Banner_5GC.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](./repositories.md#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video } [Requirements](./requirements.html){: .btn .btn-blue }

# Repositories

The following repositories are available. Please refer to the "Scope & Architecture" sections of the different projects for more context.

<img src="../../assets/images/projects/5gc_repos.png" style="width: 80%">

---

## 5GC Service Consumers
[rt-5gc-service-consumers](https://github.com/5G-MAG/rt-5gc-service-consumers){: .btn .btn-5gcsc } [Releases](../releases.html#project-5g-core-service-consumers){: .btn .btn-release }

This repository contains a collection of reusable service consumer libraries designed to talk to the 5G Core Network Functions using service interfaces.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-5gc-service-consumers#readme)
* [Releases](https://github.com/5G-MAG/rt-5gc-service-consumers/releases)

---

## Latest Releases

[Project Documentation](./5g-core-service-consumers/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 40%;">Repository</th>
      <th style="padding: 12px; width: 40%;">Version</th>
      <th style="padding: 12px; width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["5G Core Service Consumers"] %}
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.short_name }}</a></td>
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td style="padding: 12px;">{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
