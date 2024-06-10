"""
Заглушка
"""

import numpy as np

from data_base.user.user_hanler import DatabaseUsersHandler
from functions import logger

type Conclusion = str

class UserWalidater:
    """
    заглушка
    """

    @logger.info
    @staticmethod
    def check_name(user_name: str) -> tuple[bool, Conclusion]:
        """
        заглушка
        """
        user_db = DatabaseUsersHandler()

        if user_name == '':
            return None

        if len(user_name) < 5:
            return False, 'Логин должен быти не менее 5 символов'

        if user_db.select_image(user_name) is not None:
            choice_user_name = UserWalidater.__view_available_user_name(user_name, user_db)
            if choice_user_name:
                anser_ = f'Данный логин уже занят вы можете выбрать: {', '.join(choice_user_name)}'
            else:
                anser_ = 'Данный логин уже занят'
            return False, anser_

        return True, ''

    @logger.debug
    @staticmethod
    def __view_available_user_name(user_name : str, user_db: DatabaseUsersHandler):
        if not (row := user_db.close_user(user_name)):
            return False
        choice_user_name = []

        for r in row:
            if r == user_name:
                continue
            if len(choice_user_name) < 3:
                name_ = f'{r.username}{np.random.randint(0, 9)}'
                if not user_db.select_image(name_):
                    choice_user_name.append(name_)
            else: break
        return choice_user_name

    @logger.info
    @staticmethod
    def check_password(password: str) -> tuple[bool, Conclusion]:
        """
        заглушка
        """

        if len(password) < 8:
            return False, 'Пароль слишком короткий. Минимальная длина - 8 символов.'

        if not any(char.isdigit() for char in password):
            return False, 'Пароль должен содержать хотя бы одну цифру.'

        if not any(char.isupper() for char in password):
            return False, 'Пароль должен содержать хотя бы одну букву в верхнем регистре.'

        if not any(char in '!@#$%^&*()-+' for char in password):
            return False, 'Пароль должен содержать хотя бы один специальный символ: !@#$%^&*()-+'

        return True, 'Пароль надежный.'
