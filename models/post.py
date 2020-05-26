from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import *
DB_NAME="mydatabase"
engine=create_engine(f'mysql+pymysql://root:@localhost/DB_NAME',echo=False)

Base=declarative_base()
session=Session(bind=engine)

class Posts(Base):
	__tablename__='posts'
	id=Column(INTEGER,primary_key=True)
	title=Column(String(50))
	body=Column(String(50))
	

