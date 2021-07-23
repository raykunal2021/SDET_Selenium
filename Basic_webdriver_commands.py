'''capture title of the page,capture url of the page,closing and quiting browser'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.implicitly_wait(5)
#returns title of the page
print(driver.title)
#returns url of the page
print(driver.current_url)

driver.find_element_by_xpath('//button[@class="btn btn-info" and text()="    click   "]').click()

time.sleep(5)
#closing the currently focused window
#driver.close()
#closing both the web browser windows
driver.quit()
