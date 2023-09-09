from flask  import Flask
from pymongo import MongoClient
import json
import random

app = Flask("Authentication-Service")

# MongoDB Local connection 
def connect_to_mongodb_from_json(json_file):

    with open(json_file,'r'): # 'r' flag reprensents read mode opening 
        config = json.load(json_file)
    # JSON read 
    MONGO_URL= config.get("MONGO_URL")
    Collection_Name = config.get("collection")
    
    client = MongoClient(MONGO_URL)
    db = client.get_database()
    
    collection = getattr(db, Collection_Name)  # In this code, getattr(db, Collection_Name) allows you to access the collection specified by the Collection_Name variable dynamically. Make sure that Collection_Name contains the actual name of the collection you want to access from your MongoDB database.

    
    return db


