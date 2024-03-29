
import shutil

def create_settngs(id_user):
    shutil.copy(
        'Data\\settings\\json\\default.json',
        f'Data\\settings\\json\\{id_user}.json'
)
