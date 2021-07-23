from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.reddit.com/")
driver.maximize_window()
driver.implicitly_wait(3)
#directly getting cookies
#print(driver.get_cookies())

#add cookies
driver.add_cookie({"name":"kunalpython","domain":"reddit.com","value":"python"})
#using with variable
cookies=driver.get_cookies()
for i in cookies:
    print(i)
    print(len(i))
