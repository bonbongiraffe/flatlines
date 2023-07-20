# Developer seeding commands
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
    print("Hello, developer. Please enter your command from the options shown below: ")
    dev_input = input(">> ")
    #OPTIONS:
    # 'populate flights' --> populates sql flights table with all possible flights between airports, no pilots assigned
    # 'assign pilots' --> assigns pilot_id's to all flights based on: pilot_id 1 to all ODD flight_id's, pilot_id 2 to all EVEN flight_id's
    if dev_input == "populate flights":
        for origin_city, origin_airport in airport_dict[0].items():
            for destination_city, destination_airport in airport_dict[0].items():
                if origin_city != destination_city:
                    #flight = f"Flight from {origin_airport} ({origin_city}) to {destination_airport} ({destination_city})"
                    new_flight = Flight(origin=origin_airport, destination=destination_airport)
                    #print(new_flight)
                    session.add(new_flight)
    elif dev_input == "assign pilots":
        for flight in session.query(Flight):
            if flight.id%2 == 0:
                flight.pilot_id = 2
            else:
                flight.pilot_id = 1
            print(flight)

session.commit()
session.close()


