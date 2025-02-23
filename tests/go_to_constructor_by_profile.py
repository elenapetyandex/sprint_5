from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from test_login import login


def test_click_constructor_in_profile_page_go_to_homepage(driver):

    driver.implicitly_wait(3)
    driver.get('https://stellarburgers.nomoreparties.site/')

    elements = driver.find_elements(By.TAG_NAME, "button")
    elements[0].click()

    login(driver)

    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()

    driver.find_element(By.LINK_TEXT, 'Конструктор').click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()

def test_click_logo_in_profile_page_go_to_homepage(driver):
    driver.implicitly_wait(3)
    driver.get('https://stellarburgers.nomoreparties.site/')
    elements = driver.find_elements(By.TAG_NAME, "button")
    elements[0].click()
    login(driver)
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    driver.find_element(By.XPATH, "//div/a/*").click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()
