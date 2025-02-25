from select import error
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Data
import pytest




class TestRegistration:

    @pytest.mark.parametrize('name,email,password', Data.input_list)
    def test_input_valid_name_email_password_go_to_login_page(self, name, email, password, driver):


        driver.find_element(*Locators.lk_button).click()
        driver.find_element(*Locators.reg_button).click()
        reg_input_elements = driver.find_elements(*Locators.reg_input)
        for element in reg_input_elements:
            element.clear()

        reg_input_elements[0].send_keys(name)
        reg_input_elements[1].send_keys(email)
        reg_input_elements[2].send_keys(password)
        driver.find_element(*Locators.reg_button_2).click()
        WebDriverWait(driver, 3)
        assert  driver.current_url == Data.URL_login




    @pytest.mark.parametrize('name,email,password', Data.input_list_3)
    def test_invalid_password_go_to_incorect_password_message(self, name, email, password, driver):

        driver.find_element(*Locators.lk_button).click()
        driver.find_element(*Locators.reg_button).click()
        reg_input_elements = driver.find_elements(*Locators.reg_input)

        for element in reg_input_elements:
            element.clear()
        reg_input_elements[0].send_keys(name)
        reg_input_elements[1].send_keys(email)
        reg_input_elements[2].send_keys(password)
        driver.find_element(*Locators.reg_button_2).click()
        WebDriverWait(driver, 3)

        assert driver.find_element(*Locators.error_message)



