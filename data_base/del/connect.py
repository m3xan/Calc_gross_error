import os

from sqlalchemy import create_engine,text

engine = create_engine(f"sqlite:///{os.getcwd()}/Data/Data_base/sample.db", echo=True)

def test_connect():
    engine1 = create_engine(f"sqlite:///{os.getcwd()}/Data/Data_base/sample.db", echo=True)

    with engine1.connect() as connection:
        result = connection.execute(text('select "Hello"'))

        print(result.all())
