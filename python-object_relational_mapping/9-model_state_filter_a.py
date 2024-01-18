#!/usr/bin/env python3
import sys
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def filter_states(user, password, database):
    # Create a MySQL engine
    engine = create_engine(f'mysql+pymysql://{user}:{password}@localhost:3306/{database}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects with the letter a
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} user password database".format(sys.argv[0]))
        exit(1)
    user, password, database = sys.argv[1:4]
    filter_states(user, password, database)
    