from flask import Flask, request
from .facedetector import extract_faces, count_faces
from .object_detector import get_detection
from .object_detector import get_summary
from .s3_fetch import clear_images, get_picture_for_model
# from .dummy_summary_functions import batch_img_summary, summary
import os
import jsonify
import requests
import shutil
import urllib.request
import random

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
data_url = os.path.join(SITE_ROOT, "images")

img_path = [data_url + '/' + f for f in os.listdir(data_url) if not f.startswith('.')]
# for image in img_path:
#     image = data_url + '/' + image

file_name = "/giraffes.jpg"


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return f"{img_path}"

    # @app.route('/summary/<img_path>/', methods=['GET'])
    # def summary_app(img_path):
    #     # returns a single prediction for each detected face/object
    #     return summary(img_path)

    # @app.route('/batch_img_summary')
    # def batch_img_summary_app():
    #     # returns a group of predictions for each detected face/object
    #     return batch_img_summary(img_path)

    @app.route('/extract_faces')
    def faces():
        # extracts faces from a given image
        return extract_faces(img_path)

    @app.route('/extract_objects')
    def objects():
        # extracts objects from a given image
        results, classnames = get_detection(img_path)
        summary = get_summary(img_path, results, classnames)
        return summary

    @app.route('/extract_one_image/<user_id>/<image_id>', methods = ['GET'])
    def extract_one_image(user_id, image_id):
        # clear_images()
        user_id = user_id
        image_id = image_id
        # count faces from a given image
        get_picture_for_model(user_id, image_id)
        # creating new filepath
        new_image_path = SITE_ROOT + f'/images/{image_id}'
        # move image to /images/ of flask_app directory
        os.rename(f'{image_id}', new_image_path)
        # extracts objects from a given image
        results, classnames = get_detection([new_image_path])
        summary = get_summary([new_image_path], results, classnames)
        return summary

    @app.route('/count_faces/<user_id>/<image_id>', methods=['GET'])
    def count_faces_aws(user_id, image_id):
        # clear_images()
        user_id = user_id
        image_id = image_id
        # count faces from a given image
        get_picture_for_model(user_id, image_id)
        # creating new filepath
        new_image_path = SITE_ROOT + f'/images/{image_id}'
        # move image to /images/ of flask_app directory
        os.rename(f'{image_id}', new_image_path)
        return count_faces(new_image_path, user_id, image_id)

    def downloader(image_url):
        file_name = random.randrange(1,10000)
        full_file_name = 'local_file.jpg'
        urllib.request.urlretrieve(image_url,full_file_name)

    @app.route('/extract_one_image_url', methods = ['POST'])
    def extract_one_image_url():
        #
        # clear_images()
        reader = request.get_json(force=True)
        user_id = reader['user_id']
        image_url = reader['image_url']
        assert isinstance(user_id, int)
        assert isinstance(image_url, str)
        downloader(image_url)
#        if resp.status_code == 200:
#        	local_file = open('local_image.jpg', 'wb')
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
#       	resp.raw.decode_content = True
        # Copy the response stream raw data to local image file.
#        shutil.copyfileobj(resp.raw, local_file)
        # count faces from a given image
        # get_picture_for_model(user_id, image_id)
       	# creating new filepath
       	new_image_path = SITE_ROOT + '/local_file.jpg'
        # move image to /images/ of flask_app directory
        # os.rename(f'{image_id}', new_image_path)
        # extracts objects from a given image
        results, classnames = get_detection([new_image_path])
        summary = get_summary([new_image_path], results, classnames)
        return jsonify(summary)

    return app

