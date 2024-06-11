"""
Basic strategy for calculating gross error
"""

from abc import ABC, abstractmethod

from data_base.table_values.table_hanler import DatabaseTableHandler

from .strategy_id import MethodId

type Answer = list[float | None]

class Method(ABC):
    """Abstract class for method calculation"""
    id_: MethodId

    @abstractmethod
    def calculate(self, data: list[float, ], _p: float) -> Answer | None:
        """calc value with metod"""

    def _get_value_db(self, method, _n: int, _p: float) -> float | None:
        """get table value from db Method"""
        table_db = DatabaseTableHandler()
        for corrector in 0, 1, -1:
            if _value := table_db.select_method(
                method, _n + corrector, _p
            ):
                return _value
        return None
