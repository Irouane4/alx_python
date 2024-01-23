"""
This script starts a Flask web application.
The web application listens on 0.0.0.0, port 5000, and has two routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"
"""

from flask import Flask

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
