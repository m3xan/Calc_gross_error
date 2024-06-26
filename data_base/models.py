from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from data_base.engine import engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    clearance_level: Mapped[int]
    image: Mapped[str] = mapped_column(nullable= True)
    calculations: Mapped[List["Calculation"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.username!r}, fullname={self.password!r}, clearance_level={self.clearance_level!r}, image={self.image!r})"

class Calculation(Base):
    __tablename__ = "calculation"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    name_calculation: Mapped[str] = mapped_column(String(50))
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship(back_populates="calculations")
    id_metod: Mapped[int]  = mapped_column(ForeignKey('metod.id'))
    values: Mapped[List["Value"]] = relationship(
        back_populates="calculation", cascade="all, delete-orphan"
    )
    answer: Mapped[List["Answer"]] = relationship(
        back_populates="calculation", cascade="all, delete-orphan"
    )
    id_calculated: Mapped[int] = mapped_column(ForeignKey('calculated.id'))
    def __repr__(self) -> str:
        return f"Calculation(id={self.id!r}, name_calculation={self.name_calculation!r}, user_id={self.id_user!r}, value={self.values!r}, answer={self.answer!r})"

class Calculated(Base):
    __tablename__ = "calculated"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    metod_name: Mapped[bool] = mapped_column(unique=True)
    def __repr__(self) -> str:
        return f"Calculated(id={self.id!r}, name_metod={self.metod_name!r})"

class Metod(Base):
    __tablename__ = "metod"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    metod_name: Mapped[str] = mapped_column(String(40))
    def __repr__(self) -> str:
        return f"Calculated(id={self.id!r}, name_metod={self.metod_name!r})"

class Answer(Base):
    __tablename__ = "answer"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    calculation_id: Mapped[int]= mapped_column(ForeignKey('calculation.id'))
    answer_value: Mapped[int] = mapped_column(nullable= False)
    calculation: Mapped["Calculation"] = relationship(back_populates="answer")
    def __repr__(self) -> str:
        return f"Calculated(id={self.id!r}, name_metod={self.calculation_id!r}, answer_value={self.answer_value!r}, calculation={self.calculation!r})"

class Value(Base):
    __tablename__ = "calculation_value"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    calculation_id: Mapped[int]= mapped_column(ForeignKey('calculation.id'))
    value: Mapped[int] = mapped_column(nullable= False)
    calculation: Mapped["Calculation"] = relationship(back_populates="values")
    def __repr__(self) -> str:
        return f"Calculation(id={self.id!r}, user_id={self.calculation_id!r}, value={self.value!r}, calculation={self.calculation!r})"

if __name__ == '__main__':
    Base.metadata.create_all(engine)
