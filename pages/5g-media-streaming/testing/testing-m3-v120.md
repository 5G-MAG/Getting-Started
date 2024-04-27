---
layout: default
title:  Testing M3 AF v1.2.x
parent: Testing
grand_parent: 5G Downlink Media Streaming
has_children: false
nav_order: 9
---

# Testing: M3 Interface (5GMSd Application Function v1.2.0 and above)

To prepare, follow the instructions for [local user building and installation](Testing-as-a-Local-User).

# Configuration

The Application Function is an M3 Client and most of the communication is only logged at the `debug` level. To properly see the M3 Interface interactions the configuration will need to set the minimum logging level to `debug` for the `msaf` domain.

To do this edit the installed `msaf.yaml` file and set the `logger` section to the following:

```yaml
logger:
    level: debug
    domain: msaf
```

The `msaf.yaml` file in use by the Application Function is one of (in preference order):
- The file passed on the command line using the `-c` parameter.
- `${prefix}/etc/open5gs/msaf.yaml`

The command for the tests will use the installed configuration file at `${prefix}/etc/open5gs/msaf.yaml`, if the instructions for [local user building and installation](Testing-as-a-Local-User) have been followed then this will be `~/rt-5gms-application-function/install/etc/open5gs/msaf.yaml`. You can optionally take a copy of this file and make the changes to a copy and then add the `-c` command line parameter and the path to your modified copy of the configuration file to the `open5gs-msafd` commands below.

# Testing

