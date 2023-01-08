from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

link = 'http://SunInJuly.github.io/execute_script.html'

browser = webdriver.Chrome()


def calc(arg):
    return str(log(abs(12 * sin(int(arg)))))


try:
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text

    answer_field = browser.find_element(By.ID, 'answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', answer_field)
    answer_field.send_keys(calc(x))

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    robot_checkbox.click()

    robot_ratio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    robot_ratio.click()

    select_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    select_button.click()

finally:
    time.sleep(5)
    browser.quit()
