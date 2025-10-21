---
layout: default
title: Using libscMBSMF
parent: Tutorials
grand_parent: 5GC Service Consumers
has_children: false
nav_order: 2
---

# Tutorial - Using the 5GC Service Consumer libraries: libscMBSMF

## Introduction

This tutorial provides information to test the 5GC Service Consumer libraries available in [rt-5gc-service-consumers](https://github.com/5G-MAG/rt-5gc-service-consumers) repository.

This collection of reusable service consumer libraries are designed to talk to the 5G Core Network Functions using some of their defined service interfaces. The command line tools below are provided to demonstrate the use of these service consumer libraries.

## Setup the relevant Open5GS network functions

We recommend a local installation of Open5GS following the instructions provided [here](../../3gpp-ran-and-core-platforms/tutorials/5gnetwork.html).

Note that the **TMGI Allocation/Deallocation tool** and the **MBS Service tool** requires the MBS components under the `5mbs` branch of 5G-MAG's Open5GS repository. This can be cloned with: `git clone --recurse-submodules -b 5mbs https://github.com/5G-MAG/open5gs.git ~/open5gs`. The MBS Transport Function can be installed from the [rt-mbs-transport-function](https://github.com/5G-MAG/rt-mbs-transport-function) repository.

In the following examples 127.0.0.10:7777 is used as the address and port number for the NRF API (Open5GS default).

Please substitute this IP address for the one you are using with your network.

## Using the TMGI Allocation/Deallocation tool

The TMGI Allocation and Deallocation tool can request the allocation or deallocation of a TMGI. It will then display the result and exit.

The TMGI Allocation and Deallocation tool can be run with an allocation command like:

```
/usr/local/bin/tmgi-tool -n 127.0.0.10:7777
```

This will generate the following responses.

At the MB-SMF (with debug option):
```
10/21 18:15:50.561: [sbi] DEBUG: [POST] /nmbsmf-tmgi/v1/tmgi (../lib/sbi/nghttp2-server.c:1173)
10/21 18:15:50.561: [sbi] DEBUG: RECEIVED: 16 (../lib/sbi/nghttp2-server.c:1177)
10/21 18:15:50.561: [sbi] DEBUG: {"tmgiNumber":1} (../lib/sbi/nghttp2-server.c:1179)
0000: 00000004 01000000 00                  .........
10/21 18:15:50.561: [smf] DEBUG: smf_state_operational(): OGS_EVENT_NAME_SBI_SERVER (../src/smf/smf-sm.c:90)
10/21 18:15:50.561: [smf] DEBUG: TMGI allocate request received (../src/smf/nmbsmf-handler.c:36)
10/21 18:15:50.561: [smf] INFO: [Added] Number of TMGIs in SMF is now 1 (../src/smf/context.c:3213)
10/21 18:15:50.561: [sbi] DEBUG: STATUS [200] (../lib/sbi/nghttp2-server.c:645)
10/21 18:15:50.561: [sbi] DEBUG: SENDING...: 122 (../lib/sbi/nghttp2-server.c:653)
10/21 18:15:50.561: [sbi] DEBUG: {"tmgiList":[{"mbsServiceId":"AB4A6A","plmnId":{"mcc":"000","mnc":"000"}}],"expirationTime":"2025-10-21T18:15:50.561421Z"} (../lib/sbi/nghttp2-server.c:654)
10/21 18:15:50.561: [sbi] DEBUG: STREAM closed [1] (../lib/sbi/nghttp2-server.c:1284)
10/21 18:15:50.561: [sbi] DEBUG: FLAGS(0x1) [ACK] (../lib/sbi/nghttp2-server.c:1202)
0000: 00004101 04000000 01887694 d5596a6f   ..A.......v..Yjo
0010: 16e53b89 77176966 dc02d336 d3640ba1   ..;.w.if...6.d..
0020: 6196df69 7e941054 d444a820 09b502e5   a..i~..T.D. ....
0030: c0b771b0 298b46ff 0f0d8208 855f8b1d   ..q.).F......_..
0040: 75d0620d 263d4c74 41ea                u.b.&=LtA.
0000: 00007a00 01000000 017b2274 6d67694c   ..z......{"tmgiL
0010: 69737422 3a5b7b22 6d627353 65727669   ist":[{"mbsServi
0020: 63654964 223a2241 42344136 41222c22   ceId":"AB4A6A","
0030: 706c6d6e 4964223a 7b226d63 63223a22   plmnId":{"mcc":"
0040: 30303022 2c226d6e 63223a22 30303022   000","mnc":"000"
0050: 7d7d5d2c 22657870 69726174 696f6e54   }}],"expirationT
0060: 696d6522 3a223230 32352d31 302d3231   ime":"2025-10-21
0070: 5431383a 31353a35 302e3536 31343231   T18:15:50.561421
0080: 5a227d                                Z"}
10/21 18:15:50.562: [sbi] DEBUG: connection closed [127.0.0.1]:56390 (../lib/sbi/nghttp2-server.c:1008)
```

Back into the tmgi-tool (with debug option):
```
fivegmag@fivegmag:~$ /usr/local/bin/tmgi-tool -n 127.0.0.10:7777
10/21 18:15:50.559: [app] INFO: Configuration: '/tmp/tmgi-tool-yaml.qcfJQE' (../subprojects/open5gs/lib/app/ogs-init.c:144)
10/21 18:15:50.559: [sbi] INFO: NF EndPoint(addr) setup [127.0.0.10:7777] (../subprojects/open5gs/lib/sbi/context.c:430)
10/21 18:15:50.559: [tmgi-tool] INFO: Requesting TMGI... (../tools/c/tmgi-tool/app-sm.c:114)
10/21 18:15:50.559: [sbi] WARNING: Try to discover [nmbsmf-tmgi] (../subprojects/open5gs/lib/sbi/path.c:548)
10/21 18:15:50.560: [sbi] INFO: [33cbff30-ae99-41f0-b6b2-6f48c37c9174] (NRF-discover) NF registered [type:NULL] (../subprojects/open5gs/lib/sbi/nnrf-handler.c:1256)
10/21 18:15:50.560: [sbi] INFO: NF EndPoint(addr) setup [127.0.0.4:80] (../subprojects/open5gs/lib/sbi/context.c:2297)
10/21 18:15:50.560: [sbi] INFO: NF EndPoint(addr) setup [127.0.0.4:7777] (../subprojects/open5gs/lib/sbi/context.c:2034)
10/21 18:15:50.560: [sbi] INFO: [33cbff30-ae99-41f0-b6b2-6f48c37c9174] (NF-discover) NF Profile updated [type:SMF validity:30s] (../subprojects/open5gs/lib/sbi/nnrf-handler.c:1301)
10/21 18:15:50.560: [sbi] INFO: [33cbff30-ae99-41f0-b6b2-6f48c37c9174] NF Instance setup [type:SMF validity:30s] (../lib/mb-smf-service-consumer/nnrf-disc-handle.c:51)
10/21 18:15:50.561: [tmgi-tool] INFO: TMGI[0x7b1aa8000c90 (0x7b1aa8000cb0)]: plmn=000000 created (../tools/c/tmgi-tool/app-sm.c:131)
10/21 18:15:50.561: [tmgi-tool] INFO: TMGI operation finished, exiting... (../tools/c/tmgi-tool/app-sm.c:241)

```

...and a deallocation command like (for an allocated TMGI with PLMN of 001-01):

```
/usr/local/bin/tmgi-tool -d -p 001-01 -n 127.0.0.10:7777
```
To get the full command help for the TMGI Allocation and Deallocation tool use the command:

```
/usr/local/bin/tmgi-tool -h
```

## Using the MBS Service tool

The MBS Service tool will create an MBS Session and then report notifications for that MBS Session.

The MBS Service tool can be run with a command like:

```
/usr/local/bin/mbs-service-tool -TMu -S 192.168.0.1:232.0.0.59 -n 127.0.0.10:7777
```

This will generate the following responses.

At the MB-SMF (with debug option):
```
10/21 18:04:04.581: [sbi] DEBUG: [POST] /nmbsmf-mbssession/v1/mbs-sessions (../lib/sbi/nghttp2-server.c:1173)
10/21 18:04:04.581: [sbi] DEBUG: RECEIVED: 603 (../lib/sbi/nghttp2-server.c:1177)
10/21 18:04:04.581: [sbi] DEBUG: {"mbsSession":{"mbsSessionId":{"ssm":{"sourceIpAddr":{"ipv4Addr":"192.168.0.1"},"destIpAddr":{"ipv4Addr":"232.0.0.59"}}},"tmgiAllocReq":true,"serviceType":"MULTICAST","ingressTunAddrReq":true,"ssm":{"sourceIpAddr":{"ipv4Addr":"192.168.0.1"},"destIpAddr":{"ipv4Addr":"232.0.0.59"}},"mbsSessionSubsc":{"eventList":[{"eventType":"MBS_REL_TMGI_EXPIRY"},{"eventType":"BROADCAST_DELIVERY_STATUS"},{"eventType":"INGRESS_TUNNEL_ADD_CHANGE"}],"notifyUri":"http://0.0.0.0:44431/mbs-session-notify/v1/notification","nfcInstanceId":"91143286-ae97-41f0-b9c4-1dafec2dcc2b"},"activityStatus":"ACTIVE","anyUeInd":true}} (../lib/sbi/nghttp2-server.c:1179)
0000: 00000004 01000000 00                  .........
10/21 18:04:04.581: [smf] DEBUG: smf_state_operational(): OGS_EVENT_NAME_SBI_SERVER (../src/smf/smf-sm.c:90)
10/21 18:04:04.581: [smf] DEBUG: MBS Session create request received (../src/smf/nmbsmf-handler.c:294)
10/21 18:04:04.581: [smf] DEBUG: Found MBS Session (nil) (../src/smf/context.c:3610)
10/21 18:04:04.581: [smf] INFO: [Added] Number of TMGIs in SMF is now 1 (../src/smf/context.c:3213)
10/21 18:04:04.581: [smf] INFO: [Added] Number of MBS Sessions in SMF is now 1 (../src/smf/context.c:3384)
10/21 18:04:04.581: [pfcp] DEBUG: [3] LOCAL  Create  peer [127.0.0.7]:8805 (../lib/pfcp/xact.c:112)
10/21 18:04:04.581: [smf] DEBUG: N4mb Session Establishment Request (../src/smf/n4mb-build.c:45)
10/21 18:04:04.581: [smf] DEBUG: local_ingress_tunnel.len = 19, len = 1 (../src/smf/n4mb-build.c:130)
10/21 18:04:04.581: [pfcp] DEBUG: [3] LOCAL  UPD TX-50  peer [127.0.0.7]:8805 (../lib/pfcp/xact.c:196)
10/21 18:04:04.581: [pfcp] DEBUG: [3] LOCAL  Commit  peer [127.0.0.7]:8805 (../lib/pfcp/xact.c:474)
10/21 18:04:04.582: [sbi] DEBUG: FLAGS(0x1) [ACK] (../lib/sbi/nghttp2-server.c:1202)
10/21 18:04:04.582: [smf] DEBUG: smf_state_operational(): SMF_EVT_N4_MESSAGE (../src/smf/smf-sm.c:90)
10/21 18:04:04.582: [pfcp] DEBUG: [3] LOCAL  Find    peer [127.0.0.7]:8805 (../lib/pfcp/xact.c:742)
10/21 18:04:04.582: [pfcp] DEBUG: [3] LOCAL  Receive peer [127.0.0.7]:8805 (../lib/pfcp/xact.c:758)
10/21 18:04:04.582: [pfcp] DEBUG: [3] LOCAL  UPD RX-51  peer [127.0.0.7]:8805 (../lib/pfcp/xact.c:296)
10/21 18:04:04.582: [smf] DEBUG: smf_pfcp_state_associated(): SMF_EVT_N4_MESSAGE (../src/smf/pfcp-sm.c:196)
10/21 18:04:04.582: [smf] DEBUG: N4mb Session Establishment Response (../src/smf/n4mb-handler.c:64)
10/21 18:04:04.582: [pfcp] DEBUG: [3] LOCAL  Commit  peer [127.0.0.7]:8805 (../lib/pfcp/xact.c:474)
10/21 18:04:04.582: [pfcp] DEBUG: [3] LOCAL  Delete  peer [127.0.0.7]:8805 (../lib/pfcp/xact.c:819)
10/21 18:04:04.582: [smf] DEBUG: Got Created Traffic Endpoint (../src/smf/n4mb-handler.c:100)
10/21 18:04:04.582: [smf] DEBUG: Got Local Ingress Tunnel (../src/smf/n4mb-handler.c:102)
10/21 18:04:04.582: [sock] DEBUG: addr:127.0.0.7, port:37259 (../lib/core/ogs-sockaddr.c:143)
10/21 18:04:04.582: [sbi] DEBUG: STATUS [201] (../lib/sbi/nghttp2-server.c:645)
10/21 18:04:04.582: [sbi] DEBUG: SENDING...: 415 (../lib/sbi/nghttp2-server.c:653)
10/21 18:04:04.582: [sbi] DEBUG: {"mbsSession":{"mbsSessionId":{"ssm":{"sourceIpAddr":{"ipv4Addr":"192.168.0.1"},"destIpAddr":{"ipv4Addr":"232.0.0.59"}}},"tmgi":{"mbsServiceId":"EA7DDD","plmnId":{"mcc":"000","mnc":"000"}},"expirationTime":"2025-10-21T18:04:04.581858Z","serviceType":"MULTICAST","ingressTunAddr":[{"ipv4Addr":"127.0.0.7","portNumber":37259}],"ssm":{"sourceIpAddr":{"ipv4Addr":"192.168.0.1"},"destIpAddr":{"ipv4Addr":"232.0.0.59"}}}} (../lib/sbi/nghttp2-server.c:654)
10/21 18:04:04.582: [sbi] DEBUG: STREAM closed [1] (../lib/sbi/nghttp2-server.c:1284)
10/21 18:04:04.582: [smf] DEBUG: Building MBS Broadcast ContextCreate request (../src/smf/namf-build.c:197)
10/21 18:04:04.582: [smf] DEBUG: MBSSessionSetupOrModRequestTransfer (../src/smf/ngap-build.c:606)
10/21 18:04:04.582: [core] DEBUG:     IPv4[239.0.0.7] (../lib/asn1c/util/conv.c:202)
10/21 18:04:04.582: [core] DEBUG:     IPv4[192.168.55.5] (../lib/asn1c/util/conv.c:202)
10/21 18:04:04.582: [sbi] DEBUG: OGS_SBI_GET_NF_INSTANCE [nf_instance:(nil),service_name:namf-mbs-bc] (../lib/sbi/path.c:288)
10/21 18:04:04.582: [sbi] DEBUG: ogs_sbi_nf_instance_find_by_discovery_param() [nf_instance:(nil),service_name:namf-mbs-bc] (../lib/sbi/path.c:293)
10/21 18:04:04.582: [sbi] DEBUG: [POST] http://127.0.0.200:7777/namf-mbs-bc/v1/mbs-contexts (../lib/sbi/client.c:728)
10/21 18:04:04.582: [sbi] DEBUG: SENDING...[548] (../lib/sbi/client.c:497)
10/21 18:04:04.582: [sbi] DEBUG: --=-pbdLFoKMcdkYUmackBXYbQ==
Content-Type: application/json

{"mbsSessionId":{"tmgi":{"mbsServiceId":"EA7DDD","plmnId":{"mcc":"000","mnc":"000"}}},"mbsServiceArea":{"taiList":[{"plmnId":{"mcc":"000","mnc":"000"},"tac":"200"}]},"n2MbsSmInfo":{"ngapIeType":"MBS_SES_REQ","ngapData":{"contentId":"ngap-sm"}},"notifyUri":"blablabla","snssai":{"sst":1,"sd":"13"}}
--=-pbdLFoKMcdkYUmackBXYbQ==
Content-Id: ngap-sm
Content-Type: application/vnd.3gpp.ngap

 (../lib/sbi/client.c:499)
0000: 00007101 04000000 01488210 037694d5   ..q......H...v..
0010: 596a6f16 e53b8977 176966dc 02d336d3   Yjo..;.w.if...6.
0020: 640ba161 96df697e 941054d4 44a82009   d..a..i~..T.D. .
0030: b502e5c0 35700d29 8b46ff0f 0d033431   ....5p.).F....41
0040: 355f8b1d 75d0620d 263d4c74 41ea0f1f   5_..u.b.&=LtA...
0050: a99d29ae e30c044e ae05c0bb 571d75d7   ..)....N....W.u.
0060: 58aa98d1 4cab531a 105420c7 a98ee162   X...L.S..T ....b
0070: 98d0b20a 8418f521 80ff                .......!..
0000: 00019f00 01000000 017b226d 62735365   .........{"mbsSe
0010: 7373696f 6e223a7b 226d6273 53657373   ssion":{"mbsSess
0020: 696f6e49 64223a7b 2273736d 223a7b22   ionId":{"ssm":{"
0030: 736f7572 63654970 41646472 223a7b22   sourceIpAddr":{"
0040: 69707634 41646472 223a2231 39322e31   ipv4Addr":"192.1
0050: 36382e30 2e31227d 2c226465 73744970   68.0.1"},"destIp
0060: 41646472 223a7b22 69707634 41646472   Addr":{"ipv4Addr
0070: 223a2232 33322e30 2e302e35 39227d7d   ":"232.0.0.59"}}
0080: 7d2c2274 6d676922 3a7b226d 62735365   },"tmgi":{"mbsSe
0090: 72766963 65496422 3a224541 37444444   rviceId":"EA7DDD
00a0: 222c2270 6c6d6e49 64223a7b 226d6363   ","plmnId":{"mcc
00b0: 223a2230 3030222c 226d6e63 223a2230   ":"000","mnc":"0
00c0: 3030227d 7d2c2265 78706972 6174696f   00"}},"expiratio
00d0: 6e54696d 65223a22 32303235 2d31302d   nTime":"2025-10-
00e0: 32315431 383a3034 3a30342e 35383138   21T18:04:04.5818
00f0: 35385a22 2c227365 72766963 65547970   58Z","serviceTyp
0100: 65223a22 4d554c54 49434153 54222c22   e":"MULTICAST","
0110: 696e6772 65737354 756e4164 6472223a   ingressTunAddr":
0120: 5b7b2269 70763441 64647222 3a223132   [{"ipv4Addr":"12
0130: 372e302e 302e3722 2c22706f 72744e75   7.0.0.7","portNu
0140: 6d626572 223a3337 3235397d 5d2c2273   mber":37259}],"s
0150: 736d223a 7b22736f 75726365 49704164   sm":{"sourceIpAd
0160: 6472223a 7b226970 76344164 6472223a   dr":{"ipv4Addr":
0170: 22313932 2e313638 2e302e31 227d2c22   "192.168.0.1"},"
0180: 64657374 49704164 6472223a 7b226970   destIpAddr":{"ip
0190: 76344164 6472223a 22323332 2e302e30   v4Addr":"232.0.0
01a0: 2e353922 7d7d7d7d                     .59"}}}}
10/21 18:04:04.584: [sbi] DEBUG: [201:POST] http://127.0.0.200:7777/namf-mbs-bc/v1/mbs-contexts (../lib/sbi/client.c:675)
10/21 18:04:04.584: [sbi] DEBUG: RECEIVED[86] (../lib/sbi/client.c:686)
10/21 18:04:04.584: [sbi] DEBUG: {"mbsSessionId":{"tmgi":{"mbsServiceId":"EA7DDD","plmnId":{"mcc":"000","mnc":"000"}}}} (../lib/sbi/client.c:689)
10/21 18:04:04.584: [sbi] DEBUG: [NULL] NFInstance added with Ref [(null)] (../lib/sbi/context.c:1160)
10/21 18:04:04.584: [sbi] DEBUG: ogs_sbi_nf_state_initial(): ENTRY (../lib/sbi/nf-sm.c:60)
10/21 18:04:04.584: [sbi] DEBUG: ogs_sbi_nf_state_registered(): ENTRY (../lib/sbi/nf-sm.c:198)
10/21 18:04:04.584: [sbi] INFO: [AMF] (SCP-discover) NF registered [3cc54364-ae97-41f0-b71f-2ba4bced132d] (../lib/sbi/path.c:212)
10/21 18:04:04.584: [sbi] INFO: [3cc54364-ae97-41f0-b71f-2ba4bced132d] NF Instance setup [type:AMF validity:0s] (../lib/sbi/path.c:227)
10/21 18:04:04.584: [smf] DEBUG: smf_state_operational(): OGS_EVENT_NAME_SBI_CLIENT (../src/smf/smf-sm.c:90)
10/21 18:04:04.584: [smf] WARNING: Handling MBS Broadcast ContextCreate response (../src/smf/namf-handler.c:256)
```

Back into the mbs-service-tool (with debug option):

```
fivegmag@fivegmag:~$ /usr/local/bin/mbs-service-tool -TMu -S 192.168.0.1:232.0.0.59 -n 127.0.0.10:7777 -e debug
10/21 18:04:04.579: [app] INFO: Configuration: '/tmp/mbs-service-tool-yaml.0XhxCw' (../subprojects/open5gs/lib/app/ogs-init.c:144)
10/21 18:04:04.579: [mbs-service-tool] DEBUG: App initialised, configuring... (../tools/c/mbs-service-tool/init.c:70)
10/21 18:04:04.580: [sock] DEBUG: addr:127.0.0.1, port:80 (../subprojects/open5gs/lib/core/ogs-sockaddr.c:143)
10/21 18:04:04.580: [sock] DEBUG: addr:127.0.0.10, port:7777 (../subprojects/open5gs/lib/core/ogs-sockaddr.c:143)
10/21 18:04:04.580: [sbi] INFO: NF EndPoint(addr) setup [127.0.0.10:7777] (../subprojects/open5gs/lib/sbi/context.c:430)
10/21 18:04:04.580: [thread] DEBUG: [0x5e4a88ff5e30] thread started (../subprojects/open5gs/lib/core/ogs-thread.c:104)
10/21 18:04:04.580: [thread] DEBUG: [0x5e4a88ff5e30] worker signal (../subprojects/open5gs/lib/core/ogs-thread.c:66)
10/21 18:04:04.580: [mb-smf-service-consumer] DEBUG: Processing event 0x7afa9fbbae08 [ENTRY] (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:55)
10/21 18:04:04.580: [mbs-service-tool] DEBUG: Processing event 0x7afa9fbbae08 [ENTRY] (../tools/c/mbs-service-tool/app-sm.c:97)
10/21 18:04:04.580: [mbs-service-tool] INFO: Requesting MBS Session... (../tools/c/mbs-service-tool/app-sm.c:101)
10/21 18:04:04.580: [core] ERROR: Unknown Event[1506] (../subprojects/open5gs/lib/proto/event.c:72)
10/21 18:04:04.580: [mb-smf-service-consumer] DEBUG: Processing event 0x7afa98000bd0 [UNKNOWN_EVENT] (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:55)
10/21 18:04:04.580: [mbs-service-tool] DEBUG: Processing event 0x7afa98000bd0 [APP_LOCAL_EVENT_MBS_SESSION_CREATE] (../tools/c/mbs-service-tool/app-sm.c:97)
10/21 18:04:04.580: [mbs-service-tool] DEBUG: app_mbs_session_create (../tools/c/mbs-service-tool/app-sm.c:415)
10/21 18:04:04.580: [mbs-service-tool] DEBUG: app_mbs_session_create: resolving SSM (../tools/c/mbs-service-tool/app-sm.c:427)
10/21 18:04:04.580: [mb-smf-service-consumer] DEBUG: Pushing changes for MbsSession [0x7afa98000ec0 (0x7afa98000ed0)] (../lib/mb-smf-service-consumer/mbs-session.c:239)
10/21 18:04:04.580: [mb-smf-service-consumer] DEBUG: New MbsSession (../lib/mb-smf-service-consumer/mbs-session.c:251)
10/21 18:04:04.580: [mb-smf-service-consumer] DEBUG: Send create for MbsSession [0x7afa98000ec0 (0x7afa98000ed0)] (../lib/mb-smf-service-consumer/mbs-session.c:441)
10/21 18:04:04.580: [sock] DEBUG: socket create(2:1:6) (../subprojects/open5gs/lib/core/ogs-socket.c:97)
10/21 18:04:04.580: [sock] DEBUG: Turn on TCP_NODELAY (../subprojects/open5gs/lib/core/ogs-sockopt.c:139)
10/21 18:04:04.580: [sock] DEBUG: Turn on SO_REUSEADDR (../subprojects/open5gs/lib/core/ogs-sockopt.c:120)
10/21 18:04:04.580: [sock] DEBUG: socket bind 0.0.0.0:0 (../subprojects/open5gs/lib/core/ogs-socket.c:122)
10/21 18:04:04.580: [sock] DEBUG: tcp_server() [0.0.0.0]:0 (../subprojects/open5gs/lib/core/ogs-tcp.c:60)
10/21 18:04:04.580: [sbi] INFO: nghttp2_server() [http://0.0.0.0]:0 (../subprojects/open5gs/lib/sbi/nghttp2-server.c:424)
10/21 18:04:04.580: [mb-smf-service-consumer] INFO: Ephemeral notification server() [http://0.0.0.0]:44431 (../lib/mb-smf-service-consumer/nmbsmf-mbs-session-build.c:366)
10/21 18:04:04.580: [mb-smf-service-consumer] DEBUG: CreateReqData: {"mbsSession":{"mbsSessionId":{"ssm":{"sourceIpAddr":{"ipv4Addr":"192.168.0.1"},"destIpAddr":{"ipv4Addr":"232.0.0.59"}}},"tmgiAllocReq":true,"serviceType":"MULTICAST","ingressTunAddrReq":true,"ssm":{"sourceIpAddr":{"ipv4Addr":"192.168.0.1"},"destIpAddr":{"ipv4Addr":"232.0.0.59"}},"mbsSessionSubsc":{"eventList":[{"eventType":"MBS_REL_TMGI_EXPIRY"},{"eventType":"BROADCAST_DELIVERY_STATUS"},{"eventType":"INGRESS_TUNNEL_ADD_CHANGE"}],"notifyUri":"http://0.0.0.0:44431/mbs-session-notify/v1/notification","nfcInstanceId":"91143286-ae97-41f0-b9c4-1dafec2dcc2b"},"activityStatus":"ACTIVE","anyUeInd":true}} (../lib/mb-smf-service-consumer/nmbsmf-mbs-session-build.c:146)
10/21 18:04:04.580: [sbi] WARNING: Try to discover [nmbsmf-mbssession] (../subprojects/open5gs/lib/sbi/path.c:548)
10/21 18:04:04.581: [mb-smf-service-consumer] DEBUG: Processing event 0x7afa980033b0 [OGS_EVENT_NAME_SBI_CLIENT] (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:55)
10/21 18:04:04.581: [mb-smf-service-consumer] DEBUG: Client response for session [0x7afa98000ec0 (0x7afa98000ed0)] (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:130)
10/21 18:04:04.581: [sbi] INFO: [90a40650-ae97-41f0-b6a2-f9727743397a] (NRF-discover) NF registered [type:NULL] (../subprojects/open5gs/lib/sbi/nnrf-handler.c:1256)
10/21 18:04:04.581: [sock] DEBUG: addr:127.0.0.4, port:80 (../subprojects/open5gs/lib/core/ogs-sockaddr.c:143)
10/21 18:04:04.581: [sock] DEBUG: addr:127.0.0.4, port:7777 (../subprojects/open5gs/lib/core/ogs-sockaddr.c:143)
10/21 18:04:04.581: [sbi] INFO: NF EndPoint(addr) setup [127.0.0.4:80] (../subprojects/open5gs/lib/sbi/context.c:2297)
10/21 18:04:04.581: [sbi] INFO: NF EndPoint(addr) setup [127.0.0.4:7777] (../subprojects/open5gs/lib/sbi/context.c:2034)
10/21 18:04:04.581: [sbi] INFO: [90a40650-ae97-41f0-b6a2-f9727743397a] (NF-discover) NF Profile updated [type:SMF validity:30s] (../subprojects/open5gs/lib/sbi/nnrf-handler.c:1301)
10/21 18:04:04.581: [sbi] INFO: [90a40650-ae97-41f0-b6a2-f9727743397a] NF Instance setup [type:SMF validity:30s] (../lib/mb-smf-service-consumer/nnrf-disc-handle.c:51)
10/21 18:04:04.583: [mb-smf-service-consumer] DEBUG: Processing event 0x7afa980033b0 [OGS_EVENT_NAME_SBI_CLIENT] (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:55)
10/21 18:04:04.583: [mb-smf-service-consumer] DEBUG: Client response for session [0x7afa98000ec0 (0x7afa98000ed0)] (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:130)
10/21 18:04:04.583: [mb-smf-service-consumer] DEBUG: Client response for Create MBS Session received (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:194)
10/21 18:04:04.583: [sock] DEBUG: addr:127.0.0.7, port:37259 (../subprojects/open5gs/lib/core/ogs-sockaddr.c:143)
10/21 18:04:04.583: [sock] DEBUG: addr:192.168.0.1, port:0 (../subprojects/open5gs/lib/core/ogs-sockaddr.c:143)
10/21 18:04:04.583: [sock] DEBUG: addr:232.0.0.59, port:0 (../subprojects/open5gs/lib/core/ogs-sockaddr.c:143)
10/21 18:04:04.583: [mb-smf-service-consumer] DEBUG: Forwarding creation result to calling application (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:197)
10/21 18:04:04.583: [mb-smf-service-consumer] DEBUG: Pushing changes for MbsSession [0x7afa98000ec0 (0x7afa98000ed0)] (../lib/mb-smf-service-consumer/mbs-session.c:239)
10/21 18:04:04.583: [mb-smf-service-consumer] DEBUG: MbsSession [0x7afa98000ec0 (0x7afa98000ed0)] not changed (../lib/mb-smf-service-consumer/mbs-session.c:288)
10/21 18:04:04.583: [core] ERROR: Unknown Event[1506] (../subprojects/open5gs/lib/proto/event.c:72)
10/21 18:04:04.583: [mb-smf-service-consumer] DEBUG: Processing event 0x7afa98009750 [UNKNOWN_EVENT] (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:55)
10/21 18:04:04.583: [mbs-service-tool] DEBUG: Processing event 0x7afa98009750 [APP_LOCAL_EVENT_MBS_SESSION_CREATE_RESULT] (../tools/c/mbs-service-tool/app-sm.c:97)
10/21 18:04:04.583: [mbs-service-tool] INFO: MBS Session 1 [0x7afa98000ed0] created (../tools/c/mbs-service-tool/app-sm.c:118)
10/21 18:04:04.583: [mbs-service-tool] INFO:   TMGI = EA7DDD (PLMN = 000000) (../tools/c/mbs-service-tool/app-sm.c:124)
10/21 18:04:04.583: [mbs-service-tool] INFO:   UDP Tunnel = 127.0.0.7:37259 (../tools/c/mbs-service-tool/app-sm.c:135)
10/21 18:04:04.583: [mb-smf-service-consumer] DEBUG: Processing event 0x7afa98009750 [EXIT] (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:55)
10/21 18:04:04.583: [mbs-service-tool] DEBUG: Processing event 0x7afa98009750 [EXIT] (../tools/c/mbs-service-tool/app-sm.c:97)
10/21 18:04:04.583: [mb-smf-service-consumer] DEBUG: Processing event 0x7afa98009750 [ENTRY] (../lib/mb-smf-service-consumer/mb-smf-service-consumer.c:55)
10/21 18:04:04.583: [mbs-service-tool] DEBUG: Processing event 0x7afa98009750 [ENTRY] (../tools/c/mbs-service-tool/app-sm.c:185)
10/21 18:04:04.583: [mbs-service-tool] INFO: Awaiting notifications... (../tools/c/mbs-service-tool/app-sm.c:189)
```

To get the full command help for the MBS Service tool use the command:

```
/usr/local/bin/mbs-service-tool -h
```
