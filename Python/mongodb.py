import pymongo
import datetime
from pymongo import MongoClient


client = MongoClient()
client = MongoClient('localhost', 27017)
# OR client = MongoClient('localhost', 27017)

db = client['test-database']
#db2 = client.test_database

collection1 = db['test-collection']
#collection2 = db.test_collection

post = {"author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

print(post_id)