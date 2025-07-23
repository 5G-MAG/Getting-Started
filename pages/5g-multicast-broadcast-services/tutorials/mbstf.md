---
layout: default
title: Initial MBS Transport Function API examples
parent: Tutorials
grand_parent: 5G Multicast Broadcast (MBS)
has_children: false
nav_order: 2
---

# Initial MBS Transport Function API examples

This tutorial showcases the current features present in the 5G-MAG MBSTF implementation. You can check out the videos to
see more details or follow the write-up tutorial.

## Tutorial videos

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSc6fcO6cvo?si=4-uf_4Cn6i1J9Cs6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Architecture

```mermaid
---
title: "MBSTF and associated 5G NFs"
config:
  block:
    padding: 12
    useMaxWidth: true
---
block-beta
  columns 9
  block:g1:7
    columns 7
    space:3 text1["5MBS reference points"] space:3
    space:4 NEF["NEF"]:3
    space:7
    AMF["AMF"] space SMF["SMF"] space MBSMF["MB-SMF"] space MBSF["MBSF"]
    space:7
    RAN["NG-RAN"] space UPF["UPF"] space MBUPF["MB-UPF"] space MBSTF["MBSTF"]
    invis1((" ")) space:3 invis2((" ")) space:2
  end
  space AP["AP\nAF/AS"]

  NEF-- "N29mb" ---MBSMF
  NEF-- "Nmb5" ---MBSF
  MBSF-- "Nmb1" ---MBSMF
  MBSMF-- "N16mb" ---SMF
  MBSF-- "Nmb2" ---MBSTF
  MBSMF-- "N4mb" ---MBUPF
  MBSTF-- "Nmb9" ---MBUPF
  MBUPF-- "N19mb" ---UPF
  SMF-- "N4" ---UPF
  SMF-- "N11" ---AMF
  UPF-- "N3" ---RAN
  AMF-- "N2" ---RAN
  MBUPF---invis2
  invis2-- "N3mb" ---invis1
  invis1---RAN
  AP-- "N33" ---NEF
  AP-- "Nmb10" ---MBSF
  AP-- "Nmb8" ---MBSTF

  style invis1 fill:#0000,stroke:#0000,color:#0000
  style invis2 fill:#0000,stroke:#0000,color:#0000
  style text1 fill:#0000,stroke:#0000
```

## Prerequisites

