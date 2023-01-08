from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *


def calc(arg):
    return str(log(abs(12*sin(int(arg)))))


link = 'https://suninjuly.github.io/math.html'

browser = webdriver.Chrome()

try:
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(calc(x))

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    robot_checkbox.click()

    robot_radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    robot_radio.click()

    submit_button = browser.find_element(By.CLASS_NAME, 'btn-default')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()