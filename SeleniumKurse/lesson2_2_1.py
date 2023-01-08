from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()


def summa(num1, num2):
    return num1+num2


try:
    browser.get(link)

    first_digit = int(browser.find_element(By.ID, 'num1').text)
    second_digit = int(browser.find_element(By.ID, 'num2').text)

    selected_element = summa(first_digit, second_digit)
    print(selected_element)

    list_select = Select(browser.find_element(By.ID, 'dropdown'))
    list_select.select_by_visible_text(str(selected_element))

    submit_button = browser.find_element(By.CLASS_NAME, 'btn-default')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()