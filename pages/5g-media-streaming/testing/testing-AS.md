---
layout: default
title:  Testing the 5GMS AS
parent: Testing
grand_parent: 5G Downlink Media Streaming
has_children: false
nav_order: 3
---

# Developing and Testing the 5GMSd Application Server

While the instructions in the main project [README](https://github.com/5G-MAG/rt-5gms-application-server#readme) tell you how to install the 5GMSd Application Server as a system-wide application, during development it is usually more appropriate to have one or more local clones of the repository that are being used for development and testing. This page provides details of one suggested way to arrange your development environment to ensure separation from the main system during development and testing.

# Prerequisites

There are some packages that will need to be installed system wide that the build and install system relies on. These prerequisite packages are:
- **Commands**
  - Git
  - Java
  - Python 3
  - Wget
- **Python 3 modules**
  - pip
  - venv

These can usually be installed as system packages, for example:
**Debian/Ubuntu Linux and derivatives**
```bash
sudo apt -y install git default-jdk python3 wget python3-pip python3-venv
```

**RHEL/CentOS/Fedora/Rocky**
```bash
sudo dnf -y install git java-latest-openjdk python3 wget python3-pip python3-venv
```

# Checking out the project code

Since this will be used for development and testing, the instructions here will show you how to check out the latest development branch.

## Checkout for development

1. **Create a fork**
   1. Login to GitHub ([create a GitHub account](https://github.com/join) and [set an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) if you haven't already done so).
   1. On the main [GitHub project page](https://github.com/5G-MAG/rt-5gms-application-server) click on the "Fork" label in the top right of the page, then untick "Copy the `main` branch only" on the page that appears and select the "Create fork" button.
   1. On your new fork page select the `Settings` option just below the main repository title. Then select "Branches" under the "Code and automation" topic from the sections on the left, and edit the "Default branch" to change it to `development`.
   1. Clone the repository
      ```bash
      cd
      git clone --recurse-submodules git@github.com:<your-github-user>/rt-5gms-application-server.git
      ```
      Where `<your-github-user>` is the username of your GitHub login.

## Checkout for testing only

1. **Clone the 5G-MAG repository**
   ```bash
   cd
   git clone -b development --recurse-submodules https://github.com/5G-MAG/rt-5gms-application-server.git
   ```

# Creating the virtual Python environment

By using a Python virtual environment you can use upgraded versions of existing system Python modules and automatically install project module dependencies without having to install or upgrade modules system wide.

1. Create the virtual Python environment

   ```bash
   cd ~/rt-5gms-application-server
   python3 -m venv venv
   ```

1. Update base modules and test script dependencies

   ```bash
   cd ~/rt-5gms-application-server
   venv/bin/python3 -m pip install --upgrade pip build setuptools docopt PyYAML
   ```

# Build and install the 5GMSd Application Server

```bash
cd ~/rt-5gms-application-server
venv/bin/python3 -m pip install .
```

# Create a local-user friendly configuration

Save these configuration file contents as `~/rt-5gms-application-server/local-dev.conf`:
```ini
### Defaults for the 5G-MAG Reference Tools: 5GMSd applications
[DEFAULT]
log_dir = /tmp/rt-5gms-as/logs
run_dir = /tmp/rt-5gms-as

### 5GMSd Application Server specific configurations
[5gms_as]
log_level = debug
cache_dir = /tmp/rt-5gms-as/cache
certificates_cache = /tmp/rt-5gms-as/certificates
http_port = 8080
https_port = 8443
#m3_listen = localhost
#m3_port = 7777
#access_log = %(log_dir)s/application-server-access.log
#error_log = %(log_dir)s/application-server-error.log
#pid_path = %(run_dir)s/application-server.pid

### 5GMSd Application Server nginx specific configuration
[5gms_as.nginx]
root_temp = /tmp/rt-5gms-as
#client_body_temp = %(root_temp)s/client-body-tmp
#proxy_temp = %(root_temp)s/proxy-tmp
#fastcgi_temp = %(root_temp)s/fastcgi-tmp
#uwsgi_temp = %(root_temp)s/uwsgi-tmp
#scgi_temp = %(root_temp)s/scgi-tmp
#pid_path = %(root_temp)s/5gms-as-nginx.pid
```

Using this configuration will:
- Place all 5GMSd Application Server cache directories and other temporary files and logs under the `/tmp/rt-5gms-as` directory for testing.
- Change the default ports used for the 5GMSd distribution service at reference point M4d. Note that this means that all URLs output by the 5GMSd Application Function with respect to M4d will need to be manually modified to insert the new port numbers before use, e.g. if the AF publishes a URL starting `http://your.hostname/...` you will need to change that to `http://your.hostname:8080/...` in order to use the URL. This is necessary as the default ports of 80 and 443 are not available to normal unprivileged users. A normal user has to use ports with a number greater than 1024.
- Turn on `debug` level output from the 5GMSd Application Server in order to better see what it happening.
- Some settings above are commented out but may be useful while testing and so have been left in with their default values and prefixed with `#` to comment them out. If you wish to change one then remove the `#` and change the value to your desired setting.

# Running the installed 5GMSd Application server

To run the version of the 5GMSd Application Server installed in the virtual environment with the `local-dev.conf` configuration (above), use:

```bash
cd ~/rt-5gms-application-server
PATH="/usr/local/openresty/nginx/sbin:$PATH" venv/bin/5gms-application-server -c local-dev.conf
```

# Runtime configuration

The 5GMSd Application Server is configured at run-time for distribution of media via the interface at reference point M3. This is usually done by the [5GMSd Application Function](https://github.com/5G-MAG/rt-5gms-application-function), but this project also contains a simple M3 client that can be used to push run-time configuration for testing.

## M3 test client

This client script provides a simple command line interface to issue M3 API calls and see the result from the response.

The script can be run as:
```bash
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -h|{<command> <hostaddr:port> [<command-parameters>...]}
```

If the default values for `m3_listen` and `m3_port` are used in the configuration file the `<hostaddr:port>` will be `localhost:7777`.

To see the command line help use:
```bash
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -h
```

## M3 Certificates API

### List known certificates

```bash
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -c localhost:7777
```

### Add a new certificate

```bash
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -c localhost:7777 add testcert1 tests/examples/certificate-1.pem
```

### Update an existing certificate

```bash
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -c localhost:7777 update testcert1 tests/examples/certificate-1.pem
```

### Delete a certificate

```bash
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -c localhost:7777 delete testcert1
```

## M3 ContentHostingConfiguration API

### List known ContentHostingConfigurations

```bash
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -H localhost:7777
```

### Add a new ContentHostingConfiguration

```bash
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -H localhost:7777 add prov-sess-1 tests/examples/ContentHostingConfiguration_Big-Buck-Bunny_pull-ingest_http_and_https.json
```

### Update an existing ContentHostingConfiguration

```bash
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -H localhost:7777 update prov-sess-1 tests/examples/ContentHostingConfiguration_Big-Buck-Bunny_pull-ingest_https.json
```

### Delete a ContentHostingConfiguration

```bash
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -H localhost:7777 delete prov-sess-1
```

### Purge all cached objects for a ContentHostingConfiguration

```bash   
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -H localhost:7777 purge prov-sess-1
```

### Purge cached objects using a path regex for a ContentHostingConfiguration

For example to purge all DASH manifests:
```bash   
cd ~/rt-5gms-application-server
tests/m3_client_cli.py -H localhost:7777 purge prov-sess-1 '\.mpd$'
```

