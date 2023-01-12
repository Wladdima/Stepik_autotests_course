import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


class TestMainPage:
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')

    @pytest.mark.xfail
    def test_guest_should_see_search_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'input.btn.btn-default')

    

