#!/usr/bin/env python3

# AIRPORTS
#JFK - New York
#LAX - Los Angeles
#DEN - Denver
#MIA - Miami
#ORD - Chicago

# FLIGHTS
# need to generate flights to/from every airport
# 20 flights, 4 out of each airport

# SEATING CHART
# W = Window
# A = Aisle
#
# W | 01 02 | A | 03 04 | W
# W | 05 06 | A | 07 08 | W
# W | 09 10 | A | 11 12 | W
# W | 13 14 | A | 15 16 | W
# W | 17 18 | A | 19 20 | W


if __name__ == '__main__':
    print("Welcome to Flat-lines!")
    print("- to create a new reservation, please enter: 'create' ")
    print("- to edit an existing reservation, please enter your reservation number. ")
    user_input = input('>> ')
    while user_input != "x":
        user_input = input('>> ')
        #creating reservation
        if user_input == 'create':
            pass:
            print("For returning users, please enter your first and last name exactly as you did for previous reservations.")
            first_name = input("Please enter your first name: ")
            last_name = input("Please enter your last name: ")
            #set passenger_id 
                #CREATE passenger object (first name, last name), IF user doesn't already exist in db
                #pull existing passenger object from db
            #prompt user for origin 
            #prompt user for destination
                #with origin and destination match user to a flight_id
            #print seating chart for user
            #prompt user for seat number
                #CREATE reservation object (passenger_id, flight_id, seat_number)
            #return reservation_id to user

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

