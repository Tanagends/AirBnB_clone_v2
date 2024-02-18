#!/usr/bin/python3
"""Web app that renders states list html in alphabetical order"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removes the current sqlalchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_lis():
    """renders a states list template"""
    ress = storage.all("State")
    res = sorted(ress.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', res=res)


if "__main__" == __name__:
    app.run()
