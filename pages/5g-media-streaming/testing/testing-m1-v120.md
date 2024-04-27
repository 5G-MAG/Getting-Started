---
layout: default
title:  Testing M1 AF v1.2.x
parent: Testing
grand_parent: 5G Downlink Media Streaming
has_children: false
nav_order: 5
---

# Testing: M1 Interface (5GMSd Application Function v1.2.x)

To prepare, follow the instructions for [local user building and installation](Testing-as-a-Local-User).

These tests require a [5GMSd Application Server](https://github.com/5G-MAG/rt-5gms-application-server) to be running. Please follow
the instructions to [build, install and run the 5GMSd Application Server](https://github.com/5G-MAG/rt-5gms-application-server#readme) as a system service or the [instructions to run the AS as a local user](https://github.com/5G-MAG/rt-5gms-application-server/wiki/Development-and-Testing) for a temporary installation for testing.

## Test Provisioning Sessions

This will test the ability of the Application Function to allocate and retrieve information about provisioning session upon request by an Application Provider.

### Create provisioning sessions

1. Stop the Application Function if it is already running.

1. Remove previous configurations:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the Application Function:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Create a single Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-provisioning-session -e MyAppId -a MyASPId
   ```

1. Check the Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list
   ```

   This should list a single provisioning session.

1. Create a second Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-provisioning-session -e MyAppId -a MyASPId
   ```

1. Check the Provisioning Sessions:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list
   ```

   This should list the two provisioning sessions.

### Get details for a provisioning session

1. Stop the Application Function if it is already running.

1. Remove previous configurations:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the Application Function:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Create a single Provisioning Session with Content Hosting Configuration

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-stream -e MyAppId -a MyASPId -n 'Big Buck Bunny' 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
   ```

1. Check the Provisioning Session details:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list -v
   ```

   This will list the provisioning session showing the Content Hosting Configuration attached to it.

   For example:

   ```
   1c961622-c803-41ed-83c5-e304b44dbd7e:
     Certificates:
     ContentHostingConfiguration:
       Name: Big Buck Bunny
       Entry Point Path: BigBuckBunny_4s_onDemand_2014_05_09.mpd
       Ingest:
           Type: urn:3gpp:5gms:content-protocol:http-pull-ingest
           URL: https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/
       Distributions:
         - URL: http://localhost/m4d/provisioning-session-1c961622-c803-41ed-83c5-e304b44dbd7e/
           Canonical Domain Name: localhost
   ```

### Delete a provisioning session

1. Stop the Application Function if it is already running.

1. Remove previous configurations:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the Application Function:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Create a single Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-provisioning-session -e MyAppId -a MyASPId
   ```

1. Check the Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list
   ```

   This should list a single provisioning session.

1. Delete the Provisioning Session by Id:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session del-stream -p ${provisioning_session_id}
   ```

   Where `${provisioning_session_id}` is the provisioning session id of the session that was created in the earlier step.

   For example:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session del-stream -p 1c961622-c803-41ed-83c5-e304b44dbd7e
   ```

1. Check the Provisioning Session is deleted:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list
   ```

   There should be no provisioning sessions listed.

1. Create a single Provisioning Session with a stream identifier:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-stream -e MyAppId -a MyASPId -n 'Test Stream' 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
   ```

1. Check the Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list -v
   ```

1. Delete the Provisioning Session by ingest URL and entry point path:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session del-stream 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
   ```

1. Check the Provisioning Session is deleted:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list
   ```

   There should be no provisioning sessions listed.

## Server Certificates

### Create Server Certificates

1. Stop the Application Function if it is already running.

1. Remove previous configurations:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the Application Function:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Create a single Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-provisioning-session -e MyAppId -a MyASPId
   ```

1. Create a certificate:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-certificate -p ${provisioning_session_id}
   ```

   Where `${provisioning_session_id}` is the provisioning session id of the session that was created in the previous step.

1. Check the Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list -v
   ```

   The output should show a provisioning session with a single certificate where the subject and issuer of the certificate are
   identical.

   For example:

   ```
   40b75340-c8a3-41ed-9d6e-cbf27240da7a:
     Certificates:
       4fff7e04-c8a3-41ed-9d6e-cbf27240da7a:
         Serial = 723264618754945153424478507276304617300583059881
         Not before = 2023-03-22 11:18:46+00:00
         Not after = 2023-06-20 11:18:46+00:00
         Subject = C=GB,L=London,CN=localhost
                   key=C2:56:2C:A6:D7:B3:AE:C7:3A:2C:18:9D:5B:2A:EB:62:C0:7E:35:05
         Issuer = C=GB,L=London,CN=localhost
                  key=C2:56:2C:A6:D7:B3:AE:C7:3A:2C:18:9D:5B:2A:EB:62:C0:7E:35:05
         Subject Alternative Names:
           DNS:localhost
     ContentHostingConfiguration:
       Not defined
   ```

   This shows that for provisioning session 40b75340-c8a3-41ed-9d6e-cbf27240da7a there is a certificate with id
   4fff7e04-c8a3-41ed-9d6e-cbf27240da7a lasting for 90 days from 22nd Mar 2023. The "Subject" and "Issuer" both have the same
   designated name ("C=GB,L=London,CN=localhost") and key hash, showing that this is a self signed certificate. The
   "Subject Alternative Names" contains one "DNS" entry for the canonical name of the 5GMSd Application Server.

1. Create a certificate with a domain name:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-certificate -p ${provisioning_session_id} -d as.example.com
   ```

   Since a domain name was requested, the `m1-session` tool will request a CSR from the 5GMSd Application Function and sign it
   itself.

1. Check the Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list -v
   ```

   The output should now show an extra certificate on the provisioning session.

   For example:

   ```
   40b75340-c8a3-41ed-9d6e-cbf27240da7a:
     Certificates:
       4fff7e04-c8a3-41ed-9d6e-cbf27240da7a:
         Serial = 723264618754945153424478507276304617300583059881
         Not before = 2023-03-22 11:18:46+00:00
         Not after = 2023-06-20 11:18:46+00:00
         Subject = C=GB,L=London,CN=localhost
                   key=C2:56:2C:A6:D7:B3:AE:C7:3A:2C:18:9D:5B:2A:EB:62:C0:7E:35:05
         Issuer = C=GB,L=London,CN=localhost
                  key=C2:56:2C:A6:D7:B3:AE:C7:3A:2C:18:9D:5B:2A:EB:62:C0:7E:35:05
         Subject Alternative Names:
           DNS:localhost
       8aa9e5ac-c8a9-41ed-9d6e-cbf27240da7a:
         Serial = 1
         Not before = 2023-03-22 12:03:22+00:00
         Not after = 2023-04-21 12:03:22+00:00
         Subject = CN=as.example.com,O=5G-MAG
                   key=37:62:38:E1:D2:18:23:90:A9:12:2A:C7:EF:5F:7E:F8:91:3A:89:8F
         Issuer = O=5G-MAG,CN=5G-MAG Reference Tools Local CA
                  key=B4:2F:13:EE:02:D0:34:75:C0:7B:9D:C7:67:6D:90:76:F5:A8:CC:EF
         Subject Alternative Names:
           DNS:as.example.com
           DNS:localhost
     ContentHostingConfiguration:
       Not defined
   ```

   This shows that there is now a second certificate (8aa9e5ac-c8a9-41ed-9d6e-cbf27240da7a) issued by
   "5G-MAG Reference Tools Local CA" and the Subject Common Name is the domain name alias used with the `-d` command line option
   when the certificate was created. The canonical domain name of the 5GMSd Application Server is the second Subject Alternative
   Name. These certificates last for 30 days by default.

1. Reserve a certificate:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-certificate -p ${provisioning_session_id} --csr
   ```

   The output includes the new certificate id and a CSR in PEM format.

1. Check the Provisioning Session:

    ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list -v
   ```

   The output should now show a third certificate id but the certificate detail says "Certificate not yet uploaded".

   For example:

   ```
   40b75340-c8a3-41ed-9d6e-cbf27240da7a:
     Certificates:
       4fff7e04-c8a3-41ed-9d6e-cbf27240da7a:
         Serial = 723264618754945153424478507276304617300583059881
         Not before = 2023-03-22 11:18:46+00:00
         Not after = 2023-06-20 11:18:46+00:00
         Subject = C=GB,L=London,CN=localhost
                   key=C2:56:2C:A6:D7:B3:AE:C7:3A:2C:18:9D:5B:2A:EB:62:C0:7E:35:05
         Issuer = C=GB,L=London,CN=localhost
                  key=C2:56:2C:A6:D7:B3:AE:C7:3A:2C:18:9D:5B:2A:EB:62:C0:7E:35:05
         Subject Alternative Names:
           DNS:localhost
       8aa9e5ac-c8a9-41ed-9d6e-cbf27240da7a:
         Serial = 1
         Not before = 2023-03-22 12:03:22+00:00
         Not after = 2023-04-21 12:03:22+00:00
         Subject = CN=as.example.com,O=5G-MAG
                   key=37:62:38:E1:D2:18:23:90:A9:12:2A:C7:EF:5F:7E:F8:91:3A:89:8F
         Issuer = O=5G-MAG,CN=5G-MAG Reference Tools Local CA
                  key=B4:2F:13:EE:02:D0:34:75:C0:7B:9D:C7:67:6D:90:76:F5:A8:CC:EF
         Subject Alternative Names:
           DNS:as.example.com
           DNS:localhost
       2a118b8e-c8a7-41ed-9d6e-cbf27240da7a:
         Certificate not yet uploaded
     ContentHostingConfiguration:
       Not defined
   ```

   This shows that the 2a118b8e-c8a7-41ed-9d6e-cbf27240da7a certificate is waiting for a signed certificate to be uploaded.

### Output certificate details

1. Stop the Application Function if it is already running.

1. Remove previous configurations:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the Application Function:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Create a single Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-provisioning-session -e MyAppId -a MyASPId
   ```

1. Create a certificate

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-certificate -p ${provisioning_session_id}
   ```

   Where `${provisioning_session_id}` is the provisioning session id of the session that was created in the previous step.

1. Display the details of the certificate

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session show-certificate -p ${provisioning_session_id} -c ${certificate_id}
   ```

   Where `${provisioning_session_id}` is the provisioning session id of the session that was created in step 4 and
   `${certificate_id}` is the certificate id of the certificate created in the previous step.

   This will display the certificate details.

   For example:

   ```
   Certificate details for d921a6e2-c977-41ed-ae8f-4f7bb018a30b:
     Serial = 570812267048735513617861647966053937458169779179
     Not before = 2023-03-23 12:40:10+00:00
     Not after = 2023-06-21 12:40:10+00:00
     Subject = C=GB,L=London,CN=localhost
               key=E9:61:FD:5A:31:0C:ED:C0:B0:CC:29:0D:29:89:AE:EE:F9:25:89:CA
     Issuer = C=GB,L=London,CN=localhost
              key=E9:61:FD:5A:31:0C:ED:C0:B0:CC:29:0D:29:89:AE:EE:F9:25:89:CA
     Subject Alternative Names:
       DNS:localhost
   ```

1. Display the public certificate PEM data

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session show-certificate -p ${provisioning_session_id} -c ${certificate_id} -r
   ```

   The `-r` flag causes the command to display the "raw" output which is the PEM data for the certificate.

   For example:

   ```
   -----BEGIN CERTIFICATE-----
   MIIDWzCCAkOgAwIBAgIUY/wbeD1YUiEeBPLpxf8ldkkEE+swDQYJKoZIhvcNAQEL
   BQAwMjELMAkGA1UEBhMCR0IxDzANBgNVBAcMBkxvbmRvbjESMBAGA1UEAwwJbG9j
   YWxob3N0MB4XDTIzMDMyMzEyNDAxMFoXDTIzMDYyMTEyNDAxMFowMjELMAkGA1UE
   BhMCR0IxDzANBgNVBAcMBkxvbmRvbjESMBAGA1UEAwwJbG9jYWxob3N0MIIBIjAN
   BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0bftLTaaXXpW1qIDHYTTmeIGvupy
   G/dQpK5Ko9mW9IEcb+wfn2fX8SMHGA7O8TvpqUGEmyoBXIuIFmmeR+w5xQRcKkyi
   NGhIhnUIfOqaevh4MCX/8Ius9NOjF0bz+aWtwOCmWKkNvknRMzClAeVRJm6g+U6m
   IH30TE5H3ItiYxk63MNvuYeqIEK2rEKu69jWvTFkV1Wzd+5rH3ZC9qrt4uryUqAZ
   X6XPx5AkQzbnBRQooDJzhqKgW+7YFWFtwi6WX8poGwx4RuruxYRLEBDfxRCE/1k6
   ALP3IktsVp7rFqwOt0LRNH1+MLly/MIOEA+NjnaIReG3/6Kt7oAqiDCBpQIDAQAB
   o2kwZzAdBgNVHQ4EFgQU6WH9WjEM7cCwzCkNKYmu7vklicowHwYDVR0jBBgwFoAU
   6WH9WjEM7cCwzCkNKYmu7vklicowDwYDVR0TAQH/BAUwAwEB/zAUBgNVHREEDTAL
   gglsb2NhbGhvc3QwDQYJKoZIhvcNAQELBQADggEBAIAELtWEMwzoXnaWRn74JngW
   3DF5IUtdFOiEKPWzdju+RleUsQHm5hsbPxpAz/MDVKIQQBGrJNMNpMtJ1VNlAsJ1
   7gndSkSFf0zw7+DxgKYiwNj7tbBU8yTW+qVyUJh6XUxOHlaLjXzct4jw/NgjrjRZ
   YuwXKCebRf+DUtQGt87rSib+GVpI//XBweyd8D0vFnGPRU9yyAvuqUdfu7enGFMr
   qyBBqTqrTgX9o852lrMnWbc+g+of90Ym9HkVpifmc12jZSJlfS4cykvwnRqwPC9f
   YnNABBMDJwJOM8g69OIRw+67O01ZulRzCvSaSbBEG6xC08XAD7BJn9CPIMypHdw=
   -----END CERTIFICATE-----
   ```

### Upload a public certificate

**TODO:** Test where we reserve a certificate and the fetch CSR for the new certificate, sign it, and upload the result.

## Content Protocol Discovery

### List the Content Protocols available

1. Stop the Application Function if it is already running.

1. Remove previous configurations:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the Application Function:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Create a single Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-provisioning-session -e MyAppId -a MyASPId
   ```

1. List the Content Protocols for the Provisioning Session

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session protocols -p ${provisioning_session_id}
   ```

   Where `${provisioning_session_id}` is the provisioning session id of the session that was created in the previous step.

   The available protocols will be listed.

   For example:

   ```
   Protocols for 40b75340-c8a3-41ed-9d6e-cbf27240da7a:
     Downlink:
       urn:3gpp:5gms:content-protocol:http-pull-ingest
     No uplink capability
     No geo-fencing capability
   ```

## Content Hosting Provisioning

### Add a Content Hosting Configuration without certificates

1. Stop the Application Function if it is already running.

1. Remove previous configurations:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the Application Function:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Create a single Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-provisioning-session -e MyAppId -a MyASPId
   ```

1. Create the hosting configuration:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session set-stream -p ${provisioning_session_id} ~/rt-5gms-application-function/examples/ContentHostingConfiguration_Big-Buck-Bunny_pull-ingest.json
   ```

   Where `${provisioning_session_id}` is the provisioning session id of the session that was created in the previous step.

1. Check the provisioning session configuration:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list -v
   ```

   This will display the provisioning session created, showing no certificates and the details from the example
   ContentHostingConfiguration.

   For example:

   ```
   2ef78712-c9a0-41ed-ac37-f9964ab0d12a:
     Certificates:
     ContentHostingConfiguration:
       Name: Big Buck Bunny
       Entry Point Path: BigBuckBunny_4s_onDemand_2014_05_09.mpd
       Ingest:
           Type: urn:3gpp:5gms:content-protocol:http-pull-ingest
           URL: https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/
       Distributions:
         - URL: http://localhost/m4d/provisioning-session-2ef78712-c9a0-41ed-ac37-f9964ab0d12a/
           Canonical Domain Name: localhost
   ```

**Note:** The `m1-session new-stream` command is a convience command that will create a provisioning session, generate the
ContentHostingConfiguration and set it in the newly created provisioning session. The above can also be done using:
```
~/rt-5gms-application-function/install/bin/m1-session new-stream -e MyAppId -a MyASPId -n 'Big Buck Bunny' 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
```

### Add a Content Hosting Configuration which uses an existing certificate

1. Stop the Application Function if it is already running.

1. Remove previous configurations:

   ```bash
   rm -rf ~/rt-5gms-application-function/install/var/cache/rt-5gms/af/certificates
   ```

1. Start the Application Function:

   ```bash
   ~/rt-5gms-application-function/install/bin/open5gs-msafd
   ```

1. Create a single Provisioning Session:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-provisioning-session -e MyAppId -a MyASPId
   ```

1. Create a certificate:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session new-certificate -p ${provisioning_session_id}
   ```

   Where `${provisioning_session_id}` is the provisioning session id of the session that was created in the previous step.

1. Generate a ContentHostingConfiguration using the certificate:

   ```bash
   sed "s/@certificate-id@/${certificate_id}/g" ~/rt-5gms-application-function/examples/ContentHostingConfiguration_Big-Buck-Bunny_pull-ingest_https.json.tmpl > chc.json
   ```

   Where `${certificate_id}` is the certificate id of the certificate created in the previous step.

1. Create the hosting configuration using the generated ContentHostingConfiguration:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session set-stream -p ${provisioning_session_id} chc.json
   ```

   Where `${provisioning_session_id}` is the provisioning session id of the session that was created in step 4.

1. Check the provisioning session configuration:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session list -v
   ```

   This will display the provisioning session created, showing no certificates and the details from the example
   ContentHostingConfiguration.

   For example:

   ```
   ed5079d6-c9a4-41ed-b2ad-41232d457177:
     Certificates:
       fbd05ddc-c9a4-41ed-b2ad-41232d457177:
         Serial = 186484472102456711697672477872825927418601662068
         Not before = 2023-03-23 18:03:15+00:00
         Not after = 2023-06-21 18:03:15+00:00
         Subject = C=GB,L=London,CN=localhost
                   key=8A:C2:9A:48:15:6A:15:BB:EE:B7:A0:9E:07:7C:CB:A4:CF:7C:51:F5
         Issuer = C=GB,L=London,CN=localhost
                  key=8A:C2:9A:48:15:6A:15:BB:EE:B7:A0:9E:07:7C:CB:A4:CF:7C:51:F5
         Subject Alternative Names:
           DNS:localhost
     ContentHostingConfiguration:
       Name: Big Buck Bunny
       Entry Point Path: BigBuckBunny_4s_onDemand_2014_05_09.mpd
       Ingest:
           Type: urn:3gpp:5gms:content-protocol:http-pull-ingest
           URL: https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/
       Distributions:
         - URL: https://localhost/m4d/provisioning-session-ed5079d6-c9a4-41ed-b2ad-41232d457177/
           Canonical Domain Name: localhost
           Certificate: fbd05ddc-c9a4-41ed-b2ad-41232d457177
   ```

**Note:** The `m1-session new-stream` command is a convience command that will create a provisioning session, generate the
ContentHostingConfiguration and set it in the newly created provisioning session. The above configuration with the `m1-session` tool can also be done using this single command instead:
```
~/rt-5gms-application-function/install/bin/m1-session new-stream -e MyAppId -a MyASPId -n 'Big Buck Bunny' --ssl-only 'https://ftp.itec.aau.at/datasets/DASHDataset2014/BigBuckBunny/4sec/' 'BigBuckBunny_4s_onDemand_2014_05_09.mpd'
```
