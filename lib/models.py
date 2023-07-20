from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from assets import airport_dict

Base = declarative_base()

engine = create_engine('sqlite:///airline.db')
Session = sessionmaker(bind=engine)
session = Session()


class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column( Integer() , primary_key = True )
    first_name = Column( String() )
    last_name = Column( String() )

    reservations = relationship('Reservation', backref='passenger')
    flights = association_proxy( 'reservations', 'flight' )

    @property
    def name(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def __repr__( self ):
        return f'(id: {self.id}, ' + \
            f'first_name: {self.first_name}, ' + \
            f'last_name: {self.last_name})' 

class Flight(Base):
    __tablename__ = 'flights'

    id = Column( Integer(), primary_key = True )
    pilot_id = Column(Integer(), ForeignKey('pilots.id'))
    origin = Column( String() )
    destination = Column( String() )

    reservations = relationship('Reservation', backref='flight') #--> [{reservation_obj1...},{reservation_obj2...}]
    passengers = association_proxy( 'reservations', 'passenger' )

    @property #returns a list of seat numbers from 1 to 20 ommitting taken seats based on existing reservations
    def open_seats(self):
        taken_list = [reservation.seat_number for reservation in self.reservations] #--> [17,18]
        empty_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        open_list = [seat for seat in empty_list if seat not in taken_list] #--> [1,2,3,...15,16,19,20]
        return open_list

    @property #returns the seating chart with xx's in place of taken seats, string-formatted
    def seat_chart(self):
        seat_list = self.open_seats
        chart_string = ""
        #runs for i = 0,1,2,3,4 -- once for each row
        for i in range(5):
            row = []
            #runs for j = i, i+1, i+2, i+3 -- once for each seat
            for j in range((4*i)+1,(4*i)+5):
                if j in seat_list:
                    row.append(f"{j:02}")
                else:
                    row.append("xx")
            row_string = f"W | {row[0]} {row[1]} | A | {row[2]} {row[3]} | W\n"
            chart_string += row_string
        return chart_string     

    def __repr__( self ):
        return f'(id: {self.id}, ' + \
            f'origin: {self.origin}, ' + \
            f'destination: {self.destination}, ' + \
            f'pilot_id: {self.pilot_id})'
    

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column( Integer(), primary_key = True )
    passenger_id = Column( Integer(), ForeignKey('passengers.id') )
    flight_id = Column( Integer(), ForeignKey('flights.id') )
    seat_number = Column( Integer() )

    # passenger <-- usable property, backref from Passenger
    # flight <-- usable property, backref from Flight

    @property #returns the string-formatted boarding ticket with all reservation information
    def ticket(self):
        origin_airport = self.flight.origin
        origin_city = airport_dict[1][origin_airport]
        destination_airport = self.flight.destination
        destination_city = airport_dict[1][destination_airport]
        passenger_name = f"{self.passenger.first_name.capitalize()} {self.passenger.last_name.capitalize()}"
        seat_number = self.seat_number
        
        return (f"""
     ___________________________________
    |   // FLATLINES  
    |
    |      {passenger_name} 
    |      Seat: {f"{seat_number:02}"}                     
    |   {origin_city} ({origin_airport}) -->
    |   {destination_city} ({destination_airport})
    |___________________________________   

    """)

    def __repr__( self ):
        return f'(id: {self.id}, ' + \
            f'passenger_id: {self.passenger_id}, ' + \
            f'flight_id: {self.flight_id}, ' + \
            f'seat_number: {self.seat_number})'
    
class Pilot(Base):
    __tablename__ = 'pilots'

    id = Column(Integer, primary_key = True)
    first_name = Column(String(), )
    last_name = Column(String(), )

    flights = relationship('Flight', backref= 'pilot')

    @classmethod
    def ids(cls):
        id_list = session.query(Pilot.id).all()[0]
        return id_list
    
    def __repr__(self): 
        return f'<Pilot id: {self.id}, ' + \
            f'first_name: {self.first_name}, '+ \
            f'last_name: {self.last_name}, ' + \
            f'flights: {self.flights}>'
    





