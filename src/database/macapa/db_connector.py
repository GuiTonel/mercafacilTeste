import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.database import DatabaseConnector as BaseConnector


DATABASE_URL = f"{os.environ.get('MYSQL_DB_ENGINE')}://" \
                       f"{os.environ.get('MYSQL_USER')}:" \
                       f"{os.environ.get('MYSQL_PASSWORD')}@" \
                       f"{os.environ.get('MYSQL_DB_SERVER')}:" \
                       f"{os.environ.get('MYSQL_DB_PORT')}/" \
                       f"{os.environ.get('MYSQL_DATABASE_NAME')}"

class DatabaseConnector(BaseConnector):
    __base = None

    @classmethod
    def get_base_model(cls) -> object:
        try:
            if cls.__base is None:
                cls.__config()
            return cls.__base
        except Exception as e:
            raise e

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