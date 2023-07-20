#!/usr/bin/env python3
import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Passenger, Flight, Reservation, session, Pilot

#ASSETS:
from assets import *

#MAIN menu
def main_menu(*args):
    menu_dict = {
            "c": create_reservation,
            "e": edit_reservation,
            "p": register_pilot
        }
    print("""
        Please select from the following menu options:
        c - create a new reservation
        e - edit an existing reservation
        p - register as new pilot
        x - exit 
        """)
    while True:
        user_input = input(">> ")
        if user_input in menu_dict:
            menu_dict[user_input]()
            break
        elif user_input == 'x':
            print("Exiting application. Hope to see you again soon!")
            break
        else:
            print("Invalid menu option. Please try again.")

#CREATE reservation
def create_reservation():
    #prompt user for name
    print("For returning users, please enter your first and last name exactly as you did for previous reservations. *Not case sensitive")
    while True:
        first_name = input("Please enter your first name: ")
        if validate_name(first_name):
            first_name = first_name.rstrip().lower()
            break
    while True: 
        last_name = input("Please enter your last name: ")
        if validate_name(last_name):
            last_name = last_name.rstrip().lower()
            break
    #welcome back: for existing customers
    if len(session.query(Passenger).filter_by(first_name = first_name, last_name = last_name).all()) == 1:
        print(f"\nWelcome back {first_name.capitalize()} {last_name.capitalize()}.")
    #welcome to: for new customers
    else:
        new_passenger = Passenger(first_name = first_name, last_name = last_name)
        session.add(new_passenger)
        session.commit()
        print(f"Welcome to Flat-lines, {first_name.capitalize()} {last_name.capitalize()}.")
    #set current passenger
    current_passenger = session.query(Passenger).filter_by(first_name = first_name, last_name = last_name).all()[0]
    #select ORIGIN:
    print("\nFlight Origin.")
    print(city_airport_list())
    # print(airport_dict[0].keys())
    # print(airport_dict[0].values())
    while True:
        origin = input("Where are you flying from?: ").capitalize()
        if validate_airport(origin):
            origin = check_airport(origin)
            break
    #select DESTINATION:
    print("\nFlight Destination.")
    print(city_airport_list(origin))
    while True:
        destination = input("Where would you like to fly to?: ").capitalize()
        if validate_airport(destination):
            destination = check_airport(destination)
            if destination == origin:
                print("Destination cannot match origin.")
                continue
            else:
                break
    #fetch matching flight
    current_flight = session.query(Flight).filter_by(origin = origin, destination = destination).all()[0]
    #print seating chart
    print(seat_legend)
    print(current_flight.seat_chart)
    #prompt user for seat number
    while True:
        seat_number = input("Please enter your seat number: ")
        if not seat_number.isdigit():
            print("Invalid seat number. Seat number should contain only numbers. Please try again.")
            continue
        if int(seat_number) in current_flight.open_seats:
            break
        else:
            print("Invalid selection, please try again.")
    #create new reservation
    new_reservation = Reservation(passenger_id = current_passenger.id, flight_id = current_flight.id, seat_number = seat_number)    
    #print(new_reservation)
    session.add(new_reservation)
    session.commit()
    print(f"\nYour reservation id is {new_reservation.id}. Thank you for flying with Flatlines!")
    print("""
    Please select from the following menu options:
    m - return to main menu
    p - print reservation
    x - exit
    """)
    menu_dict = {
        "m": main_menu,
        "p": lambda  :print(new_reservation.ticket, """
        m - return to main menu
        p - print reservation again
        x - exit
            """)
    }
    while True:
        user_input = input(">> ")
        if user_input in menu_dict.keys():
            menu_dict[user_input]()
            break
        elif user_input == 'x':
            print("Exiting application. Hope to see you again soon!")
            break

#FIND existing reservation:
def find_reservation():
    #prompts user for reservation number and returns reservation object once found
    while True:
        print("Please enter your reservation number (or 'm' to return to the main menu): ")
        reservation_number = input(">> ")
        if reservation_number == 'm':
            main_menu()
        search_reservation = session.query(Reservation).filter_by(id=reservation_number).first()
        if search_reservation:
            break
        else: 
            print("Reservation not found. Please enter a valid reservation number.")
    return search_reservation

