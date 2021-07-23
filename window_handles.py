from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver  import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/Windows.html")
driver.implicitly_wait(5)
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH,'//button[@class="btn btn-info" and text()="    click   "]').click()
#print value of the parent windlw
print(driver.current_window_handle)
''''#print value of each open window
handles=driver.window_handles
for i in handles:
    driver.switch_to.window(i)
    print(driver.title)
    print(driver.current_url)
    # if you want to close a particular window then find its title,value and close it
    if driver.title=="SeleniumHQ Browser Automation":
        driver.close()'''


#try to switch to seocnd or 3rd window
handles=driver.window_handles[1]
driver.switch_to.window(handles)
print(driver.find_element(By.XPATH,'//div[@class="banner-message-container" and @id="banner-blm"]').text)

driver.quit()
