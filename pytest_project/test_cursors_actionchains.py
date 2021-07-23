import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def test_cursor():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://qavbox.github.io/demo/signup/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    ele=driver.find_element(By.XPATH,'//input[@id="username" and @class="EnterText"]')

    act_chn=ActionChains(driver)
    #to verify cursor showing or not
    act_chn.click(ele).perform()
    driver.save_screenshot("C:/Users/kunal/PycharmProjects/SDET_Selenium/pytest_project/cursor.png")
    act_chn.send_keys_to_element(ele,'kkr1').perform()
    time.sleep(3)
    driver.close()