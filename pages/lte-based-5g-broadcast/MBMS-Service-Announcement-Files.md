---
layout: default
title:  MBMS Service Announcement Files
parent: Tutorials
grand_parent: MBMS and LTE-based 5G Broadcast
has_children: false
nav_order: 0
---

# MBMS Service Announcement Files

The `ServiceAnnouncement(SA)` file also referred to as `bootstrap.multipart` in the context of 5G-MAG Reference Tools contains important information about the available broadcast and unicast streams. The 5G-MAG Reference Tools support three main formats. The target format needs to be configured before starting the `rt-mbms-mw` process as an automated format detection at runtime is currently not supported.

Examples of the different SA formats can be found in the [rt-common-shared project](https://github.com/5G-MAG/rt-common-shared/tree/feature/mbms/mbms/bootstrap_examples).

## Configuration of the format
The target format can directly be set in `/etc/5gmag-rt.conf` file:

```` 
mw: {
    bootstrap_format: ""
}
````

Possible values are:
* `default`: Format used for the original implementation of seamless switching
* `5gmag_bc_uc`: Format agreed on by 5G-MAG while reviewing the `default` format
* `5gmag_legacy`: Format used for the sample recordings

## Default format
The default format is the one that was used for the original seamless switching implementation implemented in close coordination between ORS and Rohde&Schwarz:

````
MIME-Version: 1.0
Content-Type: multipart/related; boundary="++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--"; type="application/mbms-envelope+xml"
Content-Description: LTE MBMS Service Announcement

--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/mbms-envelope+xml 
Content-Transfer-Encoding: 7bit
Content-Location: file:///envelope.xml

<?xml version="1.0" encoding="utf-8"?>
<metadataEnvelope xmlns="urn:3gpp:metadata:2005:MBMS:envelope"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xsi:schemaLocation="urn:3gpp:metadata:2005:MBMS:envelope MetadataEnvelope.xsd">  
  <item contentType="application/sdp"
        metadataURI="file:///TMGI-0x1009f165.sdp"
        validFrom="2021-10-12T10:59:43Z"
        validUntil="2051-10-05T10:59:43Z"
        version="1"/>  
  <item contentType="application/vnd.apple.mpegurl"
        metadataURI="file:///TMGI-0x1009f165.m3u8"
        validFrom="2021-10-12T10:59:43Z"
        validUntil="2051-10-05T10:59:43Z"
        version="1"/>  
  <item contentType="application/vnd.apple.mpegurl"
        metadataURI="http://localhost:3333/watchfolder/hls/manifest.m3u8"
        validFrom="2021-10-12T10:59:43Z"
        validUntil="2051-10-05T10:59:43Z"
        version="1"/>  
  <item contentType="application/mbms-user-service-description+xml"
        metadataURI="file:///usdBundle.xml"
        validFrom="2021-10-12T10:59:43Z"
        validUntil="2051-10-05T10:59:43Z"
        version="1"/>  
  <item contentType="application/mbms-schedule+xml"
        metadataURI="file:///TMGI-0x1009f165schedule.xml"
        validFrom="2021-10-12T10:59:43Z"
        validUntil="2051-10-05T10:59:43Z"
        version="1"/>
</metadataEnvelope>
--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/sdp
Content-Transfer-Encoding: 7bit
Content-Location: file:///TMGI-0x1009f165.sdp

v=0
o=ROHDE-SCHWARZ-BSCC 269087077 1634036383 IN IP4 11.11.11.11
s=HLS Streaming Session 0x1009f165
i=File Download Session
t=3843025183 4789105183
a=mbms-mode:broadcast-mbsfn 269087077
c=IN IP4 238.1.1.111/127
b=AS:2000
m=application 40101 FLUTE/UDP 0
a=flute-tsi:0
a=flute-ch:1
a=3GPP-QoE-Metrics:metrics={Object_Loss};rate=null;resolution=10
a=3GPP-QoE-Metrics:metrics={Network_Resource};rate=null;resolution=10

--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/vnd.apple.mpegurl
Content-Transfer-Encoding: 7bit
Content-Location: file:///TMGI-0x1009f165.m3u8

#EXTM3U
#EXT-X-VERSION:6
#EXT-X-STREAM-INF:BANDWIDTH=2305600,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.64001f,mp4a.40.2"
stream_0.m3u8

--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/vnd.apple.mpegurl
Content-Transfer-Encoding: 7bit
Content-Location: http://localhost:3333/watchfolder/hls/manifest.m3u8

#EXTM3U
#EXT-X-VERSION:6
#EXT-X-STREAM-INF:BANDWIDTH=2305600,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.64001f,mp4a.40.2"
stream_0.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1205600,RESOLUTION=960x540,FRAME-RATE=25.000,CODECS="avc1.64001f,mp4a.40.2"
stream_1.m3u8


--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/mbms-user-service-description+xml
Content-Transfer-Encoding: 7bit
Content-Location: file:///usdBundle.xml

<?xml version="1.0" encoding="utf-8"?>
<bundleDescription xmlns="urn:3GPP:metadata:2005:MBMS:userServiceDescription"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:sv="urn:3gpp:metadata:2009:MBMS:schemaVersion"
                   xmlns:r7="urn:3GPP:metadata:2007:MBMS:userServiceDescription"
                   xmlns:r8="urn:3GPP:metadata:2008:MBMS:userServiceDescription"
                   xmlns:r9="urn:3GPP:metadata:2009:MBMS:userServiceDescription"
                   xmlns:r12="urn:3GPP:metadata:2013:MBMS:userServiceDescription"
                   xmlns:r14="urn:3GPP:metadata:2017:MBMS:userServiceDescription"
                   xmlns:r15="urn:3GPP:metadata:2018:r15:MBMS:userServiceDescription"
                   xsi:schemaLocation="urn:3GPP:metadata:2005:MBMS:userServiceDescription USD-schema-main.xsd">  
  <sv:schemaVersion>1</sv:schemaVersion>  
  <userServiceDescription serviceId="urn:3gpp:rsservice1"
                          r7:serviceClass="urn:oma:bcast:ext_bsc_3gpp:bscc:rsservice1"
                          r14:romService="true">
    <name lang="EN-GB">BSCC Service1</name>
    <name lang="DE-DE">BSCC Dienst1</name>
    <serviceLanguage>EN-GB</serviceLanguage>
    <serviceLanguage>DE-DE</serviceLanguage>
    <requiredCapabilities>
      <feature>23</feature>
      <feature>27</feature>
    </requiredCapabilities>
    <deliveryMethod sessionDescriptionURI="file:///TMGI-0x1009f165.sdp">
      <sv:delimiter>0</sv:delimiter>
      <r12:broadcastAppService>
        <r12:basePattern>file:///TMGI-0x1009f165.m3u8</r12:basePattern>
        <r12:serviceArea>2</r12:serviceArea>
      </r12:broadcastAppService>
      <r12:unicastAppService>
        <r12:basePattern>http://localhost:3333/watchfolder/hls/stream_0.m3u8</r12:basePattern>
      </r12:unicastAppService>
      <sv:delimiter>0</sv:delimiter>
    </deliveryMethod>
    <r12:appService appServiceDescriptionURI="http://localhost:3333/watchfolder/hls/manifest.m3u8"
                    mimeType="application/vnd.apple.mpegurl">
      <r12:alternativeContent>
        <r12:basePattern>file:///TMGI-0x1009f165.m3u8</r12:basePattern>
        <r12:basePattern>http://localhost:3333/watchfolder/hls/stream_1.m3u8</r12:basePattern>
      </r12:alternativeContent>
      <r12:identicalContent>
        <r12:basePattern>file:///TMGI-0x1009f165.m3u8</r12:basePattern>
        <r12:basePattern>http://localhost:3333/watchfolder/hls/stream_0.m3u8</r12:basePattern>
      </r12:identicalContent>
    </r12:appService>
    <r9:schedule>
      <r9:scheduleDescriptionURI>file:///TMGI-0x1009f165schedule.xml</r9:scheduleDescriptionURI>
    </r9:schedule>
    <sv:delimiter>0</sv:delimiter>
    <r9:availabilityInfo>
      <r9:infoBinding>
        <r9:serviceArea>2</r9:serviceArea>
      </r9:infoBinding>
    </r9:availabilityInfo>
  </userServiceDescription>
</bundleDescription>
--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/mbms-schedule+xml
Content-Transfer-Encoding: 7bit
Content-Location: file:///TMGI-0x1009f165schedule.xml

<?xml version="1.0" encoding="utf-8"?>
<scheduleDescription xmlns="urn:3gpp:metadata:2011:MBMS:scheduleDescription"
                     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                     xmlns:sv="urn:3gpp:metadata:2009:MBMS:schemaVersion"
                     xsi:schemaLocation="urn:3gpp:metadata:2011:MBMS:scheduleDescription ScheduleDescription.xsd"
                     scheduleUpdate="2021-10-12T10:59:43Z">  
  <sv:schemaVersion>1</sv:schemaVersion>  
  <serviceSchedule>
    <sessionSchedule>
      <start>2021-10-12T10:59:43Z</start>
      <stop>2051-10-05T10:59:43Z</stop>
      <index>0</index>
      <sv:delimiter>0</sv:delimiter>
      <sv:delimiter>0</sv:delimiter>
    </sessionSchedule>
  </serviceSchedule>
</scheduleDescription>
--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
````


## 5G-MAG BC_UC format
This format represents a revised version of the default format:

```` 
MIME-Version: 1.0
Content-Type: multipart/related; boundary="++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--"; type="application/mbms-envelope+xml"
Content-Description: LTE MBMS Service Announcement

--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/mbms-envelope+xml
Content-Transfer-Encoding: 7bit
Content-Location: file:///envelope.xml

<?xml version="1.0" encoding="utf-8"?>
<metadataEnvelope xmlns="urn:3gpp:metadata:2005:MBMS:envelope"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xsi:schemaLocation="urn:3gpp:metadata:2005:MBMS:envelope MetadataEnvelope.xsd">
  <item contentType="application/sdp"
        metadataURI="file:///TMGI-0x1009f165.sdp"
        validFrom="2021-10-12T10:59:43Z"
        validUntil="2051-10-05T10:59:43Z"
        version="1"/>
  <item contentType="application/vnd.apple.mpegurl"
        metadataURI="file:///TMGI-0x1009f165.m3u8"
        validFrom="2021-10-12T10:59:43Z"
        validUntil="2051-10-05T10:59:43Z"
        version="1"/>
  <item contentType="application/vnd.apple.mpegurl"
        metadataURI="http://localhost:3333/watchfolder/hls/manifest.m3u8"
        validFrom="2021-10-12T10:59:43Z"
        validUntil="2051-10-05T10:59:43Z"
        version="1"/>
  <item contentType="application/mbms-user-service-description+xml"
        metadataURI="file:///usdBundle.xml"
        validFrom="2021-10-12T10:59:43Z"
        validUntil="2051-10-05T10:59:43Z"
        version="1"/>
  <item contentType="application/mbms-schedule+xml"
        metadataURI="file:///TMGI-0x1009f165schedule.xml"
        validFrom="2021-10-12T10:59:43Z"
        validUntil="2051-10-05T10:59:43Z"
        version="1"/>
</metadataEnvelope>
--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/sdp
Content-Transfer-Encoding: 7bit
Content-Location: file:///TMGI-0x1009f165.sdp

v=0
o=ROHDE-SCHWARZ-BSCC 269087077 1634036383 IN IP4 11.11.11.11
s=HLS Streaming Session 0x1009f165
i=File Download Session
t=3843025183 4789105183
a=mbms-mode:broadcast-mbsfn 269087077
c=IN IP4 238.1.1.111/127
b=AS:2000
m=application 40101 FLUTE/UDP 0
a=flute-tsi:0
a=flute-ch:1
a=3GPP-QoE-Metrics:metrics={Object_Loss};rate=null;resolution=10
a=3GPP-QoE-Metrics:metrics={Network_Resource};rate=null;resolution=10

--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/vnd.apple.mpegurl
Content-Transfer-Encoding: 7bit
Content-Location: file:///TMGI-0x1009f165.m3u8

#EXTM3U
#EXT-X-VERSION:6
#EXT-X-STREAM-INF:BANDWIDTH=2305600,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.64001f,mp4a.40.2"
stream_0.m3u8

--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/vnd.apple.mpegurl
Content-Transfer-Encoding: 7bit
Content-Location: http://localhost:3333/watchfolder/hls/manifest.m3u8

#EXTM3U
#EXT-X-VERSION:6
#EXT-X-STREAM-INF:BANDWIDTH=2305600,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.64001f,mp4a.40.2"
stream_0.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1205600,RESOLUTION=960x540,FRAME-RATE=25.000,CODECS="avc1.64001f,mp4a.40.2"
stream_1.m3u8


--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/mbms-user-service-description+xml
Content-Transfer-Encoding: 7bit
Content-Location: file:///usdBundle.xml

<?xml version="1.0" encoding="utf-8"?>
<bundleDescription xmlns="urn:3GPP:metadata:2005:MBMS:userServiceDescription"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:sv="urn:3gpp:metadata:2009:MBMS:schemaVersion"
                   xmlns:r7="urn:3GPP:metadata:2007:MBMS:userServiceDescription"
                   xmlns:r8="urn:3GPP:metadata:2008:MBMS:userServiceDescription"
                   xmlns:r9="urn:3GPP:metadata:2009:MBMS:userServiceDescription"
                   xmlns:r12="urn:3GPP:metadata:2013:MBMS:userServiceDescription"
                   xmlns:r14="urn:3GPP:metadata:2017:MBMS:userServiceDescription"
                   xmlns:r15="urn:3GPP:metadata:2018:r15:MBMS:userServiceDescription"
                   xsi:schemaLocation="urn:3GPP:metadata:2005:MBMS:userServiceDescription USD-schema-main.xsd">
  <sv:schemaVersion>1</sv:schemaVersion>
  <userServiceDescription serviceId="urn:3gpp:rsservice1"
                          r7:serviceClass="urn:oma:bcast:ext_bsc_3gpp:bscc:rsservice1"
                          r14:romService="true">
    <name lang="EN-GB">BSCC Service1</name>
    <name lang="DE-DE">BSCC Dienst1</name>
    <serviceLanguage>EN-GB</serviceLanguage>
    <serviceLanguage>DE-DE</serviceLanguage>
    <requiredCapabilities>
      <feature>23</feature>
      <feature>27</feature>
    </requiredCapabilities>
    <deliveryMethod sessionDescriptionURI="file:///TMGI-0x1009f165.sdp">
      <sv:delimiter>0</sv:delimiter>
      <r12:broadcastAppService>
        <r12:basePattern>stream_0.m3u8</r12:basePattern>
        <r12:serviceArea>2</r12:serviceArea>
      </r12:broadcastAppService>
      <r12:unicastAppService>
        <r12:basePattern>http://localhost:3333/watchfolder/hls/stream_0.m3u8</r12:basePattern>
        <r12:basePattern>http://localhost:3333/watchfolder/hls/stream_1.m3u8</r12:basePattern>
      </r12:unicastAppService>
      <sv:delimiter>0</sv:delimiter>
    </deliveryMethod>
    <r12:appService appServiceDescriptionURI="http://localhost:3333/watchfolder/hls/manifest.m3u8"
                    mimeType="application/vnd.apple.mpegurl">
      <r12:alternativeContent>
        <r12:basePattern>stream_0.m3u8</r12:basePattern>
        <r12:basePattern>http://localhost:3333/watchfolder/hls/stream_1.m3u8</r12:basePattern>
      </r12:alternativeContent>
      <r12:identicalContent>
        <r12:basePattern>stream_0.m3u8</r12:basePattern>
        <r12:basePattern>http://localhost:3333/watchfolder/hls/stream_0.m3u8</r12:basePattern>
      </r12:identicalContent>
    </r12:appService>
    <r9:schedule>
      <r9:scheduleDescriptionURI>file:///TMGI-0x1009f165schedule.xml</r9:scheduleDescriptionURI>
    </r9:schedule>
    <sv:delimiter>0</sv:delimiter>
    <r9:availabilityInfo>
      <r9:infoBinding>
        <r9:serviceArea>2</r9:serviceArea>
      </r9:infoBinding>
    </r9:availabilityInfo>
  </userServiceDescription>
</bundleDescription>
--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
Content-Type: application/mbms-schedule+xml
Content-Transfer-Encoding: 7bit
Content-Location: file:///TMGI-0x1009f165schedule.xml

<?xml version="1.0" encoding="utf-8"?>
<scheduleDescription xmlns="urn:3gpp:metadata:2011:MBMS:scheduleDescription"
                     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                     xmlns:sv="urn:3gpp:metadata:2009:MBMS:schemaVersion"
                     xsi:schemaLocation="urn:3gpp:metadata:2011:MBMS:scheduleDescription ScheduleDescription.xsd"
                     scheduleUpdate="2021-10-12T10:59:43Z">
  <sv:schemaVersion>1</sv:schemaVersion>
  <serviceSchedule>
    <sessionSchedule>
      <start>2021-10-12T10:59:43Z</start>
      <stop>2051-10-05T10:59:43Z</stop>
      <index>0</index>
      <sv:delimiter>0</sv:delimiter>
      <sv:delimiter>0</sv:delimiter>
    </sessionSchedule>
  </serviceSchedule>
</scheduleDescription>
--++++++++++++++++++++++++Rohde&Schwarz-BSCC++++++++++++++++++++++++--
````

## 5G-MAG Legacy format
5G-MAG provides multiple [sample recordings](https://github.com/5G-MAG/Documentation-and-Architecture/wiki/Sample-Files) captured and hosted by ORS. These files were recorded at the start of the project and require a specific format of the ServiceAnnouncement file:

```` 
MIME-Version: 1.0
Content-Type: multipart/related; boundary="xxx.yyy.zzz.--Rohde&Schwarz-BSCC--zzz.yyy.xxx--"; type="application/mbms-envelope+xml"
Content-Description: LTE MBMS Service Announcement

--xxx.yyy.zzz.--Rohde&Schwarz-BSCC--zzz.yyy.xxx--
Content-Type: application/mbms-envelope+xml
Content-Transfer-Encoding: 7bit
Content-Location: file:///envelope.xml

<?xml version="1.0" encoding="utf-8"?>
<metadataEnvelope xmlns="urn:3gpp:metadata:2005:MBMS:envelope"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xsi:schemaLocation="urn:3gpp:metadata:2005:MBMS:envelope MetadataEnvelope.xsd">
  <item contentType="application/sdp"
        metadataURI="file:///TMGI-0x1009f165.sdp"
        validFrom="2021-09-02T07:45:33Z"
        validUntil="2051-08-26T07:45:33Z"
        version="1"/>
  <item contentType="application/vnd.apple.mpegurl"
        metadataURI="file:///TMGI-0x1009f165.m3u8"
        validFrom="2021-09-02T07:45:33Z"
        validUntil="2051-08-26T07:45:33Z"
        version="1"/>
  <item contentType="application/vnd.apple.mpegurl"
        metadataURI="http://10.160.82.131/out/u/bbb/qxa/manifest.m3u8"
        validFrom="2021-09-02T07:45:33Z"
        validUntil="2051-08-26T07:45:33Z"
        version="1"/>
  <item contentType="application/mbms-user-service-description+xml"
        metadataURI="file:///usdBundle.xml"
        validFrom="2021-09-02T07:45:33Z"
        validUntil="2051-08-26T07:45:33Z"
        version="1"/>
  <item contentType="application/mbms-schedule+xml"
        metadataURI="file:///TMGI-0x1009f165schedule.xml"
        validFrom="2021-09-02T07:45:33Z"
        validUntil="2051-08-26T07:45:33Z"
        version="1"/>
</metadataEnvelope>
--xxx.yyy.zzz.--Rohde&Schwarz-BSCC--zzz.yyy.xxx--
Content-Type: application/sdp
Content-Transfer-Encoding: 7bit
Content-Location: file:///TMGI-0x1009f165.sdp

v=0
o=ROHDE-SCHWARZ-BSCC 269087077 1630568733 IN IP4 11.11.11.11
s=HLS Streaming Session 0x1009f165
i=File Download Session
t=3839557533 4785637533
a=mbms-mode:broadcast-mbsfn 269087077
c=IN IP4 238.1.1.111/127
b=AS:1699
m=application 40101 FLUTE/UDP 0
a=flute-tsi:16
a=flute-ch:1
a=3GPP-QoE-Metrics:metrics={Object_Loss};rate=null;resolution=10
a=3GPP-QoE-Metrics:metrics={Network_Resource};rate=null;resolution=10

--xxx.yyy.zzz.--Rohde&Schwarz-BSCC--zzz.yyy.xxx--
Content-Type: application/vnd.apple.mpegurl
Content-Transfer-Encoding: 7bit
Content-Location: file:///TMGI-0x1009f165.m3u8

#EXTM3U
#EXT-X-VERSION:3

#EXT-X-STREAM-INF:CODECS="avc1.4D401E,mp4a.40.2",BANDWIDTH=1427133,FRAME-RATE=25.000,RESOLUTION=640x360
out/u/bbb/qxa/manifest_3.m3u8?m=1614073235

--xxx.yyy.zzz.--Rohde&Schwarz-BSCC--zzz.yyy.xxx--
Content-Type: application/vnd.apple.mpegurl
Content-Transfer-Encoding: 7bit
Content-Location: http://10.160.82.131/out/u/bbb/qxa/manifest.m3u8

#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=3847133,AVERAGE-BANDWIDTH=3847133,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.4D401F,mp4a.40.2"
manifest_1.m3u8?m=1614073235
#EXT-X-STREAM-INF:BANDWIDTH=2857098,AVERAGE-BANDWIDTH=2857098,RESOLUTION=854x480,FRAME-RATE=25.000,CODECS="avc1.4D401E,mp4a.40.2"
manifest_2.m3u8?m=1614073235
#EXT-X-STREAM-INF:BANDWIDTH=1427133,AVERAGE-BANDWIDTH=1427133,RESOLUTION=640x360,FRAME-RATE=25.000,CODECS="avc1.4D401E,mp4a.40.2"
manifest_3.m3u8?m=1614073235

--xxx.yyy.zzz.--Rohde&Schwarz-BSCC--zzz.yyy.xxx--
Content-Type: application/mbms-user-service-description+xml
Content-Transfer-Encoding: 7bit
Content-Location: file:///usdBundle.xml

<?xml version="1.0" encoding="utf-8"?>
<bundleDescription xmlns="urn:3GPP:metadata:2005:MBMS:userServiceDescription"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xmlns:sv="urn:3gpp:metadata:2009:MBMS:schemaVersion"
                   xmlns:r7="urn:3GPP:metadata:2007:MBMS:userServiceDescription"
                   xmlns:r8="urn:3GPP:metadata:2008:MBMS:userServiceDescription"
                   xmlns:r9="urn:3GPP:metadata:2009:MBMS:userServiceDescription"
                   xmlns:r12="urn:3GPP:metadata:2013:MBMS:userServiceDescription"
                   xmlns:r14="urn:3GPP:metadata:2017:MBMS:userServiceDescription"
                   xmlns:r15="urn:3GPP:metadata:2018:r15:MBMS:userServiceDescription"
                   xsi:schemaLocation="urn:3GPP:metadata:2005:MBMS:userServiceDescription USD-schema-main.xsd">
  <sv:schemaVersion>1</sv:schemaVersion>
  <userServiceDescription serviceId="urn:rohde-schwarz:service:16.0"
                          r7:serviceClass="urn:oma:bcast:ext_bsc_3gpp:bscc:rsservice1"
                          r14:romService="true">
    <name>Test Service TMGI-0x1009f165</name>
    <name lang="EN">EN: Test Service TMGI-0x1009f165</name>
    <name lang="DE">DE: Test Service TMGI-0x1009f165</name>
    <serviceLanguage>EN</serviceLanguage>
    <serviceLanguage>DE</serviceLanguage>
    <requiredCapabilities>
      <feature>23</feature>
      <feature>27</feature>
    </requiredCapabilities>
    <deliveryMethod sessionDescriptionURI="file:///TMGI-0x1009f165.sdp">
      <sv:delimiter>0</sv:delimiter>
      <r12:broadcastAppService>
        <r12:basePattern>out/u/bbb/qxa/manifest_3.m3u8?m=1614073235</r12:basePattern>
        <r12:basePattern>file:///TMGI-0x1009f165.m3u8</r12:basePattern>
        <r12:serviceArea>2</r12:serviceArea>
      </r12:broadcastAppService>
      <sv:delimiter>0</sv:delimiter>
    </deliveryMethod>
    <r12:appService appServiceDescriptionURI="http://10.160.82.131/out/u/bbb/qxa/manifest.m3u8"
                    mimeType="application/vnd.apple.mpegurl"/>
    <r9:schedule>
      <r9:scheduleDescriptionURI>file:///TMGI-0x1009f165schedule.xml</r9:scheduleDescriptionURI>
    </r9:schedule>
    <sv:delimiter>0</sv:delimiter>
    <r9:availabilityInfo>
      <r9:infoBinding>
        <r9:serviceArea>2</r9:serviceArea>
      </r9:infoBinding>
    </r9:availabilityInfo>
  </userServiceDescription>
</bundleDescription>
--xxx.yyy.zzz.--Rohde&Schwarz-BSCC--zzz.yyy.xxx--
Content-Type: application/mbms-schedule+xml
Content-Transfer-Encoding: 7bit
Content-Location: file:///TMGI-0x1009f165schedule.xml

<?xml version="1.0" encoding="utf-8"?>
<scheduleDescription xmlns="urn:3gpp:metadata:2011:MBMS:scheduleDescription"
                     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                     xmlns:sv="urn:3gpp:metadata:2009:MBMS:schemaVersion"
                     xsi:schemaLocation="urn:3gpp:metadata:2011:MBMS:scheduleDescription ScheduleDescription.xsd"
                     scheduleUpdate="2021-09-02T07:45:33Z">
  <sv:schemaVersion>1</sv:schemaVersion>
  <serviceSchedule>
    <sessionSchedule>
      <start>2021-09-02T07:45:33Z</start>
      <stop>2051-08-26T07:45:33Z</stop>
      <index>0</index>
      <sv:delimiter>0</sv:delimiter>
      <sv:delimiter>0</sv:delimiter>
    </sessionSchedule>
  </serviceSchedule>
</scheduleDescription>
--xxx.yyy.zzz.--Rohde&Schwarz-BSCC--zzz.yyy.xxx--
```` 
