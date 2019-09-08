#!/usr/bin/python3
""" fetch all states"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=""):
    """ cities and states"""
    states = storage.all("State")
    cities = storage.all("City")
    if id is not "":
        for state in states.values():
            if state.id == id:
                this_state = state
                return render_template('9-states.html',
                                       state=this_state, cities=cities)
        no = "Not found!"
        return render_template('9-states.html', no=no)
    return render_template('9-states.html', states=states, cities=cities)


@app.teardown_appcontext
def close_session(self):
    """ close"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
