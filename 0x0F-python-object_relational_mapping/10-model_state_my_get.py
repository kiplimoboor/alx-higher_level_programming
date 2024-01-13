#!/usr/bin/python3

"""
    Usage: <program> user passwd database

    Lists state objects with an 'a' in the name
"""

import sys
from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == '__main__':
    args = sys.argv

    engine = create_engine(
        f'mysql+mysqldb://{args[1]}:{args[2]}@localhost:3306/{args[3]}')
    conn = engine.connect()
    session = Session(conn)

    stmt = select(State).where(State.name == {args[4]})

    result = session.execute(stmt).first()

    if result:
        print(result[0].id)
    else:
        print("Not found")
