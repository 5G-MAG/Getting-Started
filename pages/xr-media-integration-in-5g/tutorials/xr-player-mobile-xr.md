---
layout: default
title: Mobile XR on Android tutorial
parent: Tutorials
grand_parent: XR Media Integration in 5G
has_children: false
nav_order: 1
---

# Mobile XR on Android

Mobile XR refers to augmented or mixed reality applications running on handheld devices such as smartphones.


## Compatible Android devices

By default, the project is compiled for Android 9.0 (API Level 28), targeting arm64 architexture.

This can be changed in Unity's *"Player settings"* panel, under the *"Settings for Android"* tab, in the *"Other settings"* section.

Mobile XR scenarios are currently supported on **Android** through the [Google ARCore](https://docs.unity3d.com/Packages/com.unity.xr.arcore@5.1/manual/index.html) plugin. Google maintains a [list of compatible XR devices](https://developers.google.com/ar/devices?hl=fr).


## Mobile XR features

`MPEG_anchor` gltf extensions enable mobile XR use cases by supporting anchoring 3D assets to real world poses tracked by the device.
Refer to the [XR anchor documentation](./xr-player-anchoring/) for details.

`MPEG_scene_interactivity` and `MPEG_node_interactivity` gltf extensions support defining interactivity behaviors of the 3D assets.
Refer to the [Scene interactivity documentation](./xr-player-anchoring/) for details.


## Build the player for mobile AR on Android

1. Open the project, select the *XRScene*, check the player configuration

2. Ensure that the ARCore plugin is enabled for Android

3. Ensure that Android is the selected platform

4. Select the *XRScene* unity scene to be loaded by default

5. Build and install the app

6. Configure the player by following [these instructions](./xr-player-configuration)

