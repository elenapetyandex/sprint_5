from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




class TestConstructor:

    def test_click_button_sous_scroll_ingredient_list_to_sous(self, driver):
        driver.maximize_window()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.switch_souses).click()
        element = driver.find_element(*Locators.switch_souses)
        WebDriverWait(driver, 3)
        current = driver.find_element(*Locators.current_scroll)
        assert current == element and current != driver.find_element(*Locators.switch_bulki) and  current != driver.find_element(*Locators.switch_nachinki)


    def test_click_button_bulki_scroll_ingredient_list_to_bulki(self, driver):
        driver.maximize_window()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.switch_bulki).click()
        element = driver.find_element(*Locators.switch_bulki)
        WebDriverWait(driver, 3)
        current = driver.find_element(*Locators.current_scroll)
        assert current == element and current != driver.find_element(*Locators.switch_souses) and current != driver.find_element(*Locators.switch_nachinki)


    def test_click_button_nachinki_scroll_ingredient_list_to_nachinki(self, driver):
        driver.maximize_window()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.switch_nachinki).click()
        element = driver.find_element(*Locators.switch_nachinki)
        WebDriverWait(driver, 3)
        current = driver.find_element(*Locators.current_scroll)
        assert current == element and current != driver.find_element(*Locators.switch_souses) and current != driver.find_element(*Locators.switch_bulki)
