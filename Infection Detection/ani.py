from flask import Flask, render_template, redirect, url_for, request
import urllib
from urllib.request import urlretrieve
from tt import googleim
import random
import matplotlib
from goodmodel import check

import glob, os, os.path

app = Flask(__name__)
app.static_folder = 'static'


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


@app.route("/")

def infect():
	path='C:/Users/Welcome/Downloads/Infection Detection/static/im'
	imName = os.listdir(path)[0]
	abspa = path+'/'+imName
	print(abspa)
	googleim(abspa)
	res = googleim.infection
	if res=='blastomyces':
		res='blastomycosis'
	else:
		if res=='neumocystosis':
			res='pneumocystosis'
	template = res+'.html'

	print(template)
	return render_template(template)


@app.route("/pred")

def saveim():

	path='C:/Users/Welcome/Downloads/Infection Detection/static/im'
	imName = os.listdir(path)[0]
	abspa = path+'/'+imName
	
	check(abspa)
	res = check.animal

	return render_template('animal.html',n1 = imName ,n4=res)
if __name__ == '__main__':
   app.run(debug = True)
