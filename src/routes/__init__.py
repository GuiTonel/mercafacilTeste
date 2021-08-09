from flask import Blueprint, Flask

def config_routes(app : Flask):
    from .v1 import v1_blueprint
    app.register_blueprint(v1_blueprint)
