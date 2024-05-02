"""
Calc
====
import Calc
https://studfile.net/preview/3569684/
version = 0.1
"""
from abc import ABC, abstractmethod
from typing import overload
from decimal import Decimal
import statistics as stat
import math

from data_base.table_values.table_hanler import DatabaseTableHandler

class Method(ABC):
    """Abstract class for method calculation"""
    @abstractmethod
    def calculate(self, data: list[float], _p: float) -> list[float | None]: """calc value with metod"""
    @abstractmethod
    def get_value_db(self, _n: int, _p: float) -> float | None: """get table value from db Method"""

class Romanovsky(Method):
    def calculate(self, data, _p):
        max_ = Decimal(max(data))
        min_ = Decimal(min(data))
        average = Decimal(stat.fmean(data))
        _answer = []
        table_value = self.get_value_db(
            len(data),
            _p
        )
        if not table_value:
            return None
        data = [(Decimal(val) - average)**2 for val in data]
        sx = Decimal(math.sqrt(sum(data)/(len(data) - 1)))
        b1 = abs(max_ - average) / sx
        b2 = abs(min_ - average) / sx
        if b1 > table_value:
            _answer.append(float(max_))
        if b2 > table_value:
            _answer.append(float(min_))
        return _answer

    def get_value_db(self, _n, _p):
        table_db = DatabaseTableHandler()
        for corrector in [0, +1, -1]:
            correct_n = _n + corrector
            if _value := table_db.select_romanovsky(correct_n, _p):
                return _value
        return None

class Charlier(Method):
    def calculate(self, data, _p):
        _answer = []
        average = Decimal(stat.fmean(data))
        absolut_x = [abs(Decimal(val) - average) for val in data]
        table_value = self.get_value_db(
            len(data),
            _p
        )
        if not table_value:
            return None
        data_double = [(Decimal(val) - average)**2 for val in data]
        sx = Decimal(math.sqrt(sum(data_double)/(len(data_double) - 1)))
        for x in absolut_x:
            if x > sx * Decimal(table_value):
                _answer.append(
                    data[absolut_x.index(x)]
                )
        return _answer

    def get_value_db(self, _n, _p):
        table_db = DatabaseTableHandler()
        for corrector in [0, +1, -1]:
            correct_n = _n + corrector
            if _value := table_db.select_charlier(correct_n, _p):
                return _value
        return None

class Dixon(Method):
    def calculate(self, data, _p):
        _answer = []
        kd = {}
        data.sort(key=float)
        table_value = self.get_value_db(
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

    def get_value_db(self, _n, _p):
        table_db = DatabaseTableHandler()
        for corrector in [0, +1, -1]:
            correct_n = _n + corrector
            if _value := table_db.select_dixon(correct_n, _p):
                return _value
        return None

class Calculator:
    _method = None

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, method: Method) -> None: ...

    def __init__(self, method: Method = None):
        if method:
            self.set_method(method)

    def get_method(self):
        return self._method

    def set_method(self, method: Method):
        if isinstance(method, Method):
            self._method = method

    def calculate_with(self, data: list[float], _p: float):
        """calc with method"""
        if self._method:
            return self._method.calculate(data, _p)
        return None
