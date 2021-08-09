from src.service import users_service

def login( user_id ):
    user = users_service.get_client_by_id(user_id)
    return user