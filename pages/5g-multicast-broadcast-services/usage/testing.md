# Testing

This section explains how to use the Python tests present on the `test` directory.

The Python modules requirements are preinstalled on the AF container image. This container mounts the `test` directory as readonly to be able to run the tests.

To run the tests, execute an interactive session with the AF container and navigate to the test directory:
```bash
docker exec -it af bash

# inside the AF container
cd test

# to run the tests
python3 tests.py
```

The `test` directory contains the following subdirectories:
- `MB_SMF` the developed tests regarding the MB-SMF Network Function
- `utils` a Python package containing some common utils for the tests
- `support` some support files for the tests like JSON files for the requests and JSON schemas to validate them

Using the `config.toml` file some parameters can be configured:
- the log_level for the tests can be adjusted. The values supported are: DEBUG, INFO, WARNING, ERROR, CRITICAL
- some endpoint parameters like the MB-SMF address, the protocol (HTTP or HTTPS) and the port being used

The file `tests.py` contains the main logic for the tests. In this file the test suites are defined and run by the unittest testing framework.

# Detailed Instructions

## Inspect all the traffic being sent in the network

You can use tcpdump/Wireshark to sniff all the messages being sent between the Network Functions by inspecting the `br-ogs` network bridge. This bridge is created by the Docker Compose network and is used to connect all the Network Functions.

```bash
$ tcpdump -i br-ogs
```

## Connect to the AF container to start sending requests to the Network Functions

The AF container is not Open5GS related, in fact, it is not even an AF, it is just a container called AF being used to send curl requests to the Open5GS APIs.

```bash
# Connect to the AF container
docker exec -it af bash
```

Use curl inside the container to send requests to the other Network Functions:

```bash
# Inside the AF container, example of the AF sending the MB-SMF the TMGI allocate request
curl --http2-prior-knowledge \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{ "tmgiNumber": 1 }' \
  mb-smf.open5gs.org:80/nmbsmf-tmgi/v1/tmgi
```

## Configure the MB-UPF multicast

Apart from editing the `.env` for the MB-UPF to be reachable by external gNBs, the MB-UPF needs extra configuration. To be able to forward the multicast traffic to the lower layer source specific multicast (LLSSM) address, the MB-UPF needs to udpate the multicast forwarding cache (MFC) in the linux kernel.

For this purpose, the `smcroute` tool is installed on the MB-UPF container. Through the `smcroutectl` command, the MFC can be updated to the desired values. Currently this is done manually but other ways to update the MFC are being studied.

```bash
# Execute this command inside the MB-UPF container
smcroutectl add eth0 <n6mb_multicast_destination_address> ogstun
```

After this, and after creating the MBS Session, the MVP can be tested by using the AF to send multicast traffic to the MB-UPF and inspecting the MB-UPF output:
```bash
# Execute this command inside the AF container
sendip -p ipv4 -is <af_container_ip> -id <n6mb_multicast_destination_address> <mb_upf_container_ip>
```

### Full example

Create a Broadcast MBS Session using TMGI as identifier but specifying also the SSM address, this SSM will be the address that the AF will use to send the multicast traffic to the MB-UPF through the N6mb interface.

```bash
# MBS Session Create request with TMGI allocate: /nmbsmf-mbssession/v1/mbs-sessions with multicast source
curl --http2-prior-knowledge \
  --request POST \
  --header "Content-Type: application/json" \
  --data '{ "mbsSession": { "ssm": { "sourceIpAddr": { "ipv4Addr": "10.33.33.3" }, "destIpAddr": { "ipv4Addr": "239.0.0.20" } },"tmgiAllocReq": true, "serviceType":"BROADCAST" } }' \
  mb-smf.open5gs.org:80/nmbsmf-mbssession/v1/mbs-sessions
```

The AF with IP address 10.33.33.3 will send an IP packet to the multicast destination 239.0.0.20. The MB-UPF will receive the traffic being sent to this multicast group and then forward it to the LLSSM.

For this, we will configure the MB-UPF like this:
```bash
# Execute this command inside the MB-UPF container
smcroutectl add eth0 239.0.0.20 ogstun
```

This command will update the MFC of the MB-UPF to receive the traffic for the multicast group 239.0.0.20 and forward it internally using the `ogstun` interface.

After all of this is configured, the MB-UPF has been configured through PFCP to forward the traffic received to the LLSSM. The LLSSM is uses the multicast destination address `239.0.0.4` and C-TEID `33`.

Now, sending traffic with the AF to the MB-UPF with the addresses configured causes the MB-UPF to forward the traffic using GTPU to the LLSSM:

> [!TIP]
> Check AF container IP executing `ip address` from the AF container and use the `eth0` interface address as <af_container_ip>

```bash
# To send traffic from the AF to the MB-UPF
sendip -p ipv4 -is <af_container_ip> -id 239.0.0.20 mb-upf.open5gs.org
```
