from selenium import webdriver
import os, time
import configparser

#creates new bot accounts
#stores username and password in config.ini
class bot_creator:

    #__init__
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.url = "https://www.instagram.com/accounts/emailsignup/"
        self.email = 
