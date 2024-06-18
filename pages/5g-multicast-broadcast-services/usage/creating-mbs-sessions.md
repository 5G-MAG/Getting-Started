---
layout: default
title: Creating MBS Sessions
parent: Usage
grand_parent: 5G Multicast Broadcast Services
has_children: false
nav_order: 2
---
# Creating MBS Sessions

## Creating a Broadcast MBS Session

### Method 1: Creating a Broadcast MBS Session and a TMGI in the same request

With this method, the AF will ask the MB-SMF to allocate one TMGI and an MBS Session will be created and associated with this TMGI in the same request. The SSM is used for the detection of the multicast transport over N6mb.

```bash
# MBS Session Create request with TMGI allocate: /nmbsmf-mbssession/v1/mbs-sessions with multicast source
curl --http2-prior-knowledge \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{ "mbsSession": { "ssm": { "sourceIpAddr": { "ipv4Addr": "10.33.33.3" }, "destIpAddr": { "ipv4Addr": "239.0.0.20" } },"tmgiAllocReq": true, "serviceType":"BROADCAST" } }' \
  mb-smf.open5gs.org:80/nmbsmf-mbssession/v1/mbs-sessions
```

The response of the MB-SMF contains the allocated TMGI as MBS Session identifier and also de SSM specified in the request:

```json
{"mbsSession":{"mbsSessionId":{"tmgi":{"mbsServiceId":"F9ECB4","plmnId":{"mcc":"001","mnc":"01"}}},"tmgi":{"mbsServiceId":"F9ECB4","plmnId":{"mcc":"001","mnc":"01"}},"serviceType":"BROADCAST"}}
```

### Method 2: Creating a Broadcast MBS Session using an existing TMGI

With this method, the AF will ask the MB-SMF to create an MBS Session and the existing TMGI will be associated with it. The SSM is used for the detection of the multicast transport over N6mb.

```bash
# MBS Session Create request with existing TMGI: /nmbsmf-mbssession/v1/mbs-sessions
curl --http2-prior-knowledge \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{ "mbsSession": { "mbsSessionId": { "tmgi": { "mbsServiceId": "9236F7", "plmnId": { "mcc":"001", "mnc":"01" } } }, "ssm": { "sourceIpAddr": { "ipv4Addr": "10.33.33.3" }, "destIpAddr": { "ipv4Addr": "239.0.0.20" } }, "serviceType":"BROADCAST" } }' \
  mb-smf.open5gs.org:80/nmbsmf-mbssession/v1/mbs-sessions
```

The response of the MB-SMF contains the specified TMGI and SSM, using the TMGI as MBS Session identifier as specified in the request:

```json
{"mbsSession":{"mbsSessionId":{"tmgi":{"mbsServiceId":"9236F7","plmnId":{"mcc":"001","mnc":"01"}}},"tmgi":{"mbsServiceId":"9236F7","plmnId":{"mcc":"001","mnc":"01"}},"serviceType":"BROADCAST"}}
```

### Method 3: Creating a Broadcast MBS Session using SSM as identifier

> Note: To be documented

</details>
