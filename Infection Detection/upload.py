# app.py
from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
app = Flask(__name__)

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
@app.route('/sel', methods=['GET', 'POST'])
def index():
    
    # set session for image results
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
    # redirect to home if no images to display
    # if "file_urls" not in session or session['file_urls'] == []:
    #     return redirect(url_for('index'))
        
    # # set the file_urls and remove the session variable
    # file_urls = session['file_urls']
    # session.pop('file_urls', None)
    path='C:/Users/Welcome/Downloads/Infection Detection/static/im'
    imName = os.listdir(path)[0]
    return render_template('shop-single.html',n1=imName )


if __name__ == '__main__':
   app.run(debug = True)