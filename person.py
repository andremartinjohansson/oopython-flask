#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Person Module """
class Person():
    """ Person Class """

    def __init__(self):
        self.firstname = "André"
        self.lastname = "Johansson"
        self.my_age = "22"
        self.my_address = "Fridhemsgatan 24"

    def name(self):
        """ Return full name """
        return "{firstname} {lastname}".format(firstname=self.firstname, lastname=self.lastname)

    def age(self):
        """ Return age """
        return "{age} år".format(age=self.my_age)

    def address(self):
        """ Return address """
        return "{address} i Karlshamn".format(address=self.my_address)
