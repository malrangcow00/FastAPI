# SQLALCHEMY_DATABASE_URL = 'jdbc:mysql://localhost:3306/fastapi'

# database.py
from sqlalchemy import create_engine, MetaData
from databases import Database
from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)
metadata = MetaData()

database = Database(DATABASE_URL)
