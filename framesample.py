from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://londonfreelance.org/courses/frames/index.html")
driver.maximize_window()

#via frameindex not recommended as new frame introduced means index will change
#driver.switch_to.frame(2)

#via name or id
#driver.switch_to.frame("main")

#via creating frame_element
frame_element=driver.find_element(By.NAME,'main')
driver.switch_to.frame(frame_element)


headervalue=driver.find_element_by_css_selector("body>h2").text
print(headervalue)

#driver.switch_to.default_content()
driver.switch_to.parent_frame()

driver.close()