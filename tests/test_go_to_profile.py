from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import locator_list


class GoToProfile():

    @pytest.mark.parametrize('email,password', [['elena_pet_18_101@yandex.ru','arrr86$']])
    def test_input_registration_data_in_login_form_go_to_profile_page(self, email, password, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        lk_button.click()
          # login page form
        for element in login_input:
            element.clear()
        login_input[0].send_keys(email)
        login_input[1].send_keys(password)
        login_reg.click()
        lk_button.click()
        WebDriverWait(driver, 3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
