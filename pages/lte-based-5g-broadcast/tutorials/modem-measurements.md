---
layout: default
title: SDR - Measurements
parent: Tutorials
grand_parent: 5G Broadcast - TV/Radio
has_children: false
nav_order: 5
---

# Tutorial - MBMS Modem - Measurements & GPS

## Configuring a GPS mouse

*MBMS Modem* relies on GPSD (https://gpsd.gitlab.io/gpsd/) for GPS data aquisition.

Please follow the setup instruction for gpsd to configure it for your GPS
receiver: https://gpsd.gitlab.io/gpsd/installation.html

Usually, this should boil down to:

- ``sudo apt install libgps-dev gpsd``
- Checking which (virtual) serial port your GPS mouse uses, once you plug it in (e.g. ``/dev/ttyACM0``)
- Setting this device in /etc/default/gpsd:

```
# Devices gpsd should collect to at boot time.
# They need to be read/writeable, either by user gpsd or the group dialout.
DEVICES="/dev/ttyACM0"
# Other options you want to pass to gpsd
GPSD_OPTIONS=""
```

- Adding gpsd to the *dialout* group: `` sudo usermod -a -G dialout gpsd``
- Checking if everything works with one of the client applications, e.g. `cgps` (can be installed
  with `sudo apt install gpsd-clients`). This should show position data.

## Logging measurement data to a CSV file

### Configuration for measurement file

Is in ``/etc/5gmag-rt.conf``:

```
  measurement_file: {
    enabled: true;
    file_path: "/tmp/modem_measurements.csv";
    interval_secs: 10;      
    gpsd:
    {
      enabled: true;
      host: "localhost";
      port: "2947";
    }
}
```

You can modify the location of the created file here, set the interval in which measurement lines are written to it, and
enable/disable GPS.

### File format

The created file is in semicolo-separated CSV format.

The columns contain:

1. system timestamp
2. latitude
3. longitude
4. gps timestamp
5. CINR
6. PDSCH MCS
7. PDSCH BLER
8. PDSCH BER
9. MCCH MCS
10. MCCH BLER
11. MCCH BER
12. First MCH index
13. First MCH MCS
14. First MCH BLER
15. First MCH BER

If there are more MCHs, they are appended at the end of the line:

'16. Second MCH Index

'17. Second MCH MCS

'18. Second MCH BLER

'19. Second MCH BER

### Example output

```
2021-02-26T15:09:54;48.392428;16.104939;2021-02-26T15:09:54;22.847839;4;0.000000;0.000000;2;0.000000;-;0;9;0.000000;-;
2021-02-26T15:10:00;48.392428;16.104939;2021-02-26T15:10:00;27.173386;4;0.000000;0.000000;2;0.000000;-;0;9;0.000000;-;
2021-02-26T15:10:05;48.392428;16.104939;2021-02-26T15:10:05;26.828796;4;0.000000;0.000000;2;0.000000;-;0;9;0.000000;-;
2021-02-26T15:10:11;48.392428;16.104939;2021-02-26T15:10:11;23.722340;4;0.000000;0.000000;2;0.000000;-;0;9;0.000000;-;
2021-02-26T15:10:17;48.392428;16.104939;2021-02-26T15:10:17;24.914352;4;0.000000;0.000000;2;0.000000;-;0;9;0.000000;-;
2021-02-26T15:10:22;48.392428;16.104939;2021-02-26T15:10:22;26.893414;4;0.000000;0.000000;2;0.000000;-;0;9;0.000000;-;
2021-02-26T15:10:28;48.392428;16.104939;2021-02-26T15:10:28;22.102150;4;0.000000;0.000000;2;0.000000;-;0;9;0.000000;-;
2021-02-26T15:10:34;48.392428;16.104939;2021-02-26T15:10:34;22.894867;4;0.000000;0.000000;2;0.000000;-;0;9;0.000000;-;
```
