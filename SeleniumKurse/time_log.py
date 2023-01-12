import time
from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.google.com/')
search = browser.find_element(By.CLASS_NAME, 'gLFyf')
time.sleep(5)
search.send_keys(log(int(time.time())))
time.sleep(5)

