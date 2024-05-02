
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)

class User(Base):
    __tablename__ = "users"
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
    name_calculation: Mapped[str] = mapped_column(String(50))
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship(back_populates="calculations")
    id_metod: Mapped[int]  = mapped_column(ForeignKey('metod.id'), nullable= True)
    values: Mapped[List["Value"]] = relationship(
        back_populates="calculation", cascade="all, delete-orphan"
    )
    answer: Mapped[List["Answer"]] = relationship(
        back_populates="calculation", cascade="all, delete-orphan"
    )
    calculated: Mapped[bool]
    def __repr__(self) -> str:
        return f"Calculation(id={self.id!r}, name_calculation={self.name_calculation!r}, user_id={self.id_user!r}, value={self.values!r}, answer={self.answer!r})"

class Metod(Base):
    __tablename__ = "metod"
    metod_name: Mapped[str] = mapped_column(String(40))
    def __repr__(self) -> str:
        return f"Metod(id={self.id!r}, name_metod={self.metod_name!r})"

class Answer(Base):
    __tablename__ = "answer"
    calculation_id: Mapped[int]= mapped_column(ForeignKey('calculation.id'))
    answer_value: Mapped[int] = mapped_column(nullable= False)
    calculation: Mapped["Calculation"] = relationship(back_populates="answer")
    def __repr__(self) -> str:
        return f"Answer(id={self.id!r}, name_metod={self.calculation_id!r}, answer_value={self.answer_value!r}, calculation={self.calculation!r})"

class Value(Base):
    __tablename__ = "calculation_value"
    calculation_id: Mapped[int]= mapped_column(ForeignKey('calculation.id'))
    value: Mapped[float] = mapped_column(nullable= False)
    calculation: Mapped["Calculation"] = relationship(back_populates="values")
    def __repr__(self) -> str:
        return f"Value(id={self.id!r}, user_id={self.calculation_id!r}, value={self.value!r}, calculation={self.calculation!r})"
