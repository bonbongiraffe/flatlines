#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from assets import *
from models import Passenger, Flight, Reservation, Pilot

if __name__ == '__main__':
    engine = create_engine('sqlite:///airline.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    #print(session.query(Flight).filter_by(id=3).first().passenger_list)

    import ipdb; ipdb.set_trace()
