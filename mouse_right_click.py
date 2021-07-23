from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
driver.implicitly_wait(5)

'''right click/context click'''

right_click_ele=driver.find_element(By.XPATH,'//span[text()="right click me"]')
act_chains=ActionChains(driver)
act_chains.context_click(right_click_ele).perform()
right_click_options=driver.find_elements(By.CSS_SELECTOR,"li.context-menu-icon span")
for i in right_click_options:
    print(i.text)
    if i.text=='Delete':
        i.click()
        break

