from ..config.database import collection_user
from ..schemas.user_schema import user_serializer
from werkzeug.security import generate_password_hash

def create_user_service(user):
    user_dict = dict(user)
    hashed_password = generate_password_hash(user_dict.get('password'))

    user_dict.update({"password": hashed_password})

    _id = collection_user.insert_one(user_dict).inserted_id
    user = user_serializer(collection_user.find_one({"_id": _id})) 
    return {"status": "ok", "data": user}