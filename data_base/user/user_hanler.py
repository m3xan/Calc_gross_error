"""
new
"""
import hashlib
from typing import Self

from sqlalchemy import select

from data_base.user.user_models import User
from data_base.user.calc_handler import CalculationHandler, NameOfMethodCalculation
from data_base.user.orm_handler import OrmHandler

from functions.circle_image.image import Image
from global_param import STANDART_IMAGE
from data_class.data import Data

class DatabaseUsersHandler(OrmHandler):
    """
    for communicate with user bd
    """
    _instance = None

    def __new__(cls) -> Self:
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def set_id(self, user_id):
        self.__check_id(user_id)

    def get_id(self):
        return self.__user_id

    def __check_id(self, user_id):
        with self.session as session:
            sel_u_id = (
                select(User.id)
                .where(
                    User.id == user_id
                )
            )
            if result := session.execute(sel_u_id).first():
                self.__user_id = result[0]
                return result[0]
            return None

    def autorisation(self, input_username: str, input_password: str):
        """
        заглушка
        """
        input_password = hashlib.sha256(input_password.encode()).hexdigest()
        with self.session as session:
            stmt = (
                select(User)
                .where(
                    User.username == input_username, User.password == input_password
                )
            )
            result: tuple[User, ...] | None = session.execute(stmt).first()
            if result:
                self.__user_id = result[0].id
                return result[0].id
            return None

    def select_image(self, input_username: str) -> User | None:
        """
        заглушка
        """
        with self.session as session:
            stmt = (
                select(User)
                .where(User.username == input_username)
            )
            result: tuple[User, ...] | None = session.execute(stmt).first()
            if result:
                return result[0]
            return None

    def select_user(self) -> User | None:
        """
        заглушка
        """
        with self.session as session:
            stmt = (
                select(User)
                .where(
                    User.id == self.__user_id
                )
            )
            result: tuple[User, ...] | None = session.execute(stmt).first()
            if result:
                return result[0]
            return None

    def update_image(self, image: str | Image) -> User | None:
        """
        заглушка
        """
        if isinstance(image, Image):
            image = image.get_image_path()
        if isinstance(image, str):
            im = Image()
            if not im.set_image_path(image):
                return None
        with self.session as session:
            stmt = (
                select(User)
                .where(
                    User.id == self.__user_id
                )
            )
            result: tuple[User, ...] | None = session.execute(stmt).first()
            if result:
                result[0].image = image
                self._commit(session)
                return result[0]
            return None

    def update_user(
        self,
        username: str = None,
        password: str = None
    ) -> None:
        """
        заглушка
        """
        with self.session as session:
            stmt = (
                select(User)
                .where(
                    User.id == self.__user_id
                )
            )
            result: tuple[User, ...] | None= session.execute(stmt).first()
            if result:
                if username:
                    result[0].username = username
                if password:
                    password = hashlib.sha256(password.encode()).hexdigest()
                    result[0].password = password
            self._commit(session)

    def add_user(
        self,
        username: str,
        password: str,
        clearance_level: int = 1,
        image: Image | str = STANDART_IMAGE
    ) -> None:
        """
        заглушка
        """
        if isinstance(image, Image):
            image = image.get_image_path()
        password = hashlib.sha256(password.encode()).hexdigest()
        with self.session as session:
            new = User(
                username= username,
                password= password,
                clearance_level= clearance_level,
                image = image
            )
            session.add(new)
            self._commit(session)

    def close_user(self, name: str) :
        """
        заглушка
        """
        with self.session as session:
            select_ = (
                select(User.username).
                filter(
                    User.username.like(f'%{name}%')
                )
            )
            return session.execute(select_).all()

    def select_method(self, id_method: int) -> NameOfMethodCalculation | None:
        """
        заглушка
        """
        return CalculationHandler(self.__user_id).select_method(id_method)

    def select_calculation(self) -> Data:
        """
        заглушка
        """
        return CalculationHandler(self.__user_id).select_calculation()

    def save_data(self, data: Data) -> Data:
        """
        заглушка
        """
        return CalculationHandler(self.__user_id).save_data(data)

    def add_method(self, name: str):
        """
        заглушка
        """
        CalculationHandler().add_method(name)
