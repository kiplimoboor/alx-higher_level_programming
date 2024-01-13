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

    conn = engine.connect()
    session = Session(conn)

    result = session.query(State).where(State.id == 2).first()

    result.name = 'New Mexico'

    session.commit()
