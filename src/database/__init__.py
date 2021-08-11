from .db_connector import DatabaseConnector
from .base_model import BaseModel

def create_db():
    DatabaseConnector.get_base_model().metadata.create_all(DatabaseConnector.get_engine())

    from src.database.macapa import DatabaseConnector as DatabaseConnectorMacapa
    DatabaseConnectorMacapa.get_base_model().metadata.create_all(DatabaseConnectorMacapa.get_engine())

    from src.database.varejao import DatabaseConnector as DatabaseConnectorVarejao
    DatabaseConnectorVarejao.get_base_model().metadata.create_all(DatabaseConnectorVarejao.get_engine())
