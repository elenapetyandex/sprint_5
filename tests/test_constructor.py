from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest


def test_click_button_sous_scroll_ingredient_list_to_sous(driver):
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 3)

    driver.find_element(By.XPATH, ".//span[text()='Соусы']/parent::*").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//img[contains(@alt, 'Соус')]")))
    #elements_souses = driver.find_element(By.XPATH, ".//img[contains(@alt, 'Соус')]")
    elements_all = driver.find_elements(By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']")

    elements_souses = elements_all[1]

    assert elements_souses.is_enabled()
    driver.quit()

def test_click_button_bulki_scroll_ingredient_list_to_bulki(driver):
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 3)

    driver.find_element(By.XPATH, ".//span[text()='Соусы']/parent::*").click()
    elements_all = driver.find_elements(By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']")
    elements_bulki = elements_all[0]
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//img[contains(@alt, 'Соус')]")))
    driver.find_element(By.XPATH, ".//span[text()='Булки']/parent::*").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//img[contains(@alt, 'булка')]")))
    assert elements_bulki.is_enabled()
    driver.quit()

def test_click_button_bulki_scroll_ingredient_list_to_bulki(driver):
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 3)
    elements_all = driver.find_elements(By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']")
    elements_nachinki = elements_all[2]
    driver.find_element(By.XPATH, ".//span[text()='Начинки']/parent::*").click()
    WebDriverWait(driver, 3)
    assert elements_nachinki.is_enabled()
    driver.quit()