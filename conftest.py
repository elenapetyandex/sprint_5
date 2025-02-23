import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver

#@pytest.fixture()
#def driver():
#    driver = webdriver.Firefox()
#    return driver