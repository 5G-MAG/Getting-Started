# List of 5G Downlink Media Streaming Features

The following describes the features of the Application Function that have been implemented, due to be implemented or not planned
yet.

## Implemented in latest release (v1.2.0)

- Reference point M1 (AP <=> AF)
  - Provisioning Sessions (TS 26.512 v17.3.0)
  - Content Protocols Discovery (TS 26.512 v17.3.0)
  - Server Certificates Provisioning (TS 26.512 v17.3.0)
  - Content Hosting Provisioning (TS 26.512 v17.3.0)
- Reference point M3 (AS <=> AF)
  - Server Certificates Provisioning
  - Content Hosting Provisioning
- Reference point M5 (UE <=> AF)
  - Service Access Information (TS 26.512 v17.3.0)

## Being worked on for pending releases

This is a list of features being worked on for upcoming releases (and who is primarily working on that feature):

- Reference point M1 (AP <=> AF)
  - Uplift to TS 26.512 V17.4.0 (BBC)
  - Policy Templates Provisioning (BBC)
  - Uplift to TS 26.512 V17.5.0 (BBC)
  - QoE Metrics Reporting Provisioning (Fraunhofer Fokus)
- Reference point M5 (UE <=> AF)
  - Network Assistance (BBC)
  - Dynamic Policies (BBC)
  - QoE Metrics Reporting (Fraunhofer Fokus)
  - Consumption Reporting (Qualcomm)
- 5GMBS seamless switching ()

## Unimplemented

The following is a list of possible areas of the project to work on, noting which reference point(s) each is for or where a component
resides:

- Data Collection AF
- Direct Data Collection Client (UE)
- Reference point M1 (AP <=> AF)
  - Edge Computing integration
  - Content Preparation Template Provisioning
  - Consumption Reporting Provisioning
  - Event Data Processing Provisioning
- Reference point M3 (AS <=> AF)
  - Life-cycle management (heartbeat/registration/deregistration)
- Reference point M5 (UE <=> AF)
- Reference point R4 (AS <=> AF)
  - Media Streaming Access Reporting
- Reference point R6 (AP <=> AF)
  - Exposure of Dynamic Policy invocation events
  - Exposure of Network Assistance invocation events
  - Exposure of QoE Metrics Reporting events
  - Exposure of Consumption Reporting events
  - Exposure of Media Streaming Access Report events

# Supported Features in the Software Releases

## 5GMSd Application Function

The release versions of the 5GMSd Application Function support differing sets of reference points, as described by the different
versions of the 3GPP specifications, and differing levels of feature support for those interfaces. The page attempts to capture
the feature sets and specification versions for each release, starting with the most recent release or upcoming releases.

### Key

Where a feature of the specifications is supported the entry will be marked with &#x2611; and where it is unimplemented in that
version the feature will be marked with &#x2610;.

### Upcoming Release v1.3.0

<table><thead>
<tr><th>Interface reference point</th><th>Specifications & Versions</th><th>Protocols</th><th>Features</th></tr>
</thead>
</tbody>
<tr valign="top"><td>M1 (server)</td><td><ul>
  <li>TS 26.501 v17.4.0</li>
  <li>TS 26.512 v17.4.0</li>
</ul></td><td><ul>
  <li>&#x2611; HTTP/1.1</li>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2611; Content Hosting Provisioning</li>
  <li>&#x2611; Content Protocols Discovery</li>
  <li>&#x2611; Provisioning Sessions</li>
  <li>&#x2611; Server Certificates Provisioning</li>
  <li>&#x2610; Consumption Reporting Provisioning</li>
  <li>&#x2610; Content Preparation Templates Provisioning</li>
  <li>&#x2610; Edge Resources Provisioning</li>
  <li>&#x2610; Event Data Processing Provisioning</li>
  <li>&#x2610; Metrics Reporting Provisioning</li>
  <li>&#x2610; Policy Templates Provisioning</li>
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
  <li>TS 26.501 v17.4.0</li>
  <li>TS 26.512 v17.4.0</li>
</ul></td><td><ul>
  <li>&#x2611; HTTP/1.1</li>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2611; Service Access Information</li>
  <li>&#x2610; Consumption Reporting</li>
  <li>&#x2610; Dynamic Policies</li>
  <li>&#x2610; Metrics Reporting</li>
  <li>&#x2610; Network Assistance</li>
</ul></td></tr>
<tr valign="top"><td>N5 (client/server)</td><td><ul>
  <li>TS 29.525 v17.9.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Event Exposure</li>
  <li>&#x2610; UE Policy Control</li>
</ul></td></tr>
<tr valign="top"><td>N33 (client)</td><td><ul>
  <li>TS 29.591 v17.9.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Event Exposure</li>
