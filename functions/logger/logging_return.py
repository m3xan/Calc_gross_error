
import functools
import logging

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except TypeError:
            result = func()
        logging.debug(
                f'function: {func.__name__} finish with result: {result}'
            )
        return result
    return wrapper

def info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except TypeError:
            result = func()
        logging.info(
            f'function: {func.__name__} finish with result: {result}'
        )
        return result
    return wrapper
