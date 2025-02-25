from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import locator_list



class TestConstructor:

    def test_click_button_sous_scroll_ingredient_list_to_sous(self, driver):
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 3)
        switch_souses.click()
        WebDriverWait(driver, 3)
        assert current_scroll == switch_souses and current_scroll != switch_bulki and  current_scroll != switch_nachinki


    def test_click_button_bulki_scroll_ingredient_list_to_bulki(self, driver):
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 3)
        switch_bulki.click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//span[text()='Булки']/parent::*").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//img[contains(@alt, 'булка')]")))
        assert  current_scroll == switch_bulki and current_scroll != switch_souses and  current_scroll != switch_nachinki



    def test_click_button_bulki_scroll_ingredient_list_to_bulki(self, driver):
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 3)
        switch_nachinki.click()
        WebDriverWait(driver, 3)
        assert current_scroll == switch_nachinki and current_scroll != switch_souses and  current_scroll != switch_bulki
