from pymongo import MongoClient
from decouple import config


def get_database():
    CONNECTION_STRING = config('CONNECTION_URL')

    cluster = MongoClient(CONNECTION_STRING)

    db = cluster['task_manager']
    return db


db = get_database()
