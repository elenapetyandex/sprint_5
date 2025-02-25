from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import locator_list
from test_login import login


class TestGoToConstructor:

    def test_click_constructor_in_profile_page_go_to_homepage(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        homepage_buttons[0].click()

        login(driver)

        lk_button.click()

        constructor.click()
        WebDriverWait(driver, 3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_click_logo_in_profile_page_go_to_homepage(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        homepage_buttons[0].click()
        login(driver)
        lk_button.click()
        logo.click()
        WebDriverWait(driver, 3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

