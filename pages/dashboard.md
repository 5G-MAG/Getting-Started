---
layout: default
title: Community Dashboard
nav_order: 2
---

<style>
  .health-table {
    width: 100%; 
    border-collapse: collapse; 
    margin-top: 20px; 
    table-layout: fixed;
  }
  .health-table th {
    padding: 12px;
    text-align: left;
    border-bottom: 2px solid #eee;
    font-size: 0.75em;
    color: #666;
    text-transform: uppercase;
  }
  .health-table td {
    padding: 12px;
    border-bottom: 1px solid #eee;
    vertical-align: middle;
    font-size: 0.9em;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dot { height: 8px; width: 8px; border-radius: 50%; display: inline-block; margin-right: 5px; }
  .dot-green { background-color: #28a745; }
  .dot-orange { background-color: #fd7e14; }
  .dot-blue { background-color: #0366d6; }
  .btn-blue {
    background-color: #0366d6;
    color: white !important;
    padding: 5px 10px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.8em;
  }
  .stats-sub { font-size: 0.8em; color: #888; display: block; }
</style>

<img src="../assets/images/Banner_ReferenceTools.png" alt="Reference Tools Banner" /> 

# Reference Tools Projects: Community Dashboard

{% if site.data.community_stats %}
  > **Last Synced:** {{ site.data.community_stats.last_updated }}
{% else %}
  <p style="color: #d73a49; padding: 10px; border: 1px solid #d73a49; border-radius: 4px;">
    <strong>⚠️ Data Missing:</strong> Jekyll cannot find <code>_data/community_stats.json</code>. 
    Please ensure your GitHub Action has run successfully and pushed the file to the repository.
  </p>
{% endif %}

{% capture table_header %}
  <thead>
    <tr>
      <th style="width: 25%;">Repository</th>
      <th style="width: 10%;">Stars</th>
      <th style="width: 10%;">Forks</th>
      <th style="width: 15%;">Views (14d)</th>
      <th style="width: 20%;">Clones (Total)</th>
      <th style="width: 20%;">Activity</th>
    </tr>
  </thead>
{% endcapture %}

{% capture table_row_logic %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.views_14d }}</td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}
          <span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}
          <span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}
          <span class="dot dot-blue"></span> <strong>Stable</strong>
        {% endif %}
      </td>
    </tr>
{% endcapture %}

---

<img src="../assets/images/Banner_5GBCTVR.png"/> 

## Community Health - 5G Broadcast: TV and Radio Hybrid Services
[Project Documentation](./lte-based-5g-broadcast/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["5G Broadcast TV Radio"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GBCEA.png"/> 

## Community Health - 5G Broadcast: Emergency Alerts
[Project Documentation](./emergency-alerts/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["5G Broadcast Emergency Alerts"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GMS.png"/> 

## Community Health - 5G Media Streaming
[Project Documentation](./5g-media-streaming/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["5G Media Streaming"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5MBS.png"/> 

## Community Health - 5G Multicast Broadcast Services
[Project Documentation](./5g-multicast-broadcast-services/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["5G Multicast Broadcast"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GC.png"/> 

## Community Health - 5GC Service Consumers
[Project Documentation](./5g-core-service-consumers/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["5G Core Service Consumers"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_6GTestbedAITraffic.png"/> 

## Community Health - 6G Testbed and AI Traffic Characterization
[Project Documentation](./6g-testbed-ai-traffic/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["6G Testbed"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_AIML.png"/> 

## Community Health - AI/ML in Mobile Media Services
[Project Documentation](./ai-ml-evaluation-framework/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["AI ML"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_B2D.png"/> 

## Community Health - Beyond 2D Video Experiences
[Project Documentation](./beyond-2d-evaluation-framework/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["Beyond 2D"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_Avatar.png"/> 

## Community Health - Conversational Avatar Real-Time Communications
[Project Documentation](./conversational-avatar/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["Conversational Avatar"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_DVBI.png"/> 

## Community Health - DVB-I over 5G Systems
[Project Documentation](./dvbi-over-5g/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["DVB-I over 5G"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_MD.png"/> 

## Community Health - Multimedia Content Delivery Protocols
[Project Documentation](./multimedia-content-delivery/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["Multimedia Protocols"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_UEDC.png"/> 

## Community Health - UE Data Collection, Reporting & Event Exposure
[Project Documentation](./ue-data-collection-reporting-exposure/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["UE Data Collection"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_V3C_Platform.png"/> 

## Community Health - V3C Immersive Platform
[Project Documentation](./v3c-immersive-platform/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["V3C Immersive"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_XR.png"/> 

## Community Health - XR Media with MPEG-I Scene Description
[Project Documentation](./xr-media-integration-in-5g/){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["XR Media"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_CommonTools.png"/> 

## Community Health - Auxiliary tools common to various projects
[Documentation](./common-tools/index.html){: .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["Auxiliary Tools"] %}
      {{ table_row_logic }}
    {% endfor %}
  </tbody>
</table>
