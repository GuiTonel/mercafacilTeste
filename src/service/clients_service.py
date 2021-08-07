from src.database import User
from src.error import UserNotFound

def get_client_by_id( user_id ) -> User:
    user = User.get_by_id(user_id)
    if user is None:
        raise UserNotFound( f"User id {user_id} not Found" )

    return user