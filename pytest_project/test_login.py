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


    @pytest.fixture()
    def getdriver(self):
        driver=None
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.implicitly_wait(2)
        yield
        time.sleep(2)
        driver.quit()


    def test_saucedemo(self,getdriver):
        driver=getdriver
        usrname=driver.find_element_by_xpath('//input[@id="user-name" and @name="user-name"]')
        usrname.send_keys("standard_user")
        psw=driver.find_element(By.ID,'password')
        psw.send_keys("secret_sauce")
        logbtn=driver.find_element(By.ID,'login-button')
        logbtn.click()
        WebDriverWait(driver,10).until(ec.visibility_of_element_located(By.XPATH,"//span[@class='title']"))



    def test_itemcount(self,getdriver):
        driver=getdriver
        usrname = driver.find_element_by_xpath('//input[@id="user-name" and @name="user-name"]')
        usrname.send_keys("standard_user")
        psw = driver.find_element(By.ID, 'password')
        psw.send_keys("secret_sauce")
        logbtn = driver.find_element(By.ID, 'login-button')
        logbtn.click()
        WebDriverWait(driver,10).until(ec.visibility_of_element_located(By.XPATH,'//div[@class="app_logo"]'))
        time.sleep(2)
        item_count=len(driver.find_elements_by_xpath('//div[@class="inventory_item_name"]'))
        assert 6==item_count




