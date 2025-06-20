from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:rootpassword@localhost:3306/bumarket"

class engineconn:
  def __init__(self):
    self.engine = create_engine(DATABASE_URL, pool_recycle=500)

  def sessionmaker(self):
    Session = sessionmaker(bind=self.engine)
    session = Session()
    return session

  def connection(self):
    conn = self.engine.connect()
    return conn

