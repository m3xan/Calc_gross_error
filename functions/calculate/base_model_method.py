
from abc import ABC, abstractmethod

from data_base.table_values.table_hanler import DatabaseTableHandler
from functions.settings.pydantic_model import MethodId

class Method(ABC):
    """Abstract class for method calculation"""
    id: MethodId

    @abstractmethod
    def calculate(self, data: list[float, ], _p: float) -> list[float | None]: """calc value with metod"""

    def _get_value_db(self, method, _n: int, _p: float) -> float | None:
        """get table value from db Method"""
        table_db = DatabaseTableHandler()
        for corrector in 0, 1, -1:
            if _value := table_db.select_method(
                method, _n + corrector, _p
            ):
                return _value
        return None
