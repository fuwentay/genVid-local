from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

mongopass = os.environ.get('mongo_password')
cluster = MongoClient(mongopass)
db = cluster["genVid"]


### Examples

# collection_media = db["media"]
# collection_videos = db["videos"]

# post1 = {"_id": 0, "name": "tim", "score": 5}
# post2 = {"_id": 1, "name": "sam", "score": 2}

# collection_media.insert_one(post2)
# collection_media.insert_many([post1, post2])
# collection.find({"name": "bill"})
# collection.delete_one({"_id": 0})
# collection.delete_many({})
# collection.update_one({"_id: 1"}, {"$set": {"name": "tim"}})
# collection.count_documents({})