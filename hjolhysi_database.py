import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#Base
Base = declarative_base()

class Hobby_flokkar(Base):
    __tablename__ = 'hobby_flokkar'
    id = Column(Integer, primary_key=True)
    nafn = Column(String(250), nullable=False)

class Hobby_hjolhysi(Base):
    __tablename__= 'hobby_hjolhysi'
    id = Column(Integer, primary_key=True)
    nafn = Column(String(250), nullable=False)
    verð = Column(Integer, nullable=False)
    flokkur_id = Column(Integer, ForeignKey('hobby_flokkar.id'))
    flokkur = relationship(Hobby_flokkar)

class Aukahlutir(Base):
    __tablename__ = 'aukahlutir'
    id = Column(Integer, primary_key=True)
    lysing = Column(String(500), nullable=False)
    verð = Column(Integer, nullable=False)
    tegund = Column(String(250), nullable=False)

class Hjolhysi_aukahlutir(Base):
    __tablename__ = 'hjolhysi_aukahlutir'
    id = Column(Integer, primary_key=True)
    hjolhysi_id = Column(Integer, ForeignKey('hobby_hjolhysi.id'))
    chassis = Column(String(50), nullable=False)
    load_capacity = Column(String(50), nullable=False)
    wheel_rims = Column(String(50), nullable=False)
    window = Column(String(50), nullable=False)
    body = Column(String(50), nullable=False)
    living_area = Column(String(50), nullable=False)
    upholstery_combinations = Column(String(50), nullable=False)
    kitchen = Column(String(50), nullable=False)
    sleeping_area = Column(String(50), nullable=False)
    washroom = Column(String(50), nullable=False)
    water_gas_electricity = Column(String(50), nullable=False)
    lighting = Column(String(50), nullable=False)
    heating_air_condition = Column(String(50), nullable=False)
    multimedia = Column(String(50), nullable=False)
    country_specs = Column(String(50), nullable=False)
    hjolhysi = relationship(Hobby_hjolhysi)
    

#TO Do CRUD vinnsla og módel fyrir vv



# Create an engine that stores data in the local directory's
engine = create_engine('sqlite:///hobby_hjolhysi.db')

# Create all tables in the engine: "Create Table" statements in raw SQL.
Base.metadata.create_all(engine)

