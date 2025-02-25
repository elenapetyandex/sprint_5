import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def driver_firefox():
    driver = webdriver.Firefox()

    yield driver
    driver.quit()