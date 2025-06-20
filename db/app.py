from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from database import engineconn
from model import Test

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()

class Item(BaseModel):
  name: str
  number: int

@app.get("/")
async def first_get():
  example = session.query(Test).all()
  return example