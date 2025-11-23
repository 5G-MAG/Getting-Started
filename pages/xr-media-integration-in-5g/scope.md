---
layout: default
title: Scope & Architectures
parent: XR with MPEG-I SD
has_children: false
nav_order: 0
---

<img src="../../assets/images/Banner_XR.png" /> 

[Scope & Architectures](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [Features](./features.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](../releases.htmll#project-xr-media-with-mpeg-i-scene-description){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-blue } [Requirements](./requirements.html){: .btn .btn-blue }

# Scope and Architectures

This page contains information such as the specifications within the scope of the tools, high-level architectures that bring context to their applicability, features under implementation,...

## Technical Resources and Specifications

[Technical Resources](https://hub.5g-mag.com/Tech/pages/xr.html){: .btn .btn-blue } [Specifications](https://hub.5g-mag.com/Standards/pages/xr.html){: .btn .btn-blue }

# High-level architectures

## XR Media Integration in 5G

<img src="../../assets/images/projects/xr_diagram.png" style="width: 80%">

[XR Media with MPEG-I SD: Repositories](../xr-media-integration-in-5g/repositories.html){: .btn .btn-xr }
[Common Tools: Repositories](../common-tools/){: .btn .btn-common }

# XR Unity Player: Project overview

## Scene description format

The Scene Description format standardized by [ISO/IEC JTC 1/SC29/WG03](https://www.iso.org/committee/45316.html) MPEG Systems in [ISO/IEC 23090-14](https://www.iso.org/standard/86439.html) specifies a framework enabling the composition of 3D scenes for immersive experiences, anchoring 3D assets in the real world, facilitating rich interactivity, supporting real-time media delivery.

It establishes interfaces like the Media Access Function (MAF) API to enable cross-platform interoperability, ensuring efficient retrieval and processing of media data, by decoupling the Presentation Engine from media pipeline.

## XR Player implementation

<img src="./images/rt-xr-overview.jpg" style="width: 80%">

The XR Player is implemented as a Unity3D project: [rt-xr-unity-player](https://github.com/5G-MAG/rt-xr-unity-player).

The unity project builds on the following dependencies:
* [rt-xr-glTFast](https://github.com/5G-MAG/rt-xr-gITFast): parsing and instantiating of 3D scenes in Unity.
* [rt-xr-maf-native](https://github.com/5G-MAG/rt-xr-maf-native): a C++ Media Access Functions (MAF) API implementation, extensible with custom media pipeline plugins. 

### Test content

* [rt-xr-content](https://github.com/5G-MAG/rt-xr-content): test content implementing the scene description format.

See the [features page](../repositories/featuresXRplayer.md) for implementation status of the scene description format.

## MAF API & Media pipelines

The Media Access Functions (MAF) API is specified in ISO/IEC 23090-14:2023.

It's purpose is to decouple the presentation engine from media pipeline management, it allows the Presentation Engine to:
- pass View informations to the media pipelines (eg. to optimize fetching media )
- read media buffers updated by the media pipelines

The MAF API is protocol and codec agnostic, media can be fetched a remote URL.

### Media player implementation

#### MediaPlayer component 

The MediaPlayer component is part of the Presentation Engine layer:

<img src="./images/rt-xr-presentation-engine.jpg" style="width: 80%">

The MediaPlayer component uses the MAF API implemented by Media Pipelines:

<img src="./images/rt-xr-maf-implementation.jpg" style="width: 80%">

The XR Player uses a C++ implementation of the MAF API. It uses a factory / plugin pattern to allow development of media pipelines.

The mechanism by which a media pipeline is instantiated and buffers initialized, is out of the scope of ISO/IEC 23090-14.

For more on the MAF API implementation, review the [rt-xr-maf-native](https://github.com/5G-MAG/rt-xr-maf-native) repository.
