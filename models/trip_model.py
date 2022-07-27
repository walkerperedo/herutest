from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class Trip(BaseModel):
    departure_date: str
    arrival_date: str
    origin_name: str
    destination_name: str
    weather_arrival_city: str
    weather_departure_city: str
    user_id: UUID