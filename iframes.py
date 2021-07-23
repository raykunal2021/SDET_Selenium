from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
#switch to frame one and click on a link
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium.chrome").click()
#going back to main page or focus on the main page
driver.switch_to.default_content()
time.sleep(3)
#swith to second frame
driver.switch_to.frame("packageFrame")
#driver.find_element_by_css_selector("//main[@role='main']/ul/li[1]/a[@title='class in org.openqa.selenium.support.pagefactory']").click()



driver.close()