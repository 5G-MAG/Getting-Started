---
layout: default
title: Features
parent: XR with MPEG-I SD
has_children: false
nav_order: 2
---

<img src="../../assets/images/Banner_XR.png" /> 

[Scope & Architectures](./scope.html){: .btn .btn-blue } [Project Roadmap](./projects.html){: .btn .btn-blue } [Features](./features.html){: .btn .btn-blue } [GitHub Repos](./repositories.html){: .btn .btn-github } [Releases](../releases.htmll#project-xr-media-with-mpeg-i-scene-description){: .btn .btn-release } [Tutorials](./tutorials.html){: .btn .btn-blue } [Requirements](./requirements.html){: .btn .btn-blue }

# Features 

The **MPEG-I Scene Description** reference architecture and features are described in the Technical Resources. This page describes those implemented in the 5G-MAG Reference Tools.

[Technical Resources](../../../Tech/pages/xr.html){: .btn .btn-blue }

Check below the:
* [**Features implemented in the XR Unity Player**](#features-implemented-in-the-xr-unity-player)
* [**Features implemented in the XR Unity Editor**](mpeg-extensions-to-gltf-implemented-in-unity-player-and-unity-editor)

## Features implemented in the XR Unity Player

The XR Player takes 3D scenes in glTF format, supporting extensions that enable extended reality use cases. 
These extensions enable features such as XR anchoring, interactivity behaviors, and media pipelines.

- [View Changelog](https://github.com/5G-MAG/rt-xr-unity-player/releases)

### Media pipelines

Support for media sources (eg. mp4, dash, rtp, ...) exposing media buffers to the presentation engine through the <span style="color:#00B050; font-weight:bold;">MPEG_media</span>, <span style="color#00B050; font-weight:bold;">MPEG_accessor_timer</span>, <span style="color#00B050; font-weight:bold;">MPEG_buffer_circular</span> glTF extensions.

The media pipelines APIs are designed to fetch and decode timed media such as video textures, audio sources, geometry streams ...

| Reference scene       | XR Phone | XR HMD | Test content |
|:--------------------- |:-|:-|:-|
| Sample scene with media pipelines | &#x2611; | &#x2611; | [studio_apartment/studio_apartment.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/studio_apartment/studio_apartment.gltf)|

### Video texture

Supports video textures buffers through the <span style="color#0070C0; font-weight:bold;">MPEG_texture_video</span> glTF video extension. Video decoding is implemented by media pipelines.

| Reference scene       | XR Phone | XR HMD | Test content |
|:--------------------- |:-|:-|:-|
| Sample scene with video texture | &#x2611; | &#x2611; | [studio_apartment/studio_apartment.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/studio_apartment/studio_apartment.gltf)|


### Spatial audio

Supports audio sources positionned in 3D through the <span style="color##0070C0; font-weight:bold;">MPEG_audio_spatial</span>.

For each audio source the extension specifies attenuation parameters controling the audio source loudness as a function of the viewer's distance.

| Reference scene       | XR Phone | XR HMD | Test content |
|:--------------------- |:-|:-|:-|
| Sample scene with spatial audio source | &#x2611; | &#x2611; | [studio_apartment/studio_apartment.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/studio_apartment/studio_apartment.gltf)|

### Anchoring

The XR Player supports XR anchoring using the <span style="color:#7030A0; font-weight:bold;">MPEG_anchor</span> glTF extension which enables anchoring nodes and scenes to features (**Trackable**) tracked by the XR device. In augmented reality applications, anchored nodes are composited with the XR device's environment. 

The XR player leverages Unity's ARFoundation to support both handled mobile devices such as smartphones and head mounted devices (HMDs).

| Trackable type | XR Phone | XR HMD | Test content |
|:---------------|:---------|:-------------|:-------------|
| TRACKABLE_VIEWER | &#x2611; | &#x2611; | [anchoring/anchorTest_viewer_n.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/anchoring/) |
| TRACKABLE_FLOOR  | &#x2611; | &#x2610; | [awards/scene_floor_anchoring.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/awards/) |
| TRACKABLE_PLANE  | &#x2611; | &#x2611; | [awards/scene_plane_anchoring.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/awards/) |
| TRACKABLE_CONTROLLER | &#x2610; | &#x2611; | [anchoring/anchorTest_ctrl_n.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/anchoring/) |
| TRACKABLE_MARKER_2D | &#x2611; | &#x2610; | [anchoring/anchorTest_m2D_n.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/anchoring/) |
| TRACKABLE_MARKER_3D | &#x2610; | &#x2610; | [anchoring/anchorTest_m3D_n.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/anchoring/) |
| TRACKABLE_MARKER_GEO | &#x2611; | &#x2610; | [anchoring/anchorTest_geoSpatial_n_cs.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/anchoring/) |
| TRACKABLE_APPLICATION | &#x2611; | &#x2611; | [anchoring/anchorTest_app_n.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/anchoring/) |


### Interactivity

The XR Player supports specifying interactive **behaviors** in a 3D scene through the <span style="color:#7030A0; font-weight:bold;">MPEG_scene_interactivity</span> and <span style="color:#7030A0; font-weight:bold;">MPEG_node_interactivity</span> glTF extensions. 

An interactivity behavior combines one or more **triggers** that condition the execution of one or more **actions**.

The table below provide an overview of the supported triggers and actions:

| Trigger type | XR Phone | XR HMD | Test content |
|:----------------------|:-|:-|:-|
| TRIGGER_COLLISION     | &#x2611; | &#x2611; | [gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/gravity)|
| TRIGGER_PROXIMITY      | &#x2611; | &#x2611; |[gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/gravity), [geometry/UseCase_03-variant1-geometry.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/geometry)|
| TRIGGER_USER_INPUT     | &#x2611; | &#x2611; |[gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/gravity), [geometry/UseCase_03-variant3-geometry.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/geometry)|
| TRIGGER_VISIBILITY    | &#x2611; | &#x2611; |[geometry/UseCase_03-variant3-geometry.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/geometry)|

| Action type           | XR Phone | XR HMD | Test content |
|:--------------------- |:-|:-|:-|
| ACTION_ACTIVATE       | &#x2611; | &#x2611; | [gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/gravity)|
| ACTION_TRANSFORM      | &#x2611; | &#x2611; | [gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/gravity)|
| ACTION_BLOCK          | &#x2611; | &#x2611; | [gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/gravity)|
| ACTION_ANIMATION      | &#x2611; | &#x2611; | [geometry/UseCase_03-variant1-geometry.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/geometry)|
| ACTION_SET_MATERIAL   | &#x2611; | &#x2611; | [gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/main/gravity)|
| ACTION_MANIPULATE     | &#x2610; | &#x2610; |  |
| ACTION_MEDIA          | &#x2610; | &#x2610; | 🚧 [issues/19](https://github.com/5G-MAG/rt-xr-unity-player/issues/19) |
| ACTION_HAPTIC         | &#x2610; | &#x2610; |  |
| ACTION_SET_AVATAR     | &#x2610; | &#x2610; | [issues/203](https://github.com/5G-MAG/Getting-Started/issues/203) |

## MPEG extensions to glTF implemented in Unity Player and Unity Editor

Note that "Unity player" refers to the compiled application, while "Unity editor" refers to the development environment which also allows running the app without actually compiling it for the target platform.

| glTF extension                                                                     | Unity player   | Unity editor v1.1.0 |
|:-----------------------------------------------------------------------------------|:---------------|:--------------------|
| <span style="color:#00B050; font-weight:bold;">MPEG_media</span>                   | &#x2611;       | &#x2610;            |
| <span style="color:#00B050; font-weight:bold;">MPEG_buffer_circular</span>         | &#x2611;       | &#x2610;            |
| <span style="color:#00B050; font-weight:bold;">MPEG_accessor_timed</span>          | &#x2611;       | &#x2610;            |
| <span style="color:#0070C0; font-weight:bold;">MPEG_audio_spatial</span>           | &#x2611;       | &#x2610;            |
| <span style="color:#0070C0; font-weight:bold;">MPEG_texture_video</span>           | &#x2611;       | &#x2610;            |
| <span style="color:#7030A0; font-weight:bold;">MPEG_scene_interactivity</span>     | &#x2611;       | &#x2610;            |
| <span style="color:#7030A0; font-weight:bold;">MPEG_node_interactivity</span>      | &#x2611;       | &#x2610;            |
| <span style="color:#7030A0; font-weight:bold;">MPEG_node_interactivity.type</span> | &#x2611;       | &#x2610;            |
| <span style="color:#7030A0; font-weight:bold;">MPEG_anchor</span>                  | &#x2611;       | &#x2610;            |
| <span style="color:#0070C0; font-weight:bold;">MPEG_sampler_YCbCr</span>           | &#x2610;       | &#x2610;            |
| <span style="color:#0070C0; font-weight:bold;">MPEG_primitive_V3C</span>           | &#x2610;       | &#x2610;            |
| <span style="color:#7030A0; font-weight:bold;">MPEG_node_avatar</span>             | &#x2610;       | &#x2610;            |
| <span style="color:#7030A0; font-weight:bold;">MPEG_lights_texture_based</span>    | &#x2610;       | &#x2610;            |
| <span style="color:#7030A0; font-weight:bold;">MPEG_light_punctual</span>          | &#x2610;       | &#x2610;            |
| <span style="color:#7030A0; font-weight:bold;">MPEG_haptic</span>                  | &#x2610;       | &#x2610;            |
| <span style="color:#0070C0; font-weight:bold;">MPEG_mesh_linking</span>            | &#x2610;       | &#x2610;            |
| <span style="color:#0070C0; font-weight:bold;">MPEG_scene_dynamic</span>           | &#x2610;       | &#x2610;            |
| <span style="color:#0070C0; font-weight:bold;">MPEG_viewport_recommended</span>    | &#x2610;       | &#x2610;            |
| <span style="color:#0070C0; font-weight:bold;">MPEG_animation_timing</span>        | &#x2610;       | &#x2610;            |
