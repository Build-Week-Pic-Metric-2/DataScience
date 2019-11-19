from flask import Flask
# from .dummy_extract_functions import extract_objects
from .facedetector import extract_faces
# from .dummy_summary_functions import batch_img_summary, summary
import os

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
data_url = os.path.join(SITE_ROOT, "images")

img_path = '/people.jpg'

# ' {"1234_userID":{"jobID":{"face_count":5, "car_count":2}}} '


# wasn't sure how to give each user a unique id, so I made a class
# to put each user in. Will probably change this


def create_app():
    app = Flask(__name__)

    # APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    # APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['DEBUG'] = True
    # DB = SQLAlchemy(APP)

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

    @app.route('/extract_faces')
    def faces():
        # extracts faces from a given image
        # return str(img_path)
        return extract_faces(data_url + img_path)

    # @app.route('/extract_objects')
    # def objects():
    #     # extracts objects from a given image
    #     return extract_objects(img_path)

    return app


# if __name__ == "__main__":
#     load_model()
#     APP.run()
#     APP.run(threaded=False)
