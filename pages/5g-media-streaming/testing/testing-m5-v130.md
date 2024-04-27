---
layout: default
title:  Testing M5 AF v1.3.x
parent: Testing
grand_parent: 5G Downlink Media Streaming
has_children: false
nav_order: 12
---

# Testing: M5 Interface (5GMSd Application Function v1.3.0 and above)

To prepare, follow the instructions for [local user building and installation](Testing-as-a-Local-User).

# Configuration

These tests use test configurations from the `examples` directory. Some of these example configuration will need self-signed public certificates generating, and appropriate instructions are included to run the generation script with the correct configuration where appropriate.

The `msaf.yaml` file in use by the Application Function is one of (in preference order):
- The file passed on the command line using the `-c` parameter.
- `${prefix}/etc/open5gs/msaf.yaml`

These tests use the `-c` command line parameter to override the default configuration location.

See [Configuring the Application Function](Configuring-the-Application-Function) for more details on Application Function
configuration.

# Testing

This section will describe common tests and the expected outcomes for the M5 interface.

**Note: At this time the only implemented part of the M5 interface is the ServiceAccessInformation API**

## M5 API prefix

The current implementation of the interface at M5 uses the URL prefix of `http://${msaf.m5.addr}:${msaf.m5.port}/3gpp-m5/v2/`,
no other versions (i.e. "v2" only) are implemented and attempts to use another version will result a 400 Bad Request error response.

### Unsupported M5 API version

Test URL: `http://${msaf.m5.addr}:${msaf.m5.port}/3gpp-m5/v1/service-access-information`
Example command: `curl -v 'http://127.0.0.24:7777/3gpp-m5/v1/service-access-information'`

Expected result:
```
> GET /3gpp-m5/v1/service-access-information HTTP/1.1
> Host: 127.0.0.24:7777
> User-Agent: curl/7.85.0
> Accept: */*
> 
< HTTP/1.1 400 Bad Request
< Date: Tue, 07 Feb 2023 11:46:59 GMT
< Connection: close
< Content-Type: application/problem+json
< Content-Length: 124
< 
{
	"type":	"/3gpp-m5/v1",
	"title":	"Not supported version",
	"status":	400,
	"instance":	"/service-access-information"
}
```
**Note:** There may also be additional HTTP library information lines output by curl starting with a `*` character interspersed with the output.

AF log output:
```
02/07 11:46:59.263: [msaf] ERROR: Not supported version [v1] (../src/5gmsaf/msaf-sm.c:494)
```

The HTTP response is a 400 status code with a ProblemDetail JSON object in the body. The problem detail shows that the error
happened because the request contained an unsupported version. The application itself produces an `ERROR` log message indicating
that a client requested an unsupported version.

## ServiceAccessInformation

These tests describe the available actions and possible responses for the M5 ServiceAccessInformation APIs.

Interface URL: `http://${msaf.m5.addr}:${msaf.m5.port}/3gpp-m5/v2/service-access-information/${provisioningSessionId}`

Where `${provisioningSessionId}` is the provisioning session identifier for the provisioning session. This URL comes from the `Location` in the response on the interface at M1 to a createProvisioningSession API action, and is displayed by the `m1-session` tool when a `new-provisioning-session` or `new-stream` command is successful.

### Testing Success

#### Testing the unencrypted media entry point on the canonical hostname

If the ContentHostingConfiguration does not contain any `distributionConfigurations.certificateId` or
`distributionConfigurations.domainNameAlias` properties then the `mediaPlayerEntry` in the ServiceAccessInformation will use the
"http" protocol and the canonical hostname of the 5GMSd Application Server as the authority part.

1. Stop the AF if it is running.

