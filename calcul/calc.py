"""
Calc
====
import Calc

version = 0.1
"""
from decimal import Decimal
import statistics as stat
import math

def calc_roman_metod(values: list):
    max_ = Decimal(str(max(values)))
    min_ = Decimal(str(min(values)))
    average = Decimal(str(stat.fmean(values)))
    table_value = Decimal(2.64) # тут идём в базу данных за числом
    answer = []
    values = [(Decimal(val) - average)**2 for val in values]

    sx = Decimal(math.sqrt(sum(values)/(len(values) - 1)))

    b1 = abs(max_ - average) / sx
    b2 = abs(min_ - average) / sx

    if b1 > table_value:
        answer.append(float(max_))

    if b2 > table_value:
        answer.append(float(min_))

    return answer

if __name__ == '__main__':
    value = [4.88, 4.69, 4.79, 4.84, 4.69, 4.88, 4.91, 4.65, 4.89, 5.75, 4.88, 4.63, 4.83, 3.93, 4.73]
    print(*calc_roman_metod(value))
