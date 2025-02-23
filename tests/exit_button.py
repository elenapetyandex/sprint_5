from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from test_login import login

def test_click_exit_button_go_to_logout_profile(driver):
    driver.implicitly_wait(3)
    driver.get('https://stellarburgers.nomoreparties.site/')

    elements = driver.find_elements(By.TAG_NAME, "button")
    elements[0].click()

    login(driver)
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()

    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()