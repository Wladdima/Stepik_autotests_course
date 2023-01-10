from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link = 'http://suninjuly.github.io/registration1.html'
browser = webdriver.Chrome()


class TestUniqueSelector(unittest.TestCase):

    def test_congrats_page1(self):
        browser.get('http://suninjuly.github.io/registration2.html')

        first_name = browser.find_element(By.CLASS_NAME, 'first:required')
        first_name.send_keys('test')
        last_name = browser.find_element(By.CLASS_NAME, 'second:required')
        last_name.send_keys('test')
        email = browser.find_element(By.CLASS_NAME, 'third:required')
        email.send_keys('test')

        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        time.sleep(5)
        browser.quit()

        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!')