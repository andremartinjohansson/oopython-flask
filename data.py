#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Data Module """
class Data():
    """ Data Class """

    def __init__(self):
        self.url_main = "app.cgi/"
        self.url_about = "about"
        self.url_report = "report"
        self.url_farm = "farm"
        self.page_title = ""
        self.img_me = "static/images/IMG_20161128_115812.jpg"
        self.favicon_elite = "static/images/favicon.png"

    def link_main(self):
        """ Return link to home page """
        return self.url_main

    def link_about(self):
        """ Return link to about page """
        return self.url_about

    def link_report(self):
        """ Return link to report page """
        return self.url_report

    def link_farm(self):
        """ Return link to report page """
        return self.url_farm

    def title(self, url):
        """ Generate page title and return it """
        if url == "/":
            self.page_title = "Hem"
        elif url == "/about":
            self.page_title = "Om mig"
        elif url == "/report":
            self.page_title = "Redovisningar"
        elif url == "/farm":
            self.page_title = "Bondgård"
        elif url == "/humans":
            self.page_title = "Humans"
        elif url == "/animals":
            self.page_title = "Animals"
        elif url == "/vehicles":
            self.page_title = "Vehicles"
        else:
            self.page_title = "Error"
        return self.page_title

    def image(self):
        """ Return image link """
        return self.img_me

    def favicon(self):
        """ Return favicon link """
        return self.favicon_elite
