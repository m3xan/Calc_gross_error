"""
содержит декораторы для работы с временем
"""

import time

def timer_decorator(func):
    """
    Декоратор возвращает время выполнения функции
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper
