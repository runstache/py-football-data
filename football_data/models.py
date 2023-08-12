"""
Football Data Models.
"""

from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column
from sqlalchemy.types import BigInteger, String, Integer, Boolean, REAL


class Base(MappedAsDataclass, DeclarativeBase):
    """
    Base Class for Data Models.
    """
    pass


class Player(Base):
    """
    Player Data Model Class
    """

    __tablename__ = 'players'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(500))
    position_id: Mapped[int] = mapped_column(Boolean, default=False)


class Position(Base):
    """
    Position Code Model Class.
    """

    __tablename__ = 'position_codes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(5))
    description: Mapped[str] = mapped_column(String(50))


class Schedule(Base):
    """
    Schedule Item Model Class.
    """

    __tablename__ = 'schedule'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    team_id: Mapped[int]
    opponent_id: Mapped[int]
    year_value: Mapped[int]
    week_number: Mapped[int]
    game_id: Mapped[int] = mapped_column(BigInteger)
    url: Mapped[str] = mapped_column(String(255))
    type_id: Mapped[int]
    is_home: Mapped[bool]


class StatisticCategory(Base):
    """
    Statistic Category Code Model.
    """

    __tablename__ = 'statistic_categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(10))
    description: Mapped[str] = mapped_column(String(50))


class StatisticCode(Base):
    """
    Statistic Code Model.
    """

    __tablename__ = 'statistic_codes'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(15))
    description: Mapped[str] = mapped_column(String(100))


class Statistic(Base):
    """
    Statistic Code Model.
    """

    __tablename__ = 'statistics'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    statistic_code_id: Mapped[int] = mapped_column(BigInteger)
    player_id: Mapped[int] = mapped_column(BigInteger)
    team_id: Mapped[int]
    schedule_id: Mapped[int] = mapped_column(BigInteger)
    value: Mapped[float] = mapped_column(REAL)
    category_id: Mapped[int]


class Team(Base):
    """
    Team Data Model.
    """

    __tablename__ = 'team'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(255))
    code: Mapped[str] = mapped_column(String(5))
    name: Mapped[str] = mapped_column(String(100))


class TypeCode(Base):
    """
    Type Code Data Model
    """

    __tablename__ = 'type_codes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(10))
    description: Mapped[str] = mapped_column(String(50))
