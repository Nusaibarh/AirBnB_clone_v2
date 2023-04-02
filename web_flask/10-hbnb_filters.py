#!/usr/bin/python3
"""
flask webframe work
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/states_list/")
def list_states():
    allstate = storage.all(State)
    return render_template("7-states_list.html",
                           statesitems=allstate)


@app.route("/hbnb_filters/")
def list_cities():
    allstate = storage.all(State)
    allcities = storage.all(City)
    return render_template("10-hbnb_filters.html",
                           states=allstate,
                           cities=allcities)


@app.teardown_appcontext
def teardown(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
