from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.spicejet.com/")
driver.maximize_window()
driver.implicitly_wait(3)
'''move to element'''
login_ele=driver.find_element(By.XPATH,'//a[@id="ctl00_HyperLinkLogin" and @class="link" and text()="Login / Signup"]')
act_chains=ActionChains(driver)
act_chains.move_to_element(login_ele).perform()

spice_club_members_ele=driver.find_element_by_link_text("SpiceClub Members")
act_chains.move_to_element(spice_club_members_ele).perform()

member_login=driver.find_element(By.LINK_TEXT,"Member Login")
member_login.click()
time.sleep(3)

driver.close()