#!/usr/bin/python3

"""
    Creates a State Class
"""

from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
