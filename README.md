# NAME
Flat-lines

# DESCRIPTION
This is an application that allows the user to create a reservation. The user gets to choose where they are flying from as well as where they are flying to. Next the user then gets to choose the seat number they would like to sit in. More options this application allows the user to do is actually go back and edit their existing reservation. The user can cancel their reservation completely or modify their seat number. The last component that a user can use is being able to register as a pilot. The user has to put in a special password which then allows them to register as a pilot. 

# Stretch Goals: 
- pilot can eject passengers
- emergency exit row in seating chart

# CLI structure:
- main menu:
    - c: create reservation
        - m: main menu
        - p: print boarding ticket
        - x: exit application
    - e: edit reservation
        - e: change seat number
        - c: cancel
        - m: main menu
        - x: exit application
    - p: pilot menu
        - r: register new pilot
        - l: login existing pilot
        - (f): print flight list if logged in
        - (p): check passengers on flight if logged in
        - (e): eject passenger from flight if logged in
        - m: main menu
        - x: exit application
    - x: exit application

# AUTHORS 
Harjas Bedi
Frankie Wai
Sebastian Martinez