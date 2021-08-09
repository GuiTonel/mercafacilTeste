import os, json
from dotenv import load_dotenv
from flask import Flask

API_PORT = 'API_PORT'
FLASK_DEBUG = 'FLASK_DEBUG'
SERVER_CONFIG_FILENAME = 'SERVER_CONFIG_FILENAME'
FLASK_INSTANCE_RELATIVE_CONFIG = 'FLASK_INSTANCE_RELATIVE_CONFIG'

def create_app():
    load_dotenv('.env')

    app = Flask(__name__)

    from src.database import create_db
    create_db()

    from src.routes import config_routes
    config_routes(app)

    from src.error import config_error_handler
    config_error_handler(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run( port=os.getenv( API_PORT ), 
            debug=os.getenv( FLASK_DEBUG ) )
