def user_serializer(trip) -> dict:
    return{
        "id": str(trip["_id"]),
        "name": trip["name"],
        "email": trip["email"],
        "password": trip["password"]
    }