---
layout: default
title: TMGI Management
parent: Usage
grand_parent: 5G Multicast Broadcast Services
has_children: false
nav_order: 2
---

# TMGI Management

The TMGI can be created by using the `TMGI Service API` or by using the `MBS Session Service API` with the `tmgiAllocReq` set to _true_.

## Creating/Allocating a TMGI
### Method 1: TMGI Service API

With this method, the AF/AS will ask the MB-SMF to allocate the number of TMGIs present on the `tmgiNumber` field in the JSON data of the request.

```bash
# Execute this command inside the AF/AS container
# TMGI Allocate (allocate) request: /nmbsmf-tmgi/v1/tmgi
curl --http2-prior-knowledge \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{ "tmgiNumber": 1 }' \
  smf-mb-smf.5g-mag.org:80/nmbsmf-tmgi/v1/tmgi
```

The response of the MB-SMF, should send the list of allocated TMGIs:

```json
{"tmgiList":[{"mbsServiceId":"9236F7","plmnId":{"mcc":"001","mnc":"01"}}],"expirationTime":"2024-06-04T16:59:10.628193+00:00"}
```

### Method 2: MBS Session Service API

With this method, the AF/AS will ask the MB-SMF to allocate one TMGI and an MBS Session will be created and associated with this TMGI in the same request. The SSM is used for the detection of the multicast transport over N6mb.

```bash
# Execute this command inside the AF/AS container
# MBS Session Create request with TMGI allocate: /nmbsmf-mbssession/v1/mbs-sessions with multicast source
curl --http2-prior-knowledge \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{ "mbsSession": { "ssm": { "sourceIpAddr": { "ipv4Addr": "<af_as_container_ip>" }, "destIpAddr": { "ipv4Addr": "<n6mb_ip_multicast_destination_address>" } },"tmgiAllocReq": true, "serviceType":"BROADCAST" } }' \
  smf-mb-smf.5g-mag.org:80/nmbsmf-mbssession/v1/mbs-sessions
```

The response of the MB-SMF, should send the MBS Session with the allocated TMGI:

```json
{"mbsSession":{"mbsSessionId":{"tmgi":{"mbsServiceId":"0D3BE6","plmnId":{"mcc":"001","mnc":"01"}}},"tmgi":{"mbsServiceId":"0D3BE6","plmnId":{"mcc":"001","mnc":"01"}},"serviceType":"BROADCAST"}}
```

## Updating an existing TMGI

### TMGI Service API

With this method, the AF/AS will ask the MB-SMF to refresh an existing TMGI. This method is only accesible through the `TMGI Service API` but can be combined with the allocation too:

```bash
# Execute this command inside the AF/AS container
# TMGI Allocate (refresh) request: /nmbsmf-tmgi/v1/tmgi
curl --http2-prior-knowledge \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{ "tmgiList": [ { "mbsServiceId": "9236F7", "plmnId": { "mcc": "001", "mnc": "01" } } ] }' \
  smf-mb-smf.5g-mag.org:80/nmbsmf-tmgi/v1/tmgi
```

The response of the MB-SMF, should send the new expiration time for the refreshed TMGIs:

```json
{"tmgiList":[],"expirationTime":"2024-06-04T17:02:07.119039+00:00"}
```

Combination of TMGI allocate request and TMGI refresh:

```bash
# Execute this command inside the AF/AS container
# TMGI Allocate (allocate + refresh) request: /nmbsmf-tmgi/v1/tmgi
curl --http2-prior-knowledge \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{ "tmgiNumber": 1, "tmgiList": [ { "mbsServiceId": "9236F7", "plmnId": { "mcc": "001", "mnc": "01" } } ] }' \
  smf-mb-smf.5g-mag.org:80/nmbsmf-tmgi/v1/tmgi
```

The response of the MB-SMF, should send the allocated TMGIs and the new expiration time for the refreshed TMGIs:

```json
{"tmgiList":[{"mbsServiceId":"E79DA9","plmnId":{"mcc":"001","mnc":"01"}}],"expirationTime":"2024-06-04T17:03:01.036961+00:00"}
```
