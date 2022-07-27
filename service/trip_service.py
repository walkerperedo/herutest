from bson.objectid import ObjectId
from config.database import collection_trip
from schemas.trip_schema import trip_serializer

def get_trip_service(trip_id: str):
    trip = trip_serializer(collection_trip.find_one({"_id": ObjectId(trip_id)})) 
    return {"status": "ok", "data": trip}

def create_trip_service(trip):
    dicttrip = dict(trip)
    user_id = str(dicttrip.get('user_id'))
    dicttrip.update({"user_id": user_id})

    _id = collection_trip.insert_one(dicttrip).inserted_id
    trip = trip_serializer(collection_trip.find_one({"_id": _id}))
    return {"status": "ok", "data": trip}