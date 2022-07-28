from bson.objectid import ObjectId
from config.database import collection_trip
from schemas.trip_schema import trip_serializer, trips_serializer
from fastapi import HTTPException
import requests
import json

def get_trip_service(trip_id: str):
    trip = trip_serializer(collection_trip.find_one({"_id": ObjectId(trip_id)})) 
    return {"status": "ok", "data": trip}

def create_trip_service(trip):
    dicttrip = dict(trip)

    lat_arrival = dicttrip.get('lat_arrival')
    lon_arrival = dicttrip.get('lon_arrival')
    lat_departure = dicttrip.get('lat_departure')
    lon_departure = dicttrip.get('lon_departure')
    api_key = "3d512fd3cc03b10f1f5a545de5c118de"

    response_arrival = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat_arrival}&lon={lon_arrival}&appid={api_key}')

    if "message" in response_arrival.json():
        raise HTTPException(status_code=400, detail=response_arrival.json()['message'])

    description_arrival = response_arrival.json()['weather'][0]["description"]


    response_departure = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat_departure}&lon={lon_departure}&appid={api_key}')

    if "message" in response_departure.json():
        raise HTTPException(status_code=400, detail=response_arrival.json()['message'])

    description_departure = response_departure.json()['weather'][0]["description"]

    dicttrip.update({"weather_arrival_city": description_arrival})
    dicttrip.update({"weather_departure_city": description_departure})

    _id = collection_trip.insert_one(dicttrip).inserted_id
    saved_trip = trip_serializer(collection_trip.find_one({"_id": _id}))
    return {"status": "ok", "data": saved_trip}

def get_trips_from_user_service(user_id):
    trip = trips_serializer(collection_trip.find({"user_id": user_id}))
    return {"status": "ok", "data": trip}
