# Automated Hardware Test Bench in Python

![Tests](https://github.com/adouberyl/hardware_testbench_project/actions/workflows/tests.yml/badge.svg)

A small test-automation project written in Python. It simulates a hardware device
(a regulated power supply), drives it through a simulated connection, and checks its
behavior with an automated test suite. The tests run automatically on every push
through GitHub Actions, and the project can also run inside a Docker container.

## Overview

The goal of this project is to imitate, in software, the way a test engineer drives
and validates a hardware device. The device is fully simulated, which makes the whole
pipeline reproducible and easy to run anywhere.

This side project, built over the summer, allowed me to apply key concepts from my
Computer Science and Microelectronics Engineering curriculum to test automation. It
serves as a practical demonstration of:

- object-oriented design, with a clear separation between the device, the connection,
  and the driver
- automated testing with pytest (fixtures, parametrization, mocking, and coverage)
- continuous integration with GitHub Actions
- containerization with Docker
- logging and custom exceptions for robust error handling

## Architecture

The code is built around three classes connected by composition:

```
Driver  ──►  Connection  ──►  Device
(high-level    (carries the    (simulates the
 commands)      commands)       hardware)
```

- **Driver** is the high-level interface. It contains a connection, sets and reads the
  voltage, and translates the error codes returned by the device into Python exceptions.
- **Connection** contains the device. It carries the commands from the driver to the
  device and returns its answer.
- **Device** receives text commands (for example `SET V 3.3`, `GET V`, `STATUS`) and
  interprets them, returning a value or an error code.

This design makes it possible to replace the simulated connection with a real serial
connection later, without changing the driver.

## Prerequisites

- Python 3.12 or later (the CI runs on Python 3.12, and the Docker image is based on
  `python:3.12-slim`)
- The dependencies listed in `requirements.txt` (mainly `pytest` and `pytest-cov`)

## Installation

Clone the repository, then create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows (Git Bash)
# source .venv/bin/activate      # Linux / macOS
pip install -r requirements.txt
```

## Usage

Run the demonstration script:

```bash
python main.py
```

It sets a voltage, reads it back, and shows the logs and the error handling.

## Running the tests

Run the full test suite:

```bash
pytest -v
```

Run the tests with a coverage report:

```bash
pytest --cov=banc
```

## Running with Docker

Build the image and run the tests inside a container, without installing anything
locally:

```bash
docker build -t banc-de-test .
docker run --rm banc-de-test
```

## Project structure

```
.
├── banc.py              # device, connection and driver classes
├── error_config.py      # custom exceptions
├── logging_config.py    # logging configuration
├── main.py              # entry point (demonstration)
├── tests/               # pytest test suite
│   ├── test_banc.py
│   └── test_mock_driver.py
├── Dockerfile
├── requirements.txt
└── .github/workflows/   # continuous integration
```
