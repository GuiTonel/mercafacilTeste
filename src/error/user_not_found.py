class UserNotFound(Exception):
    def __init__( self, msg ):
        self.msg = msg
        self.status = 404
    
    def to_response( self ):
        return {
            "error": self.msg
        }, self.status