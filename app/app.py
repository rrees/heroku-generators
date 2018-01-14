import os
import logging

import flask

from flask_sslify import SSLify

from . import handlers

ENV = os.environ.get("ENV", "PROD")

app = flask.Flask(__name__)
app.secret_key =  os.environ.get("SECRET_KEY", os.urandom(24))

if not ENV == "DEV":
    sslify = SSLify(app)

routes = [
    ('/', 'index', handlers.pages.front_page, ['GET']),
    ('/generator/<generator_id>', 'generator', handlers.pages.generator, ['GET']),
]

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500