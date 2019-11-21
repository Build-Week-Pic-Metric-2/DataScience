"""Fetching image from s3 for model analysis"""
import boto3
import os
import shutil

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

bucket_name = 'testpicmetric'
current_region = 'us-east-2'


# ### ASSUMING JSON FROM BACK-END
# directory_name = 
# user_id = 'textpicmetric/


def get_picture_for_model(user_id, image_id):
    """Tapping into s3 bucket for single image"""
    path = f'images/{user_id}/{image_id}'
    s3_resource.Object(bucket_name, path).download_file(f'{image_id}')
    return None


def clear_images():
    folder_path = '/images'
    for file_object in os.listdir(folder_path):
        file_object_path = os.path.join(folder_path, file_object)
        if os.path.isfile(file_object_path):
            os.unlink(file_object_path)
        else:
            shutil.rmtree(file_object_path)