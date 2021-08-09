from .contacts_not_found import ContactsNotFound
from .auth_not_found import AuthenticationNotFound
from .expired_token import ExpiredToken
from .user_not_found import UserNotFound
from .invalid_token import InvalidToken
from .invalid_number import InvalidNumber

import traceback

from flask import Flask
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError

def config_error_handler(app: Flask):
    @app.errorhandler( Exception )
    def generic_handler( err ):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": str(err) }, 500

    @app.errorhandler( HTTPException )
    def generic_handler( err ):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return { "error": str(err) }, err.code

    @app.errorhandler( ContactsNotFound )
    def event_already_exist_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return err.to_response()

    @app.errorhandler( AuthenticationNotFound )
    def missing_information_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return err.to_response()

    @app.errorhandler( ExpiredToken )
    def event_already_exist_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return err.to_response()

    @app.errorhandler( UserNotFound )
    def missing_information_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return err.to_response()

    @app.errorhandler( InvalidToken )
    def event_already_exist_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return err.to_response()

    @app.errorhandler( InvalidNumber )
    def missing_information_handler(err):
        app.logger.debug(traceback.format_exc())
        app.logger.error(err)
        return err.to_response()
