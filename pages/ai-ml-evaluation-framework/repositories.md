---
layout: default
title: Repositories
parent: AI / ML Evaluation
has_children: false
nav_order: 3
---

<img src="../../assets/images/Banner_AIML.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](./repositories.html#latest-releases){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Video Library](./tutorials.html#video-library){: .btn .btn-video } [Requirements](./requirements.html){: .btn .btn-blue }

# Software Repositories

The following repositories are available. Please refer to the "Scope" section of the different projects for more context.

{% include architecture_table.html ids="ML1" %}

*Note: Auxiliary repositories are indicated with a dashed border.*

Note that these repositories are currently private and under testing. **Early access** can be requested at: [https://www.5g-mag.com/early-access](https://www.5g-mag.com/early-access)

---

## AI/ML Evaluation Framework
[rt-ai-ml-evaluation-framework](https://github.com/5G-MAG/rt-ai-ml-evaluation-framework){: .btn .btn-testbed }

This repository holds code related to the implementation of the AI/ML evaluation framework as defined in 3GPP SA4 TR26.927.

Additional information:
* [Information and how to download, build, install and run](https://github.com/5G-MAG/rt-ai-ml-evaluation-framework#readme)

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
    {% for item in site.data.releases.projects["AI ML"] %}
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.short_name }}</a></td>
      <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td style="padding: 12px;">{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
