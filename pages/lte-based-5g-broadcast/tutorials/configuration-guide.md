---
layout: default
title: Linux stack - Configuration guide
parent: Tutorials
grand_parent: 5G Broadcast (MBMS)
has_children: false
nav_order: 0
---

# Linux stack - Configuration guide

## Setup Resources

* [Hardware, OS & SDR Requirements](../additional/hardware-requirements.html)
* [Sample Files](../additional/sample-files.html)
* [Service Announcement Formats](../additional/rt-common-shared/MBMS-service-announcement-files.html)

## Preparation

After each reboot of your machine run:

1. `sudo systemctl start 5gmag-rt-modem`
2. `sudo systemctl stop 5gmag-rt-modem`

Make sure that you have the latest nginx config enabled in `/etc/nginx/sites-enabled/5gmag-rt-wui`. Compare it to the
config that is provided
[here](https://github.com/5G-MAG/rt-common-shared/blob/feature/mbms/mbms/common-config/5gmag-rt-wui)

## Different SA formats

The 5G-MAG Reference Tools support three different service announcement formats. In the examples below we either use the
`5gmag_legacy` format for the recordings or the `default` format for seamless switching. To use the seamless switching
format that was agreed in 5G-MAG you have to use `5gmag_bc_uc`. The corresponding service announcement example file is
labeled `bootstrap.multipart.seamlessswitching.hls.5gmag`. More details can be found in the
[Service Announcement Formats](../additional/rt-common-shared/MBMS-service-announcement-files.html) section.

## Playback of 5GBC together with the MBMS Modem

Set the target configuration in `etc/5gmag-rt-conf`:

````
  seamless_switching: {
    enabled: <TRUE OR FALSE>;
    truncate_cdn_playlist_segments: 3
  }
  bootstrap_format: <TARGET FORMAT>;
  local_service: {
    enabled: false
  }
````

## Playback of legacy recordings

Set the configuration in `etc/5gmag-rt-conf` to use the legacy format:

```` 
  seamless_switching: {
    enabled: false;
  }
  bootstrap_format: "5gmag_legacy";
  local_service: {
    enabled: false;
  }
```` 

If you want to play the recorded content in a loop consider increasing the cache values to avoid segments with the same
url being deleted immediately:

```` 
  cache: { 
    max_segments_per_stream: 30;
    max_file_age: 1200;    /* seconds */
    max_total_size: 128; /* megabyte */
  }
```` 

## FLUTE ffmpeg watchfolder with signaling server

### HLS seamless switching

Set the config file for the rt-mbms-examples project in `flute-ffmpeg\config\default.cfg` to:

````
general : {
          multicast_ip = "238.1.1.111";
          multicast_port = 40101;
          mtu = 1500;
          rate_limit = 1200000;
          watchfolder_path = "<PATH TO YOUR WEBSERVER WHERE HLS SEGMENTS ARE WRITTEN TO>";
          path_to_transmit = "<RELATIVE PATH FROM THE ROOT OF YOUR WEBSERVER>"
          stream_type = "hls";
          transmit_service_announcement = true;
          dash: {
              number_of_init_segments = 3;
              resend_init_in_sec = 30;
              service_announcement = "../supporting_files/mbms/bootstrap_examples/bootstrap.multipart.legacy.dash";
          };
          hls: {
              service_announcement = "../supporting_files/mbms/bootstrap_examples/bootstrap.multipart.seamlessswitching.hls";
              media_playlists_to_ignore_in_multicast = []
          }
          webserver_port: 3010;
}
```` 

Note: For seamless switching to work the `watchfolder_path` needs to point to a webserver that hosts the segments.

Enable seamless switching in the `etc/5gmag-rt-conf` file:

```` 
  seamless_switching: {
    enabled: true;
    truncate_cdn_playlist_segments: 3
  }
```` 

### DASH Broadcast

Disable seamless switching and set the right SA format in the `etc/5gmag-rt-conf` file:

```` 
  seamless_switching: {
    enabled: false;
    truncate_cdn_playlist_segments: 3
  },
bootstrap_format: "5gmag_legacy";

````

Adjust the config for flute-ffmpeg:

```` 
general : {
          multicast_ip = "238.1.1.111";
          multicast_port = 40101;
          mtu = 1500;
          rate_limit = 1200000;
          watchfolder_path = "/home/dsi/5G-MAG/simple-express-server/public/watchfolder/dash";
          path_to_transmit = ""
          stream_type = "dash";
          transmit_service_announcement = true;
          dash: {
              number_of_init_segments = 3;
              resend_init_in_sec = 30;
              service_announcement = "../supporting_files/mbms/bootstrap_examples/bootstrap.multipart.legacy.dash";
          };
          hls: {
              service_announcement = "../supporting_files/mbms/bootstrap_examples/bootstrap.multipart.seamlessswitching.hls";
              media_playlists_to_ignore_in_multicast = []
          }
          webserver_port: 3010;
}
````  

### HLS Broadcast

Disable seamless switching and set the right SA format in the `etc/5gmag-rt-conf` file:

```` 
  seamless_switching: {
    enabled: false;
    truncate_cdn_playlist_segments: 3
  },
bootstrap_format: "5gmag_legacy";

````

Adjust the config for flute-ffmpeg:

```` 
general : {
          multicast_ip = "238.1.1.111";
          multicast_port = 40101;
          mtu = 1500;
          rate_limit = 1200000;
          watchfolder_path = "/home/dsi/5G-MAG/simple-express-server/public/watchfolder/hls";
          path_to_transmit = "watchfolder/hls/"
          stream_type = "hls";
          transmit_service_announcement = true;
          dash: {
              number_of_init_segments = 3;
              resend_init_in_sec = 30;
              service_announcement = "../supporting_files/mbms/bootstrap_examples/bootstrap.multipart.legacy.dash";
          };
          hls: {
              service_announcement = "../supporting_files/mbms/bootstrap_examples/bootstrap.multipart.legacy.hls";
              media_playlists_to_ignore_in_multicast = []
          }
          webserver_port: 3010;
}
```` 

## FLUTE ffmpeg with local Service Announcement

In this example we dont need the http server that signals the `mch_info.json`. Instead, we start the MBMS Middleware
directly with a local service announcement file

### General

Enable the local service in the `etc/5gmag-rt-conf` file:

````
  local_service: {
    enabled: true;
  }
````

Disable `transmit_service_announcement` in the flute-ffmpeg `default.cfg` file:

```` 
transmit_service_announcement = false;
````  

### HLS seamless switching

Point to a local service announcement file with seamless switching support in the `etc/5gmag-rt-conf` file e.g.:

````
  local_service: {
    bootstrap_file: "/home/dsi/5G-MAG/rt-common-shared/mbms/bootstrap_examples/bootstrap.multipart.seamlessswitching.hls";
  }
````

Enable seamless switching in the `etc/5gmag-rt-conf` file:

```` 
  seamless_switching: {
    enabled: true;
    truncate_cdn_playlist_segments: 3
  },
bootstrap_format: "";

````

### HLS Broadcast

Point to a local service announcement in the `etc/5gmag-rt-conf` file e.g.:

````
  local_service: {
    bootstrap_file: "/home/dsi/5G-MAG/rt-common-shared/mbms/bootstrap_examples/bootstrap.multipart.legacy.hls";
  }
````

Disable seamless switching and set the right SA format in the `etc/5gmag-rt-conf` file:

```` 
  seamless_switching: {
    enabled: false;
    truncate_cdn_playlist_segments: 3
  },
bootstrap_format: "5gmag_legacy";

````

### DASH Broadcast

Point to a local service announcement in the `etc/5gmag-rt-conf` file e.g.:

````
  local_service: {
    bootstrap_file: "/home/dsi/5G-MAG/rt-common-shared/mbms/bootstrap_examples/bootstrap.multipart.legacy.dash";
  }
````

Disable seamless switching and set the right SA format in the `etc/5gmag-rt-conf` file:

```` 
  seamless_switching: {
    enabled: false;
    truncate_cdn_playlist_segments: 3
  },
bootstrap_format: "5gmag_legacy";

````
