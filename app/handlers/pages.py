import flask

from ..data import generators

def front_page():
	return flask.render_template('index.html')

def generator(generator_id):

	return flask.render_template('generator.html', generator = generators.lookup(generator_id))