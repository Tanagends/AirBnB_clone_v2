#!/usr/bin/python3
"""Web flask application"""
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """The landing page that returns “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """returns C followed by the value of the text variable"""
    return "C {}".format(text)


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def ptext (text="is cool"):
    """Returns Python followed by text variable"""
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """displays n if its only a number"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """renders template if n is a number"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run()
