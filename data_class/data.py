
from typing import overload
import functools

import pandas as pd

from data_class.models_data import Calc
from data_class.models_data import Names
from data_class.models_data import Values
from data_class.models_data import Answers
from data_class.models_data import Methods

def vallue_error(func):
    @functools.wraps(func)
    def wrapper(*ar, **kw):
        try:
            result = func(*ar, **kw)
            return result
        except ValueError as err:
            raise err
    return wrapper

class Data:

    @overload
    def __init__(self, metadate: bool = False) -> None: ...
    @overload
    def __init__(self, _dict: dict, metadate: bool = False) -> None: ...

    def __init__(self, _obj = None, metadate = False):
        self.__name = []
        self.__value = []
        self.__answer = []
        self.__method = []
        self.meta_date = metadate
        self.__metadate = []
        self._delit = {
            Names: [],
            Values: [],
            Answers: []
        }
        if isinstance(_obj, dict):
            self.append(_obj)

    def set_metadate(self, on_metadeta: bool) -> None:
        self.meta_date = on_metadeta

    def get_metadate(self) -> None:
        return self.meta_date

    def append(self, data: dict) -> None:
        for name, values in data.items():
            self.append_name(name)
            for val in values[0]:
                self.append_value(name, val)
            for ans in values[1]:
                self.append_answer(name, ans)
            self.append_method(name, values[2])

    def append_name(self, name: tuple[int, str] | str):
        if self.meta_date:
            self.__metadate.append(
                {
                Names: [(Names.append, name)],
                Values: [],
                Answers: [],
                Methods: []
                }
            )
        else:
            self.__metadate.append(
                {
                Names: [],
                Values: [],
                Answers: [],
                Methods: []
                }
            )

        if isinstance(name, str):
            self.__name.append((0, name))
        else:
            self.__name.append(name)

        self.__value.append([])
        self.__answer.append([])
        self.__method.append(False)

    @overload
    def append_value(self, name: tuple[int, str], value: float | int) -> None: ...
    @overload
    def append_value(self, name: tuple[int, str], value: tuple[int, float]) -> None: ...

    @vallue_error
    def append_value(self, name: tuple[int, str], value):
        if isinstance(value, (int, float)):
            self.__value[self.__name.index(name)].append((0, float(value)))
            if self.meta_date:
                self.__metadate[self.__name.index(name)][Values].append([(Values.append, (0, float(value)))])
            else:
                self.__metadate[self.__name.index(name)][Values].append([])
        if isinstance(value, tuple) and isinstance(value[0], int) and isinstance(value[1], (float, int)):
            self.__value[self.__name.index(name)].append(value)
            if self.meta_date:
                self.__metadate[self.__name.index(name)][Values].append([(Values.append, value)])
            else:
                self.__metadate[self.__name.index(name)][Values].append([])

    @overload
    def append_answer(self, name: tuple[int, str], answer: list[float | int]) -> None: ...
    @overload
    def append_answer(self, name: tuple[int, str], answer: float | int) -> None: ...

    @vallue_error
    def append_answer(self, name, answer):
        if isinstance(answer, (int, float)):
            self.__answer[self.__name.index(name)].append((0, float(answer)))
            if self.meta_date:
                self.__metadate[self.__name.index(name)][Answers].append([(Answers.append, (0, float(answer)))])
        if isinstance(answer, tuple) and isinstance(answer[0], int) and isinstance(answer[1], float):
            self.__answer[self.__name.index(name)].append(answer)
            if self.meta_date:
                self.__metadate[self.__name.index(name)][Answers].append([(Answers.append, answer)])

    @vallue_error
    def append_method(self, name, method):
        if not isinstance(method, int) or method is None:
            return
        self.__method[self.__name.index(name)] = method
        if self.meta_date:
            self.__metadate[self.__name.index(name)][Methods].append(
                [(Methods.append, method)]
            )

    @vallue_error
    def append_metadate(self, name, metadate):
        self.__metadate[self.__name.index(name)].append([metadate])

    def name(self):
        for value in self.__name:
            yield value

    @vallue_error
    def value(self, name):
        for value in self.__value[self.__name.index(name)]:
            yield value

    @vallue_error
    def answer(self, name):
        for value in self.__answer[self.__name.index(name)]:
            yield value

    @vallue_error
    def method(self, name):
        return self.__method[self.__name.index(name)]

    @vallue_error
    def metadate(self, name):
        for meta in self.__metadate[self.__name.index(name)].items():
            yield meta

    def delite(self):
        for delit in self._delit.items():
            yield delit

    def issaved(self) -> bool:
        for values in self.__value:
            for value in values:
                if value[0] == 0:
                    return False
        for answers in self.__answer:
            for answer in answers:
                if answer[0] == 0:
                    return False
        return True

    def iscalc(self, name) -> bool:
        if isinstance(self.method(name), str):
            return True
        return False

    @overload
    def metadate_clear(self): ...
    @overload
    def metadate_clear(self, name_calculation, calc_model: Calc, index: int): ...

    def metadate_clear(self, name_calculation=None, calc_model=None, index=None):
        try:
            if issubclass(calc_model, Calc) and isinstance(index, int):
                self.__metadate[self.__name.index(name_calculation)][calc_model][index] = []
        except TypeError:
            if name_calculation is None and calc_model is None and index is None:
                for name in self.name():
                    self.__metadate[self.__name.index(name)] = {
                    Names: [],
                    Values: [[] for _ in range(len(self.__value[self.__name.index(name)]))],
                    Answers: [[] for _ in range(len(self.__answer[self.__name.index(name)]))],
                    Methods: []
                    }

    @overload
    def delite_clear(self): ...
    @overload
    def delite_clear(self, calc_model: Calc, old: tuple): ...

    def delite_clear(self, calc_model=None, old_=None):
        try:
            if issubclass(calc_model, Calc) and isinstance(old_, list):
                self._delit[calc_model].remove(old_[0])
        except TypeError:
            if calc_model is None and old_ is None:
                self._delit = {
                    Names: [],
                    Values: [],
                    Answers: []
                }

    def change_name(self, name, new_name):
        index = self.__name.index(name)
        if self.__name[index][1] != new_name:
            self.__name[index] = (name[0], new_name)
            if self.meta_date:
                self.__metadate[index][Names].append(
                    (self.__name[index], (Names.change, (name[0], new_name)))
                )

    def change_value(self, name, index, new_value):
        old_value = self.__value[self.__name.index(name)][index]
        if old_value[1] != new_value:
            self.__value[self.__name.index(name)][index] = (old_value[0], new_value)
            if self.meta_date:
                self.__metadate[self.__name.index(name)][Values][index].append(
                    (name, (Values.change, (old_value, new_value)))
                )

    def change_answer(self, name, index, new_answer):
        old_answer = self.__answer[self.__name.index(name)][index]
        if old_answer[1] != new_answer:
            self.__answer[self.__name.index(name)][index] = (old_answer[0], new_answer)
            if self.meta_date:
                self.__metadate[self.__name.index(name)][Answers][index].append(
                    (name, (Answers.change, (old_answer, new_answer)))
                )

    def change_method(self, name, new_method):
        if self.__method[self.__name.index(name)] != new_method:
            self.__method[self.__name.index(name)] = new_method
            if self.meta_date:
                self.__metadate[self.__name.index(name)][Methods].append(
                    (name, (Methods.change, new_method))
                )

    def delite_name(self, name):
        del self[name]
        if name[0] != 0:
            self._delit[Names].append(name)

    def delite_value(self, name, index):
        value = self.__value[self.__name.index(name)][index]
        del self.__value[self.__name.index(name)][index]
        del self.__metadate[self.__name.index(name)][Values][index]
        self._delit[Values].append((name, (value)))

    def to_DataFrame(self):
        return pd.DataFrame({
            'name': [name[1] for name in self.__name],
            'value': [[value[1] for value in values] for values in self.__value],
            'method': self.__method,
            'answer': [[answer[1] for answer in answers] for answers in self.__answer],
        })

    def __len__(self): #len()
        return len(self.__name)

    @vallue_error
    def __getitem__(self, name: tuple[int, str]): #self[name]
        index = self.__name.index(name)
        return [self.__value[index], self.__answer[index], self.__method[index]]

    @vallue_error
    def __delitem__(self, name): #del self[name]
        index = self.__name.index(name)
        del self.__name[index]
        del self.__value[index]
        del self.__answer[index]
        del self.__method[index]
        if self.meta_date:
            del self.__metadate[index]

    def __iter__(self): #for x in container:
        for index, name in enumerate(self.__name):
            yield name, (self.__value[index], self.__answer[index], self.__method[index])

    def __add__(self, other):
        if isinstance(other, Data):
            meta = self.meta_date
            self.meta_date = other.meta_date
            for name in other.name():
                self.append_name(name)
                for value in other.value(name):
                    self.append_value(name, value)
                for answer in other.answer(name):
                    self.append_answer(name, answer)
                self.append_method(name, other.method(name))
            self.meta_date = meta
        return self

    def __bool__(self) -> bool:
        return len(self.__name) != 0

    def __str__(self) -> str:
        return str(dict(self))

    def __dict__(self) -> dict:
        data = {}
        for index, name in enumerate(self.__name):
            data[name] = [self.__method[index], self.__value[index],  self.__answer[index]]
        return data
