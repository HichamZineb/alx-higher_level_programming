#!/usr/bin/python3
""" Script that lists all State objects from the database hbtn_0e_6_usa. """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()

    if states:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
