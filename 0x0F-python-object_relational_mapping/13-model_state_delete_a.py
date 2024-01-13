#!/usr/bin/python3

"""
    Usage: <program> user passwd database

    Deletes all states with an 'a'
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

if __name__ == '__main__':
    args = sys.argv
    engine = create_engine(
        f'mysql+mysqldb://{args[1]}:{args[2]}@localhost:3306/{args[3]}')

    session = Session(engine.connect())

    states = session.query(State).where(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
