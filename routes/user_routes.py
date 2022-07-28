from fastapi import APIRouter
from controller.user_controller import create_user_controller
from models.user_model import User

user_api_router = APIRouter()

@user_api_router.post("/user")
def create_user(user: User):
  return create_user_controller(user)
