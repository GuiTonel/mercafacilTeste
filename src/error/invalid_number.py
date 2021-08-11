class InvalidNumber(Exception):
    def __init__( self, msg ):
        self.msg = msg
        self.status = 400
    
    def to_response( self ):
        return {
            "error": self.msg
        }, self.status