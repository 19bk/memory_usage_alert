# Memory Usage Alert System

This project provides a way to monitor system memory usage and trigger an alert if memory usage exceeds a predefined threshold. The alert is sent as an HTTP request to a Flask API, which then processes and acknowledges the alert.

## Components:

1. **Memory Monitor Script (`monitor.py`)**: A Python script that continuously checks the system's memory usage using the `psutil` library. If the memory usage exceeds the set threshold, it sends an alert to the Flask API.

2. **Flask API (`app.py`)**: A Flask-based REST API that listens for alerts from the monitor script. It provides an endpoint (`/receive-alert`) to receive and acknowledge memory usage alerts.

3. **Docker & Docker Compose**: The project uses Docker to containerize the Flask API and a MongoDB database. Docker Compose is used to manage and orchestrate these containers.

## Setup and Running:

### Prerequisites:

- Docker and Docker Compose installed.
- Python 3.x with `pip` for running the memory monitor script.

### Steps:

1. **Clone the repository**:
   ```bash
   git clone [repository_url] memory_usage_alert
   cd memory_usage_alert
   ```

2. **Build and Start the Containers**:
   ```bash
   sudo docker-compose up --build
   ```

3. **Run the Memory Monitor Script**:
   In a separate terminal:
   ```bash
   cd monitor
   pip install -r requirements.txt
   python monitor.py
   ```

4. **Testing**:
   The Flask API provides a `/value` endpoint for CRUD operations with key-value pairs stored in the MongoDB database. You can use tools like `curl` or Postman to test these endpoints.

## Configuration:

- **Memory Threshold**: The memory usage threshold after which an alert is sent is defined in `monitor.py` as `MEMORY_THRESHOLD`. By default, it's set to 40%.

- **API URL**: The Flask API endpoint to which the monitor script sends alerts is defined in `monitor.py` as `API_URL`. It's set to `http://localhost:8080/receive-alert` by default.

## Troubleshooting:

1. **Docker Issues**: If you face issues with Docker or Docker Compose, ensure that the Docker daemon is running. Restarting the Docker service or rebooting the system can resolve many common issues.

2. **Connection Issues**: Ensure that the Flask API is running and accessible if the monitor script cannot send alerts. Check the Docker logs for any errors.

3. **Dependencies**: Ensure that all Python dependencies are installed, both for the Flask API (in the Docker container) and the memory monitor script.
