"""
Run to query all objects in AWS bucket
"""
import boto3
import os
print('Connecting to s3')
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'testpicmetric'
# ### ASSUMING JSON FROM BACK-END
# directory_name =
# user_id = ’textpicmetric/
##### CREATING DIRECTORIES FOR testpicmetric
# import boto3
# s3 = boto3.client(‘s3’)
# bucket_name = “aniketbucketpython”
# directory_name = “aniket/bucket/python” #it’s name of your folders
# s3.put_object(Bucket=bucket_name, Key=(directory_name+‘/’))
current_region = 'us-east-2'
for my_bucket_object in s3_resource.Bucket(bucket_name).objects.all():
    print(my_bucket_object)
