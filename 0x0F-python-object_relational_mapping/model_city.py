#!/usr/bin/python3

"""
    Contains class definition of a city
"""

from sqlalchemy import MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from model_state import Base


class City(Base):
    """
        Class definition of city
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
