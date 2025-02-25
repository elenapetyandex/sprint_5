from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from test_login import login
import  locator_list


class TestExitButton:

    def test_click_exit_button_go_to_logout_profile(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')

        homepage_buttons[0].click()
        login(driver)
        lk_button.click()

        exit_button.click()

        lk_button.click()
        WebDriverWait(driver, 3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
