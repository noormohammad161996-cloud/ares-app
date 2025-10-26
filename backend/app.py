from flask import Flask, request, jsonify
from flask_cors import CORS       # ✅ Import CORS
from business import get_data

app = Flask(__name__)
CORS(app)                         # ✅ Allow frontend to access backend

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api', methods=['GET'])
def api1():
    data = get_data()
    data = {'data': data}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8083, debug=True)
