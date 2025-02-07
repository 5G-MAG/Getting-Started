Agree with David that a separate column for each release would be a more nuanced way of expressing what has been implemented in the 5G-MAG Reference tools.
One small detail: TS26512_R4_DataReporting.yaml exists in Release 17, per David's table below. However, it's not a target for future reference tools development in my opinion. I think we would start from the Release 18 variant, ignoring Release 17 completely. So the it's the one in the second column that should be bold and italic; the one in the first column should still be listed, but shouldn't be either bold or italic.
For TS26512_Mas_Configuration, David has correctly shown that there is no standardised API in Release 17. However, we have implemented a pre-standardisation variant of the 5GMS AS configuration API at reference point M3d that is quite similar to what eventually appeared in Release 18. It's not fully compliant because the service name is different and so are some details. I'm not sure how best to document that, though.

On 13/01/2025 10:04, David Waring wrote:
Your list below includes the 3GPP Release 18 5G Media Streaming APIs (from TS 26.510 & TS 26.512). However, the 5GMS AF and AS are only on Release 17 5GMS  APIs (TS 26.512 only - TS 26.510 does not exist in Release 17). In Release 18 of 5GMS a lot of the APIs were renamed and moved from TS 26.512 to become more generic versions in TS 26.510 to handle both uplink and downlink for unicast and MBS services. This means that for some APIs there's a direct mapping, but other parts of the APIs are only in the new in TS 26.510 or updated TS 26.512 for Release 18.

The following is a rough mapping of Release 17 to Release 18.


| Scope | Release 17 | Release 18 |
| ----- | ---------- | ---------- |
TS26512_CommonData.yaml	TS26510_CommonData.yaml
TS26512_CommonData.yaml
TS26512_M1_ConsumptionReportingProvisioning.yaml	TS26510_Maf_Provisioning_ConsumptionReporting.yaml
TS26512_M1_ContentHostingProvisioning.yaml	TS26510_Maf_Provisioning_ContentHosting.yaml
TS26512_M1_ContentPreparationTemplatesProvisioning.yaml	TS26510_Maf_Provisioning_ContentPreparationTemplates.yaml
TS26512_M1_ContentProtocolsDiscovery.yaml	TS26510_Maf_Provisioning_ContentProtocols.yaml
TS26512_M1_EdgeResourcesProvisioning.yaml	TS26510_Maf_Provisioning_EdgeResources.yaml
TS26512_M1_EventDataProcessingProvisioning.yaml	TS26510_Maf_Provisioning_EventDataProcessing.yaml
TS26512_M1_MetricsReportingProvisioning.yaml	TS26510_Maf_Provisioning_MetricsReporting.yaml
TS26512_M1_PolicyTemplatesProvisioning.yaml	TS26510_Maf_Provisioning_PolicyTemplates.yaml
TS26512_M1_ProvisioningSessions.yaml	TS26510_Maf_Provisioning_ProvisioningSessions.yaml
TS26512_M1_ServerCertificatesProvisioning.yaml	TS26510_Maf_Provisioning_ServerCertificates.yaml
N/A	TS26510_Maf_Provisioning_ContentPublishing.yaml
N/A	TS26510_Maf_Provisioning_RealTimeCommunication.yaml
TS26512_M5_ConsumptionReporting.yaml	TS26510_Maf_SessionHandling_ConsumptionReporting.yaml
TS26512_M5_DynamicPolicies.yaml	TS26510_Maf_SessionHandling_DynamicPolicy.yaml
TS26512_M5_MetricsReporting.yaml	TS26510_Maf_SessionHandling_MetricsReporting.yaml
TS26512_M5_NetworkAssistance.yaml	TS26510_Maf_SessionHandling_NetworkAssistance.yaml
TS26512_M5_ServiceAccessInformation.yaml	TS26510_Maf_SessionHandling_ServiceAccessInformation.yaml
N/A	TS26512_Mas_Configuration_ContentHosting.yaml
N/A	TS26512_Mas_Configuration_ContentPreparationTemplates.yaml
N/A	TS26512_Mas_Configuration_ContentPublishing.yaml
N/A	TS26512_Mas_Configuration_ServerCertificates.yaml
N/A	TS26512_R2_DataReporting.yaml
TS26512_R4_DataReporting.yaml	TS26512_R4_DataReporting.yaml
N/A	TS26512_EventExposure.yaml

{note :}
Note that not all aspects of these APIs are implemented. For example Content Preparation, Edge resources, Geo-fencing and URL signing in TS26512_M1_ContentHostingProvisioning.yaml are not implemented
