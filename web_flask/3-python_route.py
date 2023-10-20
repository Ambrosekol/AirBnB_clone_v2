#!/usr/bin/python3


"""
This is a python a script that starts a Flask web application
1. ALX task 0
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_txt_input(text):
    newval = text.replace('_', ' ')
    return "C {}".format(escape(newval))


@app.route("/python/", defaults={'text': "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_txt_input(text):
    newchar = text.replace('_', ' ')
    return "python {}".format(escape(newchar))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
