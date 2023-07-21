# Flatlines: Flatiron School's Premiere Airline

## User Experience
Book your flight with Flatlines from a growing list of airports (currently operating out of five major US airports as of 21-Jul-2023!). Select your seat on our cozy Flatline 404 Airbus that carries only 20 passengers per flight, and engineered in-house! Print your boarding pass to finish your reservation and log back in anytime with your reservation number to change your seat for no additional charge or cancel your reservation. If interested, register as a pilot for Flatlines (once obtaining the secret password) and pilot flights for us. Pilots can eject passengers from the flights they are piloting. Fly with us at Flatlines today!

## Quick-Start Guide:
1. clone repository onto your local machine
2. cd into directory on your terminal
3. cd into `/lib` directory
4. run the command `python cli.py` in your terminal to start application

## Features
1. CLI structure:
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
        - p: pilot menu (password protected)
            - r: register new pilot
            - l: login existing pilot
                - e: edit flight
                    - s: print passenger list and seating chart
                    - e: eject passenger from flight
                - f: print flight list if logged in
            - m: main menu
            - x: exit application
        - x: exit application
2. SQL database schema:
    - Passengers: first_name, last_name, id
    - Flights: origin, destination, pilot, id
    - Reservations: passenger_id, flight_id, seat_number
    - Pilots: first_name, last_name, id
3. Graphical Prints:
    - passenger boarding ticket
    - flight seating chart

## Challenges:
- SQLalchemy and Alembic
- CLI looping and breaking
- formatting interpolated strings

## Next Steps:
- Factor all menu loops into general function
- Option to export boarding pass to .txt file with File i/o functions
- Emergency exit row in seating chart
- Algorithm to concert passenger id and reservation id to unique hashes
- Admin portal for creating flights and assigning pilots to flights
- Adding new airports and new cities
- Create date/time system for flights
- Create price system for flights

### Thank you for viewing our project, 
--Harjas Bedi</br>
--Sebastian Martinez</br>
--Francesco Wai