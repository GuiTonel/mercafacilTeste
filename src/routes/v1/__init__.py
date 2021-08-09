from flask import Blueprint

v1_blueprint = Blueprint('v1', __name__, url_prefix='/v1')

from .contacts import contacts_blueprint
v1_blueprint.register_blueprint( contacts_blueprint )

from .user import users_blueprint 
v1_blueprint.register_blueprint( users_blueprint )
