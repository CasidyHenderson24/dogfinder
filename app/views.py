# -*- coding: utf-8 -*-

from app import app
from flask import render_template 

@app. route('/')

@app.route('/index')
def index():
	return render_template('petdraft.html')

@app.route('/first')
def first():
	return render_template('first.html')



@app.route('/second')
def second():
	return render_template('second.html')


@app.route('/third')
def third():
	return render_template('third.html')