1. Clean up old persistent data:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the AF:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Configure a simple stream:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-stream -e AppId -n 'Simple Stream' 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
   ```

1. Using the provisioning session id, returned from the `m1-session` command, perform a GET request on the interface URL.

   Example command if the provisioning session id is 0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c:

   ```bash
   curl -v 'http://127.0.0.24:7777/3gpp-m5/v2/service-access-information/0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c'
   ```

   Expected result:

   ```
   > GET /3gpp-m5/v2/service-access-information/f863831c-daa8-41ed-862b-c1f4c44bccf3 HTTP/1.1
   > Host: 127.0.0.24:7777
   > User-Agent: curl/7.85.0
   > Accept: */*
   > 
   < HTTP/1.1 200 OK
   < Date: Fri, 14 Apr 2023 09:44:47 GMT
   < Connection: close
   < Content-Type: application/json
   < ETag: 38548172d8eca143db6b4b11af8df6dea66d62acb45f751c9348f257c9682165
   < Last-Modified: Fri, 14 Apr 2023 09:44:37 GMT
   < Cache-Control: max-age=60
   < Server: 5GMSdAF-localhost/17 (info.title=M5_ServiceAccessInformation; info.version=2.2.0) rt-5gms-application-function/1.3.0
   < Content-Length: 339
   {
       "provisioningSessionId":	"f863831c-daa8-41ed-862b-c1f4c44bccf3",
       "provisioningSessionType":	"DOWNLINK",
       "streamingAccess":	{
           "entryPoints":	[{
               "locator":	"http://localhost/m4d/provisioning-session-f863831c-daa8-41ed-862b-c1f4c44bccf3/BigBuckBunny_4s_onDemand_2014_05_09.mpd",
               "contentType":	"application/dash+xml"
           }]
       }
   }
   ```
   **Note:** There may also be additional HTTP library information lines output by curl starting with a `*` character interspersed with the output.

   The HTTP response is a 200 status code with the body containing a ServiceAccessInformation JSON object. The
   `provisioningSessionId` in the ServiceAccessInformation object should match the id presented in the request URL. The
   `provisioningSessionType` will be "DOWNLINK". The `mediaPlayerEntry` will be a "http://" URL for the canonical name set in the
   `msaf.yaml` file in the `msaf.applicationServers.canonicalHostname` property, and a path starting with the value of the
   `msaf.applicationServers.urlPathPrefixFormat` and ending in "`/BigBuckBunny_4s_onDemand_2014_05_09.mpd`" (which comes from the
   `entryPointPath` in the `m1-session` command).

#### Testing the encrypted media entry point on the canonical hostname

If the ContentHostingConfiguration contains `distributionConfigurations.certificateId` properties then an "https://" will be used
for the `mediaPlayerEntry` in the ServiceAccessInformation.

1. Stop the AF if it is running.

1. Clean up old persistent data:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the AF:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Configure a simple stream with self-signed HTTPS distribution:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-stream -e AppId -n 'Simple HTTPS Stream' --with-ssl 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
   ```

1. Using the provisioning session id, returned from the `m1-session` command, perform a GET request on the interface URL

   Example command if the provisioning session id is 30c20cea-daab-41ed-87fe-93ba2b9b790a:

   ```bash
   curl -v 'http://127.0.0.24:7777/3gpp-m5/v2/service-access-information/30c20cea-daab-41ed-87fe-93ba2b9b790a'
   ```

   Expected result should look like:

   ```
   > GET /3gpp-m5/v2/service-access-information/30c20cea-daab-41ed-87fe-93ba2b9b790a HTTP/1.1
   > Host: 127.0.0.24:7777
   > User-Agent: curl/7.85.0
   > Accept: */*
   > 
   < HTTP/1.1 200 OK
   < Date: Fri, 14 Apr 2023 10:00:40 GMT
   < Connection: close
   < ETag: 8c12228d39cd5e015fdab5e7972084a6bbd12747b4c482e0cdc1ce82bbac597e
   < Last-Modified: Fri, 14 Apr 2023 10:00:31 GMT
   < Cache-Control: max-age=60
   < Server: 5GMSdAF-localhost/17 (info.title=M5_ServiceAccessInformation; info.version=2.2.0) rt-5gms-application-function/1.3.0
   < Content-Type: application/json
   < Content-Length: 340
   < 
   {
       "provisioningSessionId":	"30c20cea-daab-41ed-87fe-93ba2b9b790a",
       "provisioningSessionType":	"DOWNLINK",
       "streamingAccess":	{
           "entryPoints":	[{
               "locator":	"https://localhost/m4d/provisioning-session-30c20cea-daab-41ed-87fe-93ba2b9b790a/BigBuckBunny_4s_onDemand_2014_05_09.mpd",
               "contentType":	"application/dash+xml"
           }]
       }
   }
   ```
   **Note:** There may also be additional HTTP library information lines output by curl starting with a `*` character interspersed with the output.

   The HTTP response is a 200 status code with the body containing a ServiceAccessInformation JSON object. The
   `provisioningSessionId` in the ServiceAccessInformation object should match the id presented in the request URL. The
   `provisioningSessionType` will be "DOWNLINK". The `mediaPlayerEntry` will be a "https://" URL (to show the AF is giving
   preference to the HTTPS access point) for the canonical name `localhost` (set in the `msaf.yaml` file in the
   `msaf.applicationServers.canonicalHostname` property), and a path starting with the value of the
   `msaf.applicationServers.urlPathPrefixFormat` and ending in "`/BigBuckBunny_4s_onDemand_2014_05_09.mpd`" (which comes from the
   `entryPointPath` in the `m1-session` command).

#### Testing the `mediaPlayerEntry` when providing a `domainNameAlias`

If the ContentHostingConfiguration given in the `msaf.yaml` configuration file includes a
`distributionConfigurations.domainNameAlias` then this hostname will be used as the authority for the `mediaPlayerEntry` in the
ServiceAccessInformation in preference to the canonical hostname of the AS.

To test this:
1. Stop the AF process.

1. Clean up old persistent data:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the AF:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Configure a simple stream with self-signed HTTPS distribution:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-stream -e AppId -n 'Simple HTTPS Stream' -d 'media.example.com' 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
   ```

