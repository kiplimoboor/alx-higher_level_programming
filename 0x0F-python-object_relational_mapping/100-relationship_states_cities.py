#!/usr/bin/python3

"""
    Usage: <program> user password database

    Creates state California, with city San Francisco
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base
from relationship_state import State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    session = Session(engine.connect())
    Base.metadata.create_all(engine)

    state = State(name='California')
    state.cities = [City(name='San Francisco')]
    session.add(state)
    session.commit()
