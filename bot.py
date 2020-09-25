from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time
import configparser

"""
bot class
can login to an account
can follow/unfollow
like, post, comment
"""
class bot:

    """
    constructor with username and password
    username : username for the account
    password: password for the account

    using selenium.webdriver.Chrome
    """
    def __init__(self, username, password):


        #trying different load options for off-tab bot run
        #self.driver = webdriver.Chrome("./chromedriver")
        self.options = Options()
        self.options.page_load_strategy = 'none'
        self.driver = webdriver.Chrome(executable_path="./chromedriver",options=self.options)
        self.username = username
        self.password = password
        self.url = "https://instagram.com"

        self.login()

    """
    request instagram and login to the account
    """
    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.url))
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()



        # from selenium.webdriver.common.by import By
        # from selenium.webdriver.support.ui import WebDriverWait
        # from selenium.webdriver.support import expected_conditions
        #
        #
        # enter_username = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        # enter_username.send_keys(self.username)
        # enter_password = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        # enter_password.send_keys(self.password)

    """
    gets the instagram site for the given username
    """
    def nav_user_profile(self, user):
        self.driver.get("{}/{}/".format(self.url, user))

    """
    follows the given username by default
    unfollows given username if specified true
    """
    def user_follow_action(self, user, unfollow=False):
        #button_text = "Following" if unfollow else "Follow"
        self.nav_user_profile(user)
        time.sleep(2)
        if (unfollow):
            self.driver.find_elements_by_xpath("//span[@aria-label='Following']")[0].click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
        else:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()

        #self.driver.find_element_by_xpath("//button[contains(text(), {})]".format(button_text)).click()


    # def follow_user(self, user):
    #     self.nav_user_profile(user)
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]").click()



    """
    follows a large number of unfollowed "friends of friends"
    the specific number to follow is given
    """
    def mass_follow(self, to_follow):
        #self.nav_user_profile(self.username)
        self.driver.get("{}/{}/{}/".format(self.url, user, "followers"))
        time.sleep(2)
        #self.driver.find_element_by_xpath("//span[contains(text(), 'followers')]").click()


    """
    get all the followers of the user
    returns map of lists of the followers
    """
    def get_followers(self):
        #self.driver.get("{}/{}/{}/".format(self.url, self.username, "followers"))
        self.nav_user_profile(self.username)
        time.sleep(2)
        expected_follower_count = int(self.driver.find_element_by_xpath("//a[text()[contains(.,'followers')]]/span").text)
        self.driver.find_element_by_xpath("//a[text()[contains(.,'followers')]]").click()
        time.sleep(2)

        #popup with follower list
        list_box = self.driver.find_element_by_xpath("//h1[contains(text(), 'Followers')]/../../../div[2]")

        #load all the followers
        scroll_height = 0
        curr_height = 1

        while True:
            #loop manager
            if (scroll_height == curr_height and
                len(list_box.find_elements_by_tag_name('li')) >= expected_follower_count):
                break;

            scroll_height = curr_height
            curr_height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
            """, list_box)
            time.sleep(3)
            print("sh: %d\nch: %d" % (scroll_height, curr_height))


        #sort followers by those that are followed back and thsoe that aren't
        #make map with three keys: following, follow, requested, Verified
        #values are lists of followers
        map = {
            "Following" : [],
            "Follow" : [],
            "Requested" : [],
            "Verified": []
        }

        followers = [li for li in list_box.find_elements_by_tag_name('li') if li!='' and li.text!='']
        print(len(followers))

        #extract username, name, and follow status from list item
        for f in followers:
            #print(f.text + "\n\n\n")
            info = f.text.split("\n")
            key = info[-1]
            map[key].append(info[0])

            #check for verification
            if (len(info)==4):
                map["Verified"].append(info[0])


        print(map)

        return map


    """
    get all the users this bot is following
    returns map of lists of the followers
    """
    def get_following(self):
        #self.driver.get("{}/{}/{}/".format(self.url, self.username, "followers"))
        self.nav_user_profile(self.username)
        time.sleep(2)
        expected_following_count = int(self.driver.find_element_by_xpath("//a[text()[contains(.,'following')]]/span").text)
        print(expected_following_count)
        self.driver.find_element_by_xpath("//a[text()[contains(.,'following')]]").click()
        time.sleep(2)

        #popup with follower list
        list_box = self.driver.find_element_by_xpath("//h1[contains(text(), 'Following')]/../../../div[2]")

        #load all the followers
        scroll_height = 0
        curr_height = 1

        while True:
            #loop manager
            if (scroll_height == curr_height and
                len(list_box.find_elements_by_tag_name('li')) >= expected_following_count):
                break;

            scroll_height = curr_height
            curr_height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
            """, list_box)
            time.sleep(3)
            #print("sh: %d\nch: %d" % (scroll_height, curr_height))


        #sort followers by those that are followed back and thsoe that aren't
        #make map with three keys: following, follow, requested, Verified
        #values are lists of followers
        map = {
            "Following" : [],
            "Verified": []
        }

        following = [li for li in list_box.find_elements_by_tag_name('li') if li!='' and li.text!='']
        #print(len(following))

        #extract username, name, and follow status from list item
        for f in following:
            #print(f.text + "\n\n\n")
            info = f.text.split("\n")
            key = info[-1]
            map[key].append(info[0])

            #check for verification
            if (len(info)==4):
                map["Verified"].append(info[0])


        #print(map)

        return map








###TESTING
if __name__ == '__main__':
    parser = configparser.ConfigParser()
    parser.read("./../config.ini")
    bot = bot(parser["Default"]["username"], parser["Default"]["password"])
    time.sleep(2)
    bot.get_following()
    #bot = bot('username', 'password')
    #bot.follow_user("jared9anderson")
    #bot.user_follow_action("masuee.art", True)
