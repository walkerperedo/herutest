from pymongo import MongoClient

client = MongoClient()

db = client.heru_test

collection_trip = db['trip']
collection_user = db['user']