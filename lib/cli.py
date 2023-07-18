#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Passenger, Flight, Reservation

if __name__ == '__main__':
    engine = create_engine('sqlite:///airline.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# AIRPORTS
#JFK - New York
#LAX - Los Angeles
#DEN - Denver
#MIA - Miami
#ORD - Chicago

# FLIGHTS
# need to generate flights to/from every airport
# 20 flights, 4 out of each airport

seating_chart = """
SEATING CHART
W = Window
A = Aisle

W | 01 02 | A | 03 04 | W
W | 05 06 | A | 07 08 | W
W | 09 10 | A | 11 12 | W
W | 13 14 | A | 15 16 | W
W | 17 18 | A | 19 20 | W
"""

#NEED TO UPDATE WITH KEYS FROM AIRPORT DICT
cities = ["New York City", "Denver", "Los Angeles", "Miami", "Chicago"]

if __name__ == '__main__':
    print("Welcome to Flat-lines!")
    print("- to create a new reservation, please enter: 'create' ")
    print("- to edit an existing reservation, please enter your reservation number. ")
    user_input = input('>> ')
        #creating reservation
    if user_input == 'create':
        print("For returning users, please enter your first and last name exactly as you did for previous reservations.")
        print("*Not case sensitive")
        first_name = input("Please enter your first name: ").lower()
        last_name = input("Please enter your last name: ").lower()
        #if passenger is found in the database
        if len(session.query(Passenger).filter_by(first_name = first_name, last_name = last_name).all()) == 1:
            print(f"Welcome back {first_name} {last_name}.")
        #if no passenger is found in the database
        else:
            new_passenger = Passenger(first_name = first_name, last_name = last_name)
            session.add(new_passenger)
            session.commit
            print(f"Welcome to Flat-lines, {first_name} {last_name}.")
        current_passenger = session.query(Passenger).filter_by(first_name = first_name, last_name = last_name).all()  
        #import ipdb; ipdb.set_trace()
        origin = input("Where are you flying from?: ")
        destination = input("Where would you like to fly to?: ")
            #with origin and destination match user to a flight_id
        current_flight = session.query(Flight).filter_by(origin = origin, destination = destination).all()
        print(seating_chart)
        seat_num = input("Please enter your desired seat number: ")
            #CREATE reservation object (passenger_id, flight_id, seat_number)
        new_reservation = Reservation(passenger_id = current_passenger.id, flight_id = current_flight.id, seat_number = seat_number)
        #return reservation_id to user
        session.add(new_reservation)
        session.commit()
        print(f"Your reservation number is ...")

    #editing existing reservation
    if user_input == 1234:
        pass
        #display reservation information to user
        #prompt user with options: CANCEL or EDIT
        #EDIT
            #display seating chart
            #prompt user for new seat number
        #CANCEL
            #prompt user "are you sure? y/n"
            #delete if y
            #return to options if n

    elif user_input != "x" :
        user_input = input('>> ')

