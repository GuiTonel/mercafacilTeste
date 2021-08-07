import sqlalchemy as db

from src.database import BaseModel, DatabaseConnector
from src.enums import DatabaseEnum

class User( BaseModel, DatabaseConnector.get_base_model() ):
    __tablename__ = 'usuario'

    nome = db.Column( db.String(255), nullable=False )
    database_type = db.Column(db.Integer, db.CheckConstraint( f"database IN {DatabaseEnum.to_sql_list()}" ), nullable=False )

