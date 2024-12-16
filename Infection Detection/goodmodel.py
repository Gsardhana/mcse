
import tensorflow
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import urllib
import time
from urllib.request import urlretrieve

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from keras.models import load_model
classifier = load_model('dogcat_model_bak.h5')


def check(im):
  img1 = image.load_img(im, target_size=(64, 64))
  img = image.img_to_array(img1)
  img = img/255
  # create a batch of size 1 [N,H,W,C]
  img = np.expand_dims(img, axis=0)
  prediction = classifier.predict(img, batch_size=None,steps=1) #gives all class prob.
  if(prediction[:,:]>0.5):
      check.animal = 'Dog'
      value ='Dog :%1.2f'%(prediction[0,0])
      plt.text(20, 62,value,color='red',fontsize=18,bbox=dict(facecolor='white',alpha=0.8))
  else:
      check.animal = 'Cat'
      value ='Cat :%1.2f'%(1.0-prediction[0,0])
      plt.text(20, 62,value,color='red',fontsize=18,bbox=dict(facecolor='white',alpha=0.8))

  plt.imshow(img1)
  plt.show()
  # time.sleep(1)
  # plt.close()
  print( check.animal)

#check('a6.jpg')