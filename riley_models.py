"""models.py is 3 functions: count_img, writeToJSONFile, export_count_json"""

import os
import json


def count_img(folder_name):
    """Number of Files in chosen folder using os.walk"""
    dir_name = os.getcwd() + '/' + 'output' + '/' + folder_name
    file_count = sum([len(files) for r, d, files in os.walk(dir_name)])
    # print('Number of Files using os.walk          :', file_count)
    return(file_count)


def writeToJSONFile(path, fileName, data):
    """This Function asks for a location, name, and info to be stored in a
       .json file.

       Agr: path, fileName, data.
       Rtn: .json file at specified location.
    """
    filePathNameWExt = path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


def export_count_json():
    """This Function combines count_img and writeToJSONFile to Export a
      .json file to the Back-End.
    """
    path = os.getcwd()  # Making path for writeToJSONFile
    filename = 'export'  # Making path for writeToJSONFile
    # Making Data for writeToJSONFile with count_img
    data = {
        'user_ID' : {
            'job_ID': {
                "face_count": count_img('Test'),
                "car_count": 2
                      }
                    }
            }
    writeToJSONFile(path, filename, data)
