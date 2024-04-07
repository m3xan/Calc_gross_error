"""
Calc
====
import Calc

version = 0.1
"""
from abc import ABC, abstractmethod
from decimal import Decimal
import statistics as stat
import math

class Method(ABC):
    @abstractmethod
    def calculate(self, data: list[float]) -> list:
        pass

class Romanovski(Method):
    def calculate(self, data):
        max_ = Decimal(max(data))
        min_ = Decimal(min(data))
        average = Decimal(stat.fmean(data))
        table_value = Decimal(2.64) # тут идём в базу данных за числом
        answer = []
        data = [(Decimal(val) - average)**2 for val in data]

        sx = Decimal(math.sqrt(sum(data)/(len(data) - 1)))

        b1 = abs(max_ - average) / sx
        b2 = abs(min_ - average) / sx
        if b1 > table_value:
            answer.append(float(max_))

        if b2 > table_value:
            answer.append(float(min_))

        return answer

class Calculator:
    def __init__(self, method: Method):
        self._method = method

    def calculate_with(self, data):
        return self._method.calculate(data)

if __name__ == '__main__':
    value = [4.88, 4.69, 4.79, 4.84, 4.69, 4.88, 4.91, 4.65, 4.89, 5.75, 4.88, 4.63, 4.83, 3.93, 4.73]
    calculator = Calculator(Romanovski())
    answer = calculator.calculate_with(value)
    print(*answer)
