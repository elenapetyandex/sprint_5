import pytest
from selenium import webdriver


from data import Data

@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.chrome()
    chrome_driver.get(Data.URL_homepage)
    yield chrome_driver
    chrome_driver.quit()