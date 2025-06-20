from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Test(Base):
  __tablename__ = 'test'


  id = Column(BIGINT, autoincrement=True, primary_key=True)
  name=Column(TEXT, nullable=False)
  number = Column(INT, nullable=False)