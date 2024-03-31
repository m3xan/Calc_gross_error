from global_param import ECHO

class Singleton(object):
    _instance = None
    _logger = None
    _echo = None
    def __new__(cls, echo = ECHO):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
            cls._echo = echo
        return cls._instance
