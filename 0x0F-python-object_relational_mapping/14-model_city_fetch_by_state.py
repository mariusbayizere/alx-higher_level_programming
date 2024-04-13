#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py that prints
all City objects from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for bigg in (session.query(State.name, City.id, City.name)
                        .filter(State.id == City.state_id)):
        print(bigg[0] + ": (" + str(bigg[1]) + ") " + bigg[2])
