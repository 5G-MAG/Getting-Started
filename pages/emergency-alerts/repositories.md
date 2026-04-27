---
layout: default
title: Repositories
parent: 5G Broadcast - Emergency Alerts
has_children: false
nav_order: 3
---

<img src="../../assets/images/Banner_5GBCEA.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](./repositories.html#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video } [Requirements](./requirements.html){: .btn .btn-blue }

# Software Repositories

The following repositories are available. Please refer to the "Scope" section of the different projects for more context.

{% include architecture_table.html ids="W1" %}

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
    {% for item in site.data.releases.projects["5G Broadcast Emergency Alerts"] %}
      {% if item.tag contains "-ea-" %}
    <tr>
      <td><a href="https://github.com/5G-MAG/{{ item.short_name }}" class="btn btn-5gbcea">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn btn-5gbcea">{{ item.tag }}</a></td>
      <td><span class="date-cell-release {% if item.blink %}blink-animation{% endif %}"><strong>{{ item.date }}</strong></span></td>
    </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>
