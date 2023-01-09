from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()


def browser_test(link):
    browser.get(link)

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

    browser.quit()
    return welcome_text


class TestUniqueSelector(unittest.TestCase):

    def test_congrats_page1(self):
        self.assertEqual('Congratulations! You have successfully registered!',
                         browser_test('http://suninjuly.github.io/registration1.html'), 'Registration failed')

    def test_congrats_page2(self):
        self.assertEqual('Congratulations! You have successfully registered!',
                         browser_test('http://suninjuly.github.io/registration2.html'), 'Registration failed')


if __name__ == "__main__":
    unittest.main()



