# HTTP Endpoint Health Monitoring Program

## Overview

This program monitors the health of a set of HTTP endpoints by making periodic GET requests to each endpoint every 15 seconds. It tracks the availability percentage of each domain and logs the cumulative availability percentage for each domain to the console after each test cycle.

The program reads the list of HTTP endpoints from a YAML file, performs health checks, and outputs the availability status, including the success rate of each endpoint over time.

## Features

- **HTTP Health Checks**: Periodically checks the health of a list of HTTP endpoints.
- **Availability Monitoring**: Tracks the success and failure rate of each endpoint.
- **YAML Configuration**: Loads a list of HTTP endpoints from a YAML file.
- **Cumulative Logging**: Logs the cumulative availability percentage of each domain after every test cycle (every 15 seconds).
- **Interval-based Monitoring**: Checks the health of the endpoints at fixed intervals (every 15 seconds).

## Requirements

- **Python 3.x**: Ensure you have Python 3 or later installed.
- **Requests**: Python package to make HTTP requests. You can install it using:
  ```bash
  pip install requests
  ```
- **PyYAML**: Python package for parsing YAML files. Install it using:
  ```bash
  pip install pyyaml
  ```

## Setup and Installation

### 1. Clone or Download the Repository

You can either clone the repository or download the script files.

```bash
git clone https://github.com/mthomasbc/take-home-exercise.git
cd take-home-exercise
```

### 2. Install Required Dependencies

Install the necessary Python libraries:

```bash
pip install requests pyyaml
```

### 3. Create a YAML File for Endpoints

Create a YAML file (e.g., `sample.yaml`) with the list of HTTP endpoints to monitor. The format should look like this:

```yaml
- "https://fetch.com"
- "https://fetch.com/careers"
- "https://fetch.com/some/post/endpoint"
- "https://fetchrewards.com/"
```

### 4. Run the Program

Run the program by providing the path to the YAML file containing the list of HTTP endpoints.

```bash
python main.py 
```

The program will start monitoring the endpoints, checking their health every 15 seconds, and logging the availability status.

## How It Works

1. **Input**: The program takes the path to a YAML file containing a list of HTTP endpoints.
2. **Health Checks**: Every 15 seconds, the program makes an HTTP GET request to each endpoint in the list.
3. **Availability Tracking**: The program tracks the number of successful responses (status code 200) and the total number of requests for each endpoint.
4. **Logging**: After each 15-second test cycle, the program calculates the availability percentage for each domain and logs it to the console.

## Example Output

```bash
Monitoring endpoints from: sample.yaml

Availability after 15 seconds:
Domain: fetch.com, Availability: 100.00%
Domain: fetchrewards.com, Availability: 66.67%

Availability after 15 seconds:
Domain: fetch.com, Availability: 100.00%
Domain: fetchrewards.com, Availability: 66.67%
```

## Parameters

- **Interval**: The program checks the health of the endpoints every 15 seconds. You can modify this interval by adjusting the `time` parameter in the `main()` function.
- **Availability Calculation**: Availability for each domain is calculated as the ratio of successful requests to the total requests made (successful/total * 100).

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
