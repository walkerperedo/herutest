from fastapi import FastAPI
from routes.trip_routes import trip_api_router

app = FastAPI()
app.include_router(trip_api_router)