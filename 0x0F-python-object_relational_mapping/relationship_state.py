#!/usr/bin/python3

"""
    Creates a State Class
"""


from typing import List
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
        Class that maps to a table with same attributes
    """
    __tablename__ = 'states'
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    cities: Mapped[List['City']] = relationship(
        back_populates='state', cascade="all, delete")
