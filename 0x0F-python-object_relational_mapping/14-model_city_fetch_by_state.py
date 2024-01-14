#!/usr/bin/python3

"""
    Usage: <program> user passwd database

    Prints all the Cities details
"""

from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    session = Session(engine.connect())

    rows = session.query(City.name, City.id, State.name).join(State).all()

    for row in rows:
        print(f'{row[2]}: ({row[1]}) {row[0]}')

    session.close()
