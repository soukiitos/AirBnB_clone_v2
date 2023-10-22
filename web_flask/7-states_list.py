#!/usr/bin/python3
'''Start a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list')
def states_list():
    '''Define state list'''
    path = '7-states_list.html'
    states = storage.all(State)
    sorted_state = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_state=sorted_state)


@app.teardown_appcontext
def app_teardown(arg=None):
    '''Define app teardown'''
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
