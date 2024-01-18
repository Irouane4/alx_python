import sys
from sqlalchemy import (create_engine, Column, Integer, String, ForeignKey,
                        CheckConstraint, UniqueConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):
    """Represents a state in the United States.
    
    Attributes:
        id (int): A unique identifier for the state.
        name (str): The name of the state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<State(id='%s', name='%s')>" % (self.id, self.name)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    