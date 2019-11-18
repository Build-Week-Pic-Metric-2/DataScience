""" entry point for twitoff flask app """

from .app import create_app

# APP is a global variable
APP = create_app()

# run this in terminal with FLASK_APP=flask_app:APP flask run
