import re

from src.error import InvalidNumber

class IContact():

    @classmethod
    def to_model( cls, nome, celular ):
        celular = cls.format_number(cls, celular )
        nome = cls.format_name(cls, nome)
        cls.validate_cell_number(cls, celular)
        return cls.from_dict( { "nome": nome, "celular": celular } )

    def format_number(self, celular):
        return celular

    def format_name(self, nome):
        return nome
    
    def validate_cell_number(self, celular):
        if not re.search( self.CELLPHONE_NUMBER_REGEX, celular ):
            raise InvalidNumber( f"The number {celular} is not valid" )