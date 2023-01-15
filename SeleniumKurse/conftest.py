import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('address', ["236895", "236896", "236897", "236898", "236899", "236903", "236904",
                                         "236905"])
def test_open_browser(browser, address):
    browser.get(f"https://stepik.org/lesson/{address}/step/1")


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