This tutorial assumes that you have cloned and built the [rt-mbs-transport-function repository](https://github.com/5G-MAG/rt-mbs-transport-function).

## Description

In this tutorial we will configure the MBSTF with a variety of MBS Distribution Session types. This tutorial will also cover optional integration with the MB-SMF and MB-UPF.

You should follow the build instructions for the [rt-mbs-transport-function repository](https://github.com/5G-MAG/rt-mbs-transport-function) found in the README.md on the repository main page.

For these examples you will also need Wireshark, to view the results, and either build the 5G-MAG version of Open5GS with UDP tunnelling or the install the *netcat* package to fake an MB-UPF UDP tunnel.

---

### Step 1a: (Optional) Create an MBS Session on the MB-UPF with UDP tunnel

This is the first option for creating a UDP tunnel for multicast distribution. This implements the following highlighted steps from creating an MBS User Service.

```mermaid
---
title: "MBS User Service Creation: MBS Session creation on the MB-SMF"
config:
  sequence:
    showSequenceNumbers: true
---
sequenceDiagram
  participant MBUPF as MB-UPF
  participant MBSMF as MB-SMF
  participant MBSF
  participant AP as AF/AS

  activate MBSMF
  activate MBUPF
  activate MBSF

  AP->>MBSF : Create MBS User Service
  MBSF-->>AP : MBS User Service created
  AP->>MBSF : Add MBS User Data Ingest<br/>Session to MBS User Service
  rect rgb(160, 255, 160)
    MBSF->>MBSMF : Add MBS Session and request tunnel
    MBSMF->>MBUPF : Set up Multicast/Broadcast service and<br/>create an ingress tunnel
    MBUPF-->>MBSMF : MBS created and tunnel details
    MBSMF-->>MBSF : MBS Session created and tunnel details
  end

  deactivate MBSF
  deactivate MBSMF
  deactivate MBUPF
```
To use this you will need a 5G core with MB-UPF and MB-SMF that are capable of allocating ingress tunnels, such as the one found in the [5G-MAG/open5gs](https://github.com/5G-MAG/open5gs/tree/feature/mbs-udp-tunnel-creation) repository in the `feature/mbs-udp-tunnel-creation` branch.<!-- Change this to the 5mbs branch when tunnelling is merged -->

Start the NRF, SCP, AMF, MB-UPF and MB-SMF.
```sh
git clone --depth 1 --recurse-submodules -b feature/mbs-udp-tunnel-creation https://github.com/5G-MAG/open5gs.git ~/open5gs
cd ~/open5gs
meson setup --prefix=$PWD/install build
ninja -C build install
LD_LIBRARY_PATH="$PWD/install/lib64:$PWD/install/lib" export LD_LIBRARY_PATH
install/bin/open5gs-nrfd > nrf.log 2>&1 &
install/bin/open5gs-scpd > scp.log 2>&1 &
install/bin/open5gs-amfd > amf.log 2>&1 &
install/bin/open5gs-smfd > smf.log 2>&1 &
sudo -E install/bin/open5gs-upfd > upf.log 2>&1 &
```

Copy this Nmbsmf_MBSSession *CreateReqData* JSON object into a file called `create-mbs-session.json`:
```json
{
  "mbsSession": {
    "mbsSessionId": {
      "ssm": {
        "sourceIpAddr": {
          "ipv4Addr": "127.0.0.1"
        },
        "destIpAddr": {
          "ipv4Addr": "232.0.0.1"
        }
      }
    },
    "tmgiAllocReq": true,
    "serviceType": "MULTICAST",
    "ingressTunAddrReq": true,
    "activityStatus": "ACTIVE",
    "anyUeInd": true
  }
}
```

Then we send this file to the MB-SMF to request a new MBS session (sequence steps 4 to 7):
```sh
curl --http2-prior-knowledge -H 'Content-Type: application/json' --data @create-mbs-session.json http://127.0.0.4:7777/nmbsmf-mbssession/v1/mbs-sessions
```

The response will contain the UDP tunnel details at JSON path `.mbsSession.ingressTunAddr`. These will need to be substituted in the `.distSession.mbUpfTunAddr` object in the Distribution Session JSON objects in the following steps in order to direct the output to the MB-UPF.

---

### Step 1b: (Optional) Fake a UDP tunnel

This can be useful if you don't want to start up 5G core functions and just want to examine the multicast coming out of the MBSTF. This will simulate a UDP tunnel as would be provided by the MB-UPF.

For this we will need the `netcat` or `nc` command from the *netcat* package (*nmap-ncat* on RHEL based systems).

The command to create a tunnel at 127.0.0.7:5678 is:
```sh
nc -u -l 127.0.0.7 5678 > /dev/null &
```

---

### Step 2: Start the mock media express server

The MBSTF, when in *PULL* mode, requires an HTTP service to request the media objects from. For the purposes of these tutorials we
will use a simple HTTP server based on the NodeJS express module which has been configured to serve some simple media objects. This simulates a media server or CDN that would be provided by the Application Provider (AP).

To start the express mock media server you will need to do the following things.

1. Clone the rt-mbs-examples repository:
   ```bash
   cd ~
   git clone -b development https://github.com/5G-MAG/rt-mbs-examples.git
   ```

1. Prepare the express server for running:
   ```bash
   cd ~/rt-mbs-examples/express-mock-media-server
   npm install
   ```

1. Run the express server:
   ```bash
   cd ~/rt-mbs-examples/express-mock-media-server
   npm start
   ```

The mock media server is now running on TCP port 3004 and ready to serve objects for the following tutorial examples.

---

### Step 3: Run the MBSTF

If the build and install instructions from [rt-mbs-transport-function](https://github.com/5G-MAG/rt-mbs-transport-function) have been followed, then the MBSTF can be run using:
```bash
sudo /usr/local/bin/open5gs-mbstfd &
```

---

### Step 4: Start and configure Wireshark to capture the encapsulated FLUTE

1. Set up the packet decoding:
   - In the *Analyze* menu, select *Decode As...* to open the "Decode As..." dialog.
   - If a rule does not exist for UDP with a port number matching the UDP tunnel (the port number given for the first tunnel in the response in Step 1a or `5678` for Step 1b), then create a new rule, set the field to `UDP port`, set the port number to the tunnel port and set the Current decoding as `IPv4`.
   - If a rule does not exist for the UDP port `5000` (the port we will use for the multicast) then create a new rule for a "UDP port", set the port number to `5000` and the Current decoding to `ALC`.
   - Select the *Save* or *OK* button to close the dialog. Saving will store the rules for next time Wireshark is started.
   ![wireshark Decode As dialog example](../../../assets/images/5mbs/wireshark-decode-as-dialog.png)

2. Select (but don't start) the correct interface for capture. This will usually be the ethernet interface if you used Step 1a or the local loopback (lo) interface if you are using Step 1b.

3. Enter the filter expression if...:
   - You followed Step 1a, enter a filter of `host <tunnel-ip-address>`, where `<tunnel-ip-address>` is the IP address of the tunnel given in the response for 1a.
   - You followed Step 1b, enter a filter of `host 127.0.0.7`.

4. Then start the capture.

---

### Step 5: Create a single shot MBS Distribution Session for pull operation

This tests the SINGLE distribution mode for *PULL*ed content. This executes the following highlighted steps from MBS User Service
provisioning using the command line to perform the actions that the MBSF would otherwise perform.

```mermaid
---
title: "MBS User Service Creation: PULL Single Shot Distribution Session creation on the MBSTF"
config:
  themeCSS: |
    .loopLine { stroke-width: 4px; stroke-dasharray: 5,5; }
  sequence:
    showSequenceNumbers: true
---
sequenceDiagram
  participant RAN as NG-RAN
  participant MBUPF as MB-UPF
  participant MBSMF as MB-SMF
  participant MBSTF
  participant MBSF
  participant AP as AF/AS

  activate RAN
  activate MBSMF
  activate MBUPF
  activate MBSF
  activate MBSTF

  AP->>MBSF : Add MBS User Data Ingest<br/>Session to MBS User Service
  MBSF->>MBSMF : Add MBS Session and request tunnel
  MBSMF->>MBUPF : Set up Multicast/Broadcast service and<br/>create an ingress tunnel
  MBUPF-->>MBSMF : MBS created and tunnel details
  MBSMF-->>MBSF : MBS Session created and tunnel details
  rect rgb(160,255,160)
    MBSF->>MBSTF : Create Distribution Session<br/>using tunnel from MB-SMF
    MBSTF-->>MBSF : Distribution Session created<br/>include push service URL if requested
  end
    MBSF-->>AP : MBS User Data Session created<br/>include push service URL if requested
  rect rgb(160,255,160)
    MBSTF->>AP : Fetch object(s) described<br/>in Distribution Session
    AP-->>MBSTF : Response with object(s)
    MBSTF->>MBUPF : Package object(s) in multicast FLUTE session packets and send to tunnel at given rate
    MBUPF->>RAN : FLUTE packets forwarded<br/>via multicast GTP to RANs
  end

  deactivate MBSTF
  deactivate MBSF
  deactivate MBSMF
  deactivate MBUPF
  deactivate RAN
```

With the following processes running:
- express server from Step 2
- the MBSTF from Step 3
- Wireshark from step 4

...perform the following actions to test a single shot distribution from *PULL* requested media objects.

Copy the following into DistSession-PULL-request.json:
```json
{
    "distSession": {
        "distSessionId": "cab87e4b-01b1-4138-9018-7d30bcb1606b",
        "distSessionState": "ACTIVE",
        "mbUpfTunAddr": {
            "ipv4Addr": "127.0.0.7",
            "portNumber": 5678
        },
        "upTrafficFlowInfo": {
            "destIpAddr": { "ipv4Addr": "232.0.0.1" },
            "portNumber": 5000
        },
        "mbr": "10 Mbps",
        "objDistributionData": {
            "objDistributionOperatingMode": "SINGLE",
            "objAcquisitionMethod": "PULL",
            "objAcquisitionIdsPull": ["object1", "object2", "object3", "object4"],
            "objIngestBaseUrl": "http://127.0.0.1:3004/",
            "objDistributionBaseUrl": "http://127.0.0.2/"
        }
    }
}
```

If you are using the option to use a running MB-SMF/MB-UPF (Step 1a) then make the following changes to the JSON above:
- The tunnel IP address for `distSession.mbUpfTunAddr.ipv4Addr` from 127.0.0.7 to the IP address for the tunnel, which was returned in the MB-SMF response.
- The port number for `distSession.mbUpfTunAddr.portNumber` from 5678 to the port number for the tunnel, which was returned in the MB-SMF response.

Then push the *DistSession* to the MBSTF to configure it (sequence steps 6 and 7):

```bash
curl --http2-prior-knowledge -H 'Content-Type: application/json' --data-binary @DistSession-PULL-request.json http://127.0.0.62:7777/nmbstf-distsession/v1/dist-sessions
```

The result should look like:

```json
{
	"distSession":	{
		"distSessionId":	"cab87e4b-01b1-4138-9018-7d30bcb1606b",
		"distSessionState":	"ACTIVE",
		"objDistributionData":	{
			"objDistributionOperatingMode":	"SINGLE",
			"objAcquisitionMethod":	"PULL",
			"objAcquisitionIdsPull":	["object1", "object2", "object3", "object4"],
			"objIngestBaseUrl":	"http://127.0.0.1:3004/",
			"objDistributionBaseUrl":	"http://127.0.0.2/"
		}
	}
}
```

The wireshark capture will look like (sequence step 11):

![Wireshark capture showing the FDT (TOI 0) packet for the first object from the PULL SINGLE Distribution Session](../../../assets/images/5mbs/wireshark-object1-fdt.png)

This shows the FDT entry for the first object pulled from the express server. Examining the packet it can be noticed that:
1. There is an outer IP and UDP protocol headers showing the packet is sent from 127.0.0.1:58158 to 127.0.0.7:49484 &#x2780; because an MB-UPF was used for this example which presented its tunnel at 127.0.0.7:49484.
1. The next pair of IP and UDP headers show that this encapculated packet is from 127.0.0.1:5000 to multicast address 232.0.0.1:5000 &#x2781;, as requested in the DistributionSession creation request.
1. The packet contents are a FLUTE packet for "TSI: 0 TOI: 0" (from the packet summary &#x2782;) which indicates an FDT packet. The FDT contents show that it is currently sending a 39 byte file &#x2785; referenced as `TOI="1"` &#x2783; with a content location of "http://127.0.0.2/object1" &#x2784;. The "http://127.0.0.2" prefix is the one requested by the *objDistributionBaseUrl* field in the DistributionSession request, and has replaced the origin prefix of "http://127.0.0.1:3004" (*objIngestBaseUrl* field).
1. The next packet contains the GTP encapsulated version of this packet &#x2786;. That packet is being multicast to the RAN from the MB-UPF.

![Wireshark capture showing the FDT (TOI 0) packet for the first object from the PULL SINGLE Distribution Session](../../../assets/images/5mbs/wireshark-object1-file.png)

This screenshot shows the FLUTE packet for TOI 1, the *object1* media object itself.

---

### Step 6: Create a single shot MBS Distribution Session for push operation

This tests the SINGLE distribution mode for *PUSH*ed content. This executes the following highlighted steps from MBS User Service
provisioning using the command line to perform the actions that the MBSF and AP would otherwise perform.

```mermaid
---
title: "MBS User Service Creation: PUSH Single Shot Distribution Session creation on the MBSTF"
config:
  themeCSS: |
    .loopLine { stroke-width: 4px; stroke-dasharray: 5,5; }
  sequence:
    showSequenceNumbers: true
---
sequenceDiagram
  participant RAN as NG-RAN
  participant MBUPF as MB-UPF
  participant MBSMF as MB-SMF
  participant MBSTF
  participant MBSF
  participant AP as AF/AS

  activate RAN
  activate MBSMF
  activate MBUPF
  activate MBSF
  activate MBSTF

  AP->>MBSF : Add MBS User Data Ingest<br/>Session to MBS User Service
  MBSF->>MBSMF : Add MBS Session and request tunnel
  MBSMF->>MBUPF : Set up Multicast/Broadcast service and<br/>create an ingress tunnel
  MBUPF-->>MBSMF : MBS created and tunnel details
  MBSMF-->>MBSF : MBS Session created and tunnel details
  rect rgb(160, 255, 160)
    MBSF->>MBSTF : Create Distribution Session<br/>using tunnel from MB-SMF
    MBSTF-->>MBSF : Distribution Session created<br/>include push service URL if requested
  end
  MBSF-->>AP : MBS User Data Session created<br/>include push service URL if requested
  rect rgb(160, 255, 160)
    AP->>MBSTF : Push object for Distribution Session
    MBSTF-->>AP : Object received OK
    MBSTF->>MBUPF : Package object(s) in multicast FLUTE session packets and send to tunnel at given rate
    MBUPF->>RAN : FLUTE packets forwarded<br/>via multicast GTP to RANs
  end

  deactivate MBSTF
  deactivate MBSF
  deactivate MBSMF
  deactivate MBUPF
  deactivate RAN
```

With the following processes running:
- express server from Step 2
- the MBSTF from Step 3
- Wireshark from step 4

...perform the following actions to test a single shot distribution for *PUSH* delivered media objects.

Copy the following into DistSession-PUSH-request.json:
```json
{
    "distSession": {
        "distSessionId": "3e3dc3fb-0677-42a3-86c6-bc44e3544b0f",
        "distSessionState": "ACTIVE",
        "mbUpfTunAddr": {
            "ipv4Addr": "127.0.0.7",
            "portNumber": 5678
        },
        "upTrafficFlowInfo": {
            "destIpAddr": { "ipv4Addr": "232.0.0.1" },
            "portNumber": 5000
        },
        "mbr": "10 Mbps",
        "objDistributionData": {
            "objDistributionOperatingMode": "SINGLE",
            "objAcquisitionMethod": "PUSH",
            "objDistributionBaseUrl": "http://127.0.0.2/"
        }
    }
}
```

If you are using the option to use a running MB-SMF/MB-UPF (Step 1a) then make the following changes to the JSON above:
- The tunnel IP address for `distSession.mbUpfTunAddr.ipv4Addr` from 127.0.0.7 to the IP address for the tunnel, which was returned in the MB-SMF response.
- The port number for `distSession.mbUpfTunAddr.portNumber` from 5678 to the port number for the tunnel, which was returned in the MB-SMF response.

Then push the *DistSession* to the MBSTF to configure it (sequence steps 6 and 7):

```bash
curl --http2-prior-knowledge -H 'Content-Type: application/json' --data-binary @DistSession-PUSH-request.json http://127.0.0.62:7777/nmbstf-distsession/v1/dist-sessions
```

The result should look like:

```json
{
    "distSession": {
        "distSessionId": "3e3dc3fb-0677-42a3-86c6-bc44e3544b0f",
        "distSessionState": "ACTIVE",
        "objDistributionData": {
            "objDistributionOperatingMode": "SINGLE",
            "objAcquisitionMethod": "PUSH",
            "objIngestBaseUrl": "http://127.0.0.1:33945/",
            "objDistributionBaseUrl": "http://127.0.0.2/"
        }
    }
}
```

Take note of the *objAcquisitionBaseUrl* prefix URL for pushing the media objects to, e.g.:
```bash
push_prefix_url="http://127.0.0.1:33945/"
```

Then we can send objects to be packaged and sent via the multicast channel (sequence steps 9 and 10). For example to send the `meson.build` file from the rt-mbs-transport-function repository that was cloned earlier we perform an HTTP PUT of the file to a URL with the prefix we remembered earlier:
```bash
curl -H 'Content-Type: text/plain' -X PUT --data-binary @"${HOME}/rt-mbs-transport-function/meson.build" "${push_prefix_url}example/path/to/object.txt"
```

Once pushed, the object is packaged as FLUTE and sent to the UDP tunnel.

The wireshark capture will look something like (sequence step 11):

![Wireshark showing FDT packet for SINGLE PUSH distribution](../../../assets/images/5mbs/wireshark-push-single-fdt.png)

This shows the FDT for the pushed file. This is encapsulated in the same way as the PULL example in Step 5. The *Content-Location* field in the FDT File entry shows it using the *objDistributionBaseUrl* followed by the path that the object was `PUT` to following the *objIngestBaseUrl*.

The file packet will look something like:

![Wireshark showing first file object packet for SINGLE PUSH distribution](../../../assets/images/5mbs/wireshark-push-single-file.png)

This packet (packet number 9 in the above image), containing the first bytes of the `meson.build` file, is followed by the rest of the file in packet number 11.

---

### Step 7: Create a streaming MBS Distribution Session for pull operation on the DASH manifest

```mermaid
---
title: "MBS User Service Creation: PULL STREAMING Distribution Session creation on the MBSTF"
config:
  themeCSS: |
    .loopLine { stroke-width: 4px; stroke-dasharray: 5,5; }
  sequence:
    showSequenceNumbers: true
---
sequenceDiagram
  participant RAN as NG-RAN
  participant MBUPF as MB-UPF
  participant MBSMF as MB-SMF
  participant MBSTF
  participant MBSF
  participant AP as AF/AS

  activate RAN
  activate MBSMF
  activate MBUPF
  activate MBSF
  activate MBSTF

  AP->>MBSF : Add MBS User Data Ingest<br/>Session to MBS User Service
  MBSF->>MBSMF : Add MBS Session and request tunnel
  MBSMF->>MBUPF : Set up Multicast/Broadcast service and<br/>create an ingress tunnel
  MBUPF-->>MBSMF : MBS created and tunnel details
  MBSMF-->>MBSF : MBS Session created and tunnel details
  rect rgb(160, 255, 160)
    MBSF->>MBSTF : Create Distribution Session<br/>using tunnel from MB-SMF
    MBSTF-->>MBSF : Distribution Session created<br/>include push service URL if requested
  end
  MBSF-->>AP : MBS User Data Session created<br/>include push service URL if requested
  rect rgb(160, 255, 160)
    MBSTF->>AP : Pull DASH manifest
    AP-->>MBSTF : DASH manifest delivered
    MBSTF->>MBUPF : DASH manifest packaged in multicast FLUTE session packets and send to tunnel at given rate
    MBUPF->>RAN : FLUTE packets forwarded<br/>via multicast GTP to RANs
    loop For each initialization segment in the DASH manifest
      MBSTF->>AP : Pull Initialization Segment
      AP-->>MBSTF : Initialization Segment delivered
      MBSTF->>MBUPF : Initialization Segment packaged in multicast FLUTE session packets and send to tunnel at given rate
      MBUPF->>RAN : FLUTE packets forwarded<br/>via multicast GTP to RANs
    end
    par If the DASH manifest has a refresh period
      loop If the DASH manifest has a refresh period
        MBSTF->>MBSTF : Wait for the next MPD refresh time
        MBSTF->>AP : Pull DASH manifest
        AP-->>MBSTF : DASH manifest delivered
        MBSTF->>MBUPF : DASH manifest packaged in multicast FLUTE session packets and send to tunnel at given rate
        MBUPF->>RAN : FLUTE packets forwarded<br/>via multicast GTP to RANs
        loop For each initialization segment in the DASH manifest
          MBSTF->>AP : Pull Initialization Segment
          AP-->>MBSTF : Initialization Segment delivered
          MBSTF->>MBUPF : Initialization Segment packaged in multicast FLUTE session packets and send to tunnel at given rate
          MBUPF->>RAN : FLUTE packets forwarded<br/>via multicast GTP to RANs
        end
      end
    and For each Representation in the current period
      loop For each Media Segment in the Representation
        MBSTF->>MBSTF : Wait for the Media Segment to become available
        MBSTF->>AP : Pull Media Segment
        AP-->>MBSTF : Media Segment delivered
        MBSTF->>MBUPF : Media Segment packaged in multicast FLUTE session packets and send to tunnel at given rate
        MBUPF->>RAN : FLUTE packets forwarded<br/>via multicast GTP to RANs
      end
    end
  end

  deactivate MBSTF
  deactivate MBSF
  deactivate MBSMF
  deactivate MBUPF
  deactivate RAN
```

```json
{
    "distSession": {
        "distSessionId": "541ebbd2-ebf9-496b-a3b8-dcd1c17fbc9d",
        "distSessionState": "ACTIVE",
        "mbUpfTunAddr": {
            "ipv4Addr": "127.0.0.7",
            "portNumber": 5678
        },
        "upTrafficFlowInfo": {
            "destIpAddr": { "ipv4Addr": "232.0.0.1" },
            "portNumber": 5000
        },
        "mbr": "10 Mbps",
        "objDistributionData": {
            "objDistributionOperatingMode": "STREAMING",
            "objAcquisitionMethod": "PULL",
            "objIngestBaseUrl": "https://livesim2.dashif.org/livesim2/WAVE/vectors/cfhd_sets/12.5_25_50/t1/2022-10-17/",
            "objAcquisitionIdsPull": ["stream.mpd"],
            "objDistributionBaseUrl": "http://127.0.0.2/"
        }
    }
}
```

```json
{
    "distSession": {
        "distSessionId": "541ebbd2-ebf9-496b-a3b8-dcd1c17fbc9d",
        "distSessionState": "ACTIVE",
        "objDistributionData": {
            "objDistributionOperatingMode": "STREAMING",
            "objAcquisitionMethod": "PULL",
            "objAcquisitionIdsPull": [
                "stream.mpd"
            ],
            "objIngestBaseUrl": "https://livesim2.dashif.org/livesim2/WAVE/vectors/cfhd_sets/12.5_25_50/t1/2022-10-17/",
            "objDistributionBaseUrl": "http://127.0.0.2/"
        }
    }
}
```

![Wireshark screenshot showing the FDT with File entry for the MPD sent as part of a PULL STREAMING Distribution Session](../../../assets/images/5mbs/wireshark-pull-streaming-mpd-fdt.png)

![Wireshark screenshot showing the MPD file contents sent as part of a PULL STREAMING Distribution Session](../../../assets/images/5mbs/wireshark-pull-streaming-mpd-file.png)

![Wireshark screenshot showing the FDT with File entry for the initialization segment sent as part of a PULL STREAMING Distribution Session](../../../assets/images/5mbs/wireshark-pull-streaming-init-seg-fdt.png)

![Wireshark screenshot showing the initialization segment file contents sent as part of a PULL STREAMING Distribution Session](../../../assets/images/5mbs/wireshark-pull-streaming-init-seg-file.png)

![Wireshark screenshot showing the FDT with File entry for the first live media segment sent as part of a PULL STREAMING Distribution Session](../../../assets/images/5mbs/wireshark-pull-streaming-media-seg-fdt.png)

![Wireshark screenshot showing the FDT with File entry for the second live media segment sent as part of a PULL STREAMING Distribution Session](../../../assets/images/5mbs/wireshark-pull-streaming-media-seg2-fdt.png)

---

### Step 8: Create a streaming MBS Distribution Session for push operation on the DASH manifest

```mermaid
---
title: "MBS User Service Creation: PUSH STREAMING Distribution Session creation on the MBSTF"
config:
  themeCSS: |
    .loopLine { stroke-width: 4px; stroke-dasharray: 10,5; }
  sequence:
    showSequenceNumbers: true
---
sequenceDiagram
  participant RAN as NG-RAN
  participant MBUPF as MB-UPF
  participant MBSMF as MB-SMF
  participant MBSTF
  participant MBSF
  participant AP as AF/AS

  activate RAN
  activate MBSMF
  activate MBUPF
  activate MBSF
  activate MBSTF

  AP->>MBSF : Add MBS User Data Ingest<br/>Session to MBS User Service
  MBSF->>MBSMF : Add MBS Session and request tunnel
  MBSMF->>MBUPF : Set up Multicast/Broadcast service and<br/>create an ingress tunnel
  MBUPF-->>MBSMF : MBS created and tunnel details
  MBSMF-->>MBSF : MBS Session created and tunnel details
  rect rgb(160, 255, 160)
    MBSF->>MBSTF : Create Distribution Session<br/>using tunnel from MB-SMF
    MBSTF-->>MBSF : Distribution Session created<br/>include push service URL if requested
  end
  MBSF-->>AP : MBS User Data Session created<br/>include push service URL if requested
  rect rgb(160, 255, 160)
    AP->>MBSTF : DASH manifest pushed
    MBSTF-->>AP : DASH manifest received OK
    MBSTF->>MBUPF : DASH manifest packaged in multicast FLUTE session packets and send to tunnel at given rate
    MBUPF->>RAN : FLUTE packets forwarded<br/>via multicast GTP to RANs
    loop For each initialization segment in the DASH manifest
      MBSTF->>AP : Pull Initialization Segment
      AP-->>MBSTF : Initialization Segment delivered
      MBSTF->>MBUPF : Initialization Segment packaged in multicast FLUTE session packets and send to tunnel at given rate
      MBUPF->>RAN : FLUTE packets forwarded<br/>via multicast GTP to RANs
    end
    par For each Representation in the current period
      loop For each Media Segment in the Representation
        MBSTF->>MBSTF : Wait for the Media Segment to become available
        MBSTF->>AP : Pull Media Segment
        AP-->>MBSTF : Media Segment delivered
        MBSTF->>MBUPF : Media Segment packaged in multicast FLUTE session packets and send to tunnel at given rate
        MBUPF->>RAN : FLUTE packets forwarded<br/>via multicast GTP to RANs
      end
    end
  end

  deactivate MBSTF
  deactivate MBSF
  deactivate MBSMF
  deactivate MBUPF
  deactivate RAN
```

```json
{
    "distSession": {
        "distSessionId": "33acd99a-8564-42a1-a96c-9f293d90c41e",
        "distSessionState": "ACTIVE",
        "mbUpfTunAddr": {
            "ipv4Addr": "127.0.0.7",
            "portNumber": 5678
        },
        "upTrafficFlowInfo": {
            "destIpAddr": { "ipv4Addr": "232.0.0.1" },
            "portNumber": 5000
        },
        "mbr": "10 Mbps",
        "objDistributionData": {
            "objDistributionOperatingMode": "STREAMING",
            "objAcquisitionMethod": "PUSH",
            "objAcquisitionIdPush": "manifest.mpd",
            "objDistributionBaseUrl": "http://127.0.0.2/"
        }
    }
}
```
