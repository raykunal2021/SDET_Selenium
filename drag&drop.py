from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.maximize_window()
driver.implicitly_wait(10)

source_ele=driver.find_element(By.ID,"draggable")
target_ele=driver.find_element(By.ID,"droppable")
act_chains=ActionChains(driver)
#single action/direct action
#act_chains.drag_and_drop(source_ele,target_ele).perform()

act_chains.click_and_hold(source_ele).move_to_element(target_ele).release().perform()
time.sleep(6)
driver.close()
