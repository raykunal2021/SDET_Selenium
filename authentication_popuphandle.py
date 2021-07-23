from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
#1st type of workaround is providing the userid/password in the get url section with colon

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
driver.close()

