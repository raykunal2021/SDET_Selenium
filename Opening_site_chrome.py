from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

browser_name="chrome"

if browser_name=="chrome":
    driver=webdriver.Chrome(ChromeDriverManager().install())
elif browser_name=="firefox":
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print("please print the correct browser name : "+browser_name)

driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/")
print(driver.title)
print(driver.current_url)
driver.close()
