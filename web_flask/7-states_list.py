#!/usr/bin/python3
""" fetch all states"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ list states in database"""
    
    obj = storage.all("States")
    for key, value in obj.items():
        lis = key.split('.')
        render_template('7-states_list.html', id=lis[1])
        render_template('7-states_list.html', name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
