---
layout: default
title: V3C Player (Android) and streaming
parent: Tutorials
grand_parent: V3C Immersive Platform
has_children: false
nav_order: 0
---

# Tutorial - V3C Immersive Platform setup for Android and streaming

## Introduction

This tutorials provides the instructions to setup the V3C Immersive Platform for an Android device using content streamed from a DASH server.

## Step 0: Setting up the environment
We are doing the installation and building the platform in Windows. The target device to install the apk with the Unity Player will be an Android phone (in this example a Samsung S21).

As indicated in the instructions in the [rt-v3c-unity-player](https://github.com/5G-MAG/rt-v3c-unity-player), we will use Unity 6000.0.25f1. We recommend downloding [Unity Hub](https://unity.com/download) and select the version of Unity to install, which can also be downloaded from here: [https://unity.com/releases/editor/whats-new/6000.0.51](https://unity.com/releases/editor/whats-new/6000.0.51)

As indicated in the instructions in the [rt-v3c-decoder-plugin](https://github.com/5G-MAG/rt-v3c-decoder-plugin), we will also need:
- Visual Studio Professional 2022 (17.11.5) - [Download from Microsoft](https://download.visualstudio.microsoft.com/download/pr/69e24482-3b48-44d3-af65-51f866a08313/1ba729c183e9f3626bb97ae6c69a294c79bc00ecdc80de7c37d18b7b4555e6d/vs_Professional.exe)
- CMake (for example 3.30.4) - [Download from Cmake](https://cmake.org/files/v3.30/cmake-3.30.4-windows-x86_64.msi)
- Android Studio - [Download from Android](https://developer.android.com/studio) - Once downloaded make sure you install NDK r27c (27.2.12479018), and API 35.
- Docker Desktop - [Download from Docker](https://docs.docker.com/desktop/setup/install/windows-install/) - this is needed to execute Docker in Windows.

## Step 1: Clone the Unity Player Repository

```
git clone https://github.com/5G-MAG/rt-v3c-unity-player  
```

Although not immerdiately used, this will create the directories where the decoder plugin files will be copied.

## Step 2: Install the Decoder Plugin

Clone the repository:

```
git clone --recurse-submodules https://github.com/5G-MAG/rt-v3c-decoder-plugin.git
```

Install the dependencies:

```
cd rt-v3c-decoder-plugin
./Scripts/dl_deps.sh
```

Add the additional dependency regarding avcodec libraries. For this, instructions are provided in [rt-common-shared](https://github.com/5G-MAG/rt-common-shared). We can use the Docker build instructions.

```
git clone --recurse-submodules https://github.com/5G-MAG/rt-common-shared.git
cd rt-common-shared/avcodec-build/
docker build -t ffmpeg-builder:27 --build-arg NDK_VERSION=27.2.12479018 .
docker run -v $(pwd)/build/ffmpeg/aarch64:/usr/build/ffmpeg --env TARGET_ABI=aarch64 --env ANDROID_API_LEVEL=35 ffmpeg-builder:27
```

In Windows, the build artifacts can be found in your user folder `C:\Users\<your_user_name>\build\ffmpeg\aarch64`.

As we are targeting an Android device, once compiled, the .so libraries from the build artifacts' lib directory can be included into the ./External/avcodec/7.1/Android/arm64-v8a/lib directory of the rt-v3c-unity-player.

At this point, back in the directory of the rt-v3c-decoder-plugin, we can compile for Android:

```
./Scripts/build_android.sh release all  
```

We can now copy the plugins into the rt-v3c-unity-player directories:

```
cd rt-v3c-unity-player
../rt-v3c-decoder-plugin/Scripts/copy_libs.sh ./Packages/V3CDecoder/Runtime/Plugins release Android
```

## Step 3: Building the Unity Player for Android

In Unity Hub, import the "rt-v3c-unity-player/V3CImmersiveTest" project. Make sure that the scene V3C-Simple Player.unity is loaded.

Go to File->Build Settings (or Ctrl+Shift+B), select the Android target and select either Build or Build and Run.

Unity will generate a .apk file that you can copy and install on your phone. To use the Build&Run feature, you will need to activate the Debug through USB feature on your device (requires developper mode).

Note that you will need to manually install the content and/or configuration files on your device. Run the application once on your device to ensure the creation of the folder.

## Step 4: Importing configuration files

In Unity Hub, import the "rt-v3c-unity-player/V3CImmersiveTest" project. Make sure that the scene V3C-Simple Player.unity is loaded.

## Step 5: Setting up a DASH streaming server

In Unity Hub, import the "rt-v3c-unity-player/V3CImmersiveTest" project. Make sure that the scene V3C-Simple Player.unity is loaded.
