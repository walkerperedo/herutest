from pymongo import MongoClient

client = MongoClient()

db = client.heru_test

collection_travel = db['trip']
colelction_user = db['user']