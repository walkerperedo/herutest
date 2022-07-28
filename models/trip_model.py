from typing import Optional
from pydantic import BaseModel
from datetime import date
from uuid import UUID

class Trip(BaseModel):
    departure_date: date
    arrival_date: date
    origin_name: str
    destination_name: str
    weather_arrival_city: Optional[str] = None
    weather_departure_city: Optional[str] = None
    user_id: UUID
    lat_arrival: str
    lon_arrival: str
    lat_departure: str
    lon_departure: str