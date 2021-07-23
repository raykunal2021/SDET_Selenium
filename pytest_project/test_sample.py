import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException

class Test:
    driver=None

def test_opening_of_browser():
    Test.driver=webdriver.Chrome(ChromeDriverManager().install())
    Test.driver.get("https://qavbox.github.io/demo/")
    Test.driver.implicitly_wait(5)
    Test.driver.maximize_window()
    print(Test.driver.title)
    assert "QAVBOX" in Test.driver.title
    print(Test.driver.current_url)
    assert "https://qavbox.github.io/demo/" in Test.driver.current_url

def test_of_elements():

    Test.driver.find_element_by_xpath('//a[text()="SignUp Form"]').click()
    Test.driver.save_screenshot("C:/Users/kunal/PycharmProjects/SDET_Selenium/pytest_project/test_sample.png")
    time.sleep(3)
    Test.driver.close()
