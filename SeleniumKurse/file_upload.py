import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
text = 'test'

with open("test_file.txt", "w") as file:
    file.write("test test test test")

current_directory = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_directory, 'test_file.txt')

try:
    browser.get(link)

    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys(text)

    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys(text)

    email = browser.find_element(By.NAME, 'email')
    email.send_keys(text)

    select_file = browser.find_element(By.ID, 'file')
    select_file.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
