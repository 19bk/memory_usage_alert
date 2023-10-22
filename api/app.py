from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive-alert', methods=['POST'])
def receive_alert():
    try:
        data = request.json
        memory_usage = data.get('memoryUsage')
        
        if memory_usage is not None:
            print(f"Received alert! Memory usage: {memory_usage}%")
            return jsonify({'message': 'Alert received', 'memoryUsage': memory_usage}), 200
        else:
            return jsonify({'message': 'Invalid data', 'error': 'memoryUsage not found'}), 400
            
    except Exception as e:
        print(e)
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
