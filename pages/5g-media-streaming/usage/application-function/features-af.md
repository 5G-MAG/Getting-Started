---
layout: default
title:  Features 5GMS AF
parent: Under Development
grand_parent: 5G Media Streaming
has_children: false
nav_order: 0
---

# 5GMSd Application Function Supported Features

The release versions of the 5GMSd Application Function support differing sets of interfaces, as described by the different
versions of the 3GPP specifications, and differing levels of feature support for those interfaces. The page attempts to capture
the feature sets and specification versions for each release, starting with the most recent release or upcoming releases.

## Key

Where a feature of the specifications is supported the entry will be marked with &#x2611;, where it is being worked on and slated for the next release the feature will be marked with &#x270E; and where it is unimplemented in that
version the feature will be marked with &#x2610;.


<table><thead>
<tr><th>Interface reference point</th><th>Specifications & Versions</th><th>Protocols</th><th>Features</th></tr>
</thead>
<tbody>
<tr valign="top"><td>M1 (server)</td><td><ul>
  <li>TS 26.501 v17.6.0</li>
  <li>TS 26.512 v17.6.0</li>
</ul></td><td><ul>
  <li>&#x2611; HTTP/1.1</li>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2611; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2611; Content Hosting Provisioning</li>
  <li>&#x2611; Content Protocols Discovery</li>
  <li>&#x2611; Provisioning Sessions</li>
  <li>&#x2611; Server Certificates Provisioning</li>
  <li>&#x2611; Consumption Reporting Provisioning</li>
  <li>&#x2610; Content Preparation Templates Provisioning</li>
  <li>&#x2610; Edge Resources Provisioning</li>
  <li>&#x2610; Event Data Processing Provisioning</li>
  <li>&#x2611; Metrics Reporting Provisioning</li>
  <li>&#x2611; Policy Templates Provisioning</li>
</ul></td></tr>
<tr valign="top"><td>M3 (client)</td><td><ul>
  <li>5G-MAG prototype</li>
</ul></td><td><ul>
  <li>&#x2611; HTTP/1.1</li>
  <li>&#x2611; HTTP/2.0</li>
  <li>&#x2611; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2611; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2611; Content Hosting Provisioning</li>
  <li>&#x2611; Server Certificates Provisioning</li>
</ul></td></tr>
<tr valign="top"><td>M5 (server)</td><td><ul>
  <li>TS 26.501 v17.6.0</li>
  <li>TS 26.512 v17.6.0</li>
</ul></td><td><ul>
  <li>&#x2611; HTTP/1.1</li>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2611; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2611; Service Access Information</li>
  <li>&#x2611; Consumption Reporting</li>
  <li>&#x2611; Dynamic Policies<br />
      &nbsp; <b>Service Data Flow Description Methods:</b><ul>
    <li>&#x2610; 2 Tuple</li>
    <li>&#x2611; 5 Tuple</li>
    <li>&#x2610; ToS</li>
    <li>&#x2610; Flow Label</li>
    <li>&#x2610; Domain Name</li>
  </ul></li>
  <li>&#x2611; Metrics Reporting</li>
  <li>&#x2611; Network Assistance<ul>
    <li>&#x2610; Throughput Estimation</li>
    <li>&#x2611; Delivery Boost</li>
  </ul></li>
</ul></td></tr>
<tr valign="top"><td>N5 (Npcf client/server)</td><td><ul>
  <li>TS 29.514 v17.8.0</li>
</ul></td><td><ul>
  <li>&#x2611; HTTP/2.0</li>
  <li>&#x2611; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2611; Policy Authorization</li>
  <li>&#x2611; Policy Authorization Notifications</li>
</ul></td></tr>
<tr valign="top"><td>N33 (client)</td><td><ul>
  <li>TS 29.591 v17.9.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Event Exposure</li>
</ul></td></tr>
<tr valign="top"><td>R4 (server)</td><td><ul>
  <li>TS 26.512 v17.6.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/1.1</li>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Media Streaming Access</li>
</ul></td></tr>
<tr valign="top"><td>R5/R6 (client/server)</td><td><ul>
  <li>TS 26.512 v17.6.0</li>
  <li>TS 29.517 v17.9.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/1.1</li>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Media Streaming QoE Event</li>
  <li>&#x2610; Media Streaming Consumption Event</li>
  <li>&#x2610; Media Streaming Network Assistance Invocation Event</li>
  <li>&#x2610; Media Streaming Dynamic Policy Invocation Event</li>
  <li>&#x2610; Media Streaming Access Event</li>
  <li>&#x2610; Event Subscription</li>
</ul></td></tr>
<tr valign="top"><td>Nbsf (client)</td><td><ul>
  <li>TS 29.513 v17.10.0</li>
  <li>TS 29.521 v17.8.0</li>
</ul></td><td><ul>
  <li>&#x2611; HTTP/2.0</li>
  <li>&#x2611; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2611; Binding Information Retrieval</li>
</ul></td></tr>
</tbody>
<tfoot>
<!--<tr><td colspan="4"><b>Notes:</b><br />1: Only the Delivery Boost feature of Network Assistance is implemented, the Throughput Estimation feature is still in development.</td></tr> -->
</tfoot>
</table>
