import boto3
from dotenv import load_dotenv

def upload_to_s3(question):
    load_dotenv()
    client = boto3.client('s3')

    # set variables
    bucket = 'genvid'
    file = 'video.mp4'
    filename = question + '.mp4'

    client.upload_file(file, bucket, filename)

upload_to_s3("hello")
