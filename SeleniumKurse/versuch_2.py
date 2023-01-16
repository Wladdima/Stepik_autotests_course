from math import *

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Chrome()

email = 'wladdima.wladimir@gmail.com'
password = 'L09d101999'


def logged_in_check():
    try:
        avatar_profile = browser.find_element(By.CSS_SELECTOR, 'button.navbar__profile-toggler')
        return True
    except NoSuchElementException:
        return False


def calc():
    return str(log(int(time.time())))


def again_button_check():
    flag = True
    try:
        browser.find_element(By.CSS_SELECTOR, '.again-btn')
    except NoSuchElementException:
        flag = False

    return flag


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


@pytest.mark.parametrize('address', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_correct_answer(address):
    browser.get(f'https://stepik.org/lesson/{address}/step/1')
    time.sleep(3)

    print(f'\nbrowser {address} is opened')

    if not logged_in_check():
        log_in(email, password)
        time.sleep(3)
        calc_answer = calc()

        if not again_button_check():
            print('\nThere is no again button')
            time.sleep(3)
            answer_field = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ember-text-area'))
            )
            answer_field.send_keys(calc_answer)
            time.sleep(3)
            submit_button = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'submit-submission'))
            )
            submit_button.click()
            time.sleep(3)
            print("\nПО КНОПКЕ КЛИКНУЛ")
            correct_text = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'lesson__hint > p'))
            ).text
            assert 'Correct!' == correct_text, 'TEXT IS NOT CORRECT'
            print('\nText is correct!')

        elif again_button_check():
            print('\nThere is an again button')
            again_button = browser.find_element(By.CSS_SELECTOR, '.again-btn')
            time.sleep(3)
            again_button.click()
            time.sleep(3)
            print('\nКНОПКУ НАШЕЛ И КЛИКНУЛ')
            answer_field = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ember-text-area'))
            )
            answer_field.send_keys(calc_answer)
            time.sleep(3)
            submit_button = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'submit-submission'))
            )
            submit_button.click()
            time.sleep(3)
            print("\nПО КНОПКЕ КЛИКНУЛ")
            correct_text = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'lesson__hint > p'))
            ).text
            assert 'Correct!' == correct_text, 'TEXT IS NOT CORRECT'
            print('\nText is correct!')

    if logged_in_check():
        calc_answer = calc()

        if not again_button_check():
            print('\nThere is no again button')
            time.sleep(3)
            answer_field = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ember-text-area'))
            )
            answer_field.send_keys(calc_answer)
            time.sleep(3)
            submit_button = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'submit-submission'))
            )
            submit_button.click()
            time.sleep(3)
            print("\nПО КНОПКЕ КЛИКНУЛ")
            correct_text = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'lesson__hint > p'))
            ).text
            assert 'Correct!' == correct_text, 'TEXT IS NOT CORRECT'
            print('\nText is correct!')

        elif again_button_check():
            print('\nThere is an again button')
            again_button = browser.find_element(By.CSS_SELECTOR, '.again-btn')
            time.sleep(3)
            again_button.click()
            time.sleep(3)
            print('\nКНОПКУ НАШЕЛ И КЛИКНУЛ')
            answer_field = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ember-text-area'))
            )
            answer_field.send_keys(calc_answer)
            time.sleep(3)
            submit_button = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'submit-submission'))
            )
            submit_button.click()
            time.sleep(3)
            print("\nПО КНОПКЕ КЛИКНУЛ")
            correct_text = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'lesson__hint > p'))
            ).text
            assert 'Correct!' == correct_text, 'TEXT IS NOT CORRECT'
            print('\nText is correct!')
