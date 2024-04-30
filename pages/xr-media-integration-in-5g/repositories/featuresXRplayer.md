---
layout: default
title:  Features XR Player
grand_parent: XR Media Integration in 5G
parent: Repositories
has_children: false
nav_order: 0
---

## XR Unity Player Features

### Planned for v1.0.0

<table>
<thead>
<tr>
<th style="text-align: left;">Extension</th>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Requirement</th>
<th style="text-align: left;">Status</th>
<th style="text-align: left;">Test content</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MPEG_anchor</td>
<td style="text-align: left;">anchors</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_anchor</td>
<td style="text-align: left;">trackable</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_anchor.trackable</td>
<td style="text-align: left;">TRACKABLE_CONTROLLER</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRACKABLE_GEOMETRIC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRACKABLE_MARKER_2D</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRACKABLE_MARKER_3D</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRACKABLE_MARKER_GEO</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRACKABLE_APPLICATION</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_anchor</td>
<td style="text-align: left;">anchors</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
</tbody>
</table>


&#x2a; anchoring and overlay of 3D content on real world

### Featured in v0.9.0

See also: [detailed implementation status of the scene description format](#scene-description-format).

| Feature                  |                       | Target   |          |
|:-------------------------|:----------------------|:---------|:---------|
|                          |                       | Windows  | Android  |
| media player &#x2a;      |                       | &#x2610; | &#x2610; |
| video texture &#x2a;     |                       | &#x2611; | &#x2610; |
| audio sources &#x2a;     |                       | &#x2611; | &#x2610; |
| interactivity            | ACTION_ACTIVATE       | &#x2611; | &#x2611; |
|                          | ACTION_MEDIA          | &#x2610; | &#x2610; |
|                          | ACTION_TRANSFORM      | &#x2611; | &#x2611; |
|                          | ACTION_BLOCK          | &#x2611; | &#x2611; |
|                          | ACTION_ANIMATION      | &#x2611; | &#x2611; |
|                          | ACTION_MANIPULATE     | &#x2611; | &#x2611; |
|                          | ACTION_SET_MATERIAL   | &#x2611; | &#x2611; |
|                          | ACTION_HAPTIC         | &#x2610; | &#x2610; |
|                          | ACTION_SET_AVATAR     | &#x2610; | &#x2610; |


&#x2a; Depends on media pipelines, see [supported platforms](#supported-platforms) below.


### Supported platforms

| Dependency               | Build target platform   | | | | |
|:-------------------------|:---------|:-------------|:-----------|:---------|:---------|
|                          | Windows  | Android      | Linux      | OSX      | iOS      |
| rt-xr-unity-player       | &#x2611; | &#x2611;     | &#x2a;     | &#x2a;   | &#x2a;   |
| Media Pipeline factory   | &#x2611; | &#x2610;     | &#x2610;   | &#x2610; | &#x2610; |
| avpipeline plugin        | &#x2611; | &#x2610;     | &#x2610;   | &#x2610; | &#x2610; |

&#x2a; untested, the application is expected to compile without issues. 

#### Tested devices 

**Smartphones**

- Android 13

**HMD**

- Meta Quest 2, 3, Pro - currently tested through Meta Quest Link on Windows 11. [XR Player - Meta Quest Link tutrial](tutorials/xr-player-win11-openXR.md).


### Scene Description format

The table below provide the implementation status of the latest stable release of [rt-xr-unity-player](https://github.com/5G-MAG/rt-xr-unity-player).

### Implemented in v0.9.0

Status: 

- &#x2611;  the feature is implemented the XR player.  
- &#x2610;  the feature is implemented by the glTF parser, but the corresponding behavior is not implemented by the XR player. 

Requirement (as defined in ISO/IEC 23090-14): 

- **O** : Optional 
- **M** : Mandatory 

<table>
<thead>
<tr>
<th style="text-align: left;">Extension</th>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Requirement</th>
<th style="text-align: left;">Status</th>
<th style="text-align: left;">Test content</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">MPEG_media</td>
<td style="text-align: left;">startTime</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">startTimeOffset</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">endTimeOffset</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">autoplay</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">autoplayGroup</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">loop</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">controls</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">alternatives</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_media.media.alternative</td>
<td style="text-align: left;">uri</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">mimeType</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">tracks</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_media.media.alternative.track</td>
<td style="text-align: left;">track</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">codecs</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_buffer_circular</td>
<td style="text-align: left;">count</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">media</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">tracks</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_accessor_timed</td>
<td style="text-align: left;">immutable</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">bufferView</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">suggestedUpdateRate</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_audio_spatial</td>
<td style="text-align: left;">sources</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">listener</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">reverbs</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_audio_spatial.sources</td>
<td style="text-align: left;">id</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">type</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">pregain</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">playbackSpeed</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">attenuation</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">attenuationParameters</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">referenceDistance</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">accessors</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">reverbFeed</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">reverbFeedGain</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_audio_spatial.listener</td>
<td style="text-align: left;">id</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_texture_video</td>
<td style="text-align: left;">accessor</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">width</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">height</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">format</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_scene_interactivity</td>
<td style="text-align: left;">triggers</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">actions</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">behaviors</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_scene_interactivity.triggers</td>
<td style="text-align: left;">TRIGGER_COLLISION</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRIGGER_PROXIMITY</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRIGGER_USER_INPUT</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRIGGER_VISIBILITY</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_scene_interactivity.actions</td>
<td style="text-align: left;">ACTION_ACTIVATE</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">ACTION_TRANSFORM</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">ACTION_BLOCK</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">ACTION_ANIMATION</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">ACTION_MEDIA</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">ACTION_MANIPULATE</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">ACTION_SET_MATERIAL</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">ACTION_HAPTIC</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">ACTION_SET_AVATAR</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_scene_interactivity.behaviors</td>
<td style="text-align: left;">triggers</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">actions</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">triggersCombinationControl</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">triggersActivationControl</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">actionsControl</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">interruptAction</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">priority</td>
<td style="text-align: left;">O</td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;">MPEG_node_interactivity</td>
<td style="text-align: left;">type</td>
<td style="text-align: left;">M</td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_node_interactivity.type</td>
<td style="text-align: left;">TRIGGER_COLLISION</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRIGGER_PROXIMITY</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRIGGER_USER_INPUT</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;">TRIGGER_VISIBILITY</td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2611;</td>
<td style="text-align: left;">&#x2611;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>



### Unimplemented

The following is a list of glTF extensions currently not implemented: 

<table>
<thead>
<tr>
<th style="text-align: left;">Extension</th>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Requirement</th>
<th style="text-align: left;">Status</th>
<th style="text-align: left;">Test content</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_sampler_YCbCr</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_primitive_V3C</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_node_avatar</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_lights_texture_based</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_light_punctual</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_haptic</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_mesh_linking</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_scene_dynamic</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_viewport_recommended</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
<tr>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;">MPEG_animation_timing</td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">&#x2610;</td>
<td style="text-align: left;">&#x2610;</td>
</tr>
</tbody>
</table>



