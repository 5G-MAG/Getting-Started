---
layout: default
title:  Docker implementation
parent: Tutorials
grand_parent: 5G Multicast Broadcast Services
has_children: false
nav_order: 3
---

# Docker Implementation
Here you will find an easy way to try the current 5G-MBS MVP being developed by the [iTEAM Mobile Communications Group](https://github.com/iTEAM-MCG) as part of the [5G-MAG](https://github.com/5G-MAG), following the 3GPP Release 17 specifications.

This implementation is being developed on top of the [Open5GS](https://github.com/open5gs/open5gs) 5G Core. The repository containing the source code can be found [here](https://github.com/5G-MAG/open5gs/tree/upv-mbs).

This playground uses Docker Compose to deploy a 5G-MBS capable 5G Core using Docker images present in a container repository.

## 5G-MBS architecture using Open5GS

![5G-MBS architecture using Open5GS](docs/images/5G-MBS_5G_Core.png)

> [!NOTE]
> Ports `TCP 27017`, `SCTP 38412` and `UDP 2152` are being exposed to the host running this Docker Compose deployment

These ports are being used for the following:
- `TCP 27017` to add subscribers to the MongoDB database
- `SCTP 38412` from the AMF for the NGAP `N2 interface`, used for the control plane connection with the external gNB
- `UDP 2152` from the MB-UPF for the GTPU `N3mb interface`, used for the data plane connection with the external gNB

> [!NOTE]
> Modify the `.env` file present on this repository to change the values being deployed on `docker-compose.yaml`

Add your host's IP address to the `DOCKER_HOST_IP` variable in the `.env` file for the MB-UPF to be reachable by external gNBs.

## Basic usage

<details>
<summary>Build it</summary>

> Note: This method uses the `docker-bake.hcl` file and requires `docker-buildx-plugin`

From the top level directory of the repository run:
```bash
docker buildx bake
```

This builds the AF, MB-SMF and MB-UPF images locally.

</details>

<details>
<summary>Deploy it</summary>
To download the rest of the Docker images from the repository and start everything:

```bash
docker compose up -d
```

To stop everything:

```bash
docker compose down
```

</details>

## Find more information

- `docs` has extra documentation regarding the project
  - [docs/Overview](docs/Overview.md) to see the current status and features of the project
  - [docs/Detailed Instructions](docs/Detailed-Instructions.md) to see how to manage the containers
  - [docs/Tests](docs/Tests.md) to see how to use the tests present in the `test` directory
- `configs` to check/modify the Network Function configuration files of the deployment
- `images` where the Network Function Dockerfiles are present
- `test` testing suite being developed in Python to test the features present
