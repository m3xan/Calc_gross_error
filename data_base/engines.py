
from sqlalchemy import create_engine

from global_param import ECHO, FilePath

user_engine = create_engine(f'sqlite:///{FilePath().user_bd}', echo= ECHO)

table_engine = create_engine(f'sqlite:///{FilePath().table_bd}', echo= ECHO)
