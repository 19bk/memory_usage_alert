### Memory Usage Alert System

This project consists of a Python script that monitors the system's memory usage and sends an alert to a Flask API when the memory usage exceeds a specified threshold.

### Prerequisites

- Python
- pip (Python package installer)
- Virtual environment (optional)

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create and activate a virtual environment (optional)**
    - On Windows:
        ```bash
        python -m venv myenv
        .\myenv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        python -m venv myenv
        source myenv/bin/activate
        ```

3. **Install required packages**
    ```bash
    pip install flask psutil requests
    ```

### Running the Flask API

1. **Start the Flask app**
    ```bash
    python app.py
    ```
    The API will be running on [http://localhost:5000/](http://localhost:5000/).

### Running the Memory Monitoring Script

1. **Open a new terminal window or tab**

2. **Activate the virtual environment (if you are using one)**

3. **Run the memory monitoring script**
    ```bash
    python memory_monitor.py
    ```

    Make sure to replace `'http://localhost:5000/receive-alert'` with the actual URL where your Flask API is running if it's different.

### Testing the System

When the memory usage exceeds the specified threshold, the `memory_monitor.py` script will send an alert to the Flask API. You can also manually test the API using curl:

```bash
curl -X POST http://localhost:5000/receive-alert -H "Content-Type: application/json" -d '{"memoryUsage": 90}'
```

You should receive a response indicating that the alert has been received.

### Customization

- You can modify the `MEMORY_THRESHOLD` in the `memory_monitor.py` script to change the memory usage threshold for sending alerts.
- The Flask API can be extended to take additional actions when an alert is received, such as sending email notifications or logging alerts to a file.

