from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
driver.maximize_window()

'''there is  a option,inspect the upload section,if type='file' option present then simply use send_keys using any file path'''

driver.find_element(By.NAME,"upfile").send_keys('C:/Users/kunal/OneDrive/Desktop/sample_upload.txt')

driver.find_element(By.XPATH,'//input[@type="submit"]').click()

time.sleep(3)

print(driver.current_url)
print(driver.title)






