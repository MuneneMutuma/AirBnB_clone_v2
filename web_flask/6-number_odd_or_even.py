#!/usr/bin/env python3
"""A script that starts a Flask web application"""

from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """A function that handles /number/<n> if n is a number"""
    return (f"{n} is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """A function that renders a template for the route /number_template/<n>"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Renders a template for /number_odd_or_even/n and shows parity of n"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
