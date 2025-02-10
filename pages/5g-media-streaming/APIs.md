---
layout: default
title: Supported APIs
parent: 5G Downlink Media Streaming
has_children: false
nav_order: 1
---

# Supported APIs for 5G Media Streaming
The table contains the 3GPP 5G Media Streaming APIs for Release 17 (TS 26.512) and Release 18 (TS 26.510 & TS 26.512). Note that the current 5G-MAG Reference Tools 5GMS AF and AS are only base on Release 17 (i.e. TS 26.510 does not exist in Release 17). Note that in 5GMS Release 18 many APIs were renamed and moved from TS 26.512 to become more generic versions in TS 26.510 to handle both uplink and downlink for unicast and MBS services.

## Relevant specifications
More information about the relevant specifications can be found in the following pages:
 - 5G Media Streaming Architecture: [Standards pages](https://5g-mag.github.io/Standards/pages/5g-media-streaming.html)
 - UE Data Collection and Event Exposure: [Standards pages](https://5g-mag.github.io/Standards/pages/data-collection-event-exposure.html)

# Classification

 Release 17 | Release 18
 ---------- | ----------
 **TS26512_CommonData.yaml**	| TS26510_CommonData.yaml, TS26512_CommonData.yaml |
 **TS26512_M1_ConsumptionReportingProvisioning.yaml** | TS26510_Maf_Provisioning_ConsumptionReporting.yaml
 **TS26512_M1_ContentHostingProvisioning.yaml** | TS26510_Maf_Provisioning_ContentHosting.yaml
 TS26512_M1_ContentPreparationTemplatesProvisioning.yaml | TS26510_Maf_Provisioning_ContentPreparationTemplates.yaml
 **TS26512_M1_ContentProtocolsDiscovery.yaml** |	TS26510_Maf_Provisioning_ContentProtocols.yaml
 TS26512_M1_EdgeResourcesProvisioning.yaml | TS26510_Maf_Provisioning_EdgeResources.yaml
 TS26512_M1_EventDataProcessingProvisioning.yaml | TS26510_Maf_Provisioning_EventDataProcessing.yaml
 **TS26512_M1_MetricsReportingProvisioning.yaml** | TS26510_Maf_Provisioning_MetricsReporting.yaml
 **TS26512_M1_PolicyTemplatesProvisioning.yaml** | TS26510_Maf_Provisioning_PolicyTemplates.yaml
 **TS26512_M1_ProvisioningSessions.yaml** | TS26510_Maf_Provisioning_ProvisioningSessions.yaml
 **TS26512_M1_ServerCertificatesProvisioning.yaml** | TS26510_Maf_Provisioning_ServerCertificates.yaml
 N/A | TS26510_Maf_Provisioning_ContentPublishing.yaml
 N/A | TS26510_Maf_Provisioning_RealTimeCommunication.yaml
 **TS26512_M5_ConsumptionReporting.yaml** | TS26510_Maf_SessionHandling_ConsumptionReporting.yaml
 **TS26512_M5_DynamicPolicies.yaml** | TS26510_Maf_SessionHandling_DynamicPolicy.yaml
 **TS26512_M5_MetricsReporting.yaml** | TS26510_Maf_SessionHandling_MetricsReporting.yaml
 **TS26512_M5_NetworkAssistance.yaml** | TS26510_Maf_SessionHandling_NetworkAssistance.yaml
 **TS26512_M5_ServiceAccessInformation.yaml** | TS26510_Maf_SessionHandling_ServiceAccessInformation.yaml
 PreStd* | TS26512_Mas_Configuration_ContentHosting.yaml
 PreStd* | TS26512_Mas_Configuration_ContentPreparationTemplates.yaml
 PreStd* | TS26512_Mas_Configuration_ContentPublishing.yaml
 PreStd* | TS26512_Mas_Configuration_ServerCertificates.yaml
 N/A | **TS26512_R2_DataReporting.yaml**
 TS26512_R4_DataReporting.yaml | **TS26512_R4_DataReporting.yaml**
 N/A | **TS26512_EventExposure.yaml**

## Legend

<span style="color: green;font-weight:bold;">TEXT</span> = Already implemented in 5G-MAG Reference Tools

<span style="color: orange;font-weight:bold;">TEXT</span> = In the implementation roadmap in 5G-MAG Reference Tools

PreStd* = Implementatio of a pre-standardisation variant of the 5GMS AS configuration API at reference point M3d that is similar to what eventually appeared in Release 18. The service name is different and so are some details.
 
{: .note }
Note that not all aspects of these APIs are implemented. For example Content Preparation, Edge resources, Geo-fencing and URL signing in TS26512_M1_ContentHostingProvisioning.yaml are not implemented.
