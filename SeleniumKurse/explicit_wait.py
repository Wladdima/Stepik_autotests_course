from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from math import *

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()


def calc(arg):
    return str(log(abs(12*sin(arg))))


try:
    browser.get(link)

    button_book = browser.find_element(By.ID, 'book')
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    button_book.click()

    x = browser.find_element(By.ID, 'input_value').text

    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(calc(int(x)))

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
