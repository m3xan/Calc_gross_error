"""
new
"""
from typing import overload

from sqlalchemy import select
from sqlalchemy.orm import Session

from data_base.models import User
from data_base.models import Calculation
from data_base.models import Value
from data_base.models import Answer
from data_base.engine import engine

from global_param import STANDART_IMAGE

class DatabaseUsersHandler:

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, user_id) -> None: ...

    def __init__(self, user_id = None) -> None:
        self.__session = Session(engine)
        self._user_id = user_id

    def autorisation(self, input_username, input_password):
        with self.__session as session:
            stmt = (
                select(User)
                .where(
                    User.username == input_username, User.password == input_password
                )
            )
            result: tuple[User, ...] | None = session.execute(stmt).first()
            if result is not None:
                self._user_id = result[0].id
                return result[0].id
            return result

    def select_image(self, input_username) -> User | None:
        with self.__session as session:
            stmt = (
                select(User)
                .where(User.username == input_username)
            )
            result: tuple[User, ...] | None = session.execute(stmt).first()
            if result is not None:
                return result[0]
            return result

    def select_user(self) -> User | None:
        with self.__session as session:
            stmt = (
                select(User)
                .where(
                    User.id == self._user_id
                )
            )
            result: tuple[User, ...] | None = session.execute(stmt).first()
            if result is not None:
                return result[0]
            return result

    def update_image(self, image = None):
        with self.__session as session:
            if image is not None:
                stmt = (
                    select(User)
                    .where(
                        User.id == self._user_id
                    )
                )
                result: tuple[User, ...] | None = session.execute(stmt).first()
                if result is not None:
                    result[0].image = image
                    self.__commit(session)
                    return result[0]
                return result
            

    def update_user(self, username= None, password= None):
        with self.__session as session:
            stmt = (
                select(User)
                .where(
                    User.id == self._user_id
                )
            )
            result: tuple[User, ...] | None= session.execute(stmt).first()
            if result is not None:
                if username is not None:
                    result[0].username = username
                if password is not None:
                    result[0].password = password
            self.__commit(session)

    def add_admin(self):
        with self.__session as session:
            new_user = User(
                username='admin',
                password='Admin123!',
                clearance_level=3,
                image = r'Data\Data_base\image\48HgiXRHVXQ.jpg'
            )
            session.add(new_user)
            self.__commit(session)

    def add_user(self, username: str, password: str):
        with self.__session as session:
            new_user = User(
                username= username,
                password= password,
                clearance_level=1,
                image = STANDART_IMAGE
            )
            session.add(new_user)
            self.__commit(session)

    def test_select_2(self, user_id: int):
        data = {}
        select_calculation = (
            select(Calculation.id, Calculation.name_calculation, Calculation.id_metod)
            .where(
                Calculation.id_user == user_id
            )
        )
        st = (
            select(Answer.answer_value)
            .where(Answer.calculation_id == user_id)
        )
        with self.__session as session:
            result = session.execute(select_calculation).all()
            for i in result:
                stm = (
                    select(Value.value)
                    .where(Value.calculation_id == i[0])
                )
                st = (
                    select(Answer.answer_value)
                    .where(Answer.calculation_id == user_id)
                )
                data[(i[0], i[1])] = [[], [], i[2]]
                values = session.execute(stm).all()
                answer_values = session.execute(st).all()
                for val in values:
                    data[(i[0], i[1])][0].append(float(val[0]))
                for val in answer_values:
                    data[(i[0], i[1])][1].append(float(val[0]))
            return data
    
    def __commit(self, session: Session):
        try:
            session.commit()
        except:
            session.rollback()
            raise

if __name__ == '__main__':
    d = DatabaseUsersHandler()
    d.add_admin()
    d.add_user(
        'user',
        'qwerty'
    )
