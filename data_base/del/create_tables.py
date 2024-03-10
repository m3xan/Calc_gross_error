from data_base.models import Base, User, Comment
from data_base.connect import engine


# print("CREATING TABLES >>>> ")
# Base.metadata.create_all(bind=engine)

def create_table():
    print("CREATING TABLES >>>> ")
    Base.metadata.create_all(bind=engine)
