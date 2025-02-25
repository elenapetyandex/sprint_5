from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import locator_list
import helpers

class TestLogin:

    def test_login_account_by_HomePage_login_successful(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        homepage_buttons[0].click()
        login(driver)
        lk_button.click()
        WebDriverWait(driver, 3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        exit_button.click()


    def test_login_by_personal_account_successful(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/')
        lk_button.click()

        login(driver)

        lk_button.click()
        WebDriverWait(driver, 3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        exit_button.click()

# вход через кнопку регистрации проверяется в регистрации

    def test_login_by_recover_password_successful(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        lk_button.click()
        password_ap.click()
        login_reg.click()
        login(driver)
        lk_button.click()
        WebDriverWait(driver, 3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        exit_button.click()




