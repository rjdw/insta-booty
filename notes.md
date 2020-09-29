# 09/17/20

source python3env/bin/activate ---to activate the virtualenv

selenium should already be installed as dependency in this virtualenv

if not then u prob forgot activate

install chromedriver for the version of chrome that you are using

for mac:

move the unzipped binary to /usr/local/bin

for windows:

move the unzipped binary to project folder

change to `self.driver = webdriver.Chrome("binary file name")`


storing bot account usernames and passwords in config.ini file


temp mail site
https://temp-mail.org/en/

# 09/18/20

moved chromedriver to project folder

using `self.driver = webdriver.Chrome("binary file name")` instead

this always for headless chromedriver implementation later

using chrome version 84.0.4147.89 (Official Build) (64-bit)

chromedriver exe is for this chrome version

**DO NOT REPLACE chromedriver version with ur own chrome version unless discussed plz**


# 09/19/20

finished follow/unfollow functionalities

working on bot_creator

temp-mail.org does not work with instagram

need gmail or some official email to not trigger instagram bot detection

# 09/21/20

feature to add: follow a bunch of people, wait for follow backs and unfollow after

need to work on gmail creation bot

can use same password for gmail account as the instagram accounts

try to make as many as possible and if ip banned from making more then start to

look into using a proxy

# 09/22/20

think about how to collect the followers and following of each account   
what data structure that sorts and divides the following that are not following back    
how to store the follower/following interaction after bot instance dies    
temporary .ini file?

# 09/23/20

collected a user's followers and sorted into map with four categories   
**ISSUE: the page does not load unless the user in actively on the chrome page**   
issue might be solvable using [chromedriver load strategy options](https://stackoverflow.com/questions/42397043/how-to-not-wait-for-page-load-to-complete-in-selenium-by-using-chromedriver-mo)   


# 09/24/20

get_followers in bot.py might not work for users with a large amount of followers, enough for instagram to have letter postfix (e.g. 1.6M)   
might run the creation bot through tor or some vpn, look for something with a good api   
mb have to change language and browser, can run tor on chrome from extension though    
not too sure about running selenium on the tor browser itself

# 09/28/20

most likely using tor browser for gmail creation
