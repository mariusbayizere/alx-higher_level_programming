#!/usr/bin/python3
""" funtion that will display name match then will receive the 4 argument
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    biger = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(biger[0].id)
    except IndexError:
        print("Not found")
