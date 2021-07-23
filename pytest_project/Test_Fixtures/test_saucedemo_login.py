import pytest
from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver import ActionChains
import time

class Test_SauceDemo:


    def test_saucedemo(getDriver):
        driver=getDriver
        driver.find_element_by_xpath('//input[@id="user-name" and @name="user-name"]').send_keys("standard_user")
        driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        driver.find_element(By.ID, 'login-button').click()
        WebDriverWait(driver,10).until(ec.visibility_of_element_located(By.XPATH,"//span[@class='title']"))
        print(driver.title)
        print(driver.current_url)







