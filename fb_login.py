import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import requests
import urllib3


def scroll_down():
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")
    count = 0
    while True:
        count = count + 1
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(8)
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print(count)





username = "9733940623"
password = "P@p@y9733940623"
options = Options()
options.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(options = options)
driver.get("https://www.facebook.com")
user = driver.find_element_by_id("email")
user.send_keys(username)
passw = driver.find_element_by_id("pass")
passw.send_keys(password)
passw.send_keys(Keys.RETURN)
time.sleep(5)
# Switch to the new window
#driver.switch_to.window(driver.window_handles[1])
file = pd.read_csv('profile_csv.csv')
profile_link = file['Profilelink']
y = 0



for x in profile_link :
    y = y+1
    '''driver.execute_script("window.open('');")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[y])'''
    m = driver.get(x)
    print(x)
    time.sleep(3)
    scroll_down()
    post_details = driver.find_element_by_id('timeline_story_column').text
    #print(post_details)
    with open('post_details['+y+'].txt', 'w', encoding='utf-8') as f :
        f.write(post_details)













