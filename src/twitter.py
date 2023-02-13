import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/vagrant/.config/google-chrome/Default')
driver = webdriver.Chrome('/home/vagrant/lib/chromedriver', options=options) 
driver.get('https://www.google.co.jp')
driver.get('https://www.google.co.jp')
 
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")
search_bar.submit()
