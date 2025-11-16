from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from business import get_data

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def api1():
    data = get_data()
    data = {'data': data}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8083, debug=True)
