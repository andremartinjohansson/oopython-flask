#!/usr/bin/env python3

""" Functions module """

from flask import request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from farm import Humans, Animals, Vehicles

engine = create_engine("sqlite:///db/farm.sqlite")

Session = sessionmaker(bind=engine)
session = Session()

def do_humans_table():
    """ Create humans table """
    humans_table = ""
    all_humans = session.query(Humans).all()
    for human in all_humans:
        humans_table += """<tr><td>{id}</td>
        <td>{name}</td>
        <td>{occupation}</td>
        <td>{age}</td>
        <td><a href='?del={id}'>Ta bort</a></td></tr>""".format(id=human.id, \
        name=human.name, occupation=human.occupation, age=human.age)
    return humans_table

def do_animals_table():
    """ Create animals table """
    animals_table = ""
    all_animals = session.query(Animals).all()
    for animal in all_animals:
        animals_table += """<tr><td>{id}</td>
        <td>{species}</td>
        <td>{name}</td>
        <td>{nr_of_legs}</td>
        <td><a href='?del={id}'>Ta bort</a></td></tr>""".format(id=animal.id, \
        species=animal.species, name=animal.name, nr_of_legs=animal.nr_of_legs)
    return animals_table

def do_vehicles_table():
    """ Create vehicles table """
    vehicles_table = ""
    all_vehicles = session.query(Vehicles).all()
    for vehicle in all_vehicles:
        vehicles_table += """<tr><td>{id}</td>
        <td>{vehicle_type}</td>
        <td>{price}</td>
        <td><a href='?del={id}'>Ta bort</a></td></tr>""".format(id=vehicle.id, \
        vehicle_type=vehicle.vehicle_type, price=vehicle.price)
    return vehicles_table

def remove_human(del_this_human):
    """ Remove a human """
    session.query(Humans).filter(Humans.id == del_this_human).delete()
    session.commit()

def remove_animal(del_this_animal):
    """ Remove an animal """
    session.query(Animals).filter(Animals.id == del_this_animal).delete()
    session.commit()

def remove_vehicle(del_this_vehicle):
    """ Remove a vehicle """
    session.query(Vehicles).filter(Vehicles.id == del_this_vehicle).delete()
    session.commit()

def add_human():
    """ Add a human """
    new_human = Humans(name=request.form["name"], occupation=request.form["occupation"], \
    age=request.form["age"])

    session.add(new_human)
    session.commit()

def add_animal():
    """ Add an animal """
    new_animal = Animals(species=request.form["species"], name=request.form["name"], \
    nr_of_legs=request.form["nr_of_legs"])

    session.add(new_animal)
    session.commit()

def add_vehicle():
    """ Add a vehicle """
    new_vehicle = Vehicles(vehicle_type=request.form["vehicle_type"], price=request.form["price"])

    session.add(new_vehicle)
    session.commit()
