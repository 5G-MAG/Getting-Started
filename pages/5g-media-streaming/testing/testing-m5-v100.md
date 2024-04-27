---
layout: default
title:  Testing M5 AF v1.0.x
parent: Testing
grand_parent: 5G Downlink Media Streaming
has_children: false
nav_order: 10
---

# Testing: M5 Interface (5GMSd Application Function v1.0.0 to v1.1.x)

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

The current implementation of the interface at M5 uses the URL prefix of `http://${msaf.sbi.addr}:${msaf.sbi.port}/3gpp-m5/v2/`,
no other versions (i.e. "v2" only) are implemented and attempts to use another version will result a 400 Bad Request error response.

### Unsupported M5 API version

Test URL: `http://${msaf.sbi.addr}:${msaf.sbi.port}/3gpp-m5/v1/service-access-information`
Example command: `curl -v 'http://127.0.0.1:7778/3gpp-m5/v1/service-access-information'`

Expected result:
```
> GET /3gpp-m5/v1/service-access-information/id HTTP/1.1
> Host: 127.0.0.1:7778
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

Interface URL: `http://${msaf.sbi.addr}:${msaf.sbi.port}/3gpp-m5/v2/service-access-information/${provisioningSessionId}`

Where `${provisioningSessionId}` is the provisioning session identifier for the provisioning session. In a full 5GMSd Application
Function this would come from the `Location` in the response on the interface at M1 to a createProvisioningSession API action.
However, in the current version of the 5GMSd Application Function there is only one provisioning session created at start up. The
currently valid provisioning session id can be found in the log output from the `open5gs-msafd` command in the line containing
"INFO: Provisioning session = ".

### Testing Success

#### Testing the unencrypted media entry point on the canonical hostname

If the ContentHostingConfiguration does not contain any `distributionConfigurations.certificateId` or
`distributionConfigurations.domainNameAlias` properties then the `mediaPlayerEntry` in the ServiceAccessInformation will use the
"http" protocol and the canonical hostname of the 5GMSd Application Server as the authority part.

1. Stop the AF if it is running.

1. Start the AF with the `Test_http_canonical-msaf.yaml` example configuration, e.g.:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd -c ~/rt-5gms-application-function/examples/Test_http_canonical-msaf.yaml
   ```

1. Using the provisioning session id from the AF log output perform a GET request on the interface URL.

   Example command if the provisioning session id is 0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c:

   ```bash
   curl -v 'http://127.0.0.1:7778/3gpp-m5/v2/service-access-information/0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c'
   ```

   Expected result:

   ```
   > GET /3gpp-m5/v2/service-access-information/0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c HTTP/1.1
   > Host: 127.0.0.1:7778
   > User-Agent: curl/7.85.0
   > Accept: */*
   > 
   < HTTP/1.1 200 OK
   < Date: Tue, 07 Feb 2023 12:11:56 GMT
   < Connection: close
   < Content-Type: application/json
   < Content-Length: 278
   < 
   {
       "provisioningSessionId":	"0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c",
       "provisioningSessionType":	"DOWNLINK",
       "streamingAccess":	{
           "mediaPlayerEntry":	"http://localhost/m4d/provisioning-session-0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c/BigBuckBunny_4s_onDemand_2014_05_09.mpd"
       }
   }
   ```
   **Note:** There may also be additional HTTP library information lines output by curl starting with a `*` character interspersed with the output.

   The HTTP response is a 200 status code with the body containing a ServiceAccessInformation JSON object. The
   `provisioningSessionId` in the ServiceAccessInformation object should match the id presented in the request URL. The
   `provisioningSessionType` will be "DOWNLINK". The `mediaPlayerEntry` will be a "http://" URL for the canonical name set in the
   `msaf.yaml` file in the `msaf.applicationServers.canonicalHostname` property, and a path starting with the value of the
   `msaf.applicationServers.urlPathPrefixFormat` and ending in "`/BigBuckBunny_4s_onDemand_2014_05_09.mpd`" (which comes from the
   `entryPointPath` in the ContentHostingConfiguration).

#### Testing the encrypted media entry point on the canonical hostname

If the ContentHostingConfiguration contains `distributionConfigurations.certificateId` properties then an "https://" will be used
for the `mediaPlayerEntry` in the ServiceAccessInformation.

1. Stop the AF if it is running.

1. Create the self signed certificate:

   ```bash
   cd ~/rt-5gms-application-function
   subprojects/rt-common-shared/5gms/scripts/make_self_signed_certs.py --af-conf=examples/Test_https_canonical-msaf.yaml
   ```

   (see the information about [generating test certificates](Configuring-the-Application-Function#generating-test-certificates)
   for more details)

1. Start the AF with the `Test_https_canonical-msaf.yaml` configuration, e.g.:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd -c ~/rt-5gms-application-function/examples/Test_https_canonical-msaf.yaml
   ```

1. Using the provisioning session id from the AF log output perform a GET request on the interface URL.

   Example command if the provisioning session id is 0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c:

   ```bash
   curl -v 'http://127.0.0.1:7778/3gpp-m5/v2/service-access-information/0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c'
   ```

   Expected result:

   ```
   > GET /3gpp-m5/v2/service-access-information/0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c HTTP/1.1
   > Host: 127.0.0.1:7778
   > User-Agent: curl/7.85.0
   > Accept: */*
   >
   < HTTP/1.1 200 OK
   < Date: Tue, 07 Feb 2023 12:11:56 GMT
   < Connection: close
   < Content-Type: application/json
   < Content-Length: 278
   <
   {
       "provisioningSessionId":    "0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c",
       "provisioningSessionType":  "DOWNLINK",
       "streamingAccess":  {
           "mediaPlayerEntry": "https://localhost/m4d/provisioning-session-0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c/BigBuckBunny_4s_onDemand_2014_05_09.mpd"
       }
   }
   ```
   **Note:** There may also be additional HTTP library information lines output by curl starting with a `*` character interspersed with the output.

   The HTTP response is a 200 status code with the body containing a ServiceAccessInformation JSON object. The
   `provisioningSessionId` in the ServiceAccessInformation object should match the id presented in the request URL. The
   `provisioningSessionType` will be "DOWNLINK". The `mediaPlayerEntry` will be a "https://" URL (to show the AF is giving
   preference to the HTTPS access point) for the canonical name `localhost` (set in the `Test_https_canonical-msaf.yaml` file in the
   `msaf.applicationServers.canonicalHostname` property), and a path starting with the value of the
   `msaf.applicationServers.urlPathPrefixFormat` and ending in "`/BigBuckBunny_4s_onDemand_2014_05_09.mpd`" (which comes from the
   `entryPointPath` in the ContentHostingConfiguration).

#### Testing the `mediaPlayerEntry` when providing a `domainNameAlias`

If the ContentHostingConfiguration given in the `msaf.yaml` configuration file includes a
`distributionConfigurations.domainNameAlias` then this hostname will be used as the authority for the `mediaPlayerEntry` in the
ServiceAccessInformation in preference to the canonical hostname of the AS.

To test this:
1. Stop the AF process.

1. Start the AF with the `Test_http_domain_alias-msaf.yaml` configuration, e.g.:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd -c ~/rt-5gms-application-function/examples/Test_http_domain_alias-msaf.yaml
   ```

