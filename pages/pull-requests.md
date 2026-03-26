---
layout: default
title: Open Pull Requests
nav_order: 3
---

<img src="../assets/images/Banner_ReferenceTools.png" /> 

# Reference Tools Projects: Open Pull Requests

> **Last Synced:** {{ site.data.pull_requests.last_updated }}

---

<img src="../assets/images/Banner_5GBCTVR.png"/> 

## Open PRs - 5G Broadcast: TV and Radio Hybrid Services

[Project Documentation](./lte-based-5g-broadcast/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["5G Broadcast TV Radio"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px; overflow: hidden; text-overflow: ellipsis;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GBCEA.png"/> 

## Open PRs - 5G Broadcast: Emergency Alerts

[Project Documentation](./emergency-alerts/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["5G Broadcast Emergency Alerts"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GMS.png"/> 

## Open PRs - 5G Media Streaming

[Project Documentation](./5g-media-streaming/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["5G Media Streaming"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5MBS.png"/> 

## Open PRs - 5G Multicast Broadcast Services

[Project Documentation](./5g-multicast-broadcast-services/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["5G Multicast Broadcast"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GC.png"/> 

## Open PRs - 5GC Service Consumers

[Project Documentation](./5g-core-service-consumers/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["5G Core Service Consumers"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_6GTestbedAITraffic.png"/> 

## Open PRs - 6G Testbed and AI Traffic Characterization

[Project Documentation](./6g-testbed-ai-traffic/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["6G Testbed"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_AIML.png"/> 

## Open PRs - AI/ML in Mobile Media Services

[Project Documentation](./ai-ml-evaluation-framework/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["AI ML"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_B2D.png"/> 

## Open PRs - Beyond 2D Video Experiences

[Project Documentation](./beyond-2d-evaluation-framework/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["Beyond 2D"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_Avatar.png"/> 

## Open PRs - Conversational Avatar Real-Time Communications

[Project Documentation](./beyond-2d-evaluation-framework/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["Conversational Avatar"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_DVBI.png"/> 

## Open PRs - DVB-I over 5G Systems

[Project Documentation](./dvbi-over-5g/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["DVB-I over 5G"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_MD.png"/> 

## Open PRs - Multimedia Content Delivery Protocols

[Project Documentation](./multimedia-content-delivery/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["Multimedia Protocols"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_UEDC.png"/> 

## Open PRs - UE Data Collection, Reporting & Event Exposure

[Project Documentation](./ue-data-collection-reporting-exposure/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["UE Data Collection"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_V3C_Platform.png"/> 

## Open PRs - V3C Immersive Platform

[Project Documentation](./v3c-immersive-platform/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["V3C Immersive"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_XR.png"/> 

## Open PRs - XR Media with MPEG-I Scene Description

[Project Documentation](./xr-media-integration-in-5g/){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["XR Media"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_CommonTools.png"/> 

## Open PRs - Auxiliary tools common to various projects

[Documentation](./common-tools/index.html){: .btn .btn-blue }

<table class="release-table" style="width:100%; border-collapse: collapse; margin-top: 20px; table-layout: fixed;">
  <thead>
    <tr style="text-align: left; border-bottom: 2px solid #eee;">
      <th style="padding: 12px; width: 30%;">Repository</th>
      <th style="padding: 12px; width: 45%;">Pull Request</th>
      <th style="padding: 12px; width: 15%;">Author</th>
      <th style="padding: 12px; width: 10%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% assign prs = site.data.pull_requests.projects["Auxiliary Tools"] %}
    {% if prs.size > 0 %}
      {% for item in prs %}
      <tr style="border-bottom: 1px solid #eee;">
        <td style="padding: 12px;"><a href="https://github.com/5G-MAG/{{ item.repo }}" class="btn">{{ item.repo }}</a></td>
        <td style="padding: 12px;"><a href="{{ item.url }}" class="btn">{{ item.title }}</a></td>
        <td style="padding: 12px;">@{{ item.user }}</td>
        <td style="padding: 12px; font-weight: bold; color: {{ item.color }};">{{ item.date }}</td>
      </tr>
      {% endfor %}
    {% else %}
      <tr><td colspan="4" style="padding: 12px; color: #666;">*No open pull requests.*</td></tr>
    {% endif %}
  </tbody>
</table>
