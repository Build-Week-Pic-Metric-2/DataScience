from flask import Flask
from facedetector import extract_faces, count_faces
from s3_fetch import get_picture_for_model, clear_images
import os
import shutil

### Make sure boto3 package installed in pipfile

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "Hello world!"

    # @app.route('/summary/<img_path>/', methods=['GET'])
    # def summary_app(img_path):
    #     # returns a single prediction for each detected face/object
    #     return summary(img_path)

    # @app.route('/batch_img_summary')
    # def batch_img_summary_app():
    #     # returns a group of predictions for each detected face/object
    #     return batch_img_summary(img_path)

    @app.route('/count_faces/<user_id>/<image_id>', methods = ['GET'])
    def faces(user_id, image_id):
        # 
        clear_images()
        user_id = user_id
        image_id = image_id
        # count faces from a given image
        get_picture_for_model(user_id, image_id)
        # creating new filepath
        new_image_path = os.getcwd() + f'/images/{image_id}'
        # move image to /images/ of flask_app directory
        os.rename(f'{image_id}', new_image_path)
        return count_faces(new_image_path, user_id, image_id)


    # @app.route('/extract_objects')
    # def objects():
    #     # extracts objects from a given image
    #     return extract_objects(img_path)

    return app
