import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

def test_drpdwn():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://qavbox.github.io/demo/signup/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    print(driver.title)
    assert "Registration Form" in driver.title
    print(driver.current_url)
    assert "https://qavbox.github.io/demo/signup/" in driver.current_url

    #select the drop ddown and count the options and publish it with dropdown.options

    element=driver.find_element_by_xpath('//select[@name="sgender"]')
    drpdwn=Select(element)
    print(len(drpdwn.options))
    all_drpdwn=drpdwn.options
    for i in all_drpdwn:
        print(i.text)

    #select a dropd down by index
    #drpdwn.select_by_index(2)

    #select by value
    #drpdwn.select_by_value("na")

    #select by visible text
    drpdwn.select_by_visible_text("Male")

    time.sleep(3)



    driver.close()



