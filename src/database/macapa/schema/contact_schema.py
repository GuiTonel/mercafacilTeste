import sqlalchemy as db

from src.database.schemas import IContact
from src.database.macapa import DatabaseConnector, BaseModel


class Contact( IContact, BaseModel, DatabaseConnector.get_base_model() ):
    CELLPHONE_NUMBER_REGEX = '\+[0-9]{2} \([0-9]{2}\) [0-9]{5}-[0-9]{4}'
    __tablename__ = 'contato'

    nome = db.Column( db.String(200), nullable=False )
    celular = db.Column( db.String(20), nullable=False )

    def format_number(self, celular):
        return f"+{celular[0:2]} ({celular[2:4]}) {celular[4:9]}-{celular[9:13]}"
    
    def format_name(self, nome: str):
        return nome.upper()