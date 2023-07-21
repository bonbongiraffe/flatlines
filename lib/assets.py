# ASSETS - Table Of Contents
#############################
# 1. Airport Dictionary
# 2. Menu
# 3. Logo
# 4. Seat Legend
# 5. Seat Template
# 6. Ticket Template
# 7. City List
# 8. Validations
#############################

#1. Airport and City Dictionaries:
airport_dict = [
        #[0]: city to airports
        {
            "New York City": "JFK",
            "Chicago": "ORD",
            "Miami": "MIA",
            "Denver": "DEN",
            "Los Angeles": "LAX"
        },
        #[1]: airport to city
        {
            "JFK": "New York City",
            "ORD": "Chicago",
            "MIA": "Miami",
            "DEN": "Denver",
            "LAX": "Los Angeles"
        }
    ] 
cities = airport_dict[0].keys()
airports = airport_dict[0].values()

#2. Menu Function (wip):
# need function objects with attributes: key_letter: 'c', description: 'create reservation', function: create_reservation
    #i.e.: 
        # m_create_reservation = {
        #     "key_letter": "c",
        #     "description": "create reservation",
        #     "function": create_reservation
        # }
    # -> menu objs structured as above ^ 3 key:value pairs
    # -> accepts 2 arguments: list of menu objs, list of arguments 
    # -> constructs menu dict
    # -> prints menu options
    # -> loops user until valid menu selection is entered
    # -> calls corresponding menu function with list of arguments
def menu_constructor(menu_list,arg_list=[]):
    menu_print = "Please select from the following menu options: "
    menu_dict = {}
    for menu_obj in menu_list:
        menu_line = f"\n\t{menu_obj["key_letter"]} - {menu_obj["description"]}"
        #build menu dict with (key) = key_letter , (value) = function
        menu_dict[menu_obj["key_letter"]] = menu_obj["function"]
        menu_print += menu_line
    print(menu_print)
    while True:
        user_input = input(">> ")
        if user_input in menu_dict.keys():
            menu_dict[user_input](*arg_list)
            break
        else:
            print("Invalid menu selection. Please try again.")

#3. Flat-Line logo:
logo = """
\t     __   __
\t    / /  / /
\t   / /  / /  
\t  / /  / /       
\t / /  / /       
\t/_/  /_/
"""

#4. seat legend:
seat_legend = """
SEATING CHART
W = Window
A = Aisle
xx = Taken Seat
"""

#5. seat template --> property method of Flight:
# W | 01 02 | A | 03 04 | W
# W | 05 06 | A | 07 08 | W
# W | 09 10 | A | 11 12 | W
# W | 13 14 | A | 15 16 | W
# W | 17 18 | A | 19 20 | W

#6. ticket template --> property method of Reservation:
# f"""
#      ___________________________________
#     |   // FLATLINES  
#     |
#     |      {passenger_name} 
#     |      Seat: {seat_number}                     
#     |   {origin_city} ({origin_airport}) -->
#     |   {destination_city} ({destination_airport})
#     |___________________________________   

#     """

#7. City List: returns formatted list of cities with airports, optionally excluding an origin city/airport
def city_airport_list ( origin_airport=None ):
    ca_list = ""
    for city in airport_dict[0]:
        if origin_airport != None:
            if airport_dict[0][city] == origin_airport:
                continue
        ca_list += f"-{city} ({airport_dict[0][city]})\n"
    return ca_list

#8. Validations:
def validate_string(input=""):
    special_characters = """"!@#$%^&*()-=_+[]}{\|/?.>,<`~';:"""
    numbers = "1234567890"
    if input == "":
        print("Input cannot be empty string.")
        return False
    if any(c in special_characters for c in input):
        print("Input cannot contain special characters.")
        return False
    elif any(c in numbers for c in input):
        print("Input cannot contain numbers.")
        return False
    else: 
        return True

def validate_name(name=""):
    if not validate_string(name):
        return False
    elif 2 <= len(name) <= 12:
        return True
    else:
        print("Name must be between 2 and 12 characters.")
        return False

def validate_airport(input):
    if not validate_string(input):
        return False
    if input.title() in airport_dict[0].keys() or input.upper() in airport_dict[0].values():
        return True
    else:
        print("Airport not found in database.")
        return False

def check_airport(input): #allowing user to input either city or airport 
    #converts city to corresponding airport
    if input.title() in airport_dict[0].keys():
        return airport_dict[0][input.title()]
    #checks and returns airport 
    elif input.upper() in airport_dict[0].values():
        return input.upper()
    else:
        print("Airport not found in database.")
