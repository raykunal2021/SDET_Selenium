import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def test_impli():
    browser_name = "firefox"

    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        print("please print the correct browser name : " + browser_name)

    driver.get("https://qavbox.github.io/demo/delay/")
    driver.maximize_window()
    driver.implicitly_wait(6)
    assert "Delay" in driver.title

    driver.find_element_by_xpath('//input[@class="btn" and @name="commit"]').click()
    
    ele=driver.find_element_by_xpath('//h2[@id="two" and text()="I am here!"]')
    print(ele.text)
    driver.close()