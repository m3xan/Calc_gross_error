"""
заглушка
"""

from global_param import ECHO

class Singleton(object):
    _instance = None
    _logger = None
    _echo = ECHO

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance
