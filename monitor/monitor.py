import psutil
import requests
import time

# Flask API endpoint
API_URL = 'http://localhost:8080/receive-alert'


# Set the memory usage threshold i used percentage here
MEMORY_THRESHOLD = 40  # 80%

def send_alert(memory_usage):
    """
    Send an HTTP request to the API to notify of high memory usage.

    Parameters:
    - memory_usage: The current memory usage percentage.
    """
    payload = {'memoryUsage': memory_usage}
    try:
        response = requests.post(API_URL, json=payload)
        print(f'Alert sent: {response.text}')
    except Exception as e:
        print(f'Failed to send alert: {e}')

while True:
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    print(f'Memory usage: {memory_usage}%')

    if memory_usage > MEMORY_THRESHOLD:
        print('Memory usage exceeded the threshold. Sending alert...')
        send_alert(memory_usage)
    # sleep to avoid overload
    time.sleep(5)
