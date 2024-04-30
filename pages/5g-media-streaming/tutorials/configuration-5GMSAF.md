---
layout: default
title:  Configuration 5GMS AF
parent: Tutorials
grand_parent: 5G Downlink Media Streaming
has_children: false
nav_order: 1
---

# Configuration of the 5GMSd Application Function

The configuration file for the 5GMSd Application function contains several settings

## File Locations

The configuration file for the 5GMSd Application Function can be found in `${prefix}/etc/open5gs/msaf.yaml`, where `${prefix}` is
the prefix used in the `meson` command (or `/usr/local` by default). By default this means that the configuration file will be
found in `/usr/local/etc/open5gs/msaf.yaml`.

The location of the configuration file can be overridden at run-time by using the `-c` command line parameter with the
`open5gs-msafd` command, for example:

```bash
/usr/local/bin/open5gs-msafd -c local-5gmsaf-config.yaml
```

## Configuration File Format

The configuration file is written in [YAML](https://yaml.org/) 1.1 file format.

Various settings in the file control things like logging output, listening and connection addresses, details of associated 5GMSd
Application Servers and other presets.

### Notation

Throughout this documentation we refer to the location of these configuration properties using a '`.`' separated path. Where a property name contains a `.` character it will be quoted using double quotes. For eaxmple, take the following snippet of YAML:

```yaml
YAML:
  files contain:
  - version 1.1: textual value
```

We would refer to the field holding the value '`textual value`' as `YAML.files contain."version 1.1"`.

### Configuration Structure

The following are the properties in the 5GMSd Application Function configuration file and typical/default values:

```yaml
logging:
  level: info
  domain: msaf

sbi:
  server:
    no_tls: true
  client:
    no_tls: true

msaf:
  open5gsIntegration: false
  sbi:
    - addr: 0.0.0.0
      port: 7778
  m1:                                   # Added in v1.2.0
    - addr: 0.0.0.0                     # Added in v1.2.0
      port: 7778                        # Added in v1.2.0
  m5:                                   # Added in v1.2.0
    - addr: 0.0.0.0                     # Added in v1.2.0
      port: 7778                        # Added in v1.2.0
  maf:                                  # Added in v1.2.0
    - addr: 127.0.0.25                  # Added in v1.2.0
      port: 7777                        # Added in v1.2.0
  applicationServers:
    - canonicalHostname: localhost
      urlPathPrefixFormat: /m4d/provisioning-session-{provisioningSessionId}/
      m3Host: localhost                                                    # Added in v1.4.0
      m3Port: 7777                                                         # Added in v1.1.0
  certificate: examples/CertificatesIndex.json                             # Removed in v1.2.0
  contentHostingConfiguration: examples/ContentHostingConfiguration.json   # Removed in v1.2.0
  provisioningSessionId: 12345678-9abc-def0-123456789abc                   # Removed in v1.1.0
  certificateManager: /usr/local/libexec/rt-5gms/af/self-signed-certmgr    # Added in v1.2.0
  serverResponseCacheControl:                                              # Added in v1.2.0
    - maxAge: 60                                                           # Added in v1.2.0
      m1ProvisioningSessions: 60                                           # Added in v1.2.0
      m1ContentHostingConfigurations: 60                                   # Added in v1.2.0
      m1ServerCertificates: 60                                             # Added in v1.2.0
      m1ContentProtocols: 86400                                            # Added in v1.2.0
      m5ServiceAccessInformation: 60                                       # Added in v1.2.0
  dataCollectionDir: /usr/local/var/log/open5gs/reports                    # Added in v1.4.0
  offerNetworkAssistance: false                                            # Added in v1.4.0
  networkAssistance:                                                       # Added in v1.4.0
    deliveryBoost:                                                         # Added in v1.4.0
      minDlBitRate: 1 Mbps                                                 # Added in v1.4.0
      boostPeriod: 30                                                      # Added in v1.4.0 

nrf:
  sbi:
    - addr:
      - 127.0.0.10
      - ::1
      port: 7777

bsf:
  notificationListener:                                                    # Added in v1.4.0
    - addr:
      - 127.0.0.99
      port: 7779

parameter:
  no_ipv4: false
  no_ipv6: false
  prefer_ipv4: false

time:
  nf_instance:
    heartbeat: 0
  message:
    duration: 10000

```

### Referencing other files

The configuration file may also reference other files. If such a reference is made then the reference is either an absolute path or a relative path to file. If it is a relative path then it is relative to the location of the configuration file.

**Warning: Be careful when moving a `msaf.yaml` configuration file to a different directory in the filesystem as any relative
pathed properties will no longer point to the correct location and will either need to be changed or the referenced files will also need to be moved too to maintain their relative paths.**

The following properties may optionally contain relative paths:
- `msaf.certificates` - This is the JSON certificates index, see [Certificates Index](#certificates-index) for more details.
- `msaf.contentHostingConfiguration` - This is a ContentHostingConfiguration JSON object used to configure the 5GMSd Application
  Server, see [ContentHostingConfiguration file](#contenthostingconfiguration-file) for more details.

## Configuration Properties

This section lists the properties in the configuration file, their use and valid values.

### Logging

**Location(s):** `logging.level` and `logging.domain`

#### Logging Level

The `logging.level` indicates the minimum level of logging messages that will be output. The default is `info`.

Allowable values are: `trace`, `debug`, `info`, `warn`, `error`, `fatal` and `none`

When `logging.domain` is also set, then this setting only affects the minimum logging level for the listed domains.

#### Logging Domain

The `logging.domain` property limits the affect of the `logging.level` property. This contains a comma separated list of domains.

Domains relevant to the 5GMSd Application Function are:
- `msaf` - 5GMSd Application Function specific logging
- `sbi`  - Open5GS SBI library functions for Client/Server operations.
- `app`  - Open5GS App library functions for generic Open5GS application routines.
- `core` - Open5GS Core functions (e.g. low level socket handling, textual parsing and formatting, and memory management routines).

#### Suggested Logging Configurations

To reduce logging to warnings, errors and fatal messages only:

```yaml
logging:
  level: warn
```

To stop all logging:

```yaml
logging:
  level: none
```

To turn debugging output on for the 5GMSd Application Function:

```yaml
logging:
  level: debug
  domain: msaf
```

### SBI interface security

**Location(s):** `sbi.server.no_tls`, `sbi.server.cacert`, `sbi.server.key`, `sbi.server.cert`, `sbi.client.no_tls`, `sbi.client.cacert`, `sbi.client.key` and `sbi.client.cert`

The `sbi.server.no_tls` indicates whether TLS should be configured for SBI server listening sockets. If `false` then no TLS is configured and the `sbi.server.cacert`, `sbi.server.key` and `sbi.server.cert` properties are ignored. If the `sbi.server.no_tls` property is `true` then the server will use:
- `sbi.server.cacert` is the filename of a file containing a CA bundle, in PEM format, to use to authenticate client public certificates.
- `sbi.server.key` is the filename of the private key, in PEM format, which is used for TLS connections for server sockets.
- `sbi.server.cert` is the filename of the public certificate, in PEM format, that will be presented as server authentication for TLS connections for server sockets.

The `sbi.client.no_tls` indicates whether TLS should be configured for outgoing client requests to other NFs. If `false` then no TLS is configured and the `sbi.client.cacert`, `sbi.client.key` and `sbi.client.cert` properties are ignored. If the `sbi.client.no_tls` property is `true` then outgoing client requests will use:
- `sbi.client.cacert` is the filename of a file containing a CA bundle, in PEM format, to use to authenticate the server certificate presented by the remote NF.
- `sbi.client.key` is the filename of a private key, in PEM format, to use for encrypting the client communications.
- `sbi.client.cert` is the filename of the public certificate, in PEM format, to use for authenticating the client with the NF.

### Open5GS integration

**Location(s):** `msaf.open5gsIntegration`

This is a boolean value (`true` or `false`) which indicates whether or not the 5GMSd Application Function will attempt to register
with a 5G Core, specifically the NRF.

If this value is `true` then the `nrf` properties will describe the connection information for the NRF to register with. See
[NRF Connection](#nrf-connection) for more details.

This is required to be `true` if you wish to use the Network Assistance or Dynamic Policies features.

### SBI and default Interface Listening Address

**Location(s):** `msaf.sbi.addr` and `msaf.sbi.port`

The listening IP address is set in `msaf.sbi.addr` and the TCP port number is set in `msaf.sbi.port`.

This address is used for SBI communications with other 5G Core Network Functions. It is also the default address for M1, M5 and
Management interfaces if they are not explicitly set in the configuration.

### M1 Interface Listening Address

**Location(s):** `msaf.m1.addr` and `msaf.m1.port`
**Version:** v1.2.0 and above

The listening IP address is set in `msaf.m1.addr` and the TCP port number is set in `msaf.m1.port`.

This is the communication address for external Application Service Providers to configure their services via the interface at
reference point M1.

### M5 Interface Listening Address

**Location(s):** `msaf.m5.addr` and `msaf.m5.port`
**Version:** v1.2.0 and above

The listening IP address is set in `msaf.m5.addr` and the TCP port number is set in `msaf.m5.port`.

This is the communication address for the 5GMSd Aware Application on the User Equipment implementing the interface at reference
point M5.

### 5GMS AF Management Interface Listening Address

**Location(s):** `msaf.maf.addr` and `msaf.maf.port`
**Version:** v1.2.0 and above

The listening IP address is set in `msaf.maf.addr` and the TCP port number is set in `msaf.maf.port`.

This is a communication interface for local 5GMSd Application Function management. This is not specified in TS 26.512 and is an
extra interface for this implementation. This should always be listening on a secure network, e.g. localhost only.

### Application Servers

**Location(s):** `msaf.applicationServers`

This property is a list of associated 5GMSd Application Servers. Each entry in the list must contain `canonicalHostname`,
`urlPathPrefixFormat` and `m3Port` (since v1.1.0) properties.

The `canonicalHostname` is the hostname or IP address of the Application Server. This is used to generate `mediaPlayerEntry` URLs for the ServiceAccessInformation objects available at interface M5 if no `domainNameAlias` is given in the ContentHostingConfiguration. From v1.1.0 of the Application Function, this is also the address that the Application Function will use for interface M3 communication with the Application Server.

The `urlPathPrefixFormat` is a template string that is used to set the first part of the URL path for distributions from the Application Server at interface M4. Where the template contains `{provisioningSessionId}` will be replaced by the provisioning session Id that is associated with the ContentHostingConfiguration.

The host name which is used for contacting the Application Server on the interface at M3 will be the `canonicalHostname` unless an `m3Host` property is defined for the application server, in which case the value of `m3Host` will be used as the host name to contact the Application Server at.

The TCP port at which the Application Server interface at M3 is listening is defined by the `m3Port` property. The combination of `canonicalHostname` or `m3Host` and `m3Port` identifies the connection address that the Application Function will use. This property is only available from v1.1.0 onwards.

Example:
```yaml
msaf:
  applicationServers:
    - canonicalHostname: ext-as.example.com
      urlPathPrefixFormat: /{provisioningSessionId}/
      m3Host: localhost
      m3Port: 7777
```

### Data Collection (Consumption Reporting)

**Location(s):** `msaf.dataCollectionDir`
**Versions:** v1.4.0 and above

The Consumption Reporting feature uses a data collection directory to store sent reports in. The path for the data collection root can be set in `msaf.dataCollectionDir`. If not set then consumption reports are discarded after being received. There is no house-keeping for this directory, so an external house-keeping process must be used to free up disk space.

### Network Assistance

**Location(s):** `msaf.open5gsIntegration`, `msaf.offerNetworkAssistance`, `msaf.networkAssistance`, `nrf.sbi` and `bsf.notificationListener`
**Versions:** v1.4.0 and above

The Network Assistance feature requires both `msaf.open5gsIntegration` and `msaf.offerNetworkAssistance` to be `true` (or `yes`) to activate. The `nrf` settings must also point to a valid NRF NF, and will be used to find a BSF and/or the PCF which is handling the policies for the UE. The `bsf.notificationListener` sets the address and optional port that will be used to listen for BSF notifications.

When active, this feature will be advertised as available via the Service Access Information objects returned from requests at interface M5.

The Delivery Boost Network Assistance feature will request a guaranteed minimum bit rate for a period of time on behalf of the client. The minimum bit rate used and the period of time are both configurable by setting the values for `msaf.networkAssistance.deliveryBoost.minDlBitRate` and `msaf.networkAssistance.deliveryBoost.boostPeriod` respectively. The `msaf.networkAssistance.deliveryBoost.minDlBitRate` must be expressed as a BitRate string according to TS 29.571, this is a decimal number followed by the bit rate units (`bps`, `Kbps`, `Mbps`, `Gbps` or `Tbps`), e.g. "0.5 Mbps" or "60 Kbps". The `msaf.networkAssistance.deliveryBoost.boostPeriod` is the integer number of seconds the boost will be activated for. These default to 1 Mbps for 30 seconds.

Example of active Network Assistance:
```yaml
msaf:
  open5gsIntegration: yes
  offerNetworkAssistance: yes
  networkAssistance:
    deliveryBoost:
      minDlBitRate: 1 Mbps
      boostPeriod: 30

nrf:
  sbi:
    - addr: 127.0.0.10
      port: 7777

bsf:
  notificationListener:
    - addr: 127.0.0.99
```

### Dynamic Policies

**Location(s):** `msaf.open5gsIntegration`, `nrf.sbi` and `bsf.notificationListener`
**Versions:** v1.4.0 and above

This feature requires the `msaf.open5gsIntegration` to be `true` (or `yes`) and the `nrf` settings to point to a valid NRF NF. The `bsf.notificationListener` sets the address and optional port that will be used to listen for BSF notifications.

Example of active Network Assistance:
```yaml 
msaf:
  open5gsIntegration: yes
  
nrf:
  sbi:
    - addr: 127.0.0.10
      port: 7777
      
bsf:
  notificationListener:
    - addr: 127.0.0.99
      port: 9000     
```

### ContentHostingConfiguration file

<span style='color:red'>**Note:** This setting is removed from v1.2.0 onwards</span>

**Location(s):** `msaf.contentHostingConfiguration`
**Version:** Up to and including v1.1, removed in v1.2.0 onwards

The hosting configuration to use comes from a ContentHostingConfiguration JSON object held in an external file. The file-path to this JSON file is stored in the `msaf.contentHostingConfiguration` property using an absolute or relative (to the `msaf.yaml` configuration file) file-path.

The ContentHostingConfiguration determines the configuration of the 5GMSd Application Server including which certificates and keys to send to the Application Server.

### Certificates Index

<span style='color:red'>**Note:** This setting will be removed from v1.2.0 onwards</span>

**Location(s):** `msaf.certificates`
**Version:** Up to and including v1.1, removed in v1.2.0 onwards

To test the distribution of media via secure HTTPS, the 5GMSd Application Function (and at runtime the 5GMSd Application Server which
will provide the hosting of the media) needs to be configured with one or more private key and public certificate pairs that can be
referenced from the ContentHostingConfiguration.

To provide this configuration the 5GMSd Application Function, an index file is used to map certificateId values to a file containing the private key, public certificate and optionally any intermediate CA public certificates, all in PEM format. The index file itself contains a JSON object where the keys are the certificateIds as found in the COntentHostingConfiguration files and the values are the relative (to the index file) or absolute path to the PEM file.

The filename of this JSON index file is stored in the `msaf.certificates` property of the `msaf.yaml` configuration file as a relative (to the configuration file) or absolute path.

For a utility to quickly generate self-signed test certificates for a configuration please see the section below on [Generating Test Certificates](#generating-test-certificates).

### Provisioning Session Id

<span style='color:red'>**Note:** This setting is removed from v1.1.0 onwards</span>

**Location(s):** `msaf.provisioningSessionId`
**Version:** Up to and including v1.0, removed in v1.1.0 onwards

This setting provides the ProvisioningSessionId to use for MVP#2. This is here so that the Application Function and Application
Server can be synchronised with the same identifier in their respective configurations.

This is the only ProvisioningSessionId the MVP#2 5GMSd Application Function will use.

### Certificate Manager Program

**Location(s):** `msaf.certificateManager`
**Version:** From version v1.2.0 onwards

This is the path of an external program that can manage certificates and request signing of certificates. The example certificate
manager program will produce simple self signed certificates and will be the default certificate manager program set in the
installed configuration.

The Certificate Manager program follows the "External Certificate Management" specification from the ["Implement M1 Server Certificates Provisionign API" issue on github](https://github.com/5G-MAG/rt-5gms-application-function/issues/17).

### Default caching ages

**Location(s):** `msaf.serverResponseCacheControl.maxAge`, `msaf.serverResponseCacheControl.m1ProvisioningSessions`,
                 `msaf.serverResponseCacheControl.m1ContentHostingConfigurations`,
                 `msaf.serverResponseCacheControl.m1ServerCertificates`, `msaf.serverResponseCacheControl.m1ContentProtocols`,
                 `msaf.serverResponseCacheControl.m5ServiceAccessInformation`
**Version:** From version v1.2.0 onwards

These configuration values give the caching time in seconds signalled with responses in the different interfaces.

| Parameter | Purpose |
| --- | --- |
| `maxAge` | The default `max-age` caching value. |
| `m1ProvisioningSessions` | The `max-age` for responses for the M1 ProvisioningSessions API. |
| `m1ContentHostingConfigurations` | The `max-age` for responses for the M1 ContentHostingProvisioning API. |
| `m1ServerCertificates` | The `max-age` for responses for the M1 ServerCertificatesProvisioning API. |
| `m1ContentProtocols` | The `max-age` for responses for the M1 ContentProtocolsDiscovery API. |
| `m5ServiceAccessInformation` | The `max-age` for responses for the M5 ServiceAccessInformation API. |

## Generating Test Certificates

<span style='color:red'>**Note:** These instructions are not needed from v1.2.0 onwards as certificates are dynamically generated
and signed.</span>

To make the generation of certificates easier for testing, a script is available in the `~/rt-5gms-application-function/subprojects/rt-common-shared/5gms/scripts/make_self_signed_certs.py` which will generate an appropriate set of self-signed test certificates. This script requires the `python3` and `openssl` commands to be present, and the Python 3 YAML module. The script executes in the `python3` environment and uses the `openssl` command to generate the PEM certificate and private key file.

If `openssl`, `python3` or Python3 yaml module are not already installed then they can be installed from your system package manager, for example:

**Ubuntu/Debian and deviratives**
```bash
sudo apt -y install openssl python3 python3-yaml
```

**RedHat/CentOS/Fedora/Rocky and derivatives**
```bash
sudo dnf -y install openssl python3 python3-pyyaml
```

The `make_self_signed_certs.py` script takes either an Application Function configuration file path or two command line parameters, the first is the file-path for a ContentHostingConfiguration JSON file representing the output of the Application Function and the
second is the file-path of a certificates index JSON file. When using this script with the Application Function it is easier to use
the former command syntax.

The script will examine the Application Function configuration file and extract the ContentHostingConfiguration. This is then examined for the certificateIds that are referenced and will create the private key and public certificate in PEM format at the file-path referenced from the certificates index JSON file. The generated certificates are self-signed, valid for 30 days and will include the `canonicalHostame` from the AF configuration and any `domainNameAlias` values from the ContentHostingConfiguration as Subject Alternative Names for the generated certificates.

For example:

```bash
~/rt-5gms-application-function/subprojects/rt-common-shared/5gms/scripts/make_self_signed_certs.py \
    --af-conf=/usr/local/etc/open5gs/msaf.yaml
```