These tests require a [5GMSd Application Server](https://github.com/5G-MAG/rt-5gms-application-server) to be running. Please follow
the instructions to [build, install and run the 5GMSd Application Server](https://github.com/5G-MAG/rt-5gms-application-server#readme) as a system service or the [instructions to run the AS as a local user](https://github.com/5G-MAG/rt-5gms-application-server/wiki/Development-and-Testing) for a temporary installation for testing.

## Test Simple HTTP Configuration

This will test the ability of the Application Function to configure an Application Server via the interface at M3 with a simple
HTTP (unencrypted) distribution. For this test a ContentHostingConfiguration is used which has no `certificateId` fields set in any `distributionConfiguration`.

1. Stop the Application Function if it is already running.

1. Remove previous configurations:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the Application Function:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Configure a simple HTTP only stream hosting session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-stream -e MyAppId -a MyASPId -n 'Big Buck Bunny' 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
   ```

1. The log output should indicate that the Application function:
   1. Requests a list of Server Certificates known by the Application Server (this is only done upon first communicating with an Application Server or when the Application Function needs to resynchronise the state from the Application Server)

      ```
      02/10 10:39:26.792: [msaf] DEBUG: M3 client: Sending GET method to Application Server [localhost] to request the list of known certificates (../src/5gmsaf/application-server-context.c:151)
      ```

   1. Receives the response

      ```
      02/10 10:39:26.834: [msaf] DEBUG: [certificates] Method [GET] with Response [200] received (../src/5gmsaf/msaf-sm.c:1111)
      ```

      There may be log output following this with a list of certificates known to the Application Server.

   1. Requests the list of known provisioning session ids on the Application Server for ContentHostingConfigurations

      ```
      02/10 10:39:26.834: [msaf] DEBUG: M3 client: Sending GET method to Application Server [localhost] to request the list of known content-hosting-configurations (../src/5gmsaf/application-server-context.c:154)
      ```

   1. Receives the response

      ```
      02/10 10:39:26.837: [msaf] DEBUG: [content-hosting-configurations] Method [GET] with Response [200] for Content Hosting Configuration operation [(null)] (../src/5gmsaf/msaf-sm.c:888)
      ```

      There may be log output following this indicating a list of ContentHostingConfigurations known to the Application Server.

   1. Pushes a new ContentHostingConfiguration to the Application Server

      ```
      02/10 10:39:26.881: [msaf] DEBUG: M3 client: Sending POST method to Application Server [localhost] for Content Hosting Configuration:  [30ef86aa-a92f-41ed-870f-4501bf315b24] (../src/5gmsaf/application-server-context.c:235)
      ```

   1. Receives a success (201) response back, removes the ContentHostingConfiguration from the upload queue and marks it as current configuration for the Application Server.

      ```
      02/10 10:39:26.966: [msaf] DEBUG: [content-hosting-configurations] Method [POST] with Response [201] recieved for Content Hosting Configuration [30ef86aa-a92f-41ed-870f-4501bf315b24] (../src/5gmsaf/msaf-sm.c:736)
      02/10 10:39:26.966: [msaf] DEBUG: Removing 30ef86aa-a92f-41ed-870f-4501bf315b24 from upload_content_hosting_configurations (../src/5gmsaf/msaf-sm.c:745)
      02/10 10:39:26.966: [msaf] DEBUG: Adding 30ef86aa-a92f-41ed-870f-4501bf315b24 to current_content_hosting_configurations (../src/5gmsaf/msaf-sm.c:747)
      ```

## Test HTTPS configuration and certificate sending

This will test the ability of the Application Function to configure an Application Server via the interface at M3 with a simple
HTTPS (encrypted) distribution, SSL/TLS private key and SSL/TLS public certificate. For this test a ContentHostingConfiguration is used which has `certificateId` fields set in the `distributionConfigurations`.

1. Stop the Application Function if it is already running.

1. Remove previous configurations:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the Application Function:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Configure a simple HTTPS only stream hosting session with self signed certificate:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-stream -e MyAppId -a MyASPId -n 'Big Buck Bunny' --ssl-only 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
   ```

1. The log output should indicate that the Application function:
   1. Requests a list of Server Certificates known by the Application Server (this is only done upon first communicating with an Application Server or when the Application Function needs to resynchronise the state from the Application Server)

      ```
      02/10 10:39:26.792: [msaf] DEBUG: M3 client: Sending GET method to Application Server [localhost] to request the list of known certificates (../src/5gmsaf/application-server-context.c:151)
      ```

   1. Receives the response

      ```
      02/10 10:39:26.834: [msaf] DEBUG: [certificates] Method [GET] with Response [200] received (../src/5gmsaf/msaf-sm.c:1111)
      ```

      There may be log output following this with a list of certificates known to the Application Server.

   1. Requests the list of known provisioning session ids on the Application Server for ContentHostingConfigurations

      ```
      02/10 10:39:26.834: [msaf] DEBUG: M3 client: Sending GET method to Application Server [localhost] to request the list of known content-hosting-configurations (../src/5gmsaf/application-server-context.c:154)
      ```

   1. Receives the response

      ```
      02/10 10:39:26.837: [msaf] DEBUG: [content-hosting-configurations] Method [GET] with Response [200] for Content Hosting Configuration operation [(null)] (../src/5gmsaf/msaf-sm.c:888)
      ```

      There may be log output following this indicating a list of ContentHostingConfigurations known to the Application Server.

   1. Pushes the private key and public certificate

      ```
      02/10 10:39:26.838: [msaf] DEBUG: M3 client: Sending POST method to Application Server [localhost]for Certificate: [30ef86aa-a92f-41ed-870f-4501bf315b24:ea94917c-3726-45c5-9706-b6bb0be77e29] (../src/5gmsaf/application-server-context.c:187
      ```

   1. Receives a success (201) response back, removes the Server Certificate from the upload queue and marks it as a current Server
      Certificate for the Application Server

      ```
      02/10 10:39:26.881: [msaf] DEBUG: [certificates] Method [POST] with Response [201] recieved for certificate [30ef86aa-a92f-41ed-870f-4501bf315b24:ea94917c-3726-45c5-9706-b6bb0be77e29] (../src/5gmsaf/msaf-sm.c:947)
      02/10 10:39:26.881: [msaf] DEBUG: Removing certificate [30ef86aa-a92f-41ed-870f-4501bf315b24:ea94917c-3726-45c5-9706-b6bb0be77e29] from upload_certificates (../src/5gmsaf/msaf-sm.c:958)
      02/10 10:39:26.881: [msaf] DEBUG: Adding certificate [30ef86aa-a92f-41ed-870f-4501bf315b24:ea94917c-3726-45c5-9706-b6bb0be77e29] to  current_certificates (../src/5gmsaf/msaf-sm.c:962)
      ```

   1. Pushes a new ContentHostingConfiguration to the Application Server

      ```
      02/10 10:39:26.881: [msaf] DEBUG: M3 client: Sending POST method to Application Server [localhost] for Content Hosting Configuration:  [30ef86aa-a92f-41ed-870f-4501bf315b24] (../src/5gmsaf/application-server-context.c:235)
      ```

   1. Receives a success (201) response back, removes the ContentHostingConfiguration from the upload queue and marks it as current configuration for the Application Server

      ```
      02/10 10:39:26.966: [msaf] DEBUG: [content-hosting-configurations] Method [POST] with Response [201] recieved for Content Hosting Configuration [30ef86aa-a92f-41ed-870f-4501bf315b24] (../src/5gmsaf/msaf-sm.c:736)
      02/10 10:39:26.966: [msaf] DEBUG: Removing 30ef86aa-a92f-41ed-870f-4501bf315b24 from upload_content_hosting_configurations (../src/5gmsaf/msaf-sm.c:745)
      02/10 10:39:26.966: [msaf] DEBUG: Adding 30ef86aa-a92f-41ed-870f-4501bf315b24 to current_content_hosting_configurations (../src/5gmsaf/msaf-sm.c:747)
      ```

   1. Using the ProvisioningSessionId from the log output, check the configuration works via the Application Server using the generated certificate:

      ```bash
      curl -k -v https://localhost/m4d/provisioning-session-30ef86aa-a92f-41ed-870f-4501bf315b24/BigBuckBunny_4s_onDemand_2014_05_09.mpd
      ```

      ...or if you followed the "instructions to run the AS as a local user" then the port number used in the request URL will need to change to 8443, e.g

      ```bash
      curl -k -v https://localhost:8443/m4d/provisioning-session-30ef86aa-a92f-41ed-870f-4501bf315b24/BigBuckBunny_4s_onDemand_2014_05_09.mpd
      ```

      This should succeed and fetch the DASH MPD file for Big Buck Bunny.

## Test state synchronisation

If the Application Function is restarted without also restarting the Application Server, then the Application Server will retain
configurations (certificates and ContentHostingConfigurations) from older runs. This allows us to observe the state synchronisation
between the Application Function and Application Server so that the Application Function knows whether it needs to create or update entries.

Perform this test by performing the [Test HTTPS configuration and certificate sending](#test-https-configuration-and-certificate-sending) test and repeating step 4 (`m1-session` command) a few times, then perform the test once more from the beginning. You will observe the list of certificates and ContentHostingConfigurations known by the Application Server include the identifiers generated in the first run by the several `m1-session` commands. For example:

```
02/10 11:51:20.871: [msaf] DEBUG: M3 client: Sending GET method to Application Server [localhost] to request the list of known certificates (../src/5gmsaf/application-server-context.c:151)
...
02/10 11:51:20.913: [msaf] DEBUG: [certificates] Method [GET] with Response [200] received (../src/5gmsaf/msaf-sm.c:1111)
02/10 11:51:20.913: [msaf] DEBUG: Adding certificate [30ef86aa-a92f-41ed-870f-4501bf315b24:ea94917c-3726-45c5-9706-b6bb0be77e29] to Current certificates (../src/5gmsaf/msaf-sm.c:1139)
02/10 11:51:20.913: [msaf] DEBUG: Adding certificate [b3e6c736-a938-41ed-b967-ff8e23a4f49f:04844ed2-b8f5-4e22-b948-2b939fc2e21c] to Current certificates (../src/5gmsaf/msaf-sm.c:1139)
...
02/10 11:51:20.913: [msaf] DEBUG: M3 client: Sending GET method to Application Server [localhost] to request the list of known content-hosting-configurations (../src/5gmsaf/application-server-context.c:154)
...
02/10 11:51:20.916: [msaf] DEBUG: [content-hosting-configurations] Method [GET] with Response [200] for Content Hosting Configuration operation [(null)] (../src/5gmsaf/msaf-sm.c:888)
02/10 11:51:20.916: [msaf] DEBUG: Adding [30ef86aa-a92f-41ed-870f-4501bf315b24] to the current Content Hosting Configuration list (../src/5gmsaf/msaf-sm.c:913)
02/10 11:51:20.916: [msaf] DEBUG: Adding [b3e6c736-a938-41ed-b967-ff8e23a4f49f] to the current Content Hosting Configuration list (../src/5gmsaf/msaf-sm.c:913)
```

This example shows the Application server already knows about:
- Certificates 
  - `30ef86aa-a92f-41ed-870f-4501bf315b24:ea94917c-3726-45c5-9706-b6bb0be77e29`
  - `b3e6c736-a938-41ed-b967-ff8e23a4f49f:04844ed2-b8f5-4e22-b948-2b939fc2e21c`
- ContentHostingConfigurations
  - `30ef86aa-a92f-41ed-870f-4501bf315b24`
  - `b3e6c736-a938-41ed-b967-ff8e23a4f49f`

