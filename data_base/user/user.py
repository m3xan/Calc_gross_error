
from functions.circle_image.image import Image
from data_base.user.user_hanler import DatabaseUsersHandler

METHOD = ['Романовского', 'Шарлье', 'Диксона']

def create_user():
    bd = DatabaseUsersHandler()
    bd.add_user(
        'admin',
        'Admin123!',
        3,
        Image(r'Data\Data_base\image\48HgiXRHVXQ.jpg')
    )
    bd.add_user(
        'user',
        'qwerty'
    )
    for i in METHOD:
        bd.add_method(i)
