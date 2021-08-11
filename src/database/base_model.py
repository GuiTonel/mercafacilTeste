from .db_connector import DatabaseConnector
from time import sleep
import datetime

from sqlalchemy import Column, BigInteger, DateTime

class BaseModel(DatabaseConnector):
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    
    @classmethod
    def get_by_id(cls, id) -> object:
        try:
            with cls.get_session() as session:
                return session.query(cls).filter(cls.id == id).first()
        except Exception as e:
            raise e
        
    def save(self) -> None:
        with self.get_session() as session:
            try:
                session.add(self)
            except Exception as e:
                raise e

    @classmethod
    def from_dict(cls, dict):
        model = cls()
        try:
            model.__dict__.update( dict )
        except Exception as e:
            raise e
        finally:
            return model

    @classmethod
    def search(cls, **kwargs):
        try:
            with DatabaseConnector.get_session() as session:
                query = session.query(cls)
                for key, value in kwargs.items():
                    query = query.filter( cls.__dict__[key] == value )
                return query.all()
        except Exception as e:
            raise e
