from flask import Blueprint, request

from src.utils.authentication import auth_jwt
from src.controller import contacts_controller

contacts_blueprint = Blueprint( 'contacts', __name__, url_prefix='/contacts' )

@contacts_blueprint.post( '/' )
@auth_jwt
def post_contacts(user_id):
    body = request.get_json()
    response = contacts_controller.insert_contacts(body, user_id)
    return response, 200