1. Using the provisioning session id from the AF log output perform a GET request on the interface URL.

   Example command if the provisioning session id is 0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c:

   ```bash
   curl -v 'http://127.0.0.1:7778/3gpp-m5/v2/service-access-information/0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c'
   ```

   Expected result:

   ```
   > GET /3gpp-m5/v2/service-access-information/0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c HTTP/1.1
   > Host: 127.0.0.1:7778
   > User-Agent: curl/7.85.0
   > Accept: */*
   >
   < HTTP/1.1 200 OK
   < Date: Tue, 07 Feb 2023 12:11:56 GMT
   < Connection: close
   < Content-Type: application/json
   < Content-Length: 278
   <
   {
       "provisioningSessionId":    "0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c",
       "provisioningSessionType":  "DOWNLINK",
       "streamingAccess":  {
           "mediaPlayerEntry": "https://media.example.com/m4d/provisioning-session-0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c/BigBuckBunny_4s_onDemand_2014_05_09.mpd"
       }
   }
   ```
   **Note:** There may also be additional HTTP library information lines output by curl starting with a `*` character interspersed with the output.

   The HTTP response is a 200 status code with the body containing a ServiceAccessInformation JSON object. The
   `provisioningSessionId` in the ServiceAccessInformation object should match the id presented in the request URL. The
   `provisioningSessionType` will be "DOWNLINK". The `mediaPlayerEntry` will be a "http://" URL followed by the
   `distributionConfigurations.domainNameAlias` property from the example
   `ContentHostingConfiguration_Big-Buck-Bunny_domain-name_http.json` file, and a path starting with the value of the
   `msaf.applicationServers.urlPathPrefixFormat` from the `Test_http_domain_alias-msaf.yaml` configuration file and ending in
   "`/BigBuckBunny_4s_onDemand_2014_05_09.mpd`" (which comes from the `entryPointPath` in the ContentHostingConfiguration).


### Testing No Such Provisioning Session

If the `${provisioningSessionId}` used in the request URL does not exist as an active provisioning session in the AF then the
HTTP response will be a 404 Not Found status code.

To test this
1. Start the AF if it is not already running, e.g.:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Using a bogus provisioning session id, perform a GET request on the interface URL.

   For example, if the provisioning session id is 0c5cc9e6-a6dd-41ed-ae90-e781c44d0f0c, then for this test we use a provisioning session id string that does not match that id.

   Example command using `does-not-exist` as a provisioning session id:

   ```bash
   curl -v 'http://127.0.0.1:7778/3gpp-m5/v2/service-access-information/does-not-exist'
   ```

   Expected result:

   ```
   > GET /3gpp-m5/v2/service-access-information/does-not-exist HTTP/1.1
   > Host: 127.0.0.1:7778
   > User-Agent: curl/7.85.0
   > Accept: */*
   >
   < HTTP/1.1 404 Not Found
   < Date: Tue, 07 Feb 2023 14:47:26 GMT
   < Connection: close
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
