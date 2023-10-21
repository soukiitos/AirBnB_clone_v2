#!/usr/bin/python3
'''Start a Flask web application'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    '''Define a hello hbnb'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''Define hbnb'''
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    '''Define c is fun'''
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
