"""
calc
====
import calc
https://studfile.net/preview/3569684/
version = 0.1
"""
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import overload
import statistics as stat
from math import sqrt

from functions.settings.pydantic_model import MethodId

from data_base.table_values.table_hanler import DatabaseTableHandler

from data_base.table_values import table_model

class Method(ABC):
    """Abstract class for method calculation"""
    id: MethodId

    @abstractmethod
    def calculate(self, data: list[float, ], _p: float) -> list[float | None]: """calc value with metod"""

    def _get_value_db(self, method, _n: int, _p: float) -> float | None:
        """get table value from db Method"""
        table_db = DatabaseTableHandler()
        for corrector in 0, 1, -1:
            if _value := table_db.select_method(
                method, _n + corrector, _p
            ):
                return _value
        return None

class Romanovsky(Method):
    id = MethodId.ROMANOVSKY
    def calculate(self, data, _p):
        max_ = Decimal(max(data))
        min_ = Decimal(min(data))
        average = Decimal(stat.fmean(data))
        _answer = []
        table_value = self._get_value_db(
            table_model.RomanovskyTable,
            len(data),
            _p
        )
        if not table_value:
            return None
        data = [(Decimal(val) - average)**2 for val in data]
        sx = Decimal(sqrt(sum(data)/(len(data) - 1)))
        b1 = abs(max_ - average) / sx
        b2 = abs(min_ - average) / sx
        if b1 > table_value:
            _answer.append(float(max_))
        if b2 > table_value:
            _answer.append(float(min_))
        return _answer

class Charlier(Method):
    id = MethodId.CHARLIER
    def calculate(self, data, _p):
        _answer = []
        average = Decimal(stat.fmean(data))
        absolut_x = [abs(Decimal(val) - average) for val in data]
        table_value = self._get_value_db(
            table_model.CharlierTable,
            len(data),
            _p
        )
        if not table_value:
            return None
        data_double = [(Decimal(val) - average)**2 for val in data]
        sx = Decimal(sqrt(sum(data_double)/(len(data_double) - 1)))
        for x in absolut_x:
            if x > sx * Decimal(table_value):
                _answer.append(
                    data[absolut_x.index(x)]
                )
        return _answer

class Dixon(Method):
    id = MethodId.DIXON
    def calculate(self, data, _p):
        _answer = []
        kd = {}
        data.sort(key=float)
        table_value = self._get_value_db(
            table_model.DixonTable,
            len(data),
            _p
        )
        if not table_value:
            return None
        for i in data:
            if i == data[0] or (i - data[data.index(i) - 1]) == (i - data[0]):
                continue
            kd[i] = (
            Decimal((i - data[data.index(i) - 1]) / (i - data[0]))
            )
        for key, item in kd.items():
            if item > Decimal(table_value):
                _answer.append(key)
        return _answer

class Calculator:

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, method: Method) -> None: ...

    def __init__(self, method = None):
        if method:
            self.method = method
        else:
            self.__method = None

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, method: Method):
        if isinstance(method, Method):
            self.__method = method

    def calculate_with(self, data: list[float], _p: float):
        """calc with method"""
        if self.__method and len(data) >= 3:
            return self.__method.calculate(data, _p)
        return None
#Конфигурационный словарик https://www.youtube.com/watch?v=yHckrS1lvG8&t=7024s 2:56:29
method_map = {
    Romanovsky.id: Romanovsky,
    Charlier.id: Charlier,
    Dixon.id: Dixon,
}
