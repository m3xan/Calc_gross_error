from abc import ABC

class Calc(ABC):
    append: int
    change: int

class Values(Calc):
    append = 1
    change = 2

class Names(Calc):
    append = 3
    change = 4

class Answers(Calc):
    append = 5
    change = 6

class Methods(Calc):
    append = 7
    change = 8
