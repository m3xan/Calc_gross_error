
from sqlalchemy import select
from sqlalchemy.orm import Session

from data_base.table_values.table_model import PValue
from data_base.table_values.table_model import RomanovskyTable
from data_base.table_values.table_model import CharlierTable
from data_base.table_values.table_model import DixonTable

from data_base.engines import table_engine as engine


class DatabaseTableHandler:

    def __init__(self) -> None:
        self.session = Session(engine)

    def select_method(self, method, _n: int, _p: float) -> float | None:
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

    def select_romanovsky(self, _n: int, _p: float) -> float | None:
        return self.select_method(
            RomanovskyTable, _n, _p
        )

    def select_charlier(self, _n: int, _p: float) -> float | None:
        return self.select_method(
            CharlierTable, _n, _p
        )

    def select_dixon(self, _n: int, _p: float) -> float | None:
        return self.select_method(
            DixonTable, _n, _p
        )
