
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators import Locators
from data import Data


class GoToProfile:


    def test_input_registration_data_in_login_form_go_to_profile_page(self, driver):
        driver.find_element(*Locators.lk_button).click()
        login_input = driver.find_elements(*Locators.login_input) # login page form
        for element in login_input:
            element.clear()
        login_input[0].send_keys(Data.reg_email)
        login_input[1].send_keys(Data.reg_password)
        driver.find_element(*Locators.login_reg).click()
        driver.find_element(*Locators.lk_button).click()
        WebDriverWait(driver, 3)
        assert driver.current_url == Data.URL_profile
