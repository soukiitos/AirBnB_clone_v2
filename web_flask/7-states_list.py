#!/usr/bin/python3
'''Start a Flask web application'''
from models import storage
from models.state import State
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


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''Define number odd or even'''
    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)


@app.route('/states_list')
def states_list():
    '''Define state list'''
    path = '7-states_list.html'
    states = storage.all('State')
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


@app.teardown_appcontext
def app_teardown(exception):
    '''Define app teardown'''
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
