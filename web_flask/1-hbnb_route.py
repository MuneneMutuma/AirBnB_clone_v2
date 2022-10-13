#!/usr/bin/env python3
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
