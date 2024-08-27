from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm


SQLALCHEMY_DATABASE_URL = 'sqlite:///.user.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(autocommit=False , autoflush=False,bind=engine)

Base = sqlalchemy.orm.declarative_base()