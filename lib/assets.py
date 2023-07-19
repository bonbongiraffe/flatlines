# ASSETS - Table Of Contents
#############################
# 1. Airport Dictionary
# 2. Menu
# 3. Logo
# 4. Seat Legend
# 5. Seat Template
# 6. Ticket Template
#############################

#1: AIRPORTS and CITIES
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

#2. Menu:

#3: Flat-Line logo:
logo = """
\t     __   __
\t    / /  / /
\t   / /  / /  
\t  / /  / /       
\t / /  / /       
\t/_/  /_/
"""

#4: seat legend:
seat_legend = """
SEATING CHART
W = Window
A = Aisle
xx = Taken Seat
"""

#5: seat template --> property method of Flight:
# W | 01 02 | A | 03 04 | W
# W | 05 06 | A | 07 08 | W
# W | 09 10 | A | 11 12 | W
# W | 13 14 | A | 15 16 | W
# W | 17 18 | A | 19 20 | W

#6: ticket template --> property method of Reservation:
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
