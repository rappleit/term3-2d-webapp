from app import application
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import db
from flask import request 
from app.serverlibrary import * 
import pickle
import numpy as np

model = pickle.load((open("predMod.pkl", "rb")))

@application.route('/')
@application.route('/index')
def index():
	return render_template('index.html', title='Predictor') 

# write down your handler for the routes here
@application.route("/predict", methods=['POST'])
def prediction():
	coc = request.form["corruptionValue"]
	pol = request.form["polValue"]
	rol = request.form["rolValue"]
	ge = request.form["geValue"]
	lr = request.form["lrValue"]
	inputArr = [coc, pol, rol, ge, lr]
	arr = np.array([[0, coc, pol, rol, ge, lr]])
	pred = model.predict(arr)
	return render_template('index.html', title='Predictor', data=pred, input=inputArr) 







