from service.trip_service import get_trip_service, create_trip_service, get_trips_from_user_service

def get_one_trip(trip_id):
    return get_trip_service(trip_id)  

def create_trip(trip):
    return create_trip_service(trip)

def get_trips_from_user_controller(user_id):
    return get_trips_from_user_service(user_id)