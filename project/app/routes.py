from app import application
from flask import render_template, flash, redirect, url_for
from werkzeug.urls import url_parse
from app import db
from flask import request 
from app.serverlibrary import * 


@application.route('/')
@application.route('/index')
def index():
	return render_template('index.html', title='Predictor') 

# write down your handler for the routes here







