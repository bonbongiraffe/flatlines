#!/usr/bin/env python3
import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Passenger, Flight, Reservation

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

#MAIN menu
def main_menu():
    menu_dict = {
            "c": create_reservation,
            "e": edit_reservation
        }
    print("""
        Please select from the following menu options:
        c - create a new reservation
        e - edit an existing reservation
        x - exit 
        """)
    while True:
        user_input = input(">> ")
        if user_input in menu_dict:
            menu_dict[user_input]()
        elif user_input == 'x':
            print("Exiting application. Hope to see you again soon!")
            break
        else:
            print("Invalid menu option. Please try again.")

#CREATE reservation
def create_reservation():
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
def edit_reservation():
    while True:
    #prompt user for reservation number
        reservation_number = input("Please enter your reservation number (or 'x' to return to the main menu): ")
        if reservation_number == 'x':
            return
        current_reservation = session.query(Reservation).filter_by(id=reservation_number).first()
        if not current_reservation:
            print("Reservation not found. Please enter a valid reservation number.")
            continue
    #fetch current_passenger... <-- reservation.passenger_id
        current_passenger = session.query(Passenger).filter_by(id=current_reservation.passenger_id).first()
    #fetch current_flight... <-- reservation.flight_id
        current_flight = session.query(Flight).filter_by(id=current_reservation.flight_id).first()
        #ipdb> print(current_flight.seat_chart)
    #display reservation information to user
        print(f"Flight Origin: {current_flight.origin}")
        print(f"Flight Destination: {current_flight.destination}")
        print(f"Seat Number: {current_reservation.seat_number}")

        while True:
    #prompt user with options: CANCEL or EDIT
            user_input = input("""
e - To edit your reservation
CANCEL - To cancel your reservation
x - To exit to main menu 
                               """)
            if user_input == 'e':
        #EDIT
        #display seating chart
                print(seat_legend)
                print(current_flight.seat_chart)

                while True:
        #prompt user for new seat number
                    new_seat_number = input("Please enter the new seat number: ")

                    if not new_seat_number.isdigit():
                        print("Invalid seat number. Seat number should contain only numbers. Please try again.")
                        continue
                    new_seat_number = int(new_seat_number)

                    total_seats = 20
                    if new_seat_number < 1 or new_seat_number > total_seats:
                        print("Invalid seat number. Seat number should be between 1 and 20. Please try again.")
                    else:
                        current_reservation.seat_number = f"{new_seat_number:02d}"
                        session.commit()
                        print("Seat number updated successfully")
                        break

            elif user_input == 'CANCEL':
        #CANCEL
        #prompt user "are you sure? y/n"
                while True:
                    confirmation = input('Are you sure you want to cancel this reservation ? (y/n): ')
                    if confirmation.lower() == 'y':
        #delete if y
                        session.delete(current_reservation)
                        session.commit()
                        print("Reservation canceled successfully.")
                        break
                    elif confirmation.lower() == 'n':
                        print("Reservation cancellation canceled")
                        break
                    else:
                        print("Invalid input. Please enter 'y' for Yes or 'n' for No.")
            elif user_input == 'x':
                return
            else:
                print("Invalid input. Please enter 'e', 'CANCEL' or 'x' to return to the main menu.")
                    
           
        #return to options if n
    #NEED: loop if user didn't enter 'e' or 'CANCEL'
    #NEED: loop to starting menu

if __name__ == '__main__':
    print(f"""
    ----------------------
    Welcome to Flat-lines!
    {logo}
    ----------------------    
    """)
    main_menu()