---
layout: default
title:  Installation 5GMS AF as Local User
parent: Testing
grand_parent: 5G Downlink Media Streaming
has_children: false
nav_order: 1
---

# Testing the 5GMSd Application Function as a Local User

**TODO: Intro**

## Build Dependencies

Before building the 5GMSd Application Function, there are a few build dependencies that are needed.

The following are needed:
- **Commands**
  - bison
  - C compiler
  - curl
  - flex
  - git
  - java
  - meson (version 0.63.0 or higher)<sup>[\[1\]](#footnote-1)</sup>
  - ninja
  - pip
  - python3
  - wget
- **Development libraries**
  - sctp
  - gnutls
  - yaml
  - nghttp2
  - talloc
  - microhttpd
  - curl
  - mongo DB
  - openssl
  - gcrypt
  - tins
  - idn
- **Python modules**
  - venv
  - yaml

Notes:
 - <a name="footnote-1"></a>[1]: `meson` must be at least version 0.63.0 to patch open5gs properly, therefore it is suggested that this be installed using the python pip module to pull the latest version rather than relying on the packaged version from your operating system.

These can be installed using your system package manager, for example:

**Ubuntu and derivatives**
```bash
sudo apt install bison build-essential curl flex git default-jdk ninja-build wget python3-pip python3-venv python3-setuptools python3-wheel python3-yaml libsctp-dev libgnutls28-dev libgcrypt-dev libssl-dev libidn11-dev libmongoc-dev libbson-dev libyaml-dev libnghttp2-dev libmicrohttpd-dev libcurl4-gnutls-dev libnghttp2-dev libtins-dev libtalloc-dev
sudo python3 -m pip install build meson
```

## Retrieving the source

When developing always use the `development` branch of the 5GMSd Application Function.

If you are intending to commit code back to the project then we advise creating your own "Fork" of the repository at <https://github.com/5G-MAG/rt-5gms-application-function>, and working on your own fork.

To clone the source use:

```bash
cd
git clone -b development --recurse-submodules git@github.com:${github_username}/rt-5gms-application-function.git
```

Where `${github_username}` is your GitHub user name.

If you are not intending committing changes back to the repository (only testing the latest development version) then you can obtain a clone using:

```bash
cd
git clone -b development --recurse-submodules https://github.com/5G-MAG/rt-5gms-application-function.git
```

If you wish to commit back changes then these should be pushed to a branch on your fork and PR raised to submit the changes back to the development branch of the 5G-MAG repository.

## Building

```bash
cd ~/rt-5gms-application-function
meson setup --prefix=`pwd`/install build
ninja -C build
```

## Installing

If you are upgrading from one release to the next then it is advisable to delete the old installed `msaf.yaml` configuration and
replace it with a new one. To delete the old installed configuration use:

```bash
cd ~/rt-5gms-application-function
rm -f install/etc/open5gs/msaf.yaml
```

To install the Application Function, its default configuration and supporting scripts:

```bash
cd ~/rt-5gms-application-function
meson install -C build --no-rebuild
```

It is advisable to review the configuration file in `~/rt-5gms-application-function/install/etc/open5gs/msaf.yaml` before running
the 5GMSd Application Function for the first time after installation.

## Configuring

The configuration can be found in `~/rt-5gms-application-function/install/etc/open5gs/msaf.yaml`. Edit this YAML file to change the operating configuration of the 5GMSd Application Function.

See the [Configuring the Application Function](Configuring-the-Application-Function) page for more details on the settings.

## Running

Once the configuration has been set, execute the 5GMSd Application Function using:

```bash
~/rt-5gms-application-function/install/bin/open5gs-msafd
```

For v1.2.0 to v1.4.0:

   To run the `m1-session` tool with a local user installation the python path for the user installed module needs to be included in
   the `PYTHONPATH` environment variable.

   ```bash
   PYTHONPATH=`find ~/rt-5gms-application-function/install -type d '(' -name 'site-packages' -o -name 'dist-packages' ')' -print` export PYTHONPATH
   ```

   The default configuration for the `m1-session` tool will try to write the persistent store to `/var/cache/rt-5gms/m1-client`. This may not be accessible as a local user and therefore it is a good idea to change the `data_store` configuration setting to a place where the local user can write to:

   ```bash
   ~/rt-5gms-application-function/install/bin/m1-session configure set data_store ~/m1-client-data-store
   ```

For v1.4.1 and above:

   The `m1-session` tool has moved to the [rt-5gms-application-provider](https://github.com/5G-MAG/rt-5gms-application-provider)
   repository. Please follow the instructions in that repository for manual installation of the M1 python tools and classes to
   install the `msaf-configuration`, `m1-session` and `m1-client` tools either to your system or to a virtual python environment.

   If you have installed the tools in the python virtual environment then activate the environment before proceeding, for example:

   ```bash
   source venv/bin/activate
   ```

   Then you can change the data store directory, for example:

   ```bash
   m1-session configure set data_store ~/m1-client-data-store
   ```

## Stopping

Press CTRL-C on the terminal from which the 5GMSd Application Function is running.

