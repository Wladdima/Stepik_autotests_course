import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from math import *


def calc():
    return str(log(int(time.time())))


@pytest.fixture
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


@pytest.fixture()
def log_in(browser):
    login_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, 'ember33'))
    )
    login_button.click()

    email = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, 'id_login_email'))
    )
    email.send_keys('wladdima.wladimir@gmail.com')

    password = browser.find_element(By.ID, 'id_login_password')
    password.send_keys('L09d101999')
    print('LOG IN IS SUCCESSFUL')


@pytest.mark.parametrize('address', ["236895", "236896"])
def test_guest_should_see_login_link(browser, log_in, address):
    link = f"https://stepik.org/lesson/{address}/step/1"
    browser.get(link)
    time.sleep(5)
    print(f"TEST {address} OK")

#, "236897", "236898", "236899", "236903", "236904", "236905"
