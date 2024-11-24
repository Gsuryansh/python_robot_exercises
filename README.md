# python_robot_exercises

# 1. Python exercise: 

success_rate.py will read a log file bs-log.txt and give the overall success rate and hourly success rate for the RRC Connection Request.

## setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Gsuryansh/python_robot_exercises.git
   cd python_robot_exercises

2. python3 success_rate.py

## Running test
It will print the overall success rate and hourly success rate for the RRC Connection Request.


# 2. Robot framework exercise


# NASA API Test Suite

This project contains a test suite for the NASA API using Robot Framework. The tests are designed to verify various aspects of the NASA API and ensure its functionality. The project is containerized using Docker to ensure consistency and ease of use.

## Project Structure
robot-api-test-framwork/ ├── config/ │ └── config.json ├── libraries/ │ └── nasa_api_library.py ├── keywords/ │ └── NasaApiKeywords.robot ├── tests/ │ └── NasaApiTests.robot ├── resources/ │ └── resource_gnf.robot ├── logs/ │ └── log.txt ├── Dockerfile ├── docker-compose.yml ├── requirements.txt └── README.md
## Files and Directories

- `config/config.json`: Configuration file containing the base URL for the NASA API.
- `libraries/nasa_api_library.py`: Python library for interacting with the NASA API.
- `keywords/NasaApiKeywords.robot`: Robot Framework keywords for the NASA API.
- `tests/NasaApiTests.robot`: Test cases for the NASA API.
- `logs/`: Directory where log files are stored.
- `Dockerfile`: Dockerfile for building the Docker image.
- `docker-compose.yml`: Docker Compose file for managing the Docker container.
- `requirements.txt`: List of Python dependencies.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/Gsuryansh/python_robot_exercises.git
   cd python_robot_exercises/robot-api-test-framework
   

2. Build the Docker image:  
docker-compose build
3. Run the tests:  
docker-compose up

## Running Tests

The tests are run inside a Docker container. The logs are saved in the logs directory on the host machine. Each test run generates a new log file with a unique name based on the current date and time.  

## configuration

The config/config.json file contains the base URL for the NASA API. You can modify this file to point to a different API endpoint if needed.  

## Dependencies

The project uses the following Python dependencies:  
1. requests
2. robotframework

These dependencies are listed in the requirements.txt file and are installed automatically when the Docker image is built. 


# 3. Combine Python and Robot

# Read log file and check the success rate
This project read the bs_log file and check for the passed and failed connection request. And calculate the overall passed rate.

## Files and Directories

- `log_file/bs_log.txt`: Log file to calculate failed and passed rate
- `libraries/calculate_success_rate.py`: Python library for calculating success rate.
- `success_rate_tests`: Test cases for the NASA API.
- `logs/`: Directory where log files are stored.
- `Dockerfile`: Dockerfile for building the Docker image.
- `docker-compose.yml`: Docker Compose file for managing the Docker container.
- `requirements.txt`: List of Python dependencies.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/Gsuryansh/python_robot_exercises.git
   cd python_robot_exercises/success_rate_robot_test
   

2. Build the Docker image:  
docker-compose build
3. Run the tests:  
docker-compose up


## Running Tests

The tests are run inside a Docker container. The logs are saved in the logs directory on the host machine. Each test run generates a new log file with a unique name based on the current date and time. Robot file accept 2 argument path of log file and success_rate if not pass at run time default value will be set which is present in test file 



