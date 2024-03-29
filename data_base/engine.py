
from sqlalchemy import create_engine

from global_param import ECHO

engine = create_engine("sqlite:///Data/Data_base/users.db", echo= ECHO)