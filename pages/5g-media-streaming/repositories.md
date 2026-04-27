---
layout: default
title: Repositories
parent: 5G Media Streaming
has_children: false
nav_order: 3
---

<img src="../../assets/images/Banner_5GMS.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](./repositories.html#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video } [Requirements](./requirements.html){: .btn .btn-blue }

# Software Repositories

The following repositories are available. Please refer to the "Scope" section of the different projects for more context.

{% include architecture_table.html ids="S1,S2,S3,S4,S5,S6,S7,S8" %}

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
    {% for item in site.data.releases.projects["5G Media Streaming"] %}
    <tr>
      <td><a href="https://github.com/5G-MAG/{{ item.short_name }}" class="btn btn-5gms">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn btn-5gms">{{ item.tag }}</a></td>
      <td><span class="date-cell-release {% if item.blink %}blink-animation{% endif %}"><strong>{{ item.date }}</strong></span></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

# Packages

This project also provides or makes use of the following packages GitHub Container packages.

## 5G Media Streaming

Components | Package
 --|--
 com.fivegmag.a5gmsmediastreamhandler | [https://github.com/5G-MAG/rt-5gms-media-stream-handler/packages/](https://github.com/5G-MAG/rt-5gms-media-stream-handler/packages/)
 com.fivegmag.a5gmscommonlibrary | [https://github.com/5G-MAG/rt-5gms-common-android-library/packages/](https://github.com/5G-MAG/rt-5gms-common-android-library/packages/)
