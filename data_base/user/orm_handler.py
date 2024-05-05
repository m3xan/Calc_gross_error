
from abc import ABC

from sqlalchemy.orm import Session
from data_base.engines import user_engine

class OrmHandler(ABC):
    session = Session(user_engine)

    def _commit(self, session: Session):
        try:
            session.commit()
        except:
            session.rollback()
            raise
