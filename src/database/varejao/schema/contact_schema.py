import sqlalchemy as db

from src.database.schemas import IContact
from src.database.varejao import DatabaseConnector, BaseModel


class Contact( IContact, BaseModel, DatabaseConnector.get_base_model() ):
    CELLPHONE_NUMBER_REGEX = '[0-9]{13}'
    __tablename__ = 'contato'

    nome = db.Column( db.String(100), nullable=False )
    celular = db.Column( db.String(13), nullable=False )
