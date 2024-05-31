
from sqlalchemy import select
from sqlalchemy.orm import Session

from data_base.table_values.table_model import P_Value
from data_base.table_values.table_model import Romanovsky_Table
from data_base.table_values.table_model import Charlier_Table
from data_base.table_values.table_model import Dixon_Table

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
                    P_Value.id
                ).where(
                    P_Value.p == _p
                ).scalar_subquery()
            )
            if result := session.execute(smet).first():
                return result[0]
            return None

    def select_romanovsky(self, _n: int, _p: float) -> float | None:
        return self.select_method(
            Romanovsky_Table, _n, _p
        )

    def select_charlier(self, _n: int, _p: float) -> float | None:
        return self.select_method(
            Charlier_Table, _n, _p
        )

    def select_dixon(self, _n: int, _p: float) -> float | None:
        return self.select_method(
            Dixon_Table, _n, _p
        )
