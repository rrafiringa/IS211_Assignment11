#!/usr/bin/env python
# -*- Coding: utf-8 -*-

"""
Assignment 11: Basic Flask application
"""

import flask

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return '<h2>Hello World!</h2>'


@app.route('/<name>')
def greet(name):
    return '<h2>Hello {}</h2>'.format(name)


if __name__ == '__main__':
    app.run(port=5000)
