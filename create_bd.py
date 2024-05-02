
from data_base.table_values.table_model import Base as Base_Table
from data_base.user.user_models import Base as Base_User
from data_base.engines import table_engine
from data_base.engines import user_engine
from data_base.table_values.value import fill_out_the_table
from data_base.user.user import create_user

if __name__ == '__main__':
    Base_Table.metadata.create_all(table_engine)
    Base_User.metadata.create_all(user_engine)
    fill_out_the_table()
    create_user()
