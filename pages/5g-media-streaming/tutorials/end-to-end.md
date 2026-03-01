---
layout: default
title: 5GMSd (with Docker)
parent: Tutorials
grand_parent: 5G Media Streaming
has_children: false
nav_order: 3
---

<img src="../../../assets/images/Banner_5GMS.png" /> 

[Scope](../scope.html){: .btn .btn-blue } [Project Roadmap](../projects.html){: .btn .btn-blue } [GitHub Repos](../repositories.html){: .btn .btn-github } [Releases](../../releases.html#project-5g-media-streaming){: .btn .btn-release } [Tutorials](../tutorials.html){: .btn .btn-tutorial } [Requirements](../requirements.html){: .btn .btn-blue }

# Tutorial - 5G MSd End-to-End deployment (with Docker)

{: .inshort }
This tutorial allows to: Deploy 5G Media Streaming.

This guide describes how to setup and configure the 5G-MAG Reference Tools - 5G Downlink Media Streaming components to
create an end to end setup as depicted in the illustration below.

<img width="934" alt="Bildschirm­foto 2023-04-06 um 09 35 46" src="https://user-images.githubusercontent.com/2427039/230307155-c0f71870-a806-4229-966a-41a8f2f838f8.png">

## Versions

This guide uses the following versions. However, it is strongly recommended to use the latest versions of the
components.

| Component               | Minimum Version |
|-------------------------|-----------------|
| Application Function    | `1.3.0`         |
| Application Server      | `1.2.0`         |
| 5GMSd Aware Application | `1.0.0`         |
| Media Session Handler   | `1.0.0`         |
| Media Stream Handler    | `1.0.0`         |
| Common Android Library  | `1.0.0`         |

## Requirements

* A host machine running Ubuntu 22.04 LTS
* A smartphone running Android 10 or later

# Server-side setup

We provide multiple ways to do the server-side setup. The easiest way is to use the Docker setup. However, in some
cases, you might want to work with a native installation or even with a reduced setup to develop new functionality on
the client-side. For that reason, the server-side setup guide is divided into three alternative sections:

* [Option 1: Docker Compose setup](#option-1-docker-compose-setup)
* [Option 2: Native common server-side setup](#option-2-common-server-side-setup)
* [Option 3: Server-side development setup](#option-3-server-side-development-setup).

## Option 1: Docker Compose setup

The required files for the Docker Compose setup are located in
the [rt-5gms-examples project](https://github.com/5G-MAG/rt-5gms-examples/tree/development/5gms-docker-setup).

The `5gms-docker-setup` provides multiple Docker Compose setups to run the 5GMS Application Function, the 5GMS
Application Server and the
5GMS Application Provider in Docker container environments. This tutorial, assumes you are using Docker Compose recipe.

<img src="../../../assets/images/5gms/5gms-docker-recipe1.png" style="width: 80%">

### Setup

First, clone the [rt-5g-examples](https://github.com/5G-MAG/rt-5gms-examples/tree/development) repository:

````bash
git clone https://github.com/5G-MAG/rt-5gms-examples.git
````

Now switch to the `5gms-docker-setup/recipe1` folder:

````bash
cd rt-5gms-examples/5gms-docker-setup/recipe1
````

Follow
the [required configuration](https://github.com/5G-MAG/rt-5gms-examples/tree/development/5gms-docker-setup/recipe1#required-configuration)
and
the [installation](https://github.com/5G-MAG/rt-5gms-examples/tree/development/5gms-docker-setup/recipe1#installation)
instructions in
the [Readme](https://github.com/5G-MAG/rt-5gms-examples/blob/development/5gms-docker-setup/recipe1/Readme.md) file.

Once completed, verify that the `m8.json` has been created and can be accessed. Open the following URLs in your browser
and verify that a valid `JSON` file is returned:

* `http://localhost/m8.json`
* `http://<<ENTER_YOUR_IP_HERE>>/m8.json`

After that you can directly jump to the [client-side setup](#client-side-setup).

## Option 2: Common server-side setup

### 1. Installing the Application Function

The first component that we need to install is the **5GMSd Application Function (AF)**. The AF is a network function
that forms part of the 5G Media Streaming framework as defined in TS 26.501. AF is a logical function which embodies
control plane aspects such as provisioning, configuration, and reporting, among others. Such functions can be
provisioned by the 5GMSd Application Provider using a RESTful HTTP-based API (M1d). Another RESTful HTTP-based
configuration and reporting API (M5d) is exposed to 5GMSd Clients.

The detailed installation guide for the AF can be found in the
corresponding [Github repository](https://github.com/5G-MAG/rt-5gms-application-function).

### 2. Installing the Application Server

Next, we need to install the **5GMSd Application Server (AS)**. The AS provides 5G Media Streaming services to a
population of 5GMSd Clients. This logical function embodies the data plane aspects that deal with media content (for
instance, a Content Delivery Network). The content is ingested (both HTTP push- or pull-based are supported) from 5GMSd
Application Providers at reference point `M2d`. The content is distributed to 5GMSd Clients at reference point `M4d`,
which supports standard pull-based content retrieval protocols (e.g. DASH).

The detailed installation guide for the AS can be found in the
corresponding [Github repository](https://github.com/5G-MAG/rt-5gms-application-server).

### 3. Running the Application Server

Now start the AS

````bash
sudo 5gms-application-server 
````

For additional options, refer to
the [documentation](../tutorials/testing-AS.html#running-the-example-without-building). Pay attention to
the port configuration of the AS, as it requires root permission to run on the standard ports (`80` & `443`).

### 4. Running the Application Function

Now that we installed the AF and the AS we can configure the AF. A detailed configuration guide is available in
the [documentation](../tutorials/application-function/configuration-5GMSAF.html) of the AF.

### 5. Configuration of the AF

For this demo, we will run AF and AS on the same machine. As we want to access the `ServiceAccessInformation` via the
`M5d` interface from our Media Session Handler running on an Android device we need to slightly modify the
configuration. The goal is to expose the `M5d` interface via the IP address of our machine but have it running on a
different port to not interfere with the default port of the `M3`interface on the AS (`Port 7777`).

1. Open `/usr/local/etc/open5gs/msaf.yaml`
2. Find the settings for `msaf:m5`
3. Replace the `addr` field with `0.0.0.0` and choose a different `port`. For instance:

````yaml
msaf:
    m5:
        -   addr: 0.0.0.0
        -   port: 7778
```` 

### 6. Starting the AF

As we installed the AF as a local user, we start it with the following command:

````bash
/usr/local/bin/open5gs-msafd
````

### 7. Creating a Content Hosting Configuration

There is a guide on how to test the AS with the AF in
the [documentation](../tutorials/testing-AS.html#testing-with-the-application-function). We are following
a slightly different approach as we use the `msaf-configuration` tool that ships with version `1.3.0` of the Application
Function. The `msaf-configuration` tool creates a `provisioningSession` and a `contentHostingConfiguration` based on a
JSON input file. Moreover, it automatically generates the required `M8` information for us that we will later need on
the client-side.

First we create a configuration file to be used by the `msaf-configuration` tool:

````yaml
[ af-sync ]
    m5_authority = <YOUR_MACHINE_IP_HERE>:<M5_PORT_HERE>
  #docroot = /var/cache/rt-5gms/as/docroots
#default_docroot = /usr/share/nginx/html
````

Replace `<YOUR_MACHINE_IP_HERE>` with the IP address of your machine and `<M5_PORT_HERE>` with the port that the `M5`
interface is running on. For instance:

````yaml
[ af-sync ]
    m5_authority = 192.168.178.55:7778
  #docroot = /var/cache/rt-5gms/as/docroots
#default_docroot = /usr/share/nginx/html
````

Place this file in `/etc/rt-5gms/af-sync.conf`

Now we define a JSON file with the streams:

````json
{
  "aspId": "5GMAG",
  "appId": "5G-MAG_Reference_Tools",
  "streams": {
    "vod": {
      "name": "BBC R&D Demo Streams",
      "ingestURL": "https://rdmedia.bbc.co.uk/",
      "distributionConfigurations": [
        {
          "domainNameAlias": "<YOUR_MACHINE_IP_HERE>"
        }
      ]
    }
  },
  "vodMedia": [
    {
      "name": "VoD: Elephant's Dream",
      "stream": "vod",
      "entryPoints": [
        {
          "relativePath": "elephants_dream/1/client_manifest-all.mpd",
          "contentType": "application/dash+xml",
          "profiles": [
            "urn:mpeg:dash:profile:isoff-live:2011"
          ]
        }
      ]
    },
    {
      "name": "VoD: Big Buck Bunny",
      "stream": "vod",
      "entryPoints": [
        {
          "relativePath": "bbb/2/client_manifest-common_init.mpd",
          "contentType": "application/dash+xml",
          "profiles": [
            "urn:mpeg:dash:profile:isoff-live:2011"
          ]
        }
      ]
    },
    {
      "name": "VoD: Testcard",
      "stream": "vod",
      "entryPoints": [
        {
          "relativePath": "testcard/vod/manifests/avc-full.mpd",
          "contentType": "application/dash+xml",
          "profiles": [
            "urn:mpeg:dash:profile:isoff-live:2011"
          ]
        },
        {
          "relativePath": "testcard/vod/manifests/avc-full.m3u8",
          "contentType": "application/x-mpegURL"
        }
      ]
    }
  ]
}
````

Again, replace `<YOUR_MACHINE_IP_HERE>` with the IP address of your machine.

Place this file in `/etc/rt-5gms/streams.json`

Now [install](https://github.com/5G-MAG/rt-5gms-application-provider/tree/master/python) and execute the
`msaf-configuration` tool:

````bash
sudo ~/usr/local/bin/msaf-configuration
````

You should see a message like this:

````bash
INFO:__main__:Publishing M8 info to: /usr/share/nginx/html, /var/cache/rt-5gms/as/docroots/192.168.178.55
````

You can check the response of the `m8` request by opening `http://localhost/m8.json` in your browser. It should look
like this:

````json
{
  "m5BaseUrl": "http://192.168.178.55:7778/3gpp-m5/v2/",
  "serviceList": [
    {
      "provisioningSessionId": "872a0eb2-e40a-41ed-bf2a-03b8343221a7",
      "name": "VoD: Llama Drama",
      "entryPoints": [
        {
          "locator": "http://192.168.178.55/m4d/provisioning-session-872a0eb2-e40a-41ed-bf2a-03b8343221a7/634cd01c-6822-4630-8444-8dd6279f94c6/CaminandesLlamaDrama4K.ism/manifest(format=mpd-time-csf)",
          "contentType": "application/dash+xml",
          "profiles": [
            "urn:mpeg:dash:profile:isoff-live:2011"
          ]
        },
        {
          "locator": "http://192.168.178.55/m4d/provisioning-session-872a0eb2-e40a-41ed-bf2a-03b8343221a7/634cd01c-6822-4630-8444-8dd6279f94c6/CaminandesLlamaDrama4K.ism/manifest(format=m3u8-aapl-v3)",
          "contentType": "application/vnd.apple.mpegurl"
        }
      ]
    }
  ]
}
````

In our Android application we will use this endpoint later to derive the required information to populate our stream
selection drowdown and to query the Application Function via `M5`.

### Optional: Creating a Server Certificate

Optionally, you can now
also [create server certificate](../tutorials/application-function/testing-m1-v130.html#server-certificates). For plain
`http` based playback we can omit this step.

The complete documentation on how to test the M5 interface for AF versions 1.2.0 and above can be
found [here](../tutorials/application-function/testing-m5-v120.html)

What we will need on the client side later is the `ServiceAccessInformation`. This will be requested via `M5d` by our
MediaSessionHandler. Since retrieving this information is done via a simple HTTP GET request, we can access the
information directly in the browser. For that reason, call the following URL and replace `{provisioningSessionId}` with
the corresponding value. For instance,

* `http://${msaf.m5.addr}:${msaf.m5.port}/3gpp-m5/v2/service-access-information/${provisioningSessionId}`

becomes

* `http://192.168.178.55:7778/3gpp-m5/v2/service-access-information/a0b5a258-d5da-41ed-b62f-cdd2806778b0`

The output should look like the following:

````json
{
  "provisioningSessionId": "a0b5a258-d5da-41ed-b62f-cdd2806778b0",
  "provisioningSessionType": "DOWNLINK",
  "streamingAccess": {
    "mediaPlayerEntry": "http://192.168.178.55/m4d/provisioning-session-a0b5a258-d5da-41ed-b62f-cdd2806778b0/BigBuckBunny_4s_onDemand_2014_05_09.mpd"
  }
}
````

## Option 3: Server-side development setup

For development purposes, it can be useful to mock the functionality of the AF and the AS. For that reason, 5G-MAG
provides a [simple static webserver](https://github.com/5G-MAG/rt-5gms-examples/tree/main/express-mock-af). The server
basically contains two endpoints to query `M8` information and the corresponding `ServiceAccessInformation`. The assets
that are linked on the webserver are pointing to third-party CDNs. However, it would also be possible to add media
content to the webserver in the `public` folder and thereby simulate a local Application Server.

### 1. Configure the webserver

Open `/express-mock-af/routes/m8.js` and adjust the `m5BaseUrl` to point to your machine.

Install the dependencies:

````bash
cd express-mock-af
npm install
````

### 2. Starting the webserver

Navigate to the root folder of the server and start it:

````bash
cd express-mock-af
npm start
```` 

# Client-side setup

Not that we have the server-side setup in place we can focus on the client side. We need to install four components (two
libraries, two Android applications) for the end-to-end setup.

## 1. Installing the 5GMSd Common Android Library

The [5GMSd Common Android Library](https://github.com/5G-MAG/rt-5gms-common-android-library) is an Android library that
includes models and helper classes used within the different client-side Android applications such as the 5GMSd-Aware
Application, 5GMSd Media Stream Handler and the 5GMSd Media Session Handler.

The installation guide can be found in the [Readme](https://github.com/5G-MAG/rt-5gms-common-android-library#readme) of
the project. Note that you need to publish the library to a local maven repository as described in the installation
guide.

## 2. Installing the 5GMSd Media Stream Handler

The [5GMSd Media Stream Handler](https://github.com/5G-MAG/rt-5gms-media-stream-handler) is an Android library that
includes the [ExoPlayer](https://github.com/google/ExoPlayer) as a dependency. The 5GMSd Media Stream Handler implements
an adapter around the ExoPlayer APIs to expose TS.26.512 M7d interface functionality. Moreover, a
MediaSessionHandlerAdapter establishes a Messenger connection to
the [Media Session Handler](https://github.com/5G-MAG/rt-5gms-media-session-handler). The 5GMSd Media Stream Handler is
included as an Android library by 5GMSd Aware Application.

The installation guide can be found in the [Readme](https://github.com/5G-MAG/rt-5gms-media-stream-handler#readme) of
the project. Note that you need to publish the library to a local maven repository as described in the installation
guide.

## 3. Installing the 5GMSd Media Session Handler

The [5GMSd Media Session Handler](https://github.com/5G-MAG/rt-5gms-media-session-handler) is an Android application
that implements functionality for 5G Media Streaming media session handling. It is implemented as an Android Messenger
Service that communicates via Inter Process Communication (IPC) with other Android libraries and applications such as
the Media Stream Handler and the 5GMSd Aware Application.

The Media Session Handler communicates with the 5GMSd Application Function via interface M5 to establish and control the
delivery of a streaming media session in the downlink direction. In addition, the Media Session Handler exposes APIs via
M6 to the 5GMSd-Aware Application and to the Media Player (for downlink streaming).

The installation guide can be found in the [Readme](https://github.com/5G-MAG/rt-5gms-media-session-handler#readme) of
the project.

## 4. Configuring and installing the 5GMSd-Aware Application

The 5GMSd-Aware Application is an Android application that serves as a reference implementation for 5GMSd. It uses
the [Media Stream Handler](https://github.com/5G-MAG/rt-5gms-media-stream-handle) for playback and communication with
the [Media Session Handler](https://github.com/5G-MAG/rt-5gms-media-session-handler).

The 5GMSd Aware Application is an application in the UE, provided by the 5GMSd Application Provider, that contains the
service logic of the 5GMSd application service, and interacts with other 5GMSd Client and Network functions via the
interfaces and APIs defined in the 5GMSd architecture.

### 4.a Common Configuration

The 5GMSd-Aware Application supports `m8` input via REST endpoints or local files. For that reason, a configuration file
located in `app/src/main/assets/config.properties.xml` is used. It contains a list of the possible `m8` endpoints. Per
default, a single 5G-MAG hosted endpoint is linked:

````xml
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
    <entry key="m85GMAGHost">https://rt.5g-mag.com/</entry>
</properties>
```` 

For our local AS and AF setup we only need to extend this list with the `M8` endpoint we created previously:

````xml
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
    <entry key="m8LocalAfAndAs">m8/config_local_af.json</entry>
    <entry key="m85LocalHost">http://<YOUR_MACHINE_IP_HERE>/
    </entry>
</properties>
````

Replace `<YOUR_MACHINE_IP_HERE>` with the IP of the machine that is running the AF and the AS, for instance:

````xml
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
    <entry key="m8LocalAfAndAs">m8/config_local_af.json</entry>
    <entry key="m85LocalHost">http://192.168.178.55/</entry>
</properties>
````

### 4.a Alternative: Development Configuration

If you are using the development web server instead of the common AF and AS installation, simply open
`app/src/main/assets/config.properties.xml` and uncomment the following two lines. These two local `.json` files
correspond to the default configuration on the static webserver.

````xml
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
    <entry key="m8LocalSingleMedia">m8/config_single_media.json</entry>
    <entry key="m8LocalMultiMedia">m8/config_multi_media.json</entry>
</properties>
````

Navigate to `app/src/main/assets/m8` and adjust the IP address of the `m5BaseUrl` in `config_single_media.json` and
`config_multi_media.json` to point to your local webserver.

As an alternative, you can also use the `M8` endpoint of the development web server. For that reason, uncomment the
following line and replace the IP address with the IP address of your machine.

````xml
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
    <entry key="m8LocalDummyHost">http://192.168.178.55:3003/m8/</entry>
</properties>
````

### 4.b Installation

The installation guide for the 5GMSd-Aware Application can be found in
the [Readme](https://github.com/5G-MAG/rt-5gms-application/tree/development/fivegmag_5GMSdAwareApplication) of the
project.

## 5. Running the application

Now that we have performed all the required setup and configuration, we can finally start our client-side applications.
Unlock your Android phone and start the `MediaSessionHandler` if it is not already running. Afterwards start the
`5GMSd-Aware Application`. Select an `M8` entry from the dropdown and then select one of the available stream URLs.
Next, click on _Start Playback_. The output should look like this:

<img width="757" alt="Bildschirm­foto 2023-04-26 um 09 43 13" src="https://user-images.githubusercontent.com/2427039/234528696-0411099a-2cf1-4397-b1d9-2b84760bdde3.png">
