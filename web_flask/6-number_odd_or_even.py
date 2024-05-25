#!/usr/bin/python3
"""
This script starts a Flask web application.

The web application listens on 0.0.0.0, port 5000 and has the following routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space)
    /python/(<text>): display “Python ” followed by
                      the value of the text variable
        (replace underscore _ symbols with a space,
        the default value is “is cool”)
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY

You must use the option strict_slashes=False in your route definition.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' at the root URL
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' at the /hbnb URL
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays 'C' followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays 'Python' followed by the value of the text variable
    (replace underscore _ symbols with a space, the default value is 'is cool')
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays 'n is a number' only if n is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template(
        'number_odd_or_even.html', n=n, odd_or_even=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)