# app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://api.example.com/data')  # External API call
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
