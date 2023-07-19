# Code for seeding flights table with all possible flights between existing airports

import sqlite3
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Flight, Base
from assets import airport_dict
import ipdb

engine = create_engine('sqlite:///airline.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    for origin_city, origin_airport in airport_dict.items():
        for destination_city, destination_airport in airport_dict.items():
            if origin_city != destination_city:
                #flight = f"Flight from {origin_airport} ({origin_city}) to {destination_airport} ({destination_city})"
                new_flight = Flight(origin=origin_airport, destination=destination_airport)
                #print(new_flight)
                session.add(new_flight)

session.commit()
session.close()


