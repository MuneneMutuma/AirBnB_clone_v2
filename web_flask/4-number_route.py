#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """A function that responds for the root route"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """A function that responds for the route /hbnb"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def C_route(text):
    """A function that handles /c/<text> routes"""
    return (f"C {text.replace('_', ' ')}")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """A function that handles /python/<text> routes and /python routes"""
    return (f"Python {text.replace('_', ' ')}")


@app.route('/number/<int:n>')
def number(n):
    """A function that handles /number/<n> if n is a number"""
    return (f"{n} is a number")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
