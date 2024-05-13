from flask import Flask, jsonify, request
import redis

app = Flask(__name__)
client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    return "Welcome  App!"

@app.route('/set/<key>/<value>')
def set_value(key, value):
    client.set(key, value)
    return f"Set {key} to {value}"

@app.route('/get/<key>')
def get_value(key):
    value = client.get(key)
    if value:
        return jsonify({key: value})
    else:
        return f"{key} not found", 404

@app.route('/delete/<key>')
def delete_value(key):
    value = client.get(key)
    if value:
        client.delete(key)
        return 'key deleted successfully'
    else:
        return f"{key} not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
