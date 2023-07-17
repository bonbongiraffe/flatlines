from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column( Integer() , primary_key = True )
    first_name = Column( String() )
    last_name = Column( String() )

class Flight(Base):
    __tablename__ = 'flights'

    id = Column( Integer(), primary_key = True )
    origin = Column( String() )
    destination = Column( String() )

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column( Integer(), primary_key = True )
    passenger_id = Column( Integer(), ForeignKey('passengers.id') )
    flight_id = Column( Integer(), ForeignKey('flights.id') )

