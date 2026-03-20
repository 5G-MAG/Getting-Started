---
layout: default
title: Repositories
parent: 6G Testbed - AI Traffic
has_children: false
nav_order: 0
---

<img src="../../assets/images/Banner_6GTestbedAITraffic.png" /> 

[Scope](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](../releases.html){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-tutorial } [Requirements](./requirements.html){: .btn .btn-blue }

# Scope

This project hosts an open-source testbed for AI/media traffic evaluation targeting 5G, 6G, and realistic UE-observed network conditions. It supports 3GPP SA4 studies and broader media delivery evaluations and may be extended and used for other purposes.

# What is being implemented? 

{: .inshort }
A testbed for 6G AI Traffic Characterization able to: Measure traffic characteristics of generative AI services (LLMs, image/video generation); Analyze agentic AI patterns such as multi-step tool calling and tool server workflows; Evaluate QoE under emulated network conditions like latency, loss, and bandwidth.

## Network emulator
The emulator supports one-way delay, jitter, loss, bandwidth shaping, and advanced netem controls (correlation, distributions, loss models, reordering, duplication, corruption, and queue limits). It can combine Hierarchical Token Bucket (HTB) rate limiting with netem impairments and is controlled via YAML profiles.

### Architecture
The network emulator is built on Linux Traffic Control (tc) with netem qdisc, providing precise control over network characteristics. Network conditions are applied at the interface level, enabling transparent emulation for any media delivery protocol without requiring modifications to the client or server implementations.

The emulator provides pre-defined network profiles derived from 3GPP 5QI specifications.

Beyond basic delay and loss parameters, the emulator supports advanced netem controls for more realistic network modeling.

The emulator supports multiple deployment configurations. 

## AI Traffic characterization testbed
The testbed provides an end-to-end framework to run scenarios, emulate network conditions, and log metrics in a reproducible manner.

Key capabilities include orchestration of scenarios, provider adapters for different commercial and self-hosted models, L3/L4 capture (tcpdump), optional L7 capture (mitmproxy), and SQLite-based logging for large-scale analysis.

### Architecture and code structure
The testbed architecture is orchestrator-centric with clear separation of scenarios, clients, network emulation, capture, and analysis:
-	orchestrator.py coordinates scenario runs, applies network profiles, handles retries, and generates reports.
-	scenarios/* implement traffic patterns (chat, agent, direct search, realtime, multimodal, image, video, computer use).
-	clients/* provide provider adapters, including OpenAI, Gemini, DeepSeek (OpenAI-compatible), and vLLM for self-hosted models.
-	netem: external dependency on the network emulator module that is proposed to be common to all studies [1].
-	capture/* provides L3/L4 pcap capture and L7 capture via mitmproxy.
-	analysis/* logs to SQLite, computes 3GPP-aligned metrics, and generates plots.

The testbed is designed to be easily usable and highly configurable.
New scenarios can be added by creating a class in scenarios/ that extends BaseScenario, registering it in scenarios/init.py, and adding a YAML entry in configs/scenarios.yaml.
New providers can be added by implementing a client in clients/ that subclasses LLMClient and registering it in the orchestrator client factory.
The testbed includes a vLLM client (clients/vllm_client.py) and example scenarios in configs/scenarios.yaml (e.g., chat_vllm). This enables evaluation of self-hosted models via the OpenAI-compatible API provided by vLLM, supporting the same metrics and logging pipeline as hosted providers.
