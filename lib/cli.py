#!/usr/bin/env python3
import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Passenger, Flight, Reservation
#from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///airline.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

#ASSETS:
from assets import logo, seating_legend
from flights import airport_dict
cities = airport_dict.keys()
airports = airport_dict.values()

if __name__ == '__main__':
    print(f"""
    ----------------------
    Welcome to Flat-lines!
    {logo}
    ----------------------
    MENU
    c - create a new reservation
    e - edit an existing reservation
    x - exit 
    """)
    user_input = input('>> ')
    #CREATE reservation
    if user_input == 'c':
        print("For returning users, please enter your first and last name exactly as you did for previous reservations. *Not case sensitive")
        first_name = input("Please enter your first name: ").lower()
        last_name = input("Please enter your last name: ").lower()
        if len(session.query(Passenger).filter_by(first_name = first_name, last_name = last_name).all()) == 1:
            print(f"Welcome back {first_name.capitalize()} {last_name.capitalize()}.")
        else:
            new_passenger = Passenger(first_name = first_name, last_name = last_name)
            session.add(new_passenger)
            session.commit()
            print(f"Welcome to Flat-lines, {first_name.capitalize()} {last_name.capitalize()}.")
        current_passenger = session.query(Passenger).filter_by(first_name = first_name, last_name = last_name).all()[0]
        print("\nFlight Origin.")
        for city in cities:
            print(f'-{city}')
        origin = input("Where are you flying from?: ")
        #NEED: add loop for if user enters invalid city name
        if origin in cities: 
            origin = airport_dict[origin]
        print("\nFlight Destination.")
        for city in cities:
            if city != origin:
                print(f'-{city}')
        destination = input("Where would you like to fly to?: ")
        #NEED: add loop for if user enters invalid city name
            #fetch matching flight
        current_flight = session.query(Flight).filter_by(origin = origin, destination = destination).all()[0]
            #print seating chart
        print(seating_legend)
        print(current_flight.seat_chart)
            #prompt user for seat number
        seat_number = input("Please enter your seat number: ")
            #create new reservation
        new_reservation = Reservation(passenger_id = current_passenger.id, flight_id = current_flight.id, seat_number = seat_number)    
        print(new_reservation)
        session.add(new_reservation)
        session.commit()
        print(f"Your reservation id is {new_reservation.id}. Thank you for flying with Flatlines!")
        #NEED: loop to starting menu

    #EDIT reservation
    if user_input == 'e':
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
        #NEED: loop to starting menu

    elif user_input != "x" :
        user_input = input('>> ')

