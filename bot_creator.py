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
        # self.insta = "https://www.instagram.com/accounts/emailsignup/"
        # self.gmail = "https://accounts.google.com/signup"



    """
    makes a username from a random first and last name and 5 digits
    returns string
    """
    def _create_username(self):
        first = randrange(1001)
        firstname = [line for i, line in enumerate(open("./util/firstname.txt")) if i == first][0].strip().lower()
        last = randrange(1001)
        lastname = [line for i, line in enumerate(open("./util/lastname.txt")) if i == last][0].strip().lower()

        number = ""
        for i in range(5):
            number += str(randrange(10))

        return firstname + lastname + number

    """
    makes a password according to gmail and instagram requirements
    for secure password would use secrets module
    this is very basic, don't care too much about the passwords
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
        res = "!@"
        for i in range(4):
            res += chr(randrange(65,91))
            res += chr(randrange(97,123))
            res += chr(randrange(48,58))

        return res


    """
    closes the brower
    """
    def close(self):
        self.driver.close()


if __name__ == '__main__':
    b = bot_creator()
