from fastapi import APIRouter
from ..controller.trip_controller import get_one_trip, create_trip, get_trips_from_user_controller
from ..models.trip_model import Trip

trip_api_router = APIRouter()

@trip_api_router.get("/trip/{trip_id}")
def get_trip(trip_id):
  return get_one_trip(trip_id)


@trip_api_router.post('/trip')
async def post_trip(trip:Trip):
    return create_trip(trip)

@trip_api_router.get('/trip/user/{user_id}')
def get_trip_from_user(user_id):
  return get_trips_from_user_controller(user_id)
