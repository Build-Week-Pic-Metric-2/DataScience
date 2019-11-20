from flask import Flask
from .facedetector import extract_faces
from .object_detector import get_detection
from .object_detector import get_summary
# from .dummy_summary_functions import batch_img_summary, summary
import os

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

    @app.route('/extract_one_image')
    def one():
        # extracts objects from a given image
        results, classnames = get_detection([data_url + file_name])
        summary = get_summary([data_url + file_name], results, classnames)
        return summary

    return app
