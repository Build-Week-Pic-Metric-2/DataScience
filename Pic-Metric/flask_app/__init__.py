""" entry point for Pic-Metric flask app """

from .app import create_app

# APP is a global variable
APP = create_app()
APP.run(host="0.0.0.0")

# run this in terminal with FLASK_APP=flask_app:APP flask run
