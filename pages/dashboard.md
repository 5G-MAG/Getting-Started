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

> **Last Synced:** {{ site.data.community_stats.last_updated }}

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
[Project Documentation](./lte-based-5g-broadcast/){: .btn-blue }

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
[Project Documentation](./emergency-alerts/){: .btn-blue }

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
[Project Documentation](./5g-media-streaming/){: .btn-blue }

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
[Project Documentation](./5g-multicast-broadcast-services/){: .btn-blue }

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
[Project Documentation](./5g-core-service-consumers/){: .btn-blue }

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
[Project Documentation](./6g-testbed-ai-traffic/){: .btn-blue }

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
[Project Documentation](./ai-ml-evaluation-framework/){: .btn-blue }

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
[Project Documentation](./beyond-2d-evaluation-framework/){: .btn-blue }

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
[Project Documentation](./conversational-avatar/){: .btn-blue }

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
[Project Documentation](./dvbi-over-5g/){: .btn-blue }

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
[Project Documentation](./multimedia-content-delivery/){: .btn-blue }

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
[Project Documentation](./ue-data-collection-reporting-exposure/){: .btn-blue }

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
[Project Documentation](./v3c-immersive-platform/){: .btn-blue }

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
[Project Documentation](./xr-media-integration-in-5g/){: .btn-blue }

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
[Documentation](./common-tools/index.html){: .btn-blue }

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
