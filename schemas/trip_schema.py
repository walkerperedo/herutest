def trip_serializer(trip) -> dict:
    return{
        "id": str(trip["_id"]),
        "departure_date": trip["departure_date"],
        "arrival_date": trip["arrival_date"],
        "origin_name": trip["origin_name"],
        "destination_name": trip["destination_name"], 
        "weather_arrival_city": trip["destination_name"], 
        "weather_departure_city": trip["weather_departure_city"],
        "user_id": str(trip["user_id"])
    }