from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://advantageonlineshopping.com/#/")
time.sleep(5)
print(driver.title)
print(driver.current_url)
driver.get("https://www.pavantestingtools.com/")
time.sleep(5)
print(driver.title)
print(driver.current_url)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)
driver.close()