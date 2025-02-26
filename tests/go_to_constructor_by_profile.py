from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
From data import Data


class TestGoToConstructor:

    def test_click_constructor_in_profile_page_go_to_homepage(self, driver):
        elements = driver.find_elements(*Locators.homepage_buttons)
        elements[0].click()

        elements = driver.find_elements(*Locators.login_input)
        for element in elements:
            element.clear()

        elements[0].send_keys(Data.reg_email)

        elements[1].send_keys(Data.reg_password)

        driver.find_element(*Locators.login_button).click()

        driver.find_element(*Locators.lk_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.constructor)))
        driver.find_element(*Locators.constructor).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((Locators.soberite_burger)))
        assert driver.current_url == Data.URL_homepage


    def test_click_logo_in_profile_page_go_to_homepage(self, driver):
        elements = driver.find_elements(*Locators.homepage_buttons)
        elements[0].click()

        elements = driver.find_elements(*Locators.login_input)
        for element in elements:
            element.clear()

        elements[0].send_keys(Data.reg_email)

        elements[1].send_keys(Data.reg_password)

        driver.find_element(*Locators.login_button).click()

        driver.find_element(*Locators.lk_button).click()
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((Locators.soberite_burger)))
        assert driver.current_url == Data.URL_homepage

