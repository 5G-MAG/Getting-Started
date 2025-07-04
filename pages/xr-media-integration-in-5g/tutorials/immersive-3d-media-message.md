---
layout: default
title:  Immersive and 3D Media message
grand_parent: XR Media Integration in 5G
parent: Tutorials
has_children: false
nav_order: 2
---

# Immersive and 3D Media message

## VR/XR/3D Scene

### Use case 1: Sharing a 3D asset as a 3GPP conforming MMS message
Example: 3GPP shares the 3GPP Emmy Statue as 3GPP conforming messaging MMS to all members

#### Reference 5G-MAG assets

To realize this use case, 5G-MAG has selected the following assets:
* [Simple academy awards model without anchoring](https://github.com/5G-MAG/rt-xr-content/tree/development/awards/awards.gltf)

Follow [these instructions](../usage/xr-player-android) to build and configure the player for Android.

### Use case 2: Sharing a 3D asset through a third-party application using 3GPP conforming containers
Example: A house rental agency offers rooms that you can walk through their assets. They share the assets through WhatsApp using 3GPP conforming containers.

#### Reference 5G-MAG assets
To realize this use case, 5G-MAG has selected the following assets, which are provided with the relevant glTF extensions:
* 🚧 [Studio apartment](https://github.com/5G-MAG/rt-xr-content/blob/development/studio_apartment/studio_apartment.gltf)

Follow [these instructions](../usage/xr-player-android) to build and configure the player for Android.


### Use case 3: Extension of use case 2 to add images inside the 3D asset
Example: An extension of use case 2 provides the ability to add your family pictures to the wall.

#### Reference 5G-MAG assets
To realize this use case, 5G-MAG has selected the following assets, which are provided with the relevant glTF extensions:
* x
* x


---

## AR Scenes

### Use case 4: Extension of use case 1 including information to anchor the model
Example: 3GPP shares the 3GPP Emmy Statue as 3GPP conforming messaging MMS to all members, including information to put it on your living desk

#### Reference 5G-MAG assets
To realize this use case, 5G-MAG has selected the following assets, which are provided with the relevant glTF extensions to signal AR anchoring:
* [academy awards model with explicit floor anchoring](https://github.com/5G-MAG/rt-xr-content/blob/development/awards/awards_floor_anchoring.gltf)
* 🚧 [academy awards model with explicit horizontal anchoring](https://github.com/5G-MAG/rt-xr-content/blob/development/awards/awards_plane_anchoring.gltf)

Follow [these instructions](../usage/xr-player-android) to build and configure the player for Android.


### Use case 5: Extension of use case 2 including information to manipulate a model with anchoring constraints
Example: Ikea offers furnitures on their webpage that you can request. They share the assets though Signal using 3GPP conforming containers. You can place the asset on your living room's floor and check how it fits.

#### Reference 5G-MAG assets
To realize this use case, 5G-MAG has selected the following assets, which are provided with the relevant glTF extensions:
* 🚧 [enable user to manipulate a 3D model anchored to the floor](https://github.com/5G-MAG/rt-xr-unity-player/issues/41)
 
