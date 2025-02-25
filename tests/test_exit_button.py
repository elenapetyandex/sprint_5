
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators import Locators
from data import Data


class TestExitButton:

    def test_click_exit_button_go_to_logout_profile(self, driver):
        buttons = driver.find_element(*Locators.homepage_buttons)
        buttons[0].click()
        elements = driver.find_elements(*Locators.login_input)
        for element in elements:
            element.clear()

        elements[0].send_keys(Data.reg_email)

        elements[1].send_keys(Data.reg_password)

        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.lk_button).click()

        driver.find_element(*Locators.exit_button).click()

        driver.find_element(*Locators.lk_button).click()
        WebDriverWait(driver, 3)
        assert driver.current_url == Data.URL_login
