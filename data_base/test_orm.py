"""
new
"""
from sqlalchemy import select
from sqlalchemy.orm import Session

from data_base.models import User
from data_base.models import Calculation
from data_base.models import Value
from data_base.models import Answer
from data_base.engine import engine
from data_base.decorator import with_session
from data_base.decorator import commit_

from global_param import STANDART_IMAGE

@with_session(engine)
def autorisation(session: Session, input_username, input_password):
    stmt = (
        select(User)
        .where(
            User.username == input_username, User.password == input_password
        )
    )
    result: tuple[User, ...] | None = session.execute(stmt).first()
    if result is not None:
        return result[0].id
    return result

@with_session(engine)
def select_image(session: Session, input_username) -> User | None:
    stmt = (
        select(User)
        .where(User.username == input_username)
    )
    result: tuple[User, ...] | None = session.execute(stmt).first()
    if result is not None:
        return result[0]
    return result

@with_session(engine)
def select_User(session: Session, user_id: int) -> User | None:
    stmt = (
        select(User)
        .where(
            User.id == user_id
        )
    )
    result: tuple[User, ...] | None = session.execute(stmt).first()
    if result is not None:
        return result[0]
    return result

@with_session(engine)
@commit_
def update_image(session: Session, user_id: int, image = None):
    if image is not None:
        stmt = (
            select(User)
            .where(
                User.id == user_id
            )
        )
        result: tuple[User, ...] | None = session.execute(stmt).first()
        if result is not None:
            result[0].image = image
            return result[0]
        return result

@with_session(engine)
@commit_
def update_user(session: Session, user_id: int, username= None, password= None):
    stmt = (
        select(User)
        .where(
            User.id == user_id
        )
    )
    result: tuple[User, ...] | None= session.execute(stmt).first()
    if result is not None:
        if username is not None:
            result[0].username = username
        if password is not None:
            result[0].password = password

@with_session(engine)
@commit_
def add_admin(session: Session):
    new_user = User(
        username='admin',
        password='Admin123!',
        clearance_level=3,
        image = r'Data\Data_base\image\EWQPps7VnkI.jpg'
    )
    session.add(new_user)

@with_session(engine)
@commit_
def add_user(session: Session, username: str, password: str):
    new_user = User(
        username= username,
        password= password,
        clearance_level=1,
        image = STANDART_IMAGE
    )
    session.add(new_user)

@with_session(engine)
def test_select(session: Session):
    stmt = (
        select(User.username, Calculation.id, Value.id, Answer.id)
        .join(User.calculations)  # Join User with Calculation
        .join(Calculation.values)  # Join Calculation with Value
        .join(Calculation.answer)
        .where(
            User.id == 1  # Filter by User ID
        )
    )

    print(stmt)
    result = session.execute(stmt).all()
    for i in result:
        print(i)

@with_session(engine)
def test_select_2(session: Session, user_id: int):
    data = {}
    stmt = (
        select(Calculation.id, Calculation.name_calculation, Calculation.id_metod)
        .where(
            Calculation.id_user == user_id
        )
    )
    result = session.execute(stmt).all()
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

if __name__ == '__main__':
    add_admin()
    add_user(
        'user',
        'qwerty'
    )
