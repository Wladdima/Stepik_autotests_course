from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()

def calc(arg):
    return str(log(abs(12*sin(arg))))

try:
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(calc(int(x)))

    submit_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
