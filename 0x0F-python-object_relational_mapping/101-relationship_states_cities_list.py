#!/usr/bin/python3

"""
    Usage: <program> user passwd database

    Lists all states, and corresponding cities
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    session = Session(engine.connect())

    rows = session.query(State).all()

    for row in rows:
        print(f'{row.id}: {row.name}')
        for city in row.cities:
            print(f'\t{city.id}: {city.name}')

    session.close()
