from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when accessing the root route"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when accessing the '/hbnb' route"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text="is cool"):
    """Display 'C ' followed by the value of the text variable (replace underscore _ symbols with a space)"""
    return "C " + text.replace("_", " ")

@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """Display 'Python ' followed by the value of the text variable (replace underscore _ symbols with a space)"""
    return "Python " + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display '<n> is a number' if n is an integer"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number_template.html', n=n)

@app.errorhandler(404)
def not_found_error(error):
    """Return a custom 404 error page"""
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)