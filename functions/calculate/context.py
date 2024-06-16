"""
Сontains context for working with strategies 
for calculating gross error
"""

from typing import overload

from .strategy.base_strategy import Method

class Calculator:
    """
    Сontext for calculating gross errors
    """

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

    def calculate_with(self, data, _p):
        if self.__method and len(data) >= 3:
            return self.__method.calculate(data, _p)
        return None
