import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import UnexpectedAlertPresentException

def test_mouseclic():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    driver.maximize_window()
    driver.implicitly_wait(3)
    act_chain=ActionChains(driver)

    try:

        rightclick=driver.find_element_by_xpath('//span[contains(text(),"right click me")]')
        act_chain.context_click(rightclick).send_keys(Keys.ARROW_DOWN).pause(3).send_keys(Keys.ARROW_DOWN).pause(2).send_keys(Keys.ENTER).perform()
        time.sleep(3)
    except UnexpectedAlertPresentException:
        print("avoid the alert")

    driver.close()


