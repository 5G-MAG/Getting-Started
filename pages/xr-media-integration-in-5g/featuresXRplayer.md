---
layout: default
title:  XR Player Features
parent: XR Media Integration in 5G
has_children: false
nav_order: 1
---

## XR Unity Player v1.0.0 features

* Adds **support for augmented reality scenes** using the `MPEG_anchor` glTF extensions which enables anchoring nodes and scenes to real world features. Anchored nodes are composited with the runtime device's camera stream. The implementation currently targets Mobile XR scenarios on Android devices such as smartphones, leveraging Google's ARCore API. 

* Adds a basic player configuration file to list multiple glTF documents, and a simple menu to load/unload and switch between scenes.

[View Changelog](https://github.com/5G-MAG/rt-xr-unity-player/releases)


### Anchoring

Supports augmented reality scenes using the `MPEG_anchor` glTF extensions which enables anchoring nodes and scenes to **Trackable** real world features. 

The implementation targets Android devices, anchored nodes are composited with the runtime device's camera stream. 

| Trackable type | Status | Test content |
|:---------------|:-------|:-------------|
| TRACKABLE_VIEWER | &#x2611; | [anchoring/anchorTest_viewer_n.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/anchoring/) |
| TRACKABLE_FLOOR | &#x2611; | [awards/scene_floor_anchoring.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/awards/) |
| TRACKABLE_PLANE | &#x2611; | [awards/scene_plane_anchoring.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/awards/) |
| TRACKABLE_CONTROLLER | &#x2610; | [anchoring/anchorTest_ctrl_n.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/anchoring/) |
| TRACKABLE_MARKER_2D | &#x2611; | [anchoring/anchorTest_m2D_n.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/anchoring/) |
| TRACKABLE_MARKER_3D | &#x2610; | [anchoring/anchorTest_m3D_n.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/anchoring/) |
| TRACKABLE_MARKER_GEO | &#x2611; | [anchoring/anchorTest_geoSpatial_n_cs.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/anchoring/) |
| TRACKABLE_APPLICATION | &#x2611; | [anchoring/anchorTest_app_n.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/anchoring/) |


### Interactivity

Supports specifying interactive **behaviors** to gltf documents through the `MPEG_scene_interactivity` and `MPEG_node_interactivity` extensions. 

An interactivity behavior combines one or more **triggers** that condition the execution one or more **actions**.

The table below provide an overview of the supported triggers and actions:

| Trigger type          | Status | Test content |
|:----------------------|:-|:-|
| TRIGGER_COLLISION     |&#x2611;|[gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/gravity)|
| TRIGGER_PROXIMITY     |&#x2611;|[gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/gravity), [geometry/UseCase_03-variant1-geometry.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/geometry)|
| TRIGGER_USER_INPUT    |&#x2611;|[gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/gravity), [geometry/UseCase_03-variant3-geometry.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/geometry)|
| TRIGGER_VISIBILITY    |&#x2611;|[geometry/UseCase_03-variant3-geometry.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/geometry)|

| Action type           | Status | Test content |
|:--------------------- |:-|:-|
| ACTION_ACTIVATE       |&#x2611;|[gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/gravity)|
| ACTION_TRANSFORM      |&#x2611;|[gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/gravity)|
| ACTION_BLOCK          |&#x2611;|[gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/gravity)|
| ACTION_ANIMATION      |&#x2611;|[geometry/UseCase_03-variant1-geometry.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/geometry)|
| ACTION_SET_MATERIAL   |&#x2611;|[gravity/gravity.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/gravity)|
| ACTION_MANIPULATE     |&#x2611;| |
| ACTION_MEDIA          |&#x2610;|[geometry/UseCase_02-variant3-geometry.gltf](https://github.com/5G-MAG/rt-xr-content/tree/development/geometry)|
| ACTION_HAPTIC         |&#x2610;| |
| ACTION_SET_AVATAR     |&#x2610;| |



### Media pipelines

{: .highlight }
Android support is planned in [#54](https://github.com/5G-MAG/rt-xr-unity-player/issues/54).

Support for media sources (eg. mp4, dash, rtp, ...) exposing media buffers to the presentation engine through the `MPEG_media`, `MPEG_accessor_timer`, `MPEG_buffer_circular` glTF extensions.

Media buffers expose decoded data not limited to video texture or audio sources.

[Sample scene with media pipelines](https://github.com/5G-MAG/rt-xr-content/tree/development/studio_apartment)


### Video texture

{: .highlight }
Android support is planned in [#54](https://github.com/5G-MAG/rt-xr-unity-player/issues/54).

Supports video textures buffers through the `MPEG_texture_video` glTF video extension is supported on Windows as of `v0.9.0`, Android support is planned for `v1.1.0`.

[Sample scene with video texture](https://github.com/5G-MAG/rt-xr-content/tree/development/studio_apartment)


### Spatial audio

{: .highlight }
Android support is planned in [#54](https://github.com/5G-MAG/rt-xr-unity-player/issues/54).

Supports audio sources positionned in 3D through the `MPEG_audio_spatial` glTF extension is supported on Windows as of `v0.9.0`, Android support is planned for `v1.1.0`.

For each audio source the extension specifies attenuation parameters controling the audio source loudness as a function of the viewer's distance.

[Sample scene with spatial audio source](https://github.com/5G-MAG/rt-xr-content/tree/development/studio_apartment)

### Overview of the MPEG extensions to glTF format implemented in v1.0.0

Note that "Unity player" refers to the compiled application, while "Unity editor" refers to the development environment which also allows running the app without actually compiling it for the target platform.

| glTF extension               | Unity player   | Unity editor   |
|:-----------------------------|:---------------|:---------------|
|                              | *Android*      |                |
| MPEG_media                   | &#x2610;       | &#x2611;       |
| MPEG_buffer_circular         | &#x2610;       | &#x2611;       |
| MPEG_accessor_timed          | &#x2610;       | &#x2611;       |
| MPEG_audio_spatial           | &#x2610;       | &#x2611;       |
| MPEG_texture_video           | &#x2610;       | &#x2611;       |
| MPEG_scene_interactivity     | &#x2611;       | &#x2611;       |
| MPEG_node_interactivity      | &#x2611;       | &#x2611;       |
| MPEG_node_interactivity.type | &#x2611;       | &#x2611;       |
| MPEG_anchor                  | &#x2611;       | &#x2610;       |
| MPEG_sampler_YCbCr           | &#x2610;       | &#x2610;       |
| MPEG_primitive_V3C           | &#x2610;       | &#x2610;       |
| MPEG_node_avatar             | &#x2610;       | &#x2610;       |
| MPEG_lights_texture_based    | &#x2610;       | &#x2610;       |
| MPEG_light_punctual          | &#x2610;       | &#x2610;       |
| MPEG_haptic                  | &#x2610;       | &#x2610;       |
| MPEG_mesh_linking            | &#x2610;       | &#x2610;       |
| MPEG_scene_dynamic           | &#x2610;       | &#x2610;       |
| MPEG_viewport_recommended    | &#x2610;       | &#x2610;       |
| MPEG_animation_timing        | &#x2610;       | &#x2610;       |

