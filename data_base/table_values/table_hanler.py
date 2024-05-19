
from sqlalchemy import select
from sqlalchemy.orm import Session

from data_base.table_values.table_model import P_Value
from data_base.table_values.table_model import Romanovsky_Table
from data_base.table_values.table_model import Charlier_Table
from data_base.table_values.table_model import Dixon_Table

from data_base.engines import table_engine as engine

class DatabaseTableHandler:

    def __init__(self) -> None:
        self.__session = Session(engine)

    def select_romanovsky(self, _n: int, _p: float) -> float | None:
        with self.__session as session:
            smet = select(
                Romanovsky_Table.value
            ).where(
                Romanovsky_Table.n_id == _n,
                Romanovsky_Table.p_id == select(
                    P_Value.id
                ).where(
                    P_Value.p == _p
                ).scalar_subquery()
            )
            if result := session.execute(smet).first():
                return result[0]
            return None

    def select_charlier(self, _n: int, _p: float) -> float | None:
        with self.__session as session:
            smet = select(
                Charlier_Table.value
            ).where(
                Charlier_Table.n_id == _n,
                Charlier_Table.p_id == select(
                    P_Value.id
                ).where(
                    P_Value.p == _p
                ).scalar_subquery()
            )
            result = session.execute(smet).first()
            if result:
                return result[0]
            return None

    def select_dixon(self, _n: int, _p: float) -> float | None:
        with self.__session as session:
            smet = select(
                Dixon_Table.value
            ).where(
                Dixon_Table.n_id == _n,
                Dixon_Table.p_id == select(
                    P_Value.id
                ).where(
                    P_Value.p == _p
                ).scalar_subquery()
            )
            result = session.execute(smet).first()
            if result:
                return result[0]
            return None
