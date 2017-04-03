#!/usr/bin/env python3

""" Classes """

from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Humans(Base):
    """ Humans Class """
    __tablename__ = "humans"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    occupation = Column(String)
    age = Column(Integer)

    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age

    def __str__(self):
        return "{n}, {o}, {a}".format(n=self.name, o=self.occupation, a=self.age)

class Animals(Base):
    """ Animals Class """
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    species = Column(String)
    name = Column(String)
    nr_of_legs = Column(Integer)

    def __init__(self, species, name, nr_of_legs):
        self.species = species
        self.name = name
        self.nr_of_legs = nr_of_legs

class Vehicles(Base):
    """ Vehicles Class """
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    vehicle_type = Column(String)
    price = Column(Float)

    def __init__(self, vehicle_type, price):
        self.vehicle_type = vehicle_type
        self.price = price
