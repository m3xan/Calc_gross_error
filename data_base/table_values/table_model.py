
from sqlalchemy import ForeignKey

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

class PValue(Base):
    __tablename__ = 'p_value'
    p: Mapped[float] = mapped_column(unique=True)
    def __repr__(self) -> str:
        return f'P_Value(id={self.id!r}, p={self.p!r})'

class NValue(Base):
    __tablename__ = 'n_value'
    n: Mapped[int] = mapped_column(unique=True)
    def __repr__(self) -> str:
        return f'N_Value(id={self.id!r}, n={self.n!r})'

class RomanovskyTable(Base):
    __tablename__ = 'romanovsky_table'
    value: Mapped[float]
    n_id: Mapped[int] = mapped_column(ForeignKey('n_value.id'))
    p_id: Mapped[int] = mapped_column(ForeignKey('p_value.id'))
    def __repr__(self) -> str:
        return f'Romanovsky_Table(id={self.id!r}, value={self.value!r}, n_id={self.n_id!r}, p_id={self.p_id!r})'

class CharlierTable(Base):
    __tablename__ = 'charlier_table'
    value: Mapped[float]
    n_id: Mapped[int] = mapped_column(ForeignKey('n_value.id'))
    p_id: Mapped[int] = mapped_column(ForeignKey('p_value.id'))
    def __repr__(self) -> str:
        return f'Charlier_Table(id={self.id!r}, value={self.value!r}, n_id={self.n_id!r})'

class DixonTable(Base):
    __tablename__ = 'dixon_table'
    value: Mapped[float]
    n_id: Mapped[int] = mapped_column(ForeignKey('n_value.id'))
    p_id: Mapped[int] = mapped_column(ForeignKey('p_value.id'))
    def __repr__(self) -> str:
        return f'Dixon_Table(id={self.id!r}, value={self.value!r}, n_id={self.n_id!r}, p_id={self.p_id!r})'
