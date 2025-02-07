---
layout: default
title: Test
parent: Home
nav_order: 0
---

# List of 3GPP APIs supported in the 5G-MAG Reference Tools projects
The list below includes 3GPP APIs supported in the different project.

## 5G Media Streaming 
The table contains the 3GPP 5G Media Streaming APIs for Release 17 (TS 26.512) and Release 18 (TS 26.510 & TS 26.512). Note that the current 5G-MAG Reference Tools 5GMS AF and AS are only base on Release 17 (i.e. TS 26.510 does not exist in Release 17). Note that in 5GMS Release 18 many APIs were renamed and moved from TS 26.512 to become more generic versions in TS 26.510 to handle both uplink and downlink for unicast and MBS services.

Scope | Release 17 | Release 18
----- | ---------- | ----------
5GMS | **TS26512_CommonData.yaml**	| TS26510_CommonData.yaml, TS26512_CommonData.yaml |
5GMS | **TS26512_M1_ConsumptionReportingProvisioning.yaml** | TS26510_Maf_Provisioning_ConsumptionReporting.yaml
5GMS | **TS26512_M1_ContentHostingProvisioning.yaml** | TS26510_Maf_Provisioning_ContentHosting.yaml
5GMS | TS26512_M1_ContentPreparationTemplatesProvisioning.yaml | TS26510_Maf_Provisioning_ContentPreparationTemplates.yaml
5GMS | **TS26512_M1_ContentProtocolsDiscovery.yaml** |	TS26510_Maf_Provisioning_ContentProtocols.yaml
5GMS | TS26512_M1_EdgeResourcesProvisioning.yaml | TS26510_Maf_Provisioning_EdgeResources.yaml
5GMS | TS26512_M1_EventDataProcessingProvisioning.yaml | TS26510_Maf_Provisioning_EventDataProcessing.yaml
5GMS | **TS26512_M1_MetricsReportingProvisioning.yaml** | TS26510_Maf_Provisioning_MetricsReporting.yaml
5GMS | **TS26512_M1_PolicyTemplatesProvisioning.yaml** | TS26510_Maf_Provisioning_PolicyTemplates.yaml
5GMS | **TS26512_M1_ProvisioningSessions.yaml** | TS26510_Maf_Provisioning_ProvisioningSessions.yaml
5GMS | **TS26512_M1_ServerCertificatesProvisioning.yaml** | TS26510_Maf_Provisioning_ServerCertificates.yaml
5GMS | N/A | TS26510_Maf_Provisioning_ContentPublishing.yaml
5GMS | N/A | TS26510_Maf_Provisioning_RealTimeCommunication.yaml
5GMS | **TS26512_M5_ConsumptionReporting.yaml** | TS26510_Maf_SessionHandling_ConsumptionReporting.yaml
5GMS | **TS26512_M5_DynamicPolicies.yaml** | TS26510_Maf_SessionHandling_DynamicPolicy.yaml
5GMS | **TS26512_M5_MetricsReporting.yaml** | TS26510_Maf_SessionHandling_MetricsReporting.yaml
5GMS | **TS26512_M5_NetworkAssistance.yaml** | TS26510_Maf_SessionHandling_NetworkAssistance.yaml
5GMS | **TS26512_M5_ServiceAccessInformation.yaml** | TS26510_Maf_SessionHandling_ServiceAccessInformation.yaml
5GMS | PreStd* | TS26512_Mas_Configuration_ContentHosting.yaml
5GMS | PreStd* | TS26512_Mas_Configuration_ContentPreparationTemplates.yaml
5GMS | PreStd* | TS26512_Mas_Configuration_ContentPublishing.yaml
5GMS | PreStd* | TS26512_Mas_Configuration_ServerCertificates.yaml
DC | N/A | **TS26512_R2_DataReporting.yaml**
DC | TS26512_R4_DataReporting.yaml | **TS26512_R4_DataReporting.yaml**
DC | N/A | **TS26512_EventExposure.yaml**

**BOLD** = Within the scope of 5G-MAG Reference Tools implementations

5GMS = 5G Media Streaming; DC = Data Collection

PreStd* = We have implemented a pre-standardisation variant of the 5GMS AS configuration API at reference point M3d that is quite similar to what eventually appeared in Release 18. It's not fully compliant because the service name is different and so are some details.
 
{: .note }
Note that not all aspects of these APIs are implemented. For example Content Preparation, Edge resources, Geo-fencing and URL signing in TS26512_M1_ContentHostingProvisioning.yaml are not implemented
