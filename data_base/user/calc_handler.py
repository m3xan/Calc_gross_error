
from typing import overload

from sqlalchemy import select
from sqlalchemy.orm import Session

from data_base.user.user_models import Calculation
from data_base.user.user_models import Value
from data_base.user.user_models import Answer
from data_base.user.user_models import Metod
from data_base.user.orm_handler import OrmHandler

from data_class.data import Data
from data_class.models_data import Names
from data_class.models_data import Values
from data_class.models_data import Answers

class CalculationHandler(OrmHandler):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, user_id: str) -> None: ...

    def __init__(self, user_id = None):
        self.__user_id = user_id

    def set_user(self, user_id: int):
        self.__user_id = user_id

    def get_user_id(self):
        return self.__user_id

    def select_method(self, id_method: int) -> str:
        with self.session as session:
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
        with self.session as session:
            result = session.execute(select_calculation).all()
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
        with self.session as session:
            for delite_item in data.delite():
                if delite_item[1]:
                    data = self.__change_calc(data, delite_item, session)
            for delite_item in data.delite():
                if delite_item[1]:
                    data = self.__delite_calc(data, delite_item, session)
            for name in data.name():
                index = 0
                for meta in data.metadate(name):
                    data = self.__add_calc(data, name, meta, index, session)
                    index += 1
            self._commit(session)
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

    def __change_name(self, data: Data, old_name: tuple, session: Session) -> Data:
        index = 0
        for name in data.name():
            if name[0] == 0:
                _new_value = name[1]
                _id = old_name[0][1][0]
                result: tuple[Calculation] = session.execute(
                    select(Calculation).where(Calculation.id == _id)
                ).first()
                result[0].name_calculation = _new_value
                data.change_name(name, (_id, _new_value))
                data.metadate_clear(name, Values, index)
                data.delite_clear(Values, old_name)
                return data
            index += 1

        return data

    def __change_value(self, data:Data, old_value: tuple, session: Session) -> Data:
        for name in data.name():
            index = 0
            for value in data.value(name):
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
                index += 1
        return data

    def __change_answer(self, data: Data, old_answer, session: Session) -> Data:
        for name in data.name():
            index = 0
            for answer in data.answer(name):
                if answer[0] == 0:
                    _new_value = answer[1]
                    _id = old_answer[0][1][0]
                    _calculation_id = name[0]
                    result: tuple[Answer] = session.execute(
                        select(Answer).where(Answer.id == _id)
                    ).first()
                    result[0].answer_value = _new_value
                    result[0].calculation_id = _calculation_id
                    data.change_value(name, index, (_id, _new_value))
                    data.metadate_clear(name, Answer, index)
                    data.delite_clear(Answer, old_answer)
                    return data
                index += 1
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
        return data

    def __delite_name(self, data: Data, delite_item, session: Session):
        calc: tuple[Calculation] = session.execute(
            select(Calculation).where(Calculation.id == delite_item[0])
        ).first()
        session.delete(calc[0])
        data.delite_clear(Names, delite_item)
        return data

    def __delite_value(self, data: Data, delite_item, session: Session):
        calc: tuple[Value] = session.execute(
            select(Value).where(Value.id == delite_item[0])
        ).first()
        session.delete(calc[0])
        data.delite_clear(Values, delite_item)
        return data

    def __delite_answer(self, data: Data, delite_item, session: Session):
        calc: tuple[Answer] = session.execute(
            select(Answer).where(Answer.id == delite_item[0])
        ).first()
        session.delete(calc[0])
        data.delite_clear(Answers, delite_item)
        return data

    def __add_calc(self, data: Data, name, metadate, index, session: Session):
        if metadate[0] == Names:
            self.__add_name(data ,name, metadate, index, session)
        if metadate[0] == Values:
            self.__add_value(name, metadate, index, session)
        if metadate[0] == Answers:
            self.__add_answer(name, metadate, index, session)
        return data

    def __add_name(self, data: Data, name, metadate, index, session: Session):
        if metadate[1][0] == Names.append:
            new = Calculation(
                name_calculation= name,
                id_user = self.__user_id,
                id_metod = data.method(name),
                calculated = data.method(name) is not None
            )
            session.add(new)
            data.metadate_clear(name, Names, index)
        if metadate[1][0] == Names.change:
            result: tuple[Calculation] = session.execute(
                select(Calculation).where(Calculation.id == name[0])
            ).first()
            result[0].name_calculation = name[1]
            result[0].id_metod = data.method(name)
            data.metadate_clear(name, Names, index)
        return data

    def __add_value(self, data: Data, name, metadate, index, session: Session):
        if metadate[1][0] == Values.append:
            new = Value(
                calculation_id = name[0],
                value = metadate[1][1][1]
            )
            session.add(new)
            data.metadate_clear(name, Values, index)
        if metadate[1][0] == Values.change:
            result: tuple[Value] = session.execute(
                select(Value).where(Value.id == metadate[1][1][0])
            ).first()
            result[0].value = metadate[1][1][1]
            data.metadate_clear(name, Values, index)
        return data

    def __add_answer(self, data: Data, name, metadate, index, session: Session):
        if metadate[1][0] == Answers.append:
            new = Answer(
                calculation_id = name[0],
                answer_value = metadate[1][1][1]
            )
            session.add(new)
            data.metadate_clear(name, Answers, index)
        if metadate[1][0] == Answers.change:
            result: tuple[Calculation] = session.execute(
                select(Answer).where(Answer.id == metadate[1][1][0])
            ).first()
            result[0].name_calculation = metadate[1][1][1]
            data.metadate_clear(name, Answers, index)
        return data

    def add_method(self, name: str):
        with self.session as session:
            new = Metod(
                metod_name = name
            )
            session.add(new)
            self._commit(session)
