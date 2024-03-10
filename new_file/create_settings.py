import os
import shutil

def create_settngs(id_user):
    shutil.copy(
        f'{os.getcwd()}\\Data\\settings\\json\\default.json',
        f'{os.getcwd()}\\Data\\settings\\json\\{id_user}.json'
)
