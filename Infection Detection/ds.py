from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import urllib
from urllib.request import urlretrieve
from goodmodel import check
from tt import googleim
import random
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import glob, os, os.path

app = Flask(__name__)
app.static_folder = 'static'


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


dropzone = Dropzone(app)
# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = False
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'
app.config['SECRET_KEY'] = 'supersecretkeygoesheri'
# Uploads settings
path='C:/Users/Welcome/Downloads/Infection Detection/static/im'
app.config['UPLOADED_PHOTOS_DEST'] = path 
#file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

@app.route("/")

def home():
	return render_template('home.html')

@app.route("/click")

def click():
	return render_template('capture.html')

@app.route("/cap")

def capture():
	link='http://192.168.43.1:8080/photo.jpg'
	path='C:/Users/Welcome/Downloads/Infection Detection/static/im'
	filelist = glob.glob(os.path.join('static/im', "*.*g"))
	for f in filelist:
		os.remove(f)
	r1 = str(random.randint(0, 1000))
	sample = r1+'.jpg'	
	full_file_name = os.path.join(path, sample)
	urllib.request.urlretrieve(link,full_file_name)
	imname = path+'/'+sample
	return render_template('shop-single.html',n1 = r1+'.jpg')


@app.route('/sel', methods=['GET', 'POST'])
def index():
	filelist = glob.glob(os.path.join('static/im', "*.*g"))
	for f in filelist:
		os.remove(f)
	if "file_urls" not in session:
		session['file_urls'] = []
    # list to hold our uploaded image urls
	file_urls = session['file_urls']
	# handle image upload from Dropzone
	if request.method == 'POST':
		file_obj = request.files
		for f in file_obj:
			file = request.files.get(f)
			
			# save the file with to our photos folder
			filename = photos.save(
				file,
				name=file.filename    
			)
			# append image urls
			file_urls.append(photos.url(filename))
		session['file_urls'] = file_urls
		return "uploading..."

	# return dropzone template on GET request    
	return render_template('index.html')


@app.route('/results')
def results(): 
	path='C:/Users/Welcome/Downloads/Infection Detection/static/im'
	imName = os.listdir(path)[0]
	return render_template('shop-single.html',n1=imName )



@app.route("/pred")

def saveim():

	path='C:/Users/Welcome/Downloads/Infection Detection/static/im'
	imName = os.listdir(path)[0]
	abspa = path+'/'+imName
	
	check(abspa)
	saveim.res = check.animal
	print(saveim.res)

	return render_template('animal.html',n1 = imName ,n4=saveim.res)

@app.route("/inf")

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
	saveim.res
	template = res +'_in_' +saveim.res +'s.html'

	print(template)
	return render_template(template,n1 = imName )


if __name__ == '__main__':
   app.run(debug = True)
