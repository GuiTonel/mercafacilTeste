from src.database.schemas import User
from src.database.varejao import Contact as ContactVarejao
from src.database.macapa import Contact as ContactMacapa
from src.enums import DatabaseEnum
from src.error import UserNotFound

def get_client_by_id( user_id ) -> User:
    user = User.get_by_id(user_id)
    if user is None:
        raise UserNotFound( f"User id {user_id} not Found" )

    return user

def get_contact_user_type( user : User ):
    if user.database_type == DatabaseEnum.POSTGRES:
        return ContactVarejao
    if user.database_type == DatabaseEnum.MYSQL:
        return ContactMacapa