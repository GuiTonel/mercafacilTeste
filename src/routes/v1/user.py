from flask import Blueprint

from src.utils.authentication import generate_jwt
from src.controller import users_controller

users_blueprint = Blueprint( 'users', __name__, url_prefix='/users' )

@users_blueprint.get( '/<user_id>' )
@generate_jwt
def login(user_id):
    response = users_controller.login(user_id)
    return response, 200

