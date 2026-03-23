---
layout: default
title: Repositories
parent: Beyond 2D Evaluation
has_children: false
nav_order: 1
---

<img src="../../assets/images/Banner_B2D.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](./repositories.html#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video } [Requirements](./requirements.html){: .btn .btn-blue }

# Software Repositories

The following repositories are available. Please refer to the "Scope" section of the different projects for more context.

<img src="../../assets/images/projects/b2d_repos.png" style="width: 80%">

---

## FS_Beyond2D Evaluation Framework
[rt-beyond2d-evaluation-framework](https://github.com/5G-MAG/rt-beyond2d-evaluation-framework){: .btn .btn-testbed }

This project holds code related to the evaluation framework for the Feasibility Study on Beyond 2D Video (FS_Beyond2D) in 3GPP TSG SA WG4 (SA4). This study is based on work item description (WID) SP-240479 New SID on Feasibility Study on Beyond 2D Video, and the study will result in technical report TR 26.956.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-beyond2d-evaluation-framework#readme)

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
    {% for item in site.data.releases.projects["Beyond 2D"] %}
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.short_name }}</a></td>
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td style="padding: 12px;">{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
