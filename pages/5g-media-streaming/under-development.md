---
layout: default
title: Under Development
parent: 5G Media Streaming
has_children: false
nav_order: 0
---

# Under Development
This page contains information such as the specifications within the scope of the tools, high-level architecture, APIs under implementation,...

## Specifications
Visit the [Standards repository](https://5g-mag.github.io/Standards/pages/5g-media-streaming.html) for more details on the specifications within the scope of the tools.

## High-level architecture

### High-level architecture: 5G Downlink Media Streaming (5GMSd)

<img src="../../assets/images/projects/5gms_diagram.png" style="width: 80%">

 * Check [here](./repositories.html) to access the repositories for 5G Downlink Media Streaming
 * Check [here](../3gpp-ran-and-core-platforms/repositories.html) to access the repositories for 3GPP RAN and Core Platforms

### High-level architecture: 5G Downlink Media Streaming (5GMSd) with 5G Core Network Components

<img src="../../assets/images/projects/5gms_5gc_diagram.png" style="width: 80%">

 * Check [here](./repositories.html) to access the repositories for 5G Downlink Media Streaming
 * Check [here](../3gpp-ran-and-core-platforms/repositories.html) to access the repositories for 3GPP RAN and Core Platforms
 * Check [here](../5g-core-network-components/repositories.html) to access the repositories for 5G Core Network Components

### High-level architecture: 5G Downlink Media Streaming (5GMSd) with UE Data Collection Reporting and Event Exposure

<img src="../../assets/images/projects/5gms_uedc_diagram.png" style="width: 80%">

 * Check [here](./repositories.html) to access the repositories for 5G Downlink Media Streaming
 * Check [here](../3gpp-ran-and-core-platforms/repositories.html) to access the repositories for 3GPP RAN and Core Platforms
 * Check [here](../ue-data-collection-reporting-exposure/repositories.html) the repositories for UE Data Collection, Reporting and Event Exposure

### High-level architecture: 5G Downlink Media Streaming (5GMSd) over eMBMS

<img src="../../assets/images/projects/5gms_5gbc_diagram.png" style="width: 80%">

 * Check [here](./repositories.html) to access the repositories for 5G Downlink Media Streaming
 * Check [here](../3gpp-ran-and-core-platforms/repositories.html) to access the repositories for 3GPP RAN and Core Platforms
 * Check [here](../lte-based-5g-broadcast/repositories.html) the repositories for 5G Broadcast

## Supported APIs for 5G Media Streaming

### Relevant specifications
The table contains the 3GPP 5G Media Streaming APIs for Release 17 (TS 26.512) and Release 18 (TS 26.510 & TS 26.512). Note that the current reference implementation of the 5GMSd AF and 5GMSd AS are based on Release 17 (TS 26.510 does not exist in Release 17). In Release 18, the media session handling APIs were moved from TS 26.512 into TS 26.510 to generalise them to support the Real-Time media Communication (RTC) System as well as the 5G Media Streaming (5GMS) System.
More information about the relevant specifications can be found in the following pages:
 - 5G Media Streaming Architecture: [Standards pages](https://5g-mag.github.io/Standards/pages/5g-media-streaming.html)
 - UE Data Collection and Event Exposure: [Standards pages](https://5g-mag.github.io/Standards/pages/data-collection-event-exposure.html)

### Classification

 Release 17 | Release 18
 ---------- | ----------
 <span style="color: green;font-weight:bold;">TS26512_CommonData.yaml</span> 	| TS26510_CommonData.yaml, TS26512_CommonData.yaml |
 <span style="color: green;font-weight:bold;">TS26512_M1_ConsumptionReportingProvisioning.yaml</span>  | TS26510_Maf_Provisioning_ConsumptionReporting.yaml
 <span style="color: green;font-weight:bold;">TS26512_M1_ContentHostingProvisioning.yaml</span>  | TS26510_Maf_Provisioning_ContentHosting.yaml
 TS26512_M1_ContentPreparationTemplatesProvisioning.yaml | TS26510_Maf_Provisioning_ContentPreparationTemplates.yaml
 <span style="color: green;font-weight:bold;">TS26512_M1_ContentProtocolsDiscovery.yaml</span>  |	TS26510_Maf_Provisioning_ContentProtocols.yaml
 TS26512_M1_EdgeResourcesProvisioning.yaml | TS26510_Maf_Provisioning_EdgeResources.yaml
 TS26512_M1_EventDataProcessingProvisioning.yaml | TS26510_Maf_Provisioning_EventDataProcessing.yaml
 <span style="color: green;font-weight:bold;">TS26512_M1_MetricsReportingProvisioning.yaml</span>  | TS26510_Maf_Provisioning_MetricsReporting.yaml
 <span style="color: green;font-weight:bold;">TS26512_M1_PolicyTemplatesProvisioning.yaml</span>  | TS26510_Maf_Provisioning_PolicyTemplates.yaml
 <span style="color: green;font-weight:bold;">TS26512_M1_ProvisioningSessions.yaml</span>  | TS26510_Maf_Provisioning_ProvisioningSessions.yaml
 <span style="color: green;font-weight:bold;">TS26512_M1_ServerCertificatesProvisioning.yaml</span>  | TS26510_Maf_Provisioning_ServerCertificates.yaml
 N/A | TS26510_Maf_Provisioning_ContentPublishing.yaml
 N/A | TS26510_Maf_Provisioning_RealTimeCommunication.yaml
 <span style="color: green;font-weight:bold;">TS26512_M5_ConsumptionReporting.yaml</span>  | TS26510_Maf_SessionHandling_ConsumptionReporting.yaml
 <span style="color: green;font-weight:bold;">TS26512_M5_DynamicPolicies.yaml</span>  | TS26510_Maf_SessionHandling_DynamicPolicy.yaml
 <span style="color: green;font-weight:bold;">TS26512_M5_MetricsReporting.yaml</span>  | TS26510_Maf_SessionHandling_MetricsReporting.yaml
 <span style="color: green;font-weight:bold;">TS26512_M5_NetworkAssistance.yaml</span>  | TS26510_Maf_SessionHandling_NetworkAssistance.yaml
 <span style="color: green;font-weight:bold;">TS26512_M5_ServiceAccessInformation.yaml</span>  | TS26510_Maf_SessionHandling_ServiceAccessInformation.yaml
 PreStd* | TS26512_Mas_Configuration_ContentHosting.yaml
 PreStd* | TS26512_Mas_Configuration_ContentPreparationTemplates.yaml
 PreStd* | TS26512_Mas_Configuration_ContentPublishing.yaml
 PreStd* | TS26512_Mas_Configuration_ServerCertificates.yaml
 N/A | <span style="color: orange;font-weight:bold;">TS26512_R2_DataReporting.yaml</span>
 TS26512_R4_DataReporting.yaml | <span style="color: orange;font-weight:bold;">TS26512_R4_DataReporting.yaml</span>
 N/A | <span style="color: orange;font-weight:bold;">TS26512_EventExposure.yaml</span>

### Legend

<span style="color: green;font-weight:bold;">TEXT</span> = Already implemented in 5G-MAG Reference Tools

<span style="color: orange;font-weight:bold;">TEXT</span> = In the implementation roadmap in 5G-MAG Reference Tools

PreStd* = Implementatio of a pre-standardisation variant of the 5GMS AS configuration API at reference point M3d that is similar to what eventually appeared in Release 18. The service name is different and so are some details.
 
{: .note }
Note that not all aspects of these APIs are implemented. For example Content Preparation, Edge resources, Geo-fencing and URL signing in TS26512_M1_ContentHostingProvisioning.yaml are not implemented.
