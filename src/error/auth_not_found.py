class AuthenticationNotFound(Exception):
    def __init__( self, msg ):
        self.__init__( msg )
        self.status = 401
    
    def to_response( self ):
        return {
            "error": self.msg
        }, self.status