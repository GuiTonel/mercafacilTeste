import os

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.database import DatabaseConnector as BaseConnector

DATABASE_NAME = 'macapa'

DATABASE_URL = f"{os.environ.get('DB_ENGINE')}://" \
                       f"{os.environ.get('DB_USER')}:" \
                       f"{os.environ.get('DB_PASS')}@" \
                       f"{os.environ.get('DB_SERVER')}:" \
                       f"{os.environ.get('DB_PORT')}/" \
                       f"{DATABASE_NAME}"

class DatabaseConnector:
    __sessionmaker = None
    __engine = None
    __base = None

    def __init__(self):
        pass

    @classmethod
    @contextmanager
    def get_session(cls):
        if cls.__sessionmaker is None:
            cls.__config()
        session = cls.__sessionmaker()
        
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def __config(cls) -> None:
        database_url = DATABASE_URL
        try:
            cls.__engine = create_engine( 
                            database_url, 
                            pool_size = int(os.environ.get('DB_POOL_SIZE')), 
                            max_overflow=int(os.environ.get('DB_MAX_OVERFLOW')) 
                           )
            cls.__sessionmaker = sessionmaker( cls.__engine, expire_on_commit=False )
            cls.__base = declarative_base()
        except Exception as e:
            raise e

    @classmethod
    def get_base_model(cls) -> object:
        try:
            if cls.__base is None:
                cls.__config()
            return cls.__base
        except Exception as e:
            raise e

    @classmethod
    def get_engine(cls):
        try:
            if cls.__engine is None:
                cls.__config()
            return cls.__engine
        except Exception as e:
            raise e