import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

'''browser='firefox'

@pytest.fixture()
def getBrowser():
    return browser'''

@pytest.fixture(scope="class")

def getDriver():
    driver = None
    driver=webdriver.Chrome(ChromeDriverManager().install())
    '''if getBrowser=='firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif getBrowser=='chrome':
        driver=webdriver.Chrome(ChromeDriverManager().install())'''
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    time.sleep(2)
    driver.quit()