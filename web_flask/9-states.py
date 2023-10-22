#!/usr/bin/python3
'''Start a Flask web application'''
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    '''Define close'''
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    '''Define state'''
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    '''Define state id'''
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
