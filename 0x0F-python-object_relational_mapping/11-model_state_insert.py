#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import insert, create_engine

if __name__ == '__main__':
    args = sys.argv
    engine = create_engine(
        f'mysql+mysqldb://{args[1]}:{args[2]}@localhost:3306/{args[3]}')
    Base.metadata.create_all(engine)
    
    conn = engine.connect()
    session = Session(conn)

    state = State(name='Louisiana')

    session.add(state)
    session.commit()
    session.refresh(state)
    print(state.id)