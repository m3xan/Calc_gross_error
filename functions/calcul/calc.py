"""
Calc
====
import Calc

version = 0.1
"""
from abc import ABC, abstractmethod
from typing import overload
from decimal import Decimal
import statistics as stat
import math

class Method(ABC):
    """Abstract class for method calculation"""
    @abstractmethod
    def calculate(self, data: list[float], _p: float) -> list: """calc value with metod"""
    @abstractmethod
    def get_table_from_db(self, _n, _p): """get table value from db Method"""

class Romanovsky(Method):
    def calculate(self, data, _p):
        max_ = Decimal(max(data))
        min_ = Decimal(min(data))
        average = Decimal(stat.fmean(data))
        table_value = self.get_table_from_db(
            len(data),
            _p
        )
        _answer = []
        data = [(Decimal(val) - average)**2 for val in data]
        sx = Decimal(math.sqrt(sum(data)/(len(data) - 1)))
        b1 = abs(max_ - average) / sx
        b2 = abs(min_ - average) / sx
        if b1 > table_value:
            _answer.append(float(max_))
        if b2 > table_value:
            _answer.append(float(min_))
        return _answer

    def get_table_from_db(self, _n, _p):
        print(self.__class__.__name__)
        return 2.64

class Calculator:
    _method = None

    @overload
    def __init__(self, method: Method) -> None: ...
    @overload
    def __init__(self) -> None: ...

    def __init__(self, method: Method = None):
        if method is not None:
            self.set_method(method)

    def get_method(self):
        return self._method

    def set_method(self, method: Method):
        if isinstance(method, Method):
            self._method = method

    def calculate_with(self, data, _p):
        """calc with method"""
        if self._method is not None:
            return self._method.calculate(data, _p)
        return None

if __name__ == '__main__':
    value = [4.88, 4.69, 4.79, 4.84, 4.69, 4.88, 4.91, 4.65, 4.89, 5.75, 4.88, 4.63, 4.83, 3.93, 4.73]
    calculator = Calculator()
    calculator.set_method(Romanovsky())
    answer = calculator.calculate_with(value, 0.99)
    print(*answer)
