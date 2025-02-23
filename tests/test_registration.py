from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import pytest
import string

#driver = webdriver.Chrome()# Google Chrome
#driver = webdriver.Firefox() # Firefox




result1 = ''.join((random.choice(string.digits) for x in range(5)))
result2 = ''.join((random.choice(string.digits) for x in range(5)))
result3 = ''.join((random.choice(string.digits) for x in range(5)))
result4 = ''.join((random.choice(string.digits) for x in range(5)))

input_list = [
    ["e", f"elena_pet_18_{result1}@yandex.ru", "arrr86"],
    ["el", f"elena_pet_18_{result2}@yandex.ru", "arrr86$"],
    ["Elena", f"elena_pet_18_{result3}@yandex.ru", "Arrr867839"]
]

@pytest.mark.parametrize('name,email,password', input_list)
def test_input_valid_name_email_password_go_to_login_page(name, email, password, driver):

    driver.implicitly_wait(3)
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()

    driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

    elements = driver.find_elements(By.TAG_NAME, "input")

    for element in elements:
        element.clear()

    elements[0].send_keys(name)
    elements[1].send_keys(email)
    elements[2].send_keys(password)

    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    assert  driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()




result5 = ''.join((random.choice(string.digits) for x in range(5)))
result6 = ''.join((random.choice(string.digits) for x in range(5)))
result7 = ''.join((random.choice(string.digits) for x in range(5)))
result8 = ''.join((random.choice(string.digits) for x in range(5)))

input_list_3= [
    ["elena", f"elena_pet_18_{result5}@yandex.ru", ""],
    ["elena", f"elena_pet_18_{result6}@yandex.ru", "a"],
    ["elena", f"elena_pet_18_{result7}@yandex.ru", "arrr"],
    ["elena", f"elena_pet_18_{result8}@yandex.ru", "arrrr"]

]

@pytest.mark.parametrize('name,email,password', input_list_3)
def test_invalid_password_go_to_incorect_password_message(name, email, password, driver):

    driver.implicitly_wait(3)
    driver.get('https://stellarburgers.nomoreparties.site/')


    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()

    driver.find_element(By.LINK_TEXT, 'Зарегистрироваться').click()

    elements = driver.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.clear()
    elements[0].send_keys(name)
    elements[1].send_keys(email)
    elements[2].send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    element = driver.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']")
    assert element
    driver.quit()


