# inicio.py
# -*- coding: utf-8 -*-
import sqlite3
from bottle import route, run, template

@route('/')
def corde_fsa():
	x=-26.157204
	y=-58.1847421
	return template('inicio.html', coord1=x, coord2=y)

run(host="localhost", port=8080, debug=True)