</ul></td></tr>
<tr valign="top"><td>Nbsf (client)</td><td><ul>
  <li>TS 29.513 v17.10.0</li>
  <li>TS 29.521 v17.8.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Binding Information Retrieval</li>
</ul></td></tr>
</tbody>
</table>

### Release v1.2.0

<table><thead>
<tr><th>Interface reference point</th><th>Specifications & Versions</th><th>Protocols</th><th>Features</th></tr>
</thead>
</tbody>
<tr valign="top"><td>M1 (server)</td><td><ul>
  <li>TS 26.501 v17.3.0</li>
  <li>TS 26.512 v17.3.0</li>
</ul></td><td><ul>
  <li>&#x2611; HTTP/1.1</li>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2611; Content Hosting Provisioning</li>
  <li>&#x2611; Content Protocols Discovery</li>
  <li>&#x2611; Provisioning Sessions</li>
  <li>&#x2611; Server Certificates Provisioning</li>
  <li>&#x2610; Consumption Reporting Provisioning</li>
  <li>&#x2610; Content Preparation Templates Provisioning</li>
  <li>&#x2610; Edge Resources Provisioning</li>
  <li>&#x2610; Event Data Processing Provisioning</li>
  <li>&#x2610; Metrics Reporting Provisioning</li>
  <li>&#x2610; Policy Templates Provisioning</li>
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
  <li>TS 26.501 v17.3.0</li>
  <li>TS 26.512 v17.3.0</li>
</ul></td><td><ul>
  <li>&#x2611; HTTP/1.1</li>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2611; Service Access Information</li>
  <li>&#x2610; Consumption Reporting</li>
  <li>&#x2610; Dynamic Policies</li>
  <li>&#x2610; Metrics Reporting</li>
  <li>&#x2610; Network Assistance</li>
</ul></td></tr>
<tr valign="top"><td>N5 (client/server)</td><td><ul>
  <li>TS 29.525 v17.9.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Event Exposure</li>
  <li>&#x2610; UE Policy Control</li>
</ul></td></tr>
<tr valign="top"><td>N33 (client)</td><td><ul>
  <li>TS 29.591 v17.9.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Event Exposure</li>
</ul></td></tr>
<tr valign="top"><td>Nbsf (client)</td><td><ul>
  <li>TS 29.513 v17.10.0</li>
  <li>TS 29.521 v17.8.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Binding Information Retrieval</li>
</ul></td></tr>
</tbody>
</table>

### Release v1.1.0

<table><thead>
<tr><th>Interface reference point</th><th>Specifications & Versions</th><th>Protocols</th><th>Features</th></tr>
</thead>
</tbody>
<tr valign="top"><td>M1 (server)</td><td><ul>
  <li>TS 26.501 v17.3.0</li>
  <li>TS 26.512 v17.3.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/1.1</li>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Content Hosting Provisioning</li>
  <li>&#x2610; Content Protocols Discovery</li>
  <li>&#x2610; Provisioning Sessions</li>
  <li>&#x2610; Server Certificates Provisioning</li>
  <li>&#x2610; Consumption Reporting Provisioning</li>
  <li>&#x2610; Content Preparation Templates Provisioning</li>
  <li>&#x2610; Edge Resources Provisioning</li>
  <li>&#x2610; Event Data Processing Provisioning</li>
  <li>&#x2610; Metrics Reporting Provisioning</li>
  <li>&#x2610; Policy Templates Provisioning</li>
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
  <li>TS 26.501 v17.3.0</li>
  <li>TS 26.512 v17.3.0</li>
</ul></td><td><ul>
  <li>&#x2611; HTTP/1.1</li>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/1.1 over SSL/TLS</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2611; Service Access Information</li>
  <li>&#x2610; Consumption Reporting</li>
  <li>&#x2610; Dynamic Policies</li>
  <li>&#x2610; Metrics Reporting</li>
  <li>&#x2610; Network Assistance</li>
</ul></td></tr>
<tr valign="top"><td>N5 (client/server)</td><td><ul>
  <li>TS 29.525 v17.9.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Event Exposure</li>
  <li>&#x2610; UE Policy Control</li>
</ul></td></tr>
<tr valign="top"><td>N33 (client)</td><td><ul>
  <li>TS 29.591 v17.9.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Event Exposure</li>
</ul></td></tr>
<tr valign="top"><td>Nbsf (client)</td><td><ul>
  <li>TS 29.513 v17.10.0</li>
  <li>TS 29.521 v17.8.0</li>
</ul></td><td><ul>
  <li>&#x2610; HTTP/2.0</li>
  <li>&#x2610; HTTP/2.0 over SSL/TLS</li>
</ul></td><td><ul>
  <li>&#x2610; Binding Information Retrieval</li>
</ul></td></tr>
</tbody>
</table>

