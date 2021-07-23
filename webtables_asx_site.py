from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www2.asx.com.au/")
driver.maximize_window()
driver.implicitly_wait(3)



driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler" and text()="Accept All Cookies"]').click()

print(driver.find_element_by_xpath())

time.sleep(3)

