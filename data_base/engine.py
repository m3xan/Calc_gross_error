import os
from sqlalchemy import create_engine

engine = create_engine(f"sqlite:///{os.getcwd()}/Data/Data_base/users.db", echo=True)