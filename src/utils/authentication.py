from flask import request
import jwt, os, datetime

from src.error import AuthenticationNotFound, ExpiredToken

SECRET_KEY = os.getenv('SECRET')
ALG = os.getenv('CODE_ALGORITHM')

def auth_jwt( function ):
    def return_function( *arg, **kwargs ):
        token = request.authorization
        if token is None:
            raise AuthenticationNotFound( 'Without authentication Header' )
        user = jwt.decode( token, SECRET_KEY, algorithms=[ALG] )
        
        if  datetime.datetime.now > user.exp:
            raise ExpiredToken("Auth token was expired")
        
        return function(user.sub)
    return return_function

def generate_jwt( function ):
    def return_function( *arg, **kwargs ):
        user = function()
        token = jwt.encode( { 
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user.id
        }, SECRET_KEY, algorithm=ALG )  
        return { 'Auth_token': token }
