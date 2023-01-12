import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    print('\nopen browser for tests..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()
