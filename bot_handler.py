from selenium import webdriver
import os, time
import configparser

"""
handles mass bot action
bots is a list of bots to be handled
"""
class bot_handler:
    def __init__ (self, bots):
        self.driver = webdriver.Chrome("./chromedriver")
        self.bots = bots
