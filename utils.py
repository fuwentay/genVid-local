import os
import shutil
import random
import time
import boto3
from dotenv import load_dotenv

# Clean directory of intermediate files and shift video to videos folder.
def clean_dir(storyline):
# TODO: add some try/excepts such that it does not break when file not found
    shutil.rmtree("/tmp/responses")
    shutil.rmtree("/tmp/images")
    os.remove("/tmp/output.mp4")
    os.remove("/tmp/"+ storyline[:10] + ".mp3")

    directory_path = "/tmp/audio/"
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

# clean_dir("The key to aldbnwildb")


# Move files to a projects folder to store all past videos created, including their raw files.
def move_files(question, storyline):
    # created new folder called project such that files will be moved to here.
    project_folder = "/tmp/project"
    project = project_folder + "/" + question
    os.mkdir(project_folder)
    os.mkdir(project)
    shutil.move('/tmp/video.mp4', project)
    shutil.move('/tmp/output.mp4', project)
    shutil.move("/tmp/" + storyline[:10] + ".mp3", project)
    shutil.move('/tmp/responses', project)
    shutil.move('/tmp/images', project)
    shutil.move('/tmp/audio', project)

# move_files("How do you eat an oreo","Once upon a")    


def random_wait():
    duration = random.random() * 120
    time.sleep(duration)


def long_wait():
    time.sleep(240)


def upload_to_s3(question):
    load_dotenv()
    client = boto3.client('s3')

    # set variables
    bucket = 'genvid'
    file = '/tmp/video.mp4'
    filename = question + '.mp4'

    client.upload_file(file, bucket, filename)



