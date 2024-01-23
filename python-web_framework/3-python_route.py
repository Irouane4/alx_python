#!/usr/bin/python3
"""
This script starts a Flask web application.
The web application listens on 0.0.0.0, port 5000, and has four routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"
- /c/<text>: Displays "C " followed by the value of the text variable
  (replace underscore _ symbols with a space)
- /python/<text>: Displays "Python " followed by the value of the text variable
  (replace underscore _ symbols with a space)
  The default value of text is "is cool"
"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" when the root route is accessed.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Displays "HBNB" when the /hbnb route is accessed.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Displays "C " followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
def display_python(text):
    """
    Displays "Python " followed by the value of the text variable
    (replace underscore _ symbols with a space).
    The default value of text is "is cool".
    """
    return 'Python {}'.format(escape(text.replace('_', ' ')))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
