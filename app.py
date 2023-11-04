# app.py
from flask import Flask, jsonify
from speech import get_certain_value

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/get_certain_value')
def get_value():
    value = get_certain_value()
    return jsonify({'value': value})

if __name__ == '__main__':
    app.run()
