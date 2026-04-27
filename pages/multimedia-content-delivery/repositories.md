---
layout: default
title: Repositories
parent: Multimedia Delivery Protocols
has_children: false
nav_order: 2
---

<img src="../../assets/images/Banner_MD.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](./repositories.html#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video } [Requirements](./requirements.html){: .btn .btn-blue }

# Software Repositories

The following repositories are available. Please refer to the "Scope" section of the different projects for more context.

{% include architecture_table.html ids="L1,L2" %}

*Note: Auxiliary repositories are indicated with a dashed border.*

---

## File Delivery over Unidirectional Transport (FLUTE)
[rt-libflute](https://github.com/5G-MAG/rt-libflute){: .btn .btn-md }

This is an implementation of a FLUTE server and client.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-libflute#readme)
* [Releases](https://github.com/5G-MAG/rt-libflute/releases)

## Real-time Object delivery over Unidirectional Transport (ROUTE), integrated within MBMS Middleware
[rt-mbms-mw / route-gpac](https://github.com/5G-MAG/rt-mbms-mw/tree/route-gpac){: .btn .btn-md }

This is an extension of the MBMS middleware implementing a ROUTE client.

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
    {% for item in site.data.releases.projects["Multimedia Protocols"] %}
    <tr>
      <td><a href="https://github.com/5G-MAG/{{ item.short_name }}" class="btn btn-md">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn btn-md">{{ item.tag }}</a></td>
      <td><span class="date-cell-release {% if item.blink %}blink-animation{% endif %}"><strong>{{ item.date }}</strong></span></td>
    </tr>
    {% endfor %}
  </tbody>
</table>
