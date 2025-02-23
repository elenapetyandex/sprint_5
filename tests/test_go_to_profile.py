from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest



input_list_2 = [
    ['elena_pet_18_101@yandex.ru','arrr86$']
]

@pytest.mark.parametrize('email,password', input_list_2)
def test_input_registration_data_in_login_form_go_to_profile_page(email, password, driver):

    driver.implicitly_wait(3)
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    elements_2 = driver.find_elements(By.TAG_NAME, 'input')  # login page form
    for element in elements_2:
        element.clear()
    elements_2[0].send_keys(email)
    elements_2[1].send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()


    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    driver.quit()