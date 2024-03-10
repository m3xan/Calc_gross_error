from sqlalchemy.orm import Session
from data_base.connect import engine


session = Session(bind=engine)