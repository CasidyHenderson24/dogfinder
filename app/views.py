# -*- coding: utf-8 -*-

from app import app
from flask import render_template 

@app. route('/')
@app. route('/home')

@app.route('/index')
def index():
	return render_template('home.html')

@app.route('/petfinder')
def petfinder():
	return render_template('petfinder.html')





@app.route('/petid')
def petid():
	return render_template('petid.html')

@app.route('/notifications')
def notifications():
	return render_template('notifications.html')

@app.route('/petowner')
def petowner():
	return render_template('petowner.html')

