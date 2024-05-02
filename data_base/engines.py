
from sqlalchemy import create_engine

from global_param import ECHO

user_engine = create_engine('sqlite:///Data/Data_base/users.db', echo= ECHO)

table_engine = create_engine('sqlite:///Data/Data_base/table.db', echo= ECHO)
