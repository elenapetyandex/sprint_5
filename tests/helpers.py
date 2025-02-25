import locator_list
rom selenium import webdriver
from selenium.webdriver.common.by import By


def login(driver):


    for element in login_input:
        element.clear()

    elements_2[0].send_keys('elena_pet_18_101@yandex.ru')

    elements_2[1].send_keys('arrr86$')

    login_button.click()