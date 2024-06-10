"""
calc
====
import strategy
https://studfile.net/preview/3569684/
version = 0.1
"""

from decimal import Decimal
import statistics as stat
import math

from functions.calculate.strategy.base_strategy import Method, MethodId

from data_base.table_values import table_model

class Romanovsky(Method):
    """
    заглушка
    """
    id_ = MethodId.ROMANOVSKY
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
        data = [(Decimal(val) - average) ** 2 for val in data]
        sx = Decimal(
            math.sqrt(sum(data) / (len(data) - 1))
        )
        b1 = abs(max_ - average) / sx
        b2 = abs(min_ - average) / sx
        if b1 > table_value:
            _answer.append(float(max_))
        if b2 > table_value:
            _answer.append(float(min_))
        return _answer

class Charlier(Method):
    """
    заглушка
    """
    id_ = MethodId.CHARLIER
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
        data_double = [(Decimal(val) - average) ** 2 for val in data]
        sx = Decimal(
            math.sqrt(sum(data_double) / (len(data_double) - 1))
        )
        for x in absolut_x:
            if x > (sx * Decimal(table_value)):
                _answer.append(
                    data[absolut_x.index(x)]
                )
        return _answer

class Dixon(Method):
    """
    заглушка
    """
    id_ = MethodId.DIXON
    def calculate(self, data, _p):
        _answer = []
        kd = {}
        data.sort(key= float)
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
                Decimal(
                    (i - data[data.index(i) - 1]) / (i - data[0])
                )
            )
        for key, item in kd.items():
            if item > Decimal(table_value):
                _answer.append(key)
        return _answer
