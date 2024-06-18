# Testing

This section explains how to use the Python tests present on the `test` directory.

The Python modules requirements are preinstalled on the AF container image. This container mounts the `test` directory as readonly to be able to run the tests.

To run the tests, execute an interactive session with the AF container and navigate to the test directory:
```bash
docker exec -it af bash

# inside the AF container
cd test

# to run the tests
python3 tests.py
```

The `test` directory contains the following subdirectories:
- `MB_SMF` the developed tests regarding the MB-SMF Network Function
- `utils` a Python package containing some common utils for the tests
- `support` some support files for the tests like JSON files for the requests and JSON schemas to validate them

Using the `config.toml` file some parameters can be configured:
- the log_level for the tests can be adjusted. The values supported are: DEBUG, INFO, WARNING, ERROR, CRITICAL
- some endpoint parameters like the MB-SMF address, the protocol (HTTP or HTTPS) and the port being used

The file `tests.py` contains the main logic for the tests. In this file the test suites are defined and run by the unittest testing framework.
