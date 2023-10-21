#!/usr/bin/python3
'''Start a Flask web application'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    '''Define hello hbhb'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''Define hbnb'''
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fub(text):
    '''Define c is fun'''
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    '''Define python with text'''
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.stricy_slashes = False
    app.run(host='0.0.0.0', port=5000)
