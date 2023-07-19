#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from assets import *
from models import Passenger, Flight, Reservation

if __name__ == '__main__':
    engine = create_engine('sqlite:///airline.db')
    Session = sessionmaker(bind=engine)
    session = Session()




    import ipdb; ipdb.set_trace()
