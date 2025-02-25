import locator_list
rom selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string

result1 = ''.join((random.choice(string.digits) for x in range(5)))
result2 = ''.join((random.choice(string.digits) for x in range(5)))
result3 = ''.join((random.choice(string.digits) for x in range(5)))
result4 = ''.join((random.choice(string.digits) for x in range(5)))

input_list = [
    ["e", f"elena_pet_18_{result1}@yandex.ru", "arrr86"],
    ["el", f"elena_pet_18_{result2}@yandex.ru", "arrr86$"],
    ["Elena", f"elena_pet_18_{result3}@yandex.ru", "Arrr867839"]
]

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

def login(driver):


    for element in login_input:
        element.clear()

    elements_2[0].send_keys('elena_pet_18_101@yandex.ru')

    elements_2[1].send_keys('arrr86$')

    login_button.click()