from instagrapi import Client
from instagrapi.types import Usertag, Location

import os
from dotenv import load_dotenv

from database import db

import time

collection_media = db["media"]

# Initiate instagrapi client
cl = Client()
cl.login(
    os.environ.get('instagram_username'), 
    os.environ.get('instagram_password')
    )

def post_video(question):
    load_dotenv()

    hashtags = "#meme #memes #funny #dankmemes #memesdaily #funnymemes #lol #humor #follow #dank #love #like #memepage #comedy #instagram #dankmeme #tiktok #anime #lmao #dailymemes #edgymemes #fun #ol #offensivememes #memestagram #bhfyp #funnymeme #instagood #shitpost #memer"
    
    time.sleep(7)

    media = cl.video_upload(
        "/tmp/project/" + question + "/video.mp4",
        "\n" + question + "\n" + "\n" + "Leave a comment below on what you want to see tomorrow!" + "\n" + "\n" + hashtags,
        usertags=[Usertag(
            user=cl.user_info_by_username(get_username(get_latest_post_id())),
            x=0.5, 
            y=0.5
            )],
        # location=Location(name='Singapore', lat=59.96, lng=30.29)
    )

    # Upload post metadata to media collection of MongoDB - genVid DB
    post_data = media.dict()
    collection_media.insert_one(post_data)


# Find the id of post based on the latest 'taken_at' timing
def get_latest_post_id():
    time.sleep(7)
    latest_table = collection_media.find().sort([("taken_at", -1)]).limit(1)
    id = latest_table[0]['id']
    return id

# Fetches comment of last post from DB
def get_comment(media_id):
    time.sleep(7)
    try:
        comments_data = cl.media_comments(media_id)
        comment_data = comments_data[0].dict()
        comment_text = comment_data['text']
        print(comment_text)
        return comment_text
    # FIXME: Empty error
    except:
        question = "A funny story"
        print(question)
        return question

# get_comment(get_latest_post_id())

def get_username(media_id):
    time.sleep(7)
    try:
        comments_data = cl.media_comments(media_id)
        comment_data = comments_data[0].dict()
        comment_user = comment_data['user']
        comment_username = comment_user['username']
        print(comment_username)
        return comment_username
    # FIXME: Empty error
    except:
        username = 'jengatrain'
        print(username)
        return username    