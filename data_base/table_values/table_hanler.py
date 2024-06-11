"""
заглушка
"""
from sqlalchemy import select
from sqlalchemy.orm import Session

from data_base.table_values.table_model import PValue
from data_base.engines import table_engine as engine
from functions import logger

class DatabaseTableHandler:
    """
    for load table value
    """

    def __init__(self) -> None:
        self.session = Session(engine)

    @logger.info
    def select_method(self, method, _n: int, _p: float) -> float | None:
        """
        sellect table value from method table
        """
        with self.session as session:
            smet = select(
                method.value
            ).where(
                method.n_id == _n,
                method.p_id == select(
                    PValue.id
                ).where(
                    PValue.p == _p
                ).scalar_subquery()
            )
            if result := session.execute(smet).first():
                return result[0]
            return None
