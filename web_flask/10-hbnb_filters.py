#!/usr/bin/python3
""" filters for hbnb site"""
from flask import Flask, render_templates
from modesl import stroage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ loads all states, cities and amenities for the hbnb site"""
    states = storage.all("State")
    cities = storage.all("Cities")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def close_session(self):
    """ closes session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
