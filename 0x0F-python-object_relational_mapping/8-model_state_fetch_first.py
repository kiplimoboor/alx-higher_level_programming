#!/usr/bin/python3

"""
    Usage: <program> user password database
    
    Lists first state object
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

    result = session.execute(select(State).order_by(State.id)).first()

    for state in result:
        print(f"{state.id}: {state.name}")
