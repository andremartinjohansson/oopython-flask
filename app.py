#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template, request, flash
from person import Person
from data import Data
import functions as func
import os, time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from farm import Humans, Animals, Vehicles

engine = create_engine("sqlite:///db/farm.sqlite")

Session = sessionmaker(bind=engine)
session = Session()

random_key_string = os.urandom(12)

app = Flask(__name__)
app.secret_key = random_key_string

# Make it easier to debug
app.debug = True
app.config.update(
    PROPAGATE_EXCEPTIONS=True
)

date = time.strftime("%d/%m/%Y")

my = Person()

my_name = my.name()
my_age = my.age()
my_address = my.address()

data = Data()

url_main = data.link_main()
url_about = data.link_about()
url_report = data.link_report()
url_farm = data.link_farm()

img_src = data.image()
elite_favicon = data.favicon()

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html", title=data.title("/"), main=url_main, \
    about=url_about, report=url_report, farm=url_farm, image=img_src, favicon=elite_favicon, \
    date=date)

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html", title=data.title("/about"), name=my_name, \
    age=my_age, address=my_address, main=url_main, about=url_about, report=url_report, \
    image=img_src, favicon=elite_favicon, farm=url_farm, date=date)

@app.route("/report")
def report():
    """ Report route """
    return render_template("redovisning.html", title=data.title("/report"), main=url_main, \
    about=url_about, report=url_report, farm=url_farm, image=img_src, favicon=elite_favicon, \
    date=date)

@app.route("/farm")
def farm():
    """ Farm route """
    return render_template("farm.html", title=data.title("/farm"), main=url_main, \
    about=url_about, report=url_report, farm=url_farm, image=img_src, favicon=elite_favicon, \
    date=date)

@app.route("/humans", methods=["POST", "GET"])
def show_human():
    """ Handle GET and POST """
    if request.method == "POST":
        func.add_human()
        flash('You successfully added a human', 'success')
    if request.method == "GET":
        del_this_human = request.args.get("del")
        if del_this_human != None:
            func.remove_human(del_this_human)
            flash('You successfully removed a human', 'success')
    return render_template("humans.html", title=data.title("/humans"), main=url_main, \
    about=url_about, report=url_report, farm=url_farm, image=img_src, favicon=elite_favicon, \
    humans_table=func.do_humans_table(), date=date)
def humans():
    """ Humans route """
    return render_template("humans.html", title=data.title("/humans"), main=url_main, \
    about=url_about, report=url_report, farm=url_farm, image=img_src, favicon=elite_favicon, \
    humans_table=func.do_humans_table(), date=date)

@app.route("/animals", methods=["POST", "GET"])
def show_animal():
    """ Handle GET and POST """
    if request.method == "POST":
        func.add_animal()
        flash('You successfully added an animal', 'success')
    if request.method == "GET":
        del_this_animal = request.args.get("del")
        if del_this_animal != None:
            func.remove_animal(del_this_animal)
            flash('You successfully removed an animal', 'success')
    return render_template("animals.html", title=data.title("/animals"), main=url_main, \
    about=url_about, report=url_report, farm=url_farm, image=img_src, favicon=elite_favicon, \
    animals_table=func.do_animals_table(), date=date)
def animals():
    """ Animals route """
    return render_template("animals.html", title=data.title("/animals"), main=url_main, \
    about=url_about, report=url_report, farm=url_farm, image=img_src, favicon=elite_favicon, \
    animals_table=func.do_animals_table(), date=date)

@app.route("/vehicles", methods=["POST", "GET"])
def show_vehicle():
    """ Handle GET and POST """
    if request.method == "POST":
        func.add_vehicle()
        flash('You successfully added a vehicle', 'success')
    if request.method == "GET":
        del_this_vehicle = request.args.get("del")
        if del_this_vehicle != None:
            func.remove_vehicle(del_this_vehicle)
            flash('You successfully removed a vehicle', 'success')
    return render_template("vehicles.html", title=data.title("/vehicles"), main=url_main, \
    about=url_about, report=url_report, farm=url_farm, image=img_src, favicon=elite_favicon, \
    vehicles_table=func.do_vehicles_table(), date=date)
def vehicles():
    """ Vehicles route """
    return render_template("vehicles.html", title=data.title("/vehicles"), main=url_main, \
    about=url_about, report=url_report, farm=url_farm, image=img_src, favicon=elite_favicon, \
    vehicles_table=func.do_vehicles_table(), date=date)

if __name__ == "__main__":
    app.run()
