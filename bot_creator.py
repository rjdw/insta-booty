from selenium import webdriver
import os, time
import configparser
from random import randrange

#creates new bot accounts
#stores username and password in config.ini
class bot_creator:

    #__init__
    def __init__(self):
        print("init")
        # self.driver = webdriver.Chrome("./chromedriver")
        # self.url = "https://www.instagram.com/accounts/emailsignup/"



    """
    makes a username from a random first and last name and 5 digits
    returns string
    """
    def _create_username(self):
        first = randrange(1001)
        firstname = [line for i, line in enumerate(open("./util/firstname.txt")) if i == first][0].strip().lower()
        last = randrange(1001)
        lastname = [line for i, line in enumerate(open("./util/firstname.txt")) if i == last][0].strip().lower()

        number = ""
        for i in range(5):
            number += str(randrange(10))

        return firstname + lastname + number

    """
    makes a password according to gmail and instagram requirements
    Instagram: combination of six or more letters, numbers and punctuation marks
    Gmail: Must be a minimum of 8 characters.
            Require a number in the password.
            Require a capital letter in the password.
            Require a lower case letter in the password.
            Require a password that does not match username.
            Suggested that you use one special character (ie: #, $, %)
    returns string
    """
    def _create_password(self):






if __name__ == '__main__':
    b = bot_creator()
