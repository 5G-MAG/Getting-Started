# XR anchoring

Anchoring attaches an entire scene, or specific nodes of a scene, to a 'trackable' definitions.

'Trackable' are standard behaviors describing how a 3D object should be positioned and scaled during an XR session.

XR anchoring is implemented in the unity player using the AR foundation framework.

- Compiling the XR Player for [mobile XR](./xr-player-android.md) scenarios
- Compiling the XR Player for [HMD](./xr-player-android.md) scenarios



## Trackable types

### 2D Marker anchoring

A node can be anchored to a 2D marker, typicaly a image real world image which will be *extended* with 3D during an XR session. A QR code can be used as a 2D marker as will.

The marker image is specified as a texture object in the glTF document.


### Floor anchoring

A common behavior for anchoring is to defined a 3D node attached to the floor, this is usefull to enforce it to be positioned at ground level.

- sample gltf scene implementing floor anchoring

### Plane anchoring

A common behavior for anchoring is to define a 3D node attached to an horizontal or a vertical plane, eg. a table top or a wall.

- sample gltf scene implementing plane anchoring


### Viewer anchoring

This trackable behavior specifies that a 3D node position is relative to the viewer. This would be for instance an HUD interface, or the player's body in a first person person perspective game.

- sample gltf scene implementing anchoring to viewer

### Geospatial anchoring

This trackable behavior specifies geospatial coordinates for positioning a 3D node in the real world.

- sample gltf scene implementing anchoring to viewer
