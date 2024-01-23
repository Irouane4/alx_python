# 10-hello_route.py

from flask import Flask, url_for, request, jsonify
import re

app = Flask(__name__)

def check_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def format_text(text):
    return re.sub('_', ' ', text)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C " + format_text(text)

@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return "Python " + format_text(text)

@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if check_int(n):
        return str(n) + " is a number"
    else:
        return jsonify({"error": "n must be an integer"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)