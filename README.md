# python_robot_exercises

# NASA API Test Suite

This project contains a test suite for the NASA API using Robot Framework. The tests are designed to verify various aspects of the NASA API and ensure its functionality. The project is containerized using Docker to ensure consistency and ease of use.

## Project Structure
robot-api-test-framwork/ ├── config/ │ └── config.json ├── libraries/ │ └── nasa_api_library.py ├── keywords/ │ └── NasaApiKeywords.robot ├── tests/ │ └── NasaApiTests.robot ├── resources/ │ └── resource_gnf.robot ├── logs/ │ └── log.txt ├── Dockerfile ├── docker-compose.yml ├── requirements.txt └── README.md
## Files and Directories

- `config/config.json`: Configuration file containing the base URL for the NASA API.
- `libraries/nasa_api_library.py`: Python library for interacting with the NASA API.
- `keywords/NasaApiKeywords.robot`: Robot Framework keywords for the NASA API.
- `tests/NasaApiTests.robot`: Test cases for the NASA API.
- `resources/resource_gnf.robot`: Additional resources for the test suite.
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
   git clone <repository_url>
   cd project_root
   

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
