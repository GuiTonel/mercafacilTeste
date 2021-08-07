class ContactsNotFound(Exception):
    def __init__( self, msg ):
        self.__init__( msg )
        self.status = 400
    
    def to_response( self ):
        return {
            "error": self.msg
        }, self.status