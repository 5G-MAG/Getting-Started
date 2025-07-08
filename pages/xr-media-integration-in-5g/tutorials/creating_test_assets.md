---
layout: default
title:  MPEG-I SD Test Assets
grand_parent: XR Media Integration in 5G
parent: Tutorials
has_children: false
nav_order: 0
---

# MPEG-I Scene Description Test Asset Creation

## Content repositories

5G-MAG is hosting a repository with test assets implementing some of the core extensions defined in MPEG-I Scene Description (ISO/IEC 23090-14): [https://github.com/5G-MAG/rt-xr-content](https://github.com/5G-MAG/rt-xr-content).

Note the assets produced by the MPEG-I SD group are typically available for download at [https://standards.iso.org/iso-iec/23090/-24/](https://standards.iso.org/iso-iec/23090/-24/).
Khronos hosts sample glTF2.0 assets on GitHub: [https://github.com/KhronosGroup/glTF-Sample-Assets.git](https://github.com/KhronosGroup/glTF-Sample-Assets.git.).

## Blender add-on to generate MPEG-I SD compliant glTF2.0 assets

The 5G-MAG Reference Tools also provides a Blender add-on to support [MPEG_* glTF extensions](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Vendor) and export glTF files.

The repository is available here: [https://github.com/5G-MAG/rt-xr-blender-exporter](https://github.com/5G-MAG/rt-xr-blender-exporter)
A tutorial is available here: [Blender glTF Exporter and Unity Player](./blender_exporter_unity_player.html)








### MPEG_anchor

### Configure anchoring of a node

![configure anchor](/doc/img/anchoring-configrure-anchor.png)

1. select the node to be anchored
2. locate the XR Anchoring panel in object properties, select an anchor type and configure the anchor


The following anchor types can be configured:
- TRACKABLE_FLOOR
- TRACKABLE_VIEWER
- TRACKABLE_CONTROLLER
- TRACKABLE_PLANE
- TRACKABLE_MARKER_2D
- TRACKABLE_MARKER_GEO
- TRACKABLE_APPLICATION

### Creating a 2D marker node

![configure anchor](/doc/img/anchoring-create-marker-2d.png)

1. locate the XR Anchoring panel (press N while the UI is focused on the 3D view)
2. select an image and hit 'create marker node', the marker 2D node is added to the scene and can now be used to configure an anchor


### MPEG_texture_video

To add a video and export it as MPEG_texture_video, first make sure that the blender's [scene output format](https://docs.blender.org/manual/en/3.6/render/output/properties/format.html) matches the framerate of the videos used as texture.

1. Create or select a material
2. Select the shader slot which will be using the video, and make it an 'Image texture'
3. Open or Select the video to use

All Image textures with a movie source are exported as MPEG_texture_video extensions:

![image texture](/doc/img/image-texture.jpg)

### MPEG_audio_spatial

#### Audio sources 

To add an audio source to the scene:

1. Add a *[Speaker](https://docs.blender.org/manual/en/latest/render/output/audio/speaker.html)* node to the scene: *3D Viewport > Add > Speaker*
2. Add a file source to the speaker's *Sound*. The file is assumed to contain a single channel of audio (MONO).
3. Configure speaker's *Distance* parameters:
    - Max Distance
    - Attenuation (roll-off factor)
    - Distance Reference
All other parameters are ignored.

The **audio attenuation model** is configured as [a scene property](https://docs.blender.org/manual/en/latest/scene_layout/scene/properties.html#data-scenes-audio) in Blender.

![audio source](/doc/img/audio-source.jpg)

![audio attenuation model](/doc/img/audio-attenuation-model.jpg)

