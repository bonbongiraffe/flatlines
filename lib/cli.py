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
from assets import logo, seat_legend, airport_dict
cities = airport_dict[0].keys()
airports = airport_dict[0].values()

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
        first_name = input("Please enter your first name: ").rstrip().lower()
        last_name = input("Please enter your last name: ").rstrip().lower()
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
        print(seat_legend)
        print(current_flight.seat_chart)
            #prompt user for seat number
        seat_number = input("Please enter your seat number: ")
            #create new reservation
        new_reservation = Reservation(passenger_id = current_passenger.id, flight_id = current_flight.id, seat_number = seat_number)    
        print(new_reservation)
        session.add(new_reservation)
        session.commit()
        print(f"Your reservation id is {new_reservation.id}. Thank you for flying with Flatlines!")
        print("""
        MENU
        m - return to main menu
        p - print reservation
        x - exit
        """)
        user_input = input(">> ")
        if user_input == "p":
            print(new_reservation.ticket)
        #NEED: loop to starting menu

    #EDIT reservation
    if user_input == 'e':
        pass
        #prompt user for reservation number
        reservation_number = input("Please enter your reservation number: ")
        current_reservation = session.query(Reservation).filter_by(id=reservation_number)
        #fetch current_passenger... <-- reservation.passenger_id
        current_passenger = session.query(Passenger).filter_by(id=current_reservation.passenger_id)
        #fetch current_flight... <-- reservation.flight_id
        current_flight = session.query(Flight).filter_by(id=current_reservation.flight_id)
            #ipdb> print(current_flight.seat_chart)
        #display reservation information to user
        print(f"Flight Origin: {current_flight.origin}")
        print(f"Flight Destination: {current_flight.destination}")
        print(f"Seat Number: {current_reservation.seat_number}")
        #prompt user with options: CANCEL or EDIT
        user_input = input("To edit, please enter 'e'. To cancel reservation, please enter 'CANCEL'")
        if user_input == 'e':
            pass
            #EDIT
            #display seating chart
            print(seat_legend)
            print(current.flight.seat_chart)
            #prompt user for new seat number
        if user_input == 'CANCEL':
            pass        
            #CANCEL
            #prompt user "are you sure? y/n"
            #delete if y
            #return to options if n
        #NEED: loop if user didn't enter 'e' or 'CANCEL'
        #NEED: loop to starting menu

    elif user_input != "x" :
        user_input = input('>> ')

