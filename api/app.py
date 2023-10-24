from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://db:27017/')  # 'db' is the name of the MongoDB service in docker-compose.yml
db = client.mydb  # 'mydb' is the name of the database
collection = db.my_collection  # Choose a collection name

@app.route('/value', methods=['GET', 'POST', 'PUT'])
def value():
    if request.method == 'POST':
        key = request.json.get('key')
        value = request.json.get('value')
        if key and value:
            collection.insert_one({'key': key, 'value': value})
            return jsonify({'message': 'Value created'}), 201
        return jsonify({'message': 'Invalid request'}), 400

    elif request.method == 'PUT':
        key = request.json.get('key')
        new_value = request.json.get('new_value')
        if key and new_value:
            collection.update_one({'key': key}, {'$set': {'value': new_value}})
            return jsonify({'message': 'Value updated'}), 200
        return jsonify({'message': 'Invalid request'}), 400

    elif request.method == 'GET':
        key = request.args.get('key')
        if key:
            item = collection.find_one({'key': key})
            if item:
                return jsonify({'value': item['value']}), 200
            return jsonify({'message': 'Key not found'}), 404
        return jsonify({'message': 'Invalid request'}), 400

@app.route('/receive-alert', methods=['POST'])
def receive_alert():
    memory_usage = request.json.get('memoryUsage')
    if memory_usage:
        # For now, just print the received alert. You can later decide to store it in MongoDB or perform other actions.
        print(f"Received memory usage alert: {memory_usage}%")
        return jsonify({'message': 'Alert received successfully'}), 200
    return jsonify({'message': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
