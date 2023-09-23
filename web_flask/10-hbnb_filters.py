#!/usr/bin/python3
"""Script that starts a Flask web application"""

""" Import Flask and render_template from flask module """
from flask import Flask, render_template

"""
    Import the State and Amenity classes from the
    models.state and models.amenity modules
"""
from models.state import State
from models.amenity import Amenity

""" Import the storage module from the models package """
from models import storage

""" Create an instance of the Flask application """
app = Flask(__name__)

""" Define a route for the web application in '/hbnb_filters """
@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Display an HTML page: (inside the BODY tag)
    """
    """ Get all State objects from the database """
    states = storage.all(State).values()

    """ Sort states alphabetically by name """
    sorted_states = sorted(states, key=lambda state: state.name)

    """ Get all Amenity objects from the database """
    amenities = storage.all(Amenity).values()

    """ Render the template '10-hbnb_filters.html'
        with the states and amenities
    """
    return render_template('10-hbnb_filters.html',
                           states=sorted_states, amenities=amenities)

"""
    Define a function to close the connection
    to the database in the context of the application
"""
@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown
    """
    storage.close()

""" Check if the file is running as the main program """
if __name__ == '__main__':
    """ Start the web app """
    """ Start Flask application on host '0.0.0.0' and port '5000' """
    app.run(host='0.0.0.0', port='5000')
