---
layout: default
title: Repositories
parent: Avatar Communications
has_children: false
nav_order: 3
---

<img src="../../assets/images/Banner_Avatar.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](./repositories.html#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video } [Requirements](./requirements.html){: .btn .btn-blue }

# Software Repositories

The following repositories are available. Please refer to the "Scope" section of the different projects for more context.

<img src="../../assets/images/projects/avatar_repos.png" style="width: 80%">

---

## Avatar Test Content
[rt-avatar-content](https://github.com/5G-MAG/rt-avatar-content){: .btn .btn-xr }

This repository holds reference MPEG ARF content for real time avatar communication.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-avatar-content#readme)

## Avatar Call
[rt-avatar-call](https://github.com/5G-MAG/rt-avatar-call){: .btn .btn-xr }

This repository supports the development of a reference framework for avatar communication. The goal is to demonstrate WebRTC communication using the MPEG ARF and related animation compression.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-avatar-call#readme)

## Avatar Unity Tracker
[rt-avatar-unity-tracker](https://github.com/5G-MAG/rt-avatar-unity-tracker){: .btn .btn-xr }

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-avatar-call#readme)

---

## Latest Releases

[Project Documentation](./beyond-2d-evaluation-framework/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 40%;">Repository</th>
      <th style="padding: 12px; width: 40%;">Version</th>
      <th style="padding: 12px; width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["Conversational Avatar"] %}
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.short_name }}</a></td>
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td style="padding: 12px;">{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
