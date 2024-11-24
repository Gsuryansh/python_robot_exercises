# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app:/robot-api-test-framework/libraries:/robot-api-test-framework/keywords

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY . /app

# Command to run the Robot Framework tests
CMD ["sh", "-c", "robot --outputdir /logs --log log_$(date +%Y%m%d%H%M%S).html tests/NasaApiTests.robot"]