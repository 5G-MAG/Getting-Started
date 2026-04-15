---
layout: default
patent: Community Dashboard
title: Software Releases
nav_order: 0
---

<style>
  .release-table {
    width: 100%; 
    border-collapse: collapse; 
    margin-top: 20px; 
    table-layout: fixed;
  }
  .release-table th {
    padding: 12px;
    text-align: left;
    border-bottom: 2px solid #eee;
  }
  .release-table td {
    padding: 12px;
    border-bottom: 1px solid #eee;
    overflow: hidden;
    text-overflow: ellipsis;
    vertical-align: top;
  }
</style>

<img src="../assets/images/Banner_ReferenceTools.png" alt="Reference Tools Banner" /> 

# Reference Tools Projects: Releases

> **Last Synced:** {{ site.data.releases.last_updated }}

---

<img src="../assets/images/Banner_5GBCTVR.png"/> 

## Latest Releases - 5G Broadcast: TV and Radio Hybrid Services
[Project Documentation](./lte-based-5g-broadcast/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["5G Broadcast TV Radio"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GBCEA.png"/> 

## Latest Releases - 5G Broadcast: Emergency Alerts
[Project Documentation](./emergency-alerts/){: .btn .btn-blue }

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
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GMS.png"/> 

## Latest Releases - 5G Media Streaming
[Project Documentation](./5g-media-streaming/){: .btn .btn-blue }

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
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5MBS.png"/> 

## Latest Releases - 5G Multicast Broadcast Services
[Project Documentation](./5g-multicast-broadcast-services/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["5G Multicast Broadcast"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GC.png"/> 

## Latest Releases - 5GC Service Consumers
[Project Documentation](./5g-core-service-consumers/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["5G Core Service Consumers"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_6GTestbedAITraffic.png"/> 

## Latest Releases - 6G Testbed and AI Traffic Characterization
[Project Documentation](./6g-testbed-ai-traffic/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["6G Testbed"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_AIML.png"/> 

## Latest Releases - AI/ML in Mobile Media Services
[Project Documentation](./ai-ml-evaluation-framework/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["AI ML"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_B2D.png"/> 

## Latest Releases - Beyond 2D Video Experiences
[Project Documentation](./beyond-2d-evaluation-framework/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["Beyond 2D"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_Avatar.png"/> 

## Latest Releases - Conversational Avatar Real-Time Communications
[Project Documentation](./conversational-avatar/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["Conversational Avatar"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_DVBI.png"/> 

## Latest Releases - DVB-I over 5G Systems
[Project Documentation](./dvbi-over-5g/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["DVB-I over 5G"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_MD.png"/> 

## Latest Releases - Multimedia Content Delivery Protocols
[Project Documentation](./multimedia-content-delivery/){: .btn .btn-blue }

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
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_UEDC.png"/> 

## Latest Releases - UE Data Collection, Reporting & Event Exposure
[Project Documentation](./ue-data-collection-reporting-exposure/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["UE Data Collection"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_V3C_Platform.png"/> 

## Latest Releases - V3C Immersive Platform
[Project Documentation](./v3c-immersive-platform/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["V3C Immersive"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_XR.png"/> 

## Latest Releases - XR Media with MPEG-I Scene Description
[Project Documentation](./xr-media-integration-in-5g/){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["XR Media"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_CommonTools.png"/> 

## Latest Releases - Auxiliary tools common to various projects
[Documentation](./common-tools/index.html){: .btn .btn-blue }

<table class="release-table">
  <thead>
    <tr>
      <th style="width: 40%;">Repository</th>
      <th style="width: 40%;">Version</th>
      <th style="width: 20%;">Date</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.releases.projects["Auxiliary Tools"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" class="btn">{{ item.short_name }}</a></td>
      <td><a href="{{ item.url }}" class="btn">{{ item.tag }}</a></td>
      <td>{{ item.date }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
