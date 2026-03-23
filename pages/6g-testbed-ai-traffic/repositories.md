---
layout: default
title: Repositories
parent: 6G Testbed - AI Traffic
has_children: false
nav_order: 3
---

<img src="../../assets/images/Banner_6GTestbedAITraffic.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](./repositories.html#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video } [Requirements](./requirements.html){: .btn .btn-blue }

# Software Repositories

The following repositories are available. Please refer to the "Scope" section of the different projects for more context.

<img src="../../assets/images/projects/6gtestbed_repos.png" style="width: 80%">

---

## 6G AI Traffic Characterization Testbed
[6G-Testbed](https://github.com/5G-MAG/6G-Testbed){: .btn .btn-testbed }

A framework for measuring and analyzing AI/LLM service traffic patterns under various network conditions, designed to support 3GPP SA4 6G Media Study contributions.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/6G-Testbed#readme)

---

## Latest Releases

[Project Documentation](./6g-testbed-ai-traffic/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 40%;">Repository</th>
      <th style="padding: 12px; width: 40%;">Version</th>
      <th style="padding: 12px; width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["6G Testbed"] %}
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.short_name }}</a></td>
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td style="padding: 12px;">{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
