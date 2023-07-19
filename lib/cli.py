#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Passenger, Flight, Reservation, Pilot, session
#from sqlalchemy.ext.declarative import declarative_base






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
    - to create a new reservation, please enter: 'create' 
    - to edit an existing reservation, please enter your reservation number.
    - to register as new pilot, type in secret password.
    - to enter pilot-only options, please enter pilot id.
    """)
    user_input = input('>> ')
        #creating reservation
    if user_input == 'create':
        print("For returning users, please enter your first and last name exactly as you did for previous reservations. *Not case sensitive")
        first_name = input("Please enter your first name: ").lower()
        last_name = input("Please enter your last name: ").lower()
        #if passenger is found in the database
        if len(session.query(Passenger).filter_by(first_name = first_name, last_name = last_name).all()) == 1:
            print(f"Welcome back {first_name.capitalize()} {last_name.capitalize()}.")
        #if no passenger is found in the database
        else:
            new_passenger = Passenger(first_name = first_name, last_name = last_name)
            session.add(new_passenger)
            session.commit()
            print(f"Welcome to Flat-lines, {first_name.capitalize()} {last_name.capitalize()}.")
        current_passenger = session.query(Passenger).filter_by(first_name = first_name, last_name = last_name).all()[0]
       
        print("\nFlight Origin.")
        for city in cities:
            print(city)
        origin = input("Where are you flying from?: ")
        #NEED: add loop for if user enters invalid city name
        if origin in cities: 
            origin = airport_dict[origin]
        print("\nFlight Destination.")
        for city in cities:
            if city != origin:
                print(city)
        destination = input("Where would you like to fly to?: ")
        #NEED: add loop for if user enters invalid city name
        #fetch matching flight
        current_flight = session.query(Flight).filter_by(origin = origin, destination = destination).all()[0]
        #print seating chart
        print(seating_legend)
        print(current_flight.seat_chart)
        #prompt user for seat number
        seat_number = input("Please enter your seat number: ")
        # import ipdb; ipdb.set_trace()

        new_reservation = Reservation(passenger_id = current_passenger.id, flight_id = current_flight.id, seat_number = seat_number)    
        print(new_reservation)
        session.add(new_reservation)
        session.commit()
        print(f"Your reservation id is {new_reservation.id}. Thank you for flying with Flatlines!")

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
    
    if user_input == 'const [torture, setTorture] = useState(SqlAlchemy)':
        print ("We see that you have gained the secret password.... and you have successfully joined flatiron airlines!")
        print("enter your first name, last name, and a personal id number.")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        id = input("Enter id number: ")

        new_pilot = Pilot(first_name = first_name, last_name = last_name, id = id)
        session.add(new_pilot)
        session.commit()

    



    elif user_input != "x" :
        user_input = input('>> ')

