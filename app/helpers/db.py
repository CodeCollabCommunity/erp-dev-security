"""Mongodb instance """
import os
from pymongo import MongoClient


client = MongoClient(os.getenv("MONGODB_URL"))
db = client[f"{os.getenv("MONGO_DB")}"]
