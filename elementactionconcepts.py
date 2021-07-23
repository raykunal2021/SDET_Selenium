from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://classic.crmpro.com/index.html")
driver.maximize_window()
driver.implicitly_wait(10)

username_ele=driver.find_element(By.NAME,"username")
password_ele=driver.find_element(By.NAME,"password")
login_ele=driver.find_element(By.XPATH,'//input[@type="submit" and @class="btn btn-small"]')

act_chains=ActionChains(driver)
act_chains.send_keys_to_element(username_ele,'batchautomation')
act_chains.send_keys_to_element(password_ele,'Test@12345')
act_chains.click(login_ele).perform()
time.sleep(5)
