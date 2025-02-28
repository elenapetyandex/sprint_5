from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import Data


class TestLogin:

    def test_login_account_by_HomePage_login_successful(self, driver):
        homepage_buttons = driver.find_elements(*Locators.homepage_buttons)
        homepage_buttons[0].click()
        elements = driver.find_elements(*Locators.login_input)
        for element in elements:
            element.clear()

        elements[0].send_keys(Data.reg_email)

        elements[1].send_keys(Data.reg_password)

        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.lk_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((Locators.exit_button)))
        assert driver.current_url == Data.URL_profile



    def test_login_by_personal_account_successful(self, driver):
        driver.find_element(*Locators.lk_button).click()

        homepage_buttons = driver.find_elements(*Locators.homepage_buttons)
        homepage_buttons[0].click()
        elements = driver.find_elements(*Locators.login_input)
        for element in elements:
            element.clear()

        elements[0].send_keys(Data.reg_email)

        elements[1].send_keys(Data.reg_password)

        driver.find_element(*Locators.login_button).click()

        driver.find_element(*Locators.lk_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((Locators.exit_button)))
        assert driver.current_url == Data.URL_profile


# вход через кнопку регистрации проверяется в регистрации

    def test_login_by_recover_password_successful(self, driver):

        driver.find_element(*Locators.lk_button).click()
        driver.find_element(*Locators.password_ap).click()
        driver.find_element(*Locators.login_reg).click()
        elements = driver.find_elements(*Locators.login_input)
        for element in elements:
            element.clear()

        elements[0].send_keys(Data.reg_email)

        elements[1].send_keys(Data.reg_password)

        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.lk_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((Locators.exit_button)))
        assert driver.current_url == Data.URL_profile





