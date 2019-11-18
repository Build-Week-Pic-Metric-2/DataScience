"""Face detector function to extract all faces from an image"""
from matplotlib import pyplot
from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN
import os
import shutil
import requests 
from io import BytesIO
import urllib.request


# extract a single face from a given photograph
def extract_faces(filename_or_orl):
# load image from file

    # # Experimenting with pulling images from URLs
    # response = requests.get(url)
    # img = Image.open(BytesIO(response.content))
    # image = Image.open(urllib.request.urlopen(url))


    # Actual code
    pixels = pyplot.imread(filename_or_orl)
    # create the detector, using default weights
    detector = MTCNN()
    # Select image file in "user[123]" and name "people"
    users = []
    # detect faces in the image
    results = detector.detect_faces(pixels)
    i=0
    for result in results:
        #insert face only if confidence is greater than 10%
        if(result['confidence'] > 0.99):
            face_x,face_y,width,height = result['box']
            #check for negative index
            if((face_x > 0) & (face_y >0)):
                face = pixels[face_y:face_y+height,face_x:face_x+width]
                face_image = Image.fromarray(face)
                face_image.save(f'{i}.jpg')
                dir_path = os.getcwd() + f'/{i}.jpg'
                shutil.move(dir_path, os.getcwd() + '/output/faces/')
                i +=1
    return f'{i} faces have been detected in the given image'

url2 = 'people.jpg'
url = 'https://raw.githubusercontent.com/Build-Week-Pic-Metric-2/DataScience/master/examples/001.jpeg'
extract_faces(url2)

# # load the photo and extract the face
# extract_faces('people.jpg')