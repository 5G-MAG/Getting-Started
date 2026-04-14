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
  </p>
{% endif %}

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

{% assign categories = "5G Broadcast TV Radio,5G Broadcast Emergency Alerts,5G Media Streaming,5G Multicast Broadcast,5G Core Service Consumers,6G Testbed,AI ML,Beyond 2D,Conversational Avatar,DVB-I over 5G,Multimedia Protocols,UE Data Collection,V3C Immersive,XR Media,Auxiliary Tools" | split: "," %}

{% for category in categories %}
  {% if site.data.community_stats.projects[category] %}
    {% if category == "5G Broadcast TV Radio" %}
      <img src="../assets/images/Banner_5GBCTVR.png"/> 
    {% elsif category == "5G Broadcast Emergency Alerts" %}
      <img src="../assets/images/Banner_5GBCEA.png"/>
    {% elsif category == "5G Media Streaming" %}
      <img src="../assets/images/Banner_5GMS.png"/>
    {% elsif category == "5G Multicast Broadcast" %}
      <img src="../assets/images/Banner_5MBS.png"/>
    {% elsif category == "5G Core Service Consumers" %}
      <img src="../assets/images/Banner_5GC.png"/>
    {% elsif category == "6G Testbed" %}
      <img src="../assets/images/Banner_6GTestbedAITraffic.png"/>
    {% elsif category == "AI ML" %}
      <img src="../assets/images/Banner_AIML.png"/>
    {% elsif category == "Beyond 2D" %}
      <img src="../assets/images/Banner_B2D.png"/>
    {% elsif category == "Conversational Avatar" %}
      <img src="../assets/images/Banner_Avatar.png"/>
    {% elsif category == "DVB-I over 5G" %}
      <img src="../assets/images/Banner_DVBI.png"/>
    {% elsif category == "Multimedia Protocols" %}
      <img src="../assets/images/Banner_MD.png"/>
    {% elsif category == "UE Data Collection" %}
      <img src="../assets/images/Banner_UEDC.png"/>
    {% elsif category == "V3C Immersive" %}
      <img src="../assets/images/Banner_V3C_Platform.png"/>
    {% elsif category == "XR Media" %}
      <img src="../assets/images/Banner_XR.png"/>
    {% elsif category == "Auxiliary Tools" %}
      <img src="../assets/images/Banner_CommonTools.png"/>
    {% endif %}

    ## Community Stats - {{ category }}
    
    <table class="health-table">
      {{ table_header }}
      <tbody>
        {% for item in site.data.community_stats.projects[category] %}
        <tr>
          <td><a href="{{ item.repo_url }}" style="font-weight: bold; color: #0366d6;">{{ item.name }}</a></td>
          <td>⭐ {{ item.stars }}</td>
          <td>🍴 {{ item.forks }}</td>
          <td>👀 {{ item.total_views }} <span class="stats-sub">{{ item.views_14d }} new</span></td>
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
        {% endfor %}
      </tbody>
    </table>
    ---
  {% endif %}
{% endfor %}
