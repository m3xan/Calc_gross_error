"""
new
"""
import hashlib
from typing import overload
import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session
import sys; sys.path.append('.')
from data_base.user.user_models import User
from data_base.user.user_models import Calculation
from data_base.user.user_models import Value
from data_base.user.user_models import Answer, Metod
from data_base.engines import user_engine as engine

from functions.circle_image.image import Image

from global_param import STANDART_IMAGE

from data_class.data import Data, Names, Values, Answers, Methods

class DatabaseUsersHandler:
    _instance = None
    __session = Session(engine)

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def set_id(self, user_id):
        self.__check_id(user_id)

    def get_id(self):
        return self.__user_id

    def __check_id(self, user_id):
        with self.__session as session:
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
        input_password = hashlib.sha256(input_password.encode()).hexdigest()
        with self.__session as session:
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
        with self.__session as session:
            stmt = (
                select(User)
                .where(User.username == input_username)
            )
            result: tuple[User, ...] | None = session.execute(stmt).first()
            if result:
                return result[0]
            return None

    def select_user(self) -> User | None:
        with self.__session as session:
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
    @overload
    def update_image(self, image: str) -> User | None: ...
    @overload
    def update_image(self, image: Image) -> User | None: ...

    def update_image(self, image):
        if isinstance(image, Image):
            image = image.get_image_path()
        if isinstance(image, str):
            im = Image()
            if not im.set_image_path(image):
                return None
        with self.__session as session:
            stmt = (
                select(User)
                .where(
                    User.id == self.__user_id
                )
            )
            result: tuple[User, ...] | None = session.execute(stmt).first()
            if result:
                result[0].image = image
                self.__commit(session)
                return result[0]
            return None

    def update_user(self, username: str = None, password: str = None):
        with self.__session as session:
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
            self.__commit(session)

    def add_user(
        self,
        username: str,
        password: str,
        clearance_level: int = 1,
        image: Image | str = STANDART_IMAGE
    ):
        if isinstance(image, Image):
            image = image.get_image_path()
        password = hashlib.sha256(password.encode()).hexdigest()
        with self.__session as session:
            new = User(
                username= username,
                password= password,
                clearance_level= clearance_level,
                image = image
            )
            session.add(new)
            self.__commit(session)

    def select_method(self, id_method: int) -> str:
        with self.__session as session:
            select(Metod).where(Metod.id == id_method)
            result: tuple[Metod, ] = session.execute(
                select(Metod).where(Metod.id == id_method)
            ).first()
            if result:
                return result[0].metod_name
            return None

    def select_calculation(self):
        data = Data()
        select_calculation = (
            select(Calculation)
            .where(
                Calculation.id_user == self.__user_id
            )
        )
        with self.__session as session:
            result: tuple[Calculation, ] = session.execute(select_calculation).all()
            for calulation in result:
                for calc in calulation:
                    stm = (
                        select(Value)
                        .where(Value.calculation_id == calc.id)
                    )
                    st = (
                        select(Answer)
                        .where(Answer.calculation_id == calc.id)
                    )
                    data.append_name((calc.id, calc.name_calculation))
                    values: tuple[Value] = session.execute(stm).all()
                    answer_values: tuple[Answer] = session.execute(st).all()
                    for value in values:
                        for val in value:
                            data.append_value((calc.id, calc.name_calculation), (val.id, val.value))
                    for answer in answer_values:
                        for ans in answer:
                            data.append_answer((calc.id, calc.name_calculation), (ans.id, ans.answer_value))
                    data.append_method((calc.id, calc.name_calculation) ,calc.id_metod)
        data.set_metadate(True)
        return data

    def save_data(self, data: Data) -> Data:
        with self.__session as session:
            for delite_item in data.delite():
                if delite_item[1]:
                    data = self.__change_calc(data, delite_item, session)
            for delite_item in data.delite():
                if delite_item[1]:
                    data = self.__delite_calc(data, delite_item, session)
            for name in data.name():
                for meta in data.metadate(name):
                    data = self.__add_calc(data, name, meta)
            self.__commit(session)
        return data

    def __change_calc(self, data ,delite_item, session):
        if delite_item[0] == Names:
            data = self.__change_name(
                data,
                delite_item[1],
                session
            )
        if delite_item[0] == Values:
            data = self.__change_value(
                data,
                delite_item[1],
                session
            )
        if delite_item[0] == Answers:
            data = self.__change_answer(
                data,
                delite_item[1],
                session
            )
        return data

    def __change_name(self, data: Data, old_name, session: Session) -> Data:
        print(data, old_name, session)
        return data

    def __change_value(self, data:Data, old_value: tuple, session: Session) -> Data:
        for name in data.name():
            index = -1
            for value in data.value(name):
                index += 1
                if value[0] == 0:
                    _new_value = value[1]
                    _id = old_value[0][1][0]
                    _calculation_id = name[0]
                    result: tuple[Value] = session.execute(
                        select(Value).where(Value.id == _id)
                    ).first()
                    result[0].value = _new_value
                    result[0].calculation_id = _calculation_id
                    data.change_value(name, index, (_id, _new_value))
                    data.metadate_clear(name, Values, index)
                    data.delite_clear(Values, old_value)
                    return data
        return data

    def __change_answer(self, data: Data, old_answer, session: Session) -> Data:
        print(data, old_answer, session)
        return data

    def __delite_calc(self, data, delite_item, session):
        if delite_item[0] == Names:
            data = self.__delite_name(
                data,
                delite_item[1],
                session
            )
        if delite_item[0] == Values:
            data = self.__delite_value(
                data,
                delite_item[1],
                session
            )
        if delite_item[0] == Answers:
            data = self.__delite_answer(
                data,
                delite_item[1],
                session
            )
        print(delite_item[1])
        return data

    def __delite_name(self, data, delite_item, session):
        return data

    def __delite_value(self, data, delite_item, session):
        return data

    def __delite_answer(self, data, delite_item, session):
        return data

    def __add_calc(self, data, name, metadate):
        print(name, metadate)
        return data

    def add_method(self, name: str):
        with self.__session as session:
            new = Metod(
                metod_name = name
            )
            session.add(new)
            self.__commit(session)

    def __commit(self, session: Session):
        try:
            session.commit()
        except:
            session.rollback()
            raise

if __name__ =='__main__':
    bd = DatabaseUsersHandler()
    bd.set_id(1)
    # print(bd.select_calculation())
    # bd.add_data(datas)
    datas = bd.select_calculation()
    print(datas)
    datas.append_value(
        (1, 'name'),
        78
    )
    datas.delite_value((1, 'name'), 2)
    start = datetime.datetime.now()
    datas = bd.save_data(datas)
    fin = datetime.datetime.now()
    print(fin - start)
