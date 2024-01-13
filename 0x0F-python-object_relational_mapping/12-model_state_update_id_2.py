#!/usr/bin/python3

"""
    Usage: <program> user passwd database

    Updates a record
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

    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
