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
  
  /* Adjusted for larger, consistent button sizing */
  .btn-blue {
    background-color: #0366d6;
    color: white !important;
    padding: 8px 16px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.9em;
    display: inline-block;
    margin-bottom: 10px;
  }
  .stats-sub { font-size: 0.8em; color: #888; display: block; }

  /* Summary Box Styles */
  .summary-container {
    display: flex;
    gap: 20px;
    margin: 20px 0;
    flex-wrap: wrap;
  }
  .summary-card {
    background: #f8f9fa;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    padding: 15px;
    flex: 1;
    min-width: 150px;
    text-align: center;
  }
  .summary-card h4 { margin: 0; color: #586069; font-size: 0.85em; text-transform: uppercase; }
  .summary-value { display: block; font-size: 1.5em; font-weight: bold; color: #0366d6; margin-top: 5px; }
</style>

<img src="../assets/images/Banner_ReferenceTools.png" alt="Reference Tools Banner" /> 

# Reference Tools Projects: Community Dashboard

> **Last Synced:** {{ site.data.community_stats.last_updated }}

{% assign total_stars = 0 %}
{% assign total_forks = 0 %}
{% assign total_views = 0 %}
{% assign total_clones = 0 %}

{% for category in site.data.community_stats.projects %}
  {% for item in category[1] %}
    {% assign total_stars = total_stars | plus: item.stars %}
    {% assign total_forks = total_forks | plus: item.forks %}
    {% assign total_views = total_views | plus: item.total_views %}
    {% assign total_clones = total_clones | plus: item.total_clones %}
  {% endfor %}
{% endfor %}

<div class="summary-container">
  <div class="summary-card">
    <h4>Total Stars</h4>
    <span class="summary-value">⭐ {{ total_stars }}</span>
  </div>
  <div class="summary-card">
    <h4>Total Forks</h4>
    <span class="summary-value">🍴 {{ total_forks }}</span>
  </div>
  <div class="summary-card">
    <h4>Total Views</h4>
    <span class="summary-value">👀 {{ total_views }}</span>
  </div>
  <div class="summary-card">
    <h4>Total Clones</h4>
    <span class="summary-value">📥 {{ total_clones }}</span>
  </div>
</div>

{% capture table_header %}
  <thead>
    <tr>
      <th style="width: 25%;">Repository</th>
      <th style="width: 10%;">Stars</th>
      <th style="width: 10%;">Forks</th>
      <th style="width: 15%;">Views (Total)</th>
      <th style="width: 20%;">Clones (Total)</th>
      <th style="width: 20%;">Activity</th>
    </tr>
  </thead>
{% endcapture %}

---

<img src="../assets/images/Banner_5GBCTVR.png"/> 

## Community Stats - 5G Broadcast: TV and Radio Hybrid Services
[Project Documentation](./lte-based-5g-broadcast/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["5G Broadcast TV Radio"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GBCEA.png"/> 

## Community Stats - 5G Broadcast: Emergency Alerts
[Project Documentation](./emergency-alerts/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["5G Broadcast Emergency Alerts"] %}
      {% if item.name contains "-ea-" %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GMS.png"/> 

## Community Stats - 5G Media Streaming
[Project Documentation](./5g-media-streaming/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["5G Media Streaming"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5MBS.png"/> 

## Community Stats - 5G Multicast Broadcast Services
[Project Documentation](./5g-multicast-broadcast-services/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["5G Multicast Broadcast"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_5GC.png"/> 

## Community Stats - 5GC Service Consumers
[Project Documentation](./5g-core-service-consumers/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["5G Core Service Consumers"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_6GTestbedAITraffic.png"/> 

## Community Stats - 6G Testbed and AI Traffic Characterization
[Project Documentation](./6g-testbed-ai-traffic/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["6G Testbed"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_AIML.png"/> 

## Community Stats - AI/ML in Mobile Media Services
[Project Documentation](./ai-ml-evaluation-framework/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["AI ML"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_B2D.png"/> 

## Community Stats - Beyond 2D Video Experiences
[Project Documentation](./beyond-2d-evaluation-framework/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["Beyond 2D"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_Avatar.png"/> 

## Community Stats - Conversational Avatar Real-Time Communications
[Project Documentation](./conversational-avatar/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["Conversational Avatar"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_DVBI.png"/> 

## Community Stats - DVB-I over 5G Systems
[Project Documentation](./dvbi-over-5g/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["DVB-I over 5G"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_MD.png"/> 

## Community Stats - Multimedia Content Delivery Protocols
[Project Documentation](./multimedia-content-delivery/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["Multimedia Protocols"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_UEDC.png"/> 

## Community Stats - UE Data Collection, Reporting & Event Exposure
[Project Documentation](./ue-data-collection-reporting-exposure/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["UE Data Collection"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_V3C_Platform.png"/> 

## Community Stats - V3C Immersive Platform
[Project Documentation](./v3c-immersive-platform/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["V3C Immersive"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_XR.png"/> 

## Community Stats - XR Media with MPEG-I Scene Description
[Project Documentation](./xr-media-integration-in-5g/){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["XR Media"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

<img src="../assets/images/Banner_CommonTools.png"/> 

## Community Stats - Auxiliary tools common to various projects
[Documentation](./common-tools/index.html){: .btn .btn-blue }

<table class="health-table">
  {{ table_header }}
  <tbody>
    {% for item in site.data.community_stats.projects["Auxiliary Tools"] %}
    <tr>
      <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
      <td>⭐ {{ item.stars }}</td>
      <td>🍴 {{ item.forks }}</td>
      <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
      <td>📥 {{ item.total_clones }} <span class="stats-sub">{{ item.clones_14d }} new</span></td>
      <td>
        {% if item.status == "Active" %}<span class="dot dot-green"></span> <strong>Active</strong>
        {% elsif item.status == "Maintenance" %}<span class="dot dot-orange"></span> <strong>Maintenance</strong>
        {% else %}<span class="dot dot-blue"></span> <strong>Stable</strong>{% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