#CHANGE seat:
def change_seat(existing_reservation):
    current_reservation = existing_reservation
    current_flight = existing_reservation.flight
    current_passenger = existing_reservation.passenger
    #print seat charg
    print(seat_legend)
    print(current_flight.seat_chart)
    while True:
    #prompt user for new seat number
        new_seat_number = input("Please enter the new seat number: ")
        if not new_seat_number.isdigit():
            print("Invalid seat number. Seat number should contain only numbers. Please try again.")
            continue
        new_seat_number = int(new_seat_number)
        if new_seat_number < 1 or new_seat_number > 20:
            print("Invalid seat number. Seat number should be between 1 and 20. Please try again.")
        if not new_seat_number in current_flight.open_seats:
            print("Seat is already taken. Please try again.")
        else:
            current_reservation.seat_number = f"{new_seat_number:02d}"
            session.commit()
            print(current_reservation.ticket)
            print("Seat number updated successfully")
            main_menu()

#CANCEL reservation:
def cancel_reservation(existing_reservation):
    while True:
        confirmation = input('Are you sure you want to cancel this reservation ? (y/n): ')
        if confirmation.lower() == 'y':
            session.delete(current_reservation)
            session.commit()
            print("Reservation canceled successfully.")
            break
        elif confirmation.lower() == 'n':
            print("Transaction cancelled. Reservation saved.")
            break
        else:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")
    main_menu()

#EDIT reservation
def edit_reservation(existing_reservation=None):
    if not existing_reservation:
        current_reservation = find_reservation()
    else:
        current_reservation = existing_reservation
    # #fetch current_passenger... <-- reservation.passenger_id
    # current_passenger = current_reservation.passenger
    # #fetch current_flight... <-- reservation.flight_id
    # current_flight = current_reservation.flight

    #display reservation information to user
    print(current_reservation.ticket)

    #prompt user with options: CANCEL or EDIT
    print("""
    Please select from the following menu options:
    e - edit your reservation
    c - cancel your reservation
    m - main menu
    x - exit application
                            """)
    menu_dict = {
        "e": change_seat,
        "c": cancel_reservation,
        "m": main_menu,
    }
    while True:
        user_input = input(">> ")
        if user_input in menu_dict:
            menu_dict[user_input](current_reservation)
        elif user_input == 'x':
            print("Exiting application. Hope to see you again soon!")
            break
        else:
            print("Invalid menu option. Please try again.")

#REGISTER new pilot
def register_pilot():
    incorrect_pass_count = 0
    while True:
        print("Please enter the secret password.")
        user_input = input(">> ")
        if user_input == 'const [torture, setTorture] = useState(SqlAlchemy)':
            print ("Welcome to Flatlines!")
            while True:
                first_name = input("Please enter your first name: ")
                if validate_name(first_name):
                    first_name = first_name.rstrip().lower()
                    break
            while True:
                last_name = input("Please enter your last name: ")
                if validate_name(last_name):
                    last_name = last_name.rstrip().lower()
                    break
            while True:
                id = input("Enter id number: ")
                if id.isdigit():
                    if int(id) not in Pilot.ids():
                        break
                    else:
                        print(f"{id} is already taken.")
                else:
                    print("id must be a number.")
            new_pilot = Pilot(first_name = first_name, last_name = last_name, id = int(id))
            session.add(new_pilot)
            session.commit()
            print("Successfully registerd new pilot.")
            main_menu()
            break
        elif incorrect_pass_count == 2:
            print("You've been ejected. Exiting application.")
            break
        else:
            incorrect_pass_count += 1
            print(f"Incorrect password. {3-incorrect_pass_count} attempts remaining.")

#CLI
if __name__ == '__main__':
    print(f"""
    ----------------------
    Welcome to Flat-lines!
    {logo}
    ----------------------
    """)
    main_menu()
    



   
