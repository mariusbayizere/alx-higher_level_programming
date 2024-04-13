#!/usr/bin/python3
""" script that lists all State objects, and corresponding City objects, contained in the database 
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for betty in session.query(State).order_by(State.id):
        print(betty.id, betty.name, sep=": ")
        for city_ins in betty.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
