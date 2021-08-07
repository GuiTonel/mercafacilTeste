from flask import Blueprint, request

from src.utils.authentication import auth_jwt

contacts_blueprint = Blueprint( 'contacts', __name__, subdomain='/contacts' )

@contacts_blueprint.post( '/' ):
@auth_jwt
def post_contacts(user_id):
    body = request.get_json()

