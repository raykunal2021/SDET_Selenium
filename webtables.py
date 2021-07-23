from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
driver.maximize_window()
driver.implicitly_wait(3)

driver.switch_to.frame(1)
time.sleep(2)
driver.switch_to.parent_frame()
#driver.find_element(By.XPATH,'//button[@id="onesignal-slidedown-cancel-button" and text()="Cancel"]').click()

# to identify the table rows
r = driver.find_elements_by_xpath ("//table[@class= 'spTable']/tbody/tr")
# to identify table columns
c = driver.find_elements_by_xpath ("//*[@class= 'spTable']/tbody/tr[3]/td")
# to get row count with len method
rc = len (r)
# to get column count with len method
cc = len (c)
for i in c:
    print(i.text)
print(rc)
print(cc)


driver.close()
