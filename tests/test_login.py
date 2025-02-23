from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

def login(driver):
    elements_2 = driver.find_elements(By.TAG_NAME, "input")

    for element in elements_2:
        element.clear()

    elements_2[0].send_keys('elena_pet_18_101@yandex.ru')

    elements_2[1].send_keys('arrr86$')

    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

def test_login_account_by_HomePage_login_successful(driver):

    driver.implicitly_wait(3)
    driver.get('https://stellarburgers.nomoreparties.site/')

    elements = driver.find_elements(By.TAG_NAME, "button")
    elements[0].click()

    login(driver)


    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()


    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

    driver.quit()

def test_login_by_personal_account_successful(driver):
    driver.implicitly_wait(3)

    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    print(1)
    login(driver)
    print(2)
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    print(3)

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

    driver.quit()

# вход через кнопку регистрации проверяется в регистрации

def test_login_by_recover_password_successful(driver):
    driver.implicitly_wait(3)
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()

    driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']").click()

    driver.find_element(By.XPATH,".//a[text()='Войти']").click()

    login(driver)
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

    driver.quit()


