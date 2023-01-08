from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *


def calc(arg):
    return str(log(abs(12*sin(int(arg)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    chest = browser.find_element(By.ID, 'treasure')
    x = chest.get_attribute('valuex')

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(calc(x))

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()

    submit_button = browser.find_element(By.CLASS_NAME, 'btn-default')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
