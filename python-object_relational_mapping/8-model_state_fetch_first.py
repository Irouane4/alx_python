import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    state = session.query(State).order_by(State.id.asc()).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

if __name__ == "__main__":
    main()
    