1. Using the provisioning session id, returned from the `m1-session` command, perform a GET request on the interface URL

   Example command if the provisioning session id is efbff530-daab-41ed-87fe-93ba2b9b790a:

   ```bash
   curl -v 'http://127.0.0.24:7777/3gpp-m5/v2/service-access-information/efbff530-daab-41ed-87fe-93ba2b9b790a'
   ```

   Expected result:

   ```
   > GET /3gpp-m5/v2/service-access-information/efbff530-daab-41ed-87fe-93ba2b9b790a HTTP/1.1
   > Host: 127.0.0.24:7777
   > User-Agent: curl/7.85.0
   > Accept: */*
   > 
   < HTTP/1.1 200 OK
   < Date: Fri, 14 Apr 2023 10:06:01 GMT
   < Connection: close
   < ETag: f5dd70a781efeefed1c034bbe640119019e1a46a55dcf50cfcccae8a323139ad
   < Last-Modified: Fri, 14 Apr 2023 10:05:51 GMT
   < Cache-Control: max-age=60
   < Server: 5GMSdAF-localhost/17 (info.title=M5_ServiceAccessInformation; info.version=2.2.0) rt-5gms-application-function/1.3.0
   < Content-Type: application/json
   < Content-Length: 347
   < 
   {
       "provisioningSessionId":	"efbff530-daab-41ed-87fe-93ba2b9b790a",
       "provisioningSessionType":	"DOWNLINK",
       "streamingAccess":	{
           "entryPoints":	[{
               "locator":	"http://media.example.com/m4d/provisioning-session-efbff530-daab-41ed-87fe-93ba2b9b790a/BigBuckBunny_4s_onDemand_2014_05_09.mpd",
               "contentType":	"application/dash+xml"
           }]
       }
   }
   ```
   **Note:** There may also be additional HTTP library information lines output by curl starting with a `*` character interspersed with the output.

   The HTTP response is a 200 status code with the body containing a ServiceAccessInformation JSON object. The
   `provisioningSessionId` in the ServiceAccessInformation object should match the id presented in the request URL. The
   `provisioningSessionType` will be "DOWNLINK". The `mediaPlayerEntry` will be a "http://" URL followed by the
   `media.example.com` FQDN given with the `-d` command line argument to the `m1-session` command, and a path starting with the
   value of the `msaf.applicationServers.urlPathPrefixFormat` from the `msaf.yaml` configuration file and ending in
   "`/BigBuckBunny_4s_onDemand_2014_05_09.mpd`" (which comes from the `entryPointPath` given on the `m1-session` command line).


### Testing No Such Provisioning Session

If the `${provisioningSessionId}` used in the request URL does not exist as an active provisioning session in the AF then the
HTTP response will be a 404 Not Found status code.

To test this
1. Start the AF if it is not already running, e.g.:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Configure a simple stream:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-stream -e AppId -n 'Simple Stream' 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
   ```

1. Using a bogus provisioning session id, i.e. anything except the provisioning session id returned by the `m1-session` command,
   perform a GET request on the interface URL.

   For example, if the provisioning session id is 0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c, then for this test we use a provisioning session id string that does not match that id.

   Example command using `does-not-exist` as a provisioning session id:

   ```bash
   curl -v 'http://127.0.0.24:7777/3gpp-m5/v2/service-access-information/does-not-exist'
   ```

   Expected result:

   ```
   > GET /3gpp-m5/v2/service-access-information/does-not-exist HTTP/1.1
   > Host: 127.0.0.24:7777
   > User-Agent: curl/7.85.0
   > Accept: */*
   >
   < HTTP/1.1 404 Not Found
   < Date: Tue, 07 Feb 2023 14:47:26 GMT
   < Connection: close
   < Server: 5GMSdAF-localhost/17 (info.title=M5_ServiceAccessInformation; info.version=2.2.0) rt-5gms-application-function/1.3.0
   < Content-Type: application/problem+json
   < Content-Length: 208
   < 
   {
       "type":	"/3gpp-m5/v2",
       "title":	"Provisioning Session not found",
       "status":	404,
       "detail":	"Provisioning Session [does-not-exist] not found.",
       "instance":	"/service-access-information/does-not-exist"
   }
   ```
   **Note:** There may also be additional HTTP library information lines output by curl starting with a `*` character interspersed with the output.

   The HTTP response is a 404 status code with the body containing a ProblemDetail JSON object.

## Consumption Reporting

**TODO!**

## Network Assistance

**TODO!**

## Dynamic Policies

**TODO!**

