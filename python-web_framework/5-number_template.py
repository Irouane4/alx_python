#!/usr/bin/python3
"""
This script starts a Flask web application.
The web application listens on 0.0.0.0, port 5000, and has six routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"
- /c/<text>: Displays "C " followed by the value of the text variable
  (replace underscore _ symbols with a space).
- /python/<text>: Displays "Python " followed by the value of the text variable
  (replace underscore _ symbols with a space). The default value of text is "is cool".
- /number/<n>: Displays "n is a number" only if n is an integer.
- /number_template/<n>: Displays an HTML page with H1 tag: "Number: n" inside the tag BODY,
  only if n is an integer.
"""

from flask import Flask, render_template

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
    (replace underscore _ symbols with a space).
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
def display_python(text):
    """
    Displays "Python " followed by the value of the text variable
    (replace underscore _ symbols with a space). The default value of text is "is cool".
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Displays "n is a number" only if n is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    Displays an HTML page with H1 tag: "Number: n" inside the tag BODY,
    only if n is an integer.
    """
    return render_template('5-number_template.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
