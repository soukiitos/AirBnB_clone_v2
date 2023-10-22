#!/usr/bin/python3
'''Start a Flask web application'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    '''Define hello hbnb'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''Define hbnb'''
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    '''Define c is fun'''
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    '''Define python with text'''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    '''Define number'''
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    '''Define number template'''
    path = '5-number.html'
    return render_template(path, n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
