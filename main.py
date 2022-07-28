from fastapi import FastAPI
from routes.trip_routes import trip_api_router
from routes.user_routes import user_api_router

app = FastAPI()
app.include_router(trip_api_router)
app.include_router(user_api_router)