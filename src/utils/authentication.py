from flask import request
import jwt, os, datetime, base64

from src.error import AuthenticationNotFound, ExpiredToken, InvalidToken

SECRET_KEY = os.getenv('SECRET_KEY')
ALG = os.getenv('CODE_ALGORITHM')


def auth_jwt( function ):
    def return_function( *arg, **kwargs ):
        token = request.headers['Authorization']
        if token is None:
            raise AuthenticationNotFound( 'Without authentication Header' )

        user = jwt.decode( token, SECRET_KEY, algorithms=[ALG] )
        
        if user is None:
            raise InvalidToken("Invalid Token.")

        return function(user['sub'])
    return return_function

def generate_jwt( function ):
    def return_function( *arg, **kwargs ):
        user, status = function( *arg, **kwargs )
        token = jwt.encode( { 
            'exp': datetime.datetime.now() + datetime.timedelta(days=2),
            'sub': user.id
        }, SECRET_KEY, algorithm=ALG )
        return { 'Auth_token': f"Basic {token}" }, status
    return return_function
