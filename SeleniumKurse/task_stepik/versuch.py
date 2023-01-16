import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time
from math import *


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(chrome_options=chrome_options)


email = 'wladdima.wladimir@gmail.com'
password = 'L09d101999'


def log_in(login, passwort):
    login_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, 'ember33'))
    )
    login_button.click()

    email_field = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, 'id_login_email'))
    )
    email_field.send_keys(login)

    password_field = browser.find_element(By.ID, 'id_login_password')
    password_field.send_keys(passwort)

    submit_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'sign-form__btn'))
    )
    submit_button.click()

    print('LOG IN IS SUCCESSFUL')


def logged_in_check():
    try:
        WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.navbar__profile-toggler'))
        )
    except NoSuchElementException:
        return False


def calc():
    return str(log(int(time.time())))


@pytest.mark.parametrize('address', ["236895", "236896"])
def test_text_correct(address):
    browser.get(f"https://stepik.org/lesson/{address}/step/1")
    time.sleep(5)
    print(f'browser {address} is opened')

    avatar_profile = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.navbar__profile-toggler'))
    )

    if not logged_in_check():

        print('НУЖНО ЛОГИНИТЬСЯ')

        log_in(email, password)

        print('НАЧИНАЮ ТЕСТ')
        answer_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ember-text-area'))
        )
        print('ПОЛЕ НАШЕЛ!')
        calc_answer = calc()

        again_button = browser.find_element(By.CSS_SELECTOR, 'again-btn')
        if again_button.is_enabled():
            again_button.click()
        else:
            answer_field.send_keys(calc_answer)
            time.sleep(3)
            submit_button = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'submit-submission'))
            )
            submit_button.click()
            time.sleep(3)
            print("ПО КНОПКЕ КЛИКНУЛ")
            correct_text = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'lesson__hint > p'))
            ).text
            assert 'Correct!' == correct_text, 'TEXT IS NOT CORRECT'
            print('Text is correct!')

"""
, "236897", "236898", "236899", "236903", "236904",
                                     "236905"
class TestStepikAuto:
    def test_send_answer(self, browser, log_in):
        print('НАЧИНАЮ ТЕСТ')
        submit_button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'sign-form__btn'))
        )
        submit_button.click()

        answer_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'ember94'))
        )

        #answer_field.click()

        print('ВСЕ ОК, ШЛЮ ОТВЕТ')

        #time.sleep(10)

        function_answer = calc()
        answer_field.send_keys(function_answer)

        send_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
        )
        send_button.click()

        correct_text = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.lesson__hint > p'))
        ).text

        assert 'Correct!' == correct_text, 'Text is not correct'

        print("TEXT IS CORRECT")

        #time.sleep(5)

"""