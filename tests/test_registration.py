from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import pytest
import string
import helpers
import locator_list

class TestRegistration():

    @pytest.mark.parametrize('name,email,password', input_list)
    def test_input_valid_name_email_password_go_to_login_page(name, email, password, driver):
        driver.implicitly_wait(3)
        driver.get('https://stellarburgers.nomoreparties.site/')
        lk_button.click()
        reg_button.click()

        for element in reg_input:
            element.clear()

        reg_input[0].send_keys(name)
        reg_input[1].send_keys(email)
        reg_input[2].send_keys(password)
        reg_button_2.click()
        WebDriverWait(driver, 3)
        assert  driver.current_url == 'https://stellarburgers.nomoreparties.site/login'




    @pytest.mark.parametrize('name,email,password', input_list_3)
    def test_invalid_password_go_to_incorect_password_message(self, name, email, password, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')

        lk_button.click()
        reg_button.click()

        for element in reg_input:
            element.clear()
        reg_input[0].send_keys(name)
        reg_input[1].send_keys(email)
        reg_input[2].send_keys(password)
        reg_button_2.click()
        WebDriverWait(driver, 3)
        assert error_message



