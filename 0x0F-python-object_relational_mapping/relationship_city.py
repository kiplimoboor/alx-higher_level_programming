#!/usr/bin/python3

"""
    Contains class definition of a city
"""

from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
        Class definition of city
    """
    __tablename__ = 'cities'
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    state_id: Mapped[int] = mapped_column(ForeignKey('states.id'))
    state: Mapped["State"] = relationship(back_populates='cities')
