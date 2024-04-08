"""Module por database uri"""
from os import getenv


def get_mongo_uri():
    host = getenv("MONGO_HOST")
    port = getenv("MONGO_PORT", 27017)
    password = getenv("MONGO_PASSWORD")
    user = getenv("MONGO_USER")
    db_name = getenv("MONGO_DB")
    return f"mongodb://{host}:{port}/{db_name}"
