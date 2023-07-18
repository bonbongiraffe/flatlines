from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column( Integer() , primary_key = True )
    first_name = Column( String() )
    last_name = Column( String() )

    def __repr__( self ):
        return f'id: {self.id}, ' + \
            f'first_name: {self.first_name}, ' + \
            f'last_name: {self.last_name}' 

class Flight(Base):
    __tablename__ = 'flights'

    id = Column( Integer(), primary_key = True )
    origin = Column( String() )
    destination = Column( String() )

    def __repr__( self ):
        return f'id: {self.id}, ' + \
            f'origin: {self.origin}, ' + \
            f'destination: {self.destination}'

# generate twenty mvp flights:
# airport_dict = {"New York City": "JFK", "Chicago": "ORD", "Miami": "MIA", "Denver": "DEN", "Los Angeles": "LAX"}
# for origin in airport_dict:
#   for destination in airport_dict:
#       if destination != origin:
#           CREATE flight object with:
#           origin = airport_dict[origin]
#           destination = airport_dict[destination]      

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column( Integer(), primary_key = True )
    passenger_id = Column( Integer(), ForeignKey('passengers.id') )
    flight_id = Column( Integer(), ForeignKey('flights.id') )

    def __repr__( self ):
        return f'id: {self.id}, ' + \
            f'passenger_id: {self.passenger_id}, ' + \
            f'flight_id: {self.flight_id}'

