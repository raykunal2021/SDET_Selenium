from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(3)

#how to get system user agents details,interview question,in chrome console section type navigator.userAgent command

print(driver.execute_script("return navigator.userAgent"))


#mobiles=driver.find_element(By.XPATH,'//a[@class="nav-a  " and text()="Mobiles"]')
#click any web element
'''driver.execute_script("arguments[0].click();",mobiles)
time.sleep(3)'''
#get page title
'''title=driver.execute_script("return document.title;")
print(title)'''
#to refresh a page
'''driver.execute_script("history.go(0);")'''

#create a alert message,used for debuging purpose
#driver.execute_script("alert('hello selenium')")

#all text present in page,used for content testing
'''inner_text=driver.execute_script("return document.documentElement.innerText")
print(inner_text)'''

#scroll down to page end
'''driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)'''

#to scroll to top of the page
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
time.sleep(3)


#to scroll down till a particular element in a page

'''driver.get("https://classic.crmpro.com/index.html")

forget_psw=driver.find_element_by_link_text("Forgot Password?")
driver.execute_script("arguments[0].scrollIntoView(true);",forget_psw)
time.sleep(5)'''

'''driver.get("https://www.amazon.in/")
img_link=driver.find_element(By.XPATH,'//span[@class="a-color-base" and normalize-space()="Get yourself a little something"]')
driver.execute_script("arguments[0].scrollIntoView(true);",img_link)
time.sleep(5)'''
driver.close()

