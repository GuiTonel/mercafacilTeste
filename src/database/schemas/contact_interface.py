import re

from src.error import InvalidNumber

class IContact():

    @classmethod
    def to_model( cls, nome, celular ):
        cls.validate_cell_number(cls, celular)
        return cls.from_dict( { "nome": nome, "celular": celular } )

    def validate_cell_number(self, celular):
        if not re.search( self.CELLPHONE_NUMBER_REGEX, celular ):
            raise InvalidNumber( f"The number {celular} is not valid" )