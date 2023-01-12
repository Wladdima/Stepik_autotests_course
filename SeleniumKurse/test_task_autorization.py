import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from math import *

link = 'https://stepik.org/lesson/236895/step/1'


def calc():
    return log(int(time.time()))


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser


@pytest.fixture(scope='function')
def log_in(browser):
    browser.get(link)
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


class TestStepikAuto:

    def test_send_answer(self, browser):

        submit_button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'sign-form__btn'))
        )
        submit_button.click()

        answer_field = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, 'ember94'))
        )

        print('ВСЕ ОК, ШЛЮ ОТВЕТ')

        answer_field.send_keys(log(int(time.time())))

        #send_button = WebDriverWait(browser, 5).until(
        #    EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
        #)
        #send_button.click()


       # correct_text = WebDriverWait(browser, 5).until(
       #     EC.element_to_be_clickable((By.ID, 'ember94'))
        #)


        #assert 'Correct!' == correct_text, 'Text is not correct